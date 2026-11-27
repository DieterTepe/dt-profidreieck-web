import json
from playwright.sync_api import sync_playwright
# Vollversion lokal (NICHT ins Repo – lizenzpflichtig, DXF-Export nur dort)
URL="file:///home/claude/y02/voll/DT-ProfiDreieck.html"
OUT="/home/claude/y02/cap/"
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
def shot(pg,name,hold,ev=None,cap=None,reuse=None):
    if not reuse: pg.screenshot(path=OUT+name+".jpg",type="jpeg",quality=92)
    shots.append({"f":(reuse or name)+".jpg","hold":hold,"ev":ev,"cap":cap,"fx":FOC[0],"fy":FOC[1],"z":FOC[2],"pan":bool(reuse)})
def tap(pg,loc,base,cap,hover=0.5,press=0.25):
    x,y=center(pg,loc)
    pg.evaluate(RING,{"x":x,"y":y}); shot(pg,base+"_hov",hover,None,cap)
    pg.evaluate(RING,{"x":x,"y":y,"pressed":True}); shot(pg,base+"_prs",press,"click",cap)
    pg.evaluate(RING,{"x":0,"y":0,"hide":True}); loc.click(); pg.wait_for_timeout(450)
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome")
    ctx=b.new_context(viewport={"width":1920,"height":1080},device_scale_factor=2,accept_downloads=True)
    pg=ctx.new_page()
    pg.goto(URL); pg.wait_for_timeout(2000)
    pg.get_by_role("button",name="Später").click(); pg.wait_for_timeout(800)
    pg.add_style_tag(content="*{caret-color:#34c3d4} ::-webkit-scrollbar{display:none}")
    vals=[("a","Länge a","400","Kante a = 400 mm"),("b","Länge b","250","Kante b = 250 mm"),("γ","Winkel γ","70","Winkel γ = 70° zwischen a und b")]
    for i,(s,t,v,c2) in enumerate(vals):
        FOC[:]=[960,540,1.45]
        cap=f"Größe {i+1}: {'Seite '+s if i<2 else 'Winkel γ'} antippen"
        shot(pg,f"in{i}_wiz",1.4 if i==0 else 0.7,None,cap)
        tap(pg,pg.locator(f'#wizOverlay .pill[title="{t}"]'),f"in{i}_pill",cap)
        f=pg.locator(f"#val{i}"); f.evaluate("e=>e.scrollIntoView({block:'center'})"); pg.wait_for_timeout(250)
        x,y=center(pg,f); FOC[:]=[x,y,1.5]
        shot(pg,f"in{i}_field",0.4,None,c2)
        for j,ch in enumerate(v):
            pg.keyboard.type(ch); pg.wait_for_timeout(100)
            shot(pg,f"in{i}_t{j}",0.2 if j<len(v)-1 else 0.8,"type",c2)
        btn=pg.locator("#wizNext")
        if btn.is_visible():
            btn.evaluate("e=>e.scrollIntoView({block:'center'})"); pg.wait_for_timeout(200)
            x,y=center(pg,btn); FOC[:]=[x,y-120,1.5]
            tap(pg,btn,f"in{i}_next",c2,0.35,0.2)
        else: pg.keyboard.press("Enter"); pg.wait_for_timeout(450)
    pg.wait_for_timeout(1200); pg.evaluate("scrollTo(0,0)"); pg.wait_for_timeout(400); FOC[:]=[960,540,1.0]
    shot(pg,"in_done",2.4,"chime","Fall SWS – alle Werte berechnet")
    # Ergebnis-Karte
    rc=pg.locator("#resultCard"); rc.screenshot(path=OUT+"erg_card.png")
    tiles=pg.evaluate("""()=>{const c=document.querySelector('#resultCard').getBoundingClientRect();const o={};
      document.querySelectorAll('#resultCard .res').forEach(r=>{const k=r.querySelector('.k')?.textContent.trim();const b=r.getBoundingClientRect();o[k]=[b.left-c.left,b.top-c.top,b.width,b.height]});
      const t=document.querySelector('#traceToggle').getBoundingClientRect();o.toggle=[t.left-c.left,t.top-c.top,t.width,t.height];return o}""")
    tg=pg.locator("#traceToggle"); tg.scroll_into_view_if_needed(); pg.wait_for_timeout(200)
    x,y=center(pg,tg)
    pg.evaluate(RING,{"x":x,"y":y}); rc.screenshot(path=OUT+"erg_card_hov.png")
    pg.evaluate(RING,{"x":x,"y":y,"pressed":True}); rc.screenshot(path=OUT+"erg_card_prs.png")
    pg.evaluate(RING,{"x":0,"y":0,"hide":True}); tg.click(); pg.wait_for_timeout(1500)
    pg.evaluate(HIDE_STICKY)
    tb=pg.locator("#traceBody"); h=tb.bounding_box()["height"]
    pg.set_viewport_size({"width":1920,"height":int(h)+300}); pg.wait_for_timeout(600)
    tb.evaluate("e=>e.scrollIntoView({block:'start'})"); pg.wait_for_timeout(300)
    tb.screenshot(path=OUT+"trace.png")
    steps=pg.evaluate("""()=>{const b=document.querySelector('#traceBody').getBoundingClientRect();
      return [...document.querySelectorAll('#traceBody .tstep')].map(s=>{const r=s.getBoundingClientRect();return {t:s.querySelector('.tstep-title')?.textContent.trim(),y:r.top-b.top,h:r.height}})}""")
    pg.set_viewport_size({"width":1920,"height":1080}); pg.wait_for_timeout(400); pg.evaluate(SHOW_STICKY)
    # Zeichnung: Hilfslinien aus
    gc=pg.locator("#graphCard"); gc.evaluate("e=>e.scrollIntoView({block:'start'})"); pg.evaluate("scrollBy(0,-90)"); pg.wait_for_timeout(500)
    x,y=center(pg,gc); FOC[:]=[x,y+10,1.75]
    shot(pg,"z_start",2.6,"whoosh","Maßstäbliche Zeichnung des Knotenblechs")
    for name in ["Umkreis","Inkreis","Seitenhalbierende"]:
        chip=pg.locator("#graphCard .vis-chip",has_text=name).first
        tap(pg,chip,f"z_{name}","Für den Laser nur die Kontur: Hilfslinien ausblenden",0.35,0.2)
    pg.wait_for_timeout(500)
    shot(pg,"z_clean",2.4,"pop","Übrig bleibt die reine Kontur mit Maßen")
    # Bezeichnung + DXF
    pg.evaluate("scrollTo(0,0)"); pg.wait_for_timeout(400)
    lab=pg.locator("#dtLabel"); x,y=center(pg,lab); FOC[:]=[1000,300,1.7]
    tap(pg,lab,"d_label","Bezeichnung eintragen",0.35,0.2)
    for j,ch in enumerate("Knotenblech K1"):
        pg.keyboard.type(ch); pg.wait_for_timeout(60)
        if j%2==1 or j==13: shot(pg,f"d_l{j}",0.14 if j<13 else 0.9,"type","Bezeichnung: Knotenblech K1")
    unit=pg.locator("#dxfUnit"); x,y=center(pg,unit)
    pg.evaluate(RING,{"x":x,"y":y}); shot(pg,"d_unit_hov",0.45,None,"DXF-Einheit: Millimeter")
    pg.evaluate(RING,{"x":x,"y":y,"pressed":True}); shot(pg,"d_unit_prs",0.2,"click","DXF-Einheit: Millimeter")
    pg.evaluate(RING,{"x":0,"y":0,"hide":True})
    pg.select_option("#dxfUnit",index=1); pg.wait_for_timeout(300)
    shot(pg,"d_unit",1.2,None,"DXF-Einheit: Millimeter")
    dbtn=pg.get_by_role("button",name="DXF (CAD)").first
    x,y=center(pg,dbtn)
    pg.evaluate(RING,{"x":x,"y":y}); shot(pg,"d_btn_hov",0.6,None,"DXF (CAD) exportieren")
    pg.evaluate(RING,{"x":x,"y":y,"pressed":True}); shot(pg,"d_btn_prs",0.3,"click","DXF (CAD) exportieren")
    pg.evaluate(RING,{"x":0,"y":0,"hide":True})
    with pg.expect_download(timeout=8000) as dl:
        dbtn.click()
    dl.value.save_as(OUT+"knotenblech.dxf"); print("dxf:",dl.value.suggested_filename)
    pg.wait_for_timeout(600)
    shot(pg,"d_done",1.6,"chime","DXF gespeichert")
    json.dump({"shots":shots,"steps":steps,"tiles":tiles},open(OUT+"timeline.json","w"),ensure_ascii=False,indent=1)
    b.close()
