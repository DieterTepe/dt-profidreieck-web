import json, sys
from playwright.sync_api import sync_playwright
URL="file:///home/claude/dietertepe/test-dreieck/DT-ProfiDreieck_Test_1-1-0.html"
OUT="/home/claude/y01/cap/"
RING="""(a)=>{let r=document.getElementById('__ring');if(!r){r=document.createElement('div');r.id='__ring';document.body.appendChild(r)}
 const R=a.pressed?22:30;
 r.style.cssText=`position:fixed;left:${a.x-R}px;top:${a.y-R}px;width:${2*R}px;height:${2*R}px;border-radius:50%;z-index:99999;pointer-events:none;`+
 (a.pressed?'background:rgba(52,195,212,.55);border:3px solid #e7eef4;box-shadow:0 0 0 10px rgba(52,195,212,.25)':'border:4px solid #34c3d4;background:rgba(52,195,212,.15);box-shadow:0 0 18px rgba(52,195,212,.8)');
 r.style.display=a.hide?'none':'block';}"""
shots=[]
FOC=[960,540,1.0]
def focus(pg,loc,z=1.5):
    loc.evaluate("e=>e.scrollIntoView({block:'center'})"); pg.wait_for_timeout(250)
    x,y=center(pg,loc); FOC[0],FOC[1],FOC[2]=x,y,z
def shot(pg,name,hold,ev=None,cap=None):
    pg.screenshot(path=OUT+name+".jpg",type="jpeg",quality=92)
    shots.append({"f":name+".jpg","hold":hold,"ev":ev,"cap":cap,"fx":FOC[0],"fy":FOC[1],"z":FOC[2]})
def center(pg,loc):
    bb=loc.bounding_box(); return bb["x"]+bb["width"]/2, bb["y"]+bb["height"]/2
def tap(pg,loc,base,cap,hover=0.55,press=0.25):
    x,y=center(pg,loc)
    pg.evaluate(RING,{"x":x,"y":y}); shot(pg,base+"_hov",hover,None,cap)
    pg.evaluate(RING,{"x":x,"y":y,"pressed":True}); shot(pg,base+"_prs",press,"click",cap)
    pg.evaluate(RING,{"x":0,"y":0,"hide":True}); loc.click(); pg.wait_for_timeout(450)

with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome")
    pg=b.new_page(viewport={"width":1920,"height":1080},device_scale_factor=2)
    pg.goto(URL); pg.wait_for_timeout(1500)
    pg.add_style_tag(content="*{caret-color:#34c3d4} ::-webkit-scrollbar{display:none}")
    vals=[("a","Länge a","7"),("b","Länge b","5"),("c","Länge c","6")]
    for i,(s,t,v) in enumerate(vals):
        cap=f"Größe {i+1}: Seite {s} antippen"
        FOC[0],FOC[1],FOC[2]=960,540,1.45
        shot(pg,f"in{i}_wiz",1.6 if i==0 else 0.7,None,cap)
        tap(pg,pg.locator(f'#wizOverlay .pill[title="{t}"]'),f"in{i}_pill",cap)
        cap2=f"Wert eingeben: {s} = {v} mm"
        focus(pg,pg.locator(f"#val{i}"))
        shot(pg,f"in{i}_field",0.45,None,cap2)
        pg.keyboard.type(v); pg.wait_for_timeout(150)
        shot(pg,f"in{i}_typed",0.9 if i==0 else 0.6,"type",cap2)
        btn=pg.locator("#wizNext")
        if btn.is_visible():
            btn.evaluate("e=>e.scrollIntoView({block:'center'})"); pg.wait_for_timeout(200)
            tap(pg,btn,f"in{i}_next",cap2,0.4,0.2)
        else: pg.keyboard.press("Enter"); pg.wait_for_timeout(450)
    pg.wait_for_timeout(1200); pg.evaluate("scrollTo(0,0)"); pg.wait_for_timeout(400); FOC[0],FOC[1],FOC[2]=960,540,1.0
    shot(pg,"in_done",2.6,"chime","Fertig – alle Werte sind berechnet")
    # Ergebnis-Karte
    rc=pg.locator("#resultCard"); rc.scroll_into_view_if_needed(); pg.evaluate("scrollTo(0,0)"); pg.wait_for_timeout(300)
    rc.screenshot(path=OUT+"erg_card.png")
    # Rechenweg
    tg=pg.locator("#traceToggle"); tg.scroll_into_view_if_needed(); pg.wait_for_timeout(200)
    x,y=center(pg,tg)
    pg.evaluate(RING,{"x":x,"y":y}); rc.screenshot(path=OUT+"erg_card_hov.png")
    pg.evaluate(RING,{"x":x,"y":y,"pressed":True}); rc.screenshot(path=OUT+"erg_card_prs.png")
    pg.evaluate(RING,{"x":0,"y":0,"hide":True}); tg.click(); pg.wait_for_timeout(700)
    pg.evaluate("""()=>{for(const e of document.querySelectorAll('body *')){const p=getComputedStyle(e).position;if((p=='fixed'||p=='sticky')&&e.id!='__ring')e.style.visibility='hidden'}}""")
    tb=pg.locator("#traceBody"); tb.screenshot(path=OUT+"trace.png")
    # step offsets inside trace body
    steps=pg.evaluate("""()=>{const b=document.querySelector('#traceBody').getBoundingClientRect();
      return [...document.querySelectorAll('#traceBody .tstep')].map(s=>{const r=s.getBoundingClientRect();return {t:s.querySelector('.tstep-title')?.textContent.trim(),y:r.top-b.top,h:r.height}})}""")
    # Zeichnung
    gc=pg.locator("#graphCard"); gc.scroll_into_view_if_needed(); pg.wait_for_timeout(400)
    gc.screenshot(path=OUT+"zeich0.png")
    chip=pg.locator("#graphCard .vis-chip",has_text="Höhen").first
    x,y=center(pg,chip); pg.evaluate(RING,{"x":x,"y":y,"pressed":True}); gc.screenshot(path=OUT+"zeich_prs.png")
    pg.evaluate(RING,{"x":0,"y":0,"hide":True}); chip.click(); pg.wait_for_timeout(600)
    gc.screenshot(path=OUT+"zeich1.png")
    json.dump({"shots":shots,"steps":steps},open(OUT+"timeline.json","w"),ensure_ascii=False,indent=1)
    b.close()
