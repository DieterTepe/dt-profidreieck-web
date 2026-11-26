import json
from playwright.sync_api import sync_playwright
URL="file:///home/claude/dietertepe/dt-profischraube-web/DT-ProfiSchraube_Test.html"
OUT="/home/claude/y03/cap/"
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
    cap="Beispiel laden: M16 10.9, axial + Querkraft"
    shot(pg,"in_start",1.4,None,cap)
    tap(pg,pg.locator("#presetSel"),"in_sel",cap)
    pg.select_option("#presetSel","kombiniert_m16"); pg.wait_for_timeout(1300)
    shot(pg,"in_loaded",1.5,"pop","Kombiniert M16 10.9 – axial + Querkraft")
    det=pg.locator("details.form-group")
    def focus_det(i,dy=0):
        d=det.nth(i); d.evaluate("e=>e.scrollIntoView({block:'center'})"); pg.wait_for_timeout(300)
        x,y=center(pg,d); FOC[:]=[662,y+dy,1.45]
    focus_det(0); shot(pg,"in_s1",2.3,None,"Schraube M16, Festigkeitsklasse 10.9")
    focus_det(1); shot(pg,"in_s2",2.3,None,"Reibung μ = 0,12 · drehmomentgesteuert angezogen")
    focus_det(2); shot(pg,"in_s3",2.3,None,"Durchsteckverbindung, Klemmlänge l_K = 40 mm")
    sm=det.nth(3).locator("summary"); sm.evaluate("e=>e.scrollIntoView({block:'center'})"); pg.wait_for_timeout(250)
    x,y=center(pg,sm); FOC[:]=[662,y+200,1.45]
    tap(pg,sm,"in_s4",'Bereich „Belastung“ öffnen',0.45,0.2)
    sm.click(); pg.wait_for_timeout(500)
    d4=det.nth(3); d4.evaluate("e=>e.scrollIntoView({block:'start'})"); pg.evaluate("scrollBy(0,-140)"); pg.wait_for_timeout(300)
    bb=d4.bounding_box(); FOC[:]=[662,bb["y"]+372,1.45]
    shot(pg,"in_s4_open",2.8,None,"Betriebskraft F_A = 12 kN axial, Querkraft F_Q = 4 kN")
    pg.evaluate("scrollTo(0,0)"); pg.wait_for_timeout(300)
    btn=pg.get_by_role("button",name="Berechnen",exact=True).first
    FOC[:]=[662,365,1.45]
    tap(pg,btn,"in_calc","Berechnen",0.5,0.25)
    btn.click(); pg.wait_for_timeout(2500); pg.evaluate("scrollTo(0,0)"); pg.wait_for_timeout(400)
    FOC[:]=[960,540,1.0]
    shot(pg,"in_done",2.4,"chime","Berechnet – das Ergebnis steht rechts")
    res=pg.locator("#outHead").locator("xpath=ancestor::section[1]")
    res.evaluate("e=>e.id='__res'")
    viz=pg.locator("#vizHead").locator("xpath=ancestor::section[1]"); viz.evaluate("e=>e.id='__viz'")
    pg.evaluate(HIDE_STICKY); res.evaluate("e=>e.scrollIntoView({block:'start'})"); pg.wait_for_timeout(300)
    res.screenshot(path=OUT+"erg_card.png")
    tiles=pg.evaluate("""()=>{const c=document.querySelector('#__res').getBoundingClientRect();const o={};
      for(const v of ['1,25','1,38','1,30']){const leaf=[...document.querySelectorAll('#__res *')].find(e=>e.children.length==0&&e.textContent.trim()===v);
        if(!leaf){o[v]=null;continue} let el=leaf;for(let i=0;i<5;i++){el=el.parentElement;const cs=getComputedStyle(el);if(parseFloat(cs.borderTopWidth)>0)break}
        const r=el.getBoundingClientRect();o[v]=[r.left-c.left,r.top-c.top,r.width,r.height]}
      const b=[...document.querySelectorAll('#__res *')].find(e=>e.children.length<=2&&/ausreichend dimensioniert/.test(e.textContent)&&e.getBoundingClientRect().height<120);
      if(b){let el=b;for(let i=0;i<4;i++){const cs=getComputedStyle(el);if(parseFloat(cs.borderTopWidth)>0||parseFloat(cs.borderLeftWidth)>0)break;el=el.parentElement}const r=el.getBoundingClientRect();o.ampel=[r.left-c.left,r.top-c.top,r.width,r.height]}
      return o}""")
    viz.evaluate("e=>e.scrollIntoView({block:'start'})"); pg.wait_for_timeout(400)
    viz.screenshot(path=OUT+"viz.png")
    vizparts=pg.evaluate("""()=>{const c=document.querySelector('#__viz').getBoundingClientRect();const h=[...document.querySelectorAll('#__viz *')].find(e=>e.children.length==0&&/Schnittdarstellung/i.test(e.textContent));return h?h.getBoundingClientRect().top-c.top:null}""")
    pg.evaluate(SHOW_STICKY)
    # Rechenweg
    sm=pg.locator("details.rechenweg > summary"); sm.evaluate("e=>e.scrollIntoView({block:'center'})"); pg.wait_for_timeout(300)
    x,y=center(pg,sm); bb=res.bounding_box(); CL={"x":bb["x"],"y":max(bb["y"],y-420),"width":bb["width"],"height":560}
    pg.evaluate(HIDE_STICKY)
    pg.evaluate(RING,{"x":x,"y":y}); pg.screenshot(path=OUT+"weg_hov.png",clip=CL)
    pg.evaluate(RING,{"x":x,"y":y,"pressed":True}); pg.screenshot(path=OUT+"weg_prs.png",clip=CL)
    pg.evaluate(RING,{"x":0,"y":0,"hide":True}); pg.evaluate(SHOW_STICKY)
    sm.click(); pg.wait_for_timeout(900); pg.evaluate(HIDE_STICKY)
    wd=pg.locator("details.rechenweg"); wd.screenshot(path=OUT+"weg.png")
    titles=["Kraftverhältnis Φ_K","Vorspannkraftverlust durch Setzen F_Z","Mindest-Montagevorspannkraft F_Mmin","Zulässige Montagevorspannkraft F_Mzul","Anziehdrehmoment M_A","Sicherheit gegen Fließen S_F","Sicherheit Flächenpressung S_P","Sicherheit gegen Gleiten S_G"]
    steps=pg.evaluate("""(ts)=>{const w=document.querySelector('details.rechenweg').getBoundingClientRect();return ts.map(t=>{const leaf=[...document.querySelectorAll('details.rechenweg *')].find(e=>e.children.length==0&&e.textContent.trim()===t);if(!leaf)return {t,y:null};
      let el=leaf;for(let i=0;i<5;i++){el=el.parentElement;if(el.getBoundingClientRect().height>90)break}const r=el.getBoundingClientRect();return {t,y:r.top-w.top,h:r.height}})}""",titles)
    json.dump({"shots":shots,"steps":steps,"tiles":tiles,"viz_schnitt":vizparts},open(OUT+"timeline.json","w"),ensure_ascii=False,indent=1)
    b.close()
