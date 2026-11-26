import json
from playwright.sync_api import sync_playwright
URL="file:///home/claude/dt-profipassung-web/DT-ProfiPassung_Testversion.html"
OUT="/home/claude/y04/cap/"
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
def zoom_on(pg,loc,z,dy=0):
    x,y=center(pg,loc); FOC[:]=[x,y+dy,z]
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
    # ---- Teil 1: 25 H7/g6 eintippen
    res=pg.locator("#outHead").locator("xpath=ancestor::section[1]"); res.evaluate("e=>e.id='__res'")
    viz=pg.locator("#vizHead").locator("xpath=ancestor::section[1]"); viz.evaluate("e=>e.id='__viz'")
    f=pg.locator("input.fit-input")
    FOC[:]=[662,420,1.45]
    cap="Teil 1: Passung direkt eintippen"
    shot(pg,"p1_start",1.4,None,cap)
    tap(pg,f,"p1_field",cap,0.4,0.2)
    f.click(); f.press("Control+a"); f.press("Backspace"); pg.wait_for_timeout(300)
    shot(pg,"p1_empty",0.35,None,cap)
    txt="25 H7/g6"
    for i,ch in enumerate(txt):
        f.type(ch); pg.wait_for_timeout(120)
        if ch!=" ": shot(pg,f"p1_t{i}",0.22,"type","Kurzeingabe: 25 H7/g6")
    pg.wait_for_timeout(800); f.evaluate("e=>e.blur()"); pg.wait_for_timeout(300)
    FOC[:]=[960,540,1.0]
    shot(pg,"p1_done",2.0,"chime","Sofort berechnet – ohne Knopfdruck")
    t1=pg.locator("#__res").get_by_text("Mindestspiel",exact=True).first
    zoom_on(pg,t1,1.9,40); shot(pg,"p1_res",3.0,"pop","Spielpassung: 7 … 41 µm Spiel",reuse="p1_done")
    pg.evaluate(HIDE_STICKY); viz.evaluate("e=>e.scrollIntoView({block:'center'})"); pg.wait_for_timeout(400)
    zoom_on(pg,viz,1.35); shot(pg,"p1_viz",3.0,"pop","Toleranzfeld: H7 über, g6 unter der Nulllinie")
    pg.evaluate(SHOW_STICKY); pg.evaluate("scrollTo(0,0)"); pg.wait_for_timeout(300)
    # ---- Teil 2: Pressverband
    FOC[:]=[662,365,1.45]
    cap="Teil 2: Beispiel Zahnrad-Schrumpfsitz laden"
    tap(pg,pg.locator("#presetSel"),"p2_sel",cap)
    pg.select_option("#presetSel","PV|0"); pg.wait_for_timeout(1300)
    shot(pg,"p2_loaded",1.6,"pop","Ø60 H7/s6 · Stahl auf Stahl")
    pv=pg.get_by_text("Pressverband berechnen (DIN 7190)",exact=True).first
    pv.evaluate("e=>e.scrollIntoView({block:'start'})"); pg.evaluate("scrollBy(0,-80)"); pg.wait_for_timeout(300)
    x,y=center(pg,pv); FOC[:]=[662,y+330,1.45]
    shot(pg,"p2_pv",3.0,None,"Werkstoffe, Fugenlänge 50 mm, Nabe Ø120, M_t = 250 Nm")
    pg.evaluate("scrollTo(0,0)"); pg.wait_for_timeout(300)
    btn=pg.get_by_role("button",name="Berechnen",exact=True).first
    FOC[:]=[662,365,1.45]
    tap(pg,btn,"p2_calc","Berechnen",0.5,0.25)
    btn.click(); pg.wait_for_timeout(2200); pg.evaluate("scrollTo(0,0)"); pg.wait_for_timeout(300)
    FOC[:]=[960,540,1.0]
    shot(pg,"p2_done",1.8,"chime","Übermaßpassung: schwerer Presssitz")
    box=pg.get_by_text("Pressverband (DIN 7190)",exact=True).first
    box.evaluate("e=>e.scrollIntoView({block:'start'})"); pg.evaluate("scrollBy(0,-120)"); pg.wait_for_timeout(300)
    pg.evaluate(HIDE_STICKY)
    zoom_on(pg,box,1.7,150); shot(pg,"p2_box",3.6,"pop","Fugendruck 24,3 … 88,6 N/mm² · Sicherheit S_F = 1,73")
    shot(pg,"p2_box2",3.6,"pop","Drehmoment 962 Nm · Einpresskraft 116,9 kN · Nabe auf 211 °C",reuse="p2_box")
    shots[-1]["fy"]=shots[-2]["fy"]+70
    viz.evaluate("e=>e.scrollIntoView({block:'center'})"); pg.wait_for_timeout(400)
    zoom_on(pg,viz,1.35); shot(pg,"p2_viz",3.0,"pop","Toleranzfeld: s6 liegt ganz über H7 – immer Übermaß")
    pg.evaluate(SHOW_STICKY)
    # ---- Rechenweg
    tg=pg.locator("button.rw-toggle").first
    tg.evaluate("e=>e.scrollIntoView({block:'center'})"); pg.wait_for_timeout(300)
    x,y=center(pg,tg); bb=res.bounding_box(); CL={"x":bb["x"],"y":max(bb["y"],y-420),"width":bb["width"],"height":560}
    pg.evaluate(HIDE_STICKY)
    pg.evaluate(RING,{"x":x,"y":y}); pg.screenshot(path=OUT+"weg_hov.png",clip=CL)
    pg.evaluate(RING,{"x":x,"y":y,"pressed":True}); pg.screenshot(path=OUT+"weg_prs.png",clip=CL)
    pg.evaluate(RING,{"x":0,"y":0,"hide":True}); pg.evaluate(SHOW_STICKY)
    tg.click(); pg.wait_for_timeout(1500); pg.evaluate(HIDE_STICKY)
    pg.set_viewport_size({"width":1920,"height":2400}); pg.wait_for_timeout(600)
    wd=pg.locator("button.rw-toggle").first.locator("xpath=..")
    wd.evaluate("e=>e.scrollIntoView({block:'start'})"); pg.wait_for_timeout(400)
    wd.screenshot(path=OUT+"weg.png")
    steps=pg.evaluate("""()=>{const w=document.querySelector('button.rw-toggle').parentElement;const wr=w.getBoundingClientRect();const out=[];
      for(const e of w.querySelectorAll('*')){if(e.children.length==0&&/^\d+$/.test(e.textContent.trim())){let blk=e;for(let i=0;i<4;i++){blk=blk.parentElement;if(blk.getBoundingClientRect().height>40)break}const r=blk.getBoundingClientRect();out.push({t:e.textContent.trim(),y:r.top-wr.top,h:r.height})}}return out}""")
    json.dump({"shots":shots,"steps":steps},open(OUT+"timeline.json","w"),ensure_ascii=False,indent=1)
    b.close()
