import json
from playwright.sync_api import sync_playwright
URL="file:///home/claude/dietertepe/dt-profischweissnaht-web/DT-ProfiSchweissnaht_Testversion.html"
OUT="/home/claude/y05/cap/"
RING="""(a)=>{let r=document.getElementById('__ring');if(!r){r=document.createElement('div');r.id='__ring';document.body.appendChild(r)}
 const R=a.pressed?22:30;
 r.style.cssText=`position:fixed;left:${a.x-R}px;top:${a.y-R}px;width:${2*R}px;height:${2*R}px;border-radius:50%;z-index:99999;pointer-events:none;`+
 (a.pressed?'background:rgba(52,195,212,.55);border:3px solid #e7eef4;box-shadow:0 0 0 10px rgba(52,195,212,.25)':'border:4px solid #34c3d4;background:rgba(52,195,212,.15);box-shadow:0 0 18px rgba(52,195,212,.8)');
 r.style.display=a.hide?'none':'block';}"""
HIDE_STICKY="""()=>{for(const e of document.querySelectorAll('body *')){const p=getComputedStyle(e).position;if((p=='fixed'||p=='sticky')&&e.id!='__ring')e.style.visibility='hidden'}}"""
SHOW_STICKY="""()=>{for(const e of document.querySelectorAll('body *')){if(e.style.visibility=='hidden')e.style.visibility=''}}"""
shots=[]; FOC=[960,540,1.0]
def center(pg,loc):
    bb=loc.bounding_box(); return bb["x"]+bb["width"]/2, bb["y"]+bb["height"]/2
def shot(pg,name,hold,ev=None,cap=None):
    pg.screenshot(path=OUT+name+".jpg",type="jpeg",quality=92)
    shots.append({"f":name+".jpg","hold":hold,"ev":ev,"cap":cap,"fx":FOC[0],"fy":FOC[1],"z":FOC[2]})
def tap(pg,loc,base,cap,hover=0.5,press=0.25):
    x,y=center(pg,loc)
    pg.evaluate(RING,{"x":x,"y":y}); shot(pg,base+"_hov",hover,None,cap)
    pg.evaluate(RING,{"x":x,"y":y,"pressed":True}); shot(pg,base+"_prs",press,"click",cap)
    pg.evaluate(RING,{"x":0,"y":0,"hide":True})
def rect_rel(pg,card,texts):
    return pg.evaluate("""([card,texts])=>{const c=document.querySelector(card).getBoundingClientRect();const o={};
      for(const t of texts){const leaf=[...document.querySelectorAll(card+' *')].find(e=>e.children.length==0&&e.textContent.trim()===t);
        if(!leaf){o[t]=null;continue} let el=leaf;for(let i=0;i<4&&el.parentElement;i++){const cs=getComputedStyle(el);if(parseFloat(cs.borderTopWidth)>0||cs.backgroundColor!='rgba(0, 0, 0, 0)')break;el=el.parentElement}
        const r=el.getBoundingClientRect();o[t]=[r.left-c.left,r.top-c.top,r.width,r.height]} return o}""",[card,texts])

with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome")
    pg=b.new_page(viewport={"width":1920,"height":1080},device_scale_factor=2)
    pg.goto(URL); pg.wait_for_timeout(2000)
    pg.add_style_tag(content="::-webkit-scrollbar{display:none}")
    # 1 Beispiel laden
    FOC[:]=[662,365,1.45]
    cap="Beispiel laden: Rundrohr unter Torsion"
    shot(pg,"in_start",1.4,None,cap)
    tap(pg,pg.locator("#presetSel"),"in_sel",cap)
    pg.select_option("#presetSel","rohr"); pg.wait_for_timeout(1200)
    shot(pg,"in_loaded",1.6,"pop","Rundrohr 114,3 × 6 auf Platte, Torsion 9 kNm")
    secs=[("acc_werkstoff","Werkstoff: S235 – f_u = 360 N/mm²"),
          ("acc_naht","Umlaufende Kehlnaht, a = 4 mm"),
          ("acc_geometrie","Rundrohr: d = 114,3 mm, Wanddicke 6 mm"),
          ("acc_lasten","Last: Torsionsmoment T = 9 kNm")]
    for sid,c in secs:
        head=pg.locator(f"#{sid} > :first-child")
        head.evaluate("e=>e.scrollIntoView({block:'center'})"); pg.wait_for_timeout(250)
        x,y=center(pg,head); FOC[:]=[640,y,1.45]
        tap(pg,head,f"in_{sid}",c,0.45,0.2)
        head.click(); pg.wait_for_timeout(500)
        sec=pg.locator(f"#{sid}")
        sec.evaluate("e=>e.scrollIntoView({block:'center'})"); pg.wait_for_timeout(300)
        x,y=center(pg,sec); FOC[:]=[640,y,1.45]
        shot(pg,f"in_{sid}_open",2.4,None,c)
    pg.evaluate("scrollTo(0,0)"); pg.wait_for_timeout(300)
    btn=pg.get_by_role("button",name="Berechnen",exact=True)
    FOC[:]=[900,360,1.45]
    tap(pg,btn,"in_calc","Berechnen",0.5,0.25)
    btn.click(); pg.wait_for_timeout(2500); pg.evaluate("scrollTo(0,0)"); pg.wait_for_timeout(400)
    FOC[:]=[960,540,1.0]
    shot(pg,"in_done",2.6,"chime","Nachweis erfüllt – das Ergebnis steht rechts")
    # Ergebnis
    rc=pg.locator("#cardResult"); rc.screenshot(path=OUT+"erg_card.png")
    tiles=rect_rel(pg,"#cardResult",["Nachweis erfüllt","Ausnutzung η","Vergleichsspannung σ_v","Grenzwert R_d","a-Maß","Nahtlänge gesamt"])
    # Nahtbild
    gc=pg.locator("#cardGrafik"); gc.evaluate("e=>e.scrollIntoView({block:'start'})"); pg.wait_for_timeout(400)
    pg.evaluate(HIDE_STICKY); gc.screenshot(path=OUT+"naht.png"); pg.evaluate(SHOW_STICKY)
    # Rechenweg: Knopf
    wg=pg.locator("#cardWeg"); tg=pg.locator("#accBtn_weg_detail")
    tg.evaluate("e=>e.scrollIntoView({block:'center'})"); pg.wait_for_timeout(300)
    x,y=center(pg,tg); bb=wg.bounding_box(); cy=max(bb["y"],y-420); CL={"x":bb["x"],"y":cy,"width":bb["width"],"height":560}
    pg.evaluate(RING,{"x":x,"y":y}); pg.evaluate(HIDE_STICKY)
    pg.screenshot(path=OUT+"weg_hov.png",clip=CL)
    pg.evaluate(RING,{"x":x,"y":y,"pressed":True})
    pg.screenshot(path=OUT+"weg_prs.png",clip=CL)
    pg.evaluate(RING,{"x":0,"y":0,"hide":True}); pg.evaluate(SHOW_STICKY)
    tg.click(); pg.wait_for_timeout(900)
    pg.evaluate(HIDE_STICKY); wg.screenshot(path=OUT+"weg.png")
    steps=pg.evaluate("""()=>{const w=document.querySelector('#cardWeg').getBoundingClientRect();return [...document.querySelectorAll('#cardWeg .rw-titel')].map(e=>{const box=e.parentElement.getBoundingClientRect();return {t:e.textContent.trim(),y:box.top-w.top,h:box.height}})}""")
    json.dump({"shots":shots,"steps":steps,"tiles":tiles},open(OUT+"timeline.json","w"),ensure_ascii=False,indent=1)
    b.close()
