import ezdxf, math
from playwright.sync_api import sync_playwright
d=ezdxf.readfile("/home/claude/y02/cap/knotenblech.dxf"); m=d.modelspace()
lines=[(tuple(e.dxf.start)[:2],tuple(e.dxf.end)[:2]) for e in m if e.dxftype()=="LINE" and e.dxf.layer=="DREIECK"]
texts=[(tuple(e.dxf.insert)[:2],e.dxf.text,e.dxf.height) for e in m if e.dxftype()=="TEXT"]
pts=[p for l in lines for p in l]
minx=min(p[0] for p in pts); maxx=max(p[0] for p in pts); miny=min(p[1] for p in pts); maxy=max(p[1] for p in pts)
# Zeichenfläche
VX,VY,VW,VH=420,150,1360,820
s=min((VW-360)/(maxx-minx),(VH-300)/(maxy-miny))
ox=VX+180+((VW-360)-(maxx-minx)*s)/2-minx*s; oy=VY+VH-150-((VH-300)-(maxy-miny)*s)/2+miny*s
P=lambda p:(ox+p[0]*s, oy-p[1]*s)
# Pfad in Reihenfolge
path=[P(lines[0][0])]+[P(l[1]) for l in lines]
seg=[math.dist(path[i],path[i+1]) for i in range(len(path)-1)]; L=sum(seg)
def page(prog, show_text):
    # Teil des Pfads bis prog
    rest=prog*L; pd=f"M{path[0][0]:.1f},{path[0][1]:.1f}"; head=path[0]
    for i,sl in enumerate(seg):
        a,b=path[i],path[i+1]
        if rest>=sl: pd+=f" L{b[0]:.1f},{b[1]:.1f}"; rest-=sl; head=b
        else:
            f=rest/sl; head=(a[0]+(b[0]-a[0])*f,a[1]+(b[1]-a[1])*f); pd+=f" L{head[0]:.1f},{head[1]:.1f}"; break
    grid=""
    step=50*s
    gx0=VX+((ox-VX)%step); gy0=VY+((oy-VY)%step)
    x=gx0
    while x<VX+VW: grid+=f'<line x1="{x:.1f}" y1="{VY}" x2="{x:.1f}" y2="{VY+VH}"/>'; x+=step
    y=gy0
    while y<VY+VH: grid+=f'<line x1="{VX}" y1="{y:.1f}" x2="{VX+VW}" y2="{y:.1f}"/>'; y+=step
    tx=""
    if show_text:
        for (p,t,h) in texts:
            q=P(p); tx+=f'<text x="{q[0]:.1f}" y="{q[1]:.1f}">{t}</text>'
    laser=f'<circle cx="{head[0]:.1f}" cy="{head[1]:.1f}" r="9" fill="#fff" filter="url(#g)"/><circle cx="{head[0]:.1f}" cy="{head[1]:.1f}" r="22" fill="rgba(255,180,60,.35)" filter="url(#g)"/>' if 0<prog<1 else ""
    o=P((0,0))
    return f'''<html><body style="margin:0;width:1920px;height:1080px;background:#0b0e12;font-family:Inter;color:#e7eef4">
<div style="position:absolute;left:0;top:0;right:0;height:70px;background:#141a21;border-bottom:1px solid #2a333c;display:flex;align-items:center;padding:0 40px;gap:24px">
 <span style="font-weight:800;color:#34c3d4;letter-spacing:.08em">DXF-VORSCHAU</span>
 <span style="font-family:'JetBrains Mono','DejaVu Sans Mono';font-size:22px;color:#cfd8df">Dreieck_2026-11-27_Knotenblech_K1.dxf</span>
 <span style="margin-left:auto;font-size:20px;color:#94a4b2">Einheit: <b style="color:#e7eef4">mm</b> · Maßstab 1:1</span></div>
<div style="position:absolute;left:40px;top:150px;width:330px;background:#141a21;border:1px solid #2a333c;border-radius:14px;padding:22px 24px;font-size:22px">
 <div style="font-weight:800;color:#94a4b2;letter-spacing:.12em;font-size:18px;margin-bottom:14px">EBENEN</div>
 <div style="display:flex;align-items:center;gap:12px;margin:10px 0"><i style="width:18px;height:18px;background:#e7eef4;border-radius:4px;display:inline-block"></i>DREIECK <span style="margin-left:auto;color:#94a4b2">3 Linien</span></div>
 <div style="display:flex;align-items:center;gap:12px;margin:10px 0"><i style="width:18px;height:18px;background:#e0b44a;border-radius:4px;display:inline-block"></i>BESCHRIFTUNG <span style="margin-left:auto;color:#94a4b2">6 Texte</span></div>
 <div style="height:1px;background:#2a333c;margin:18px 0"></div>
 <div style="font-weight:800;color:#94a4b2;letter-spacing:.12em;font-size:18px;margin-bottom:10px">ABMESSUNGEN</div>
 <div style="font-family:'JetBrains Mono','DejaVu Sans Mono';font-size:21px;line-height:1.7">X: {minx:.2f} … {maxx:.2f}<br>Y: {miny:.2f} … {maxy:.2f}<br>Kontur: {sum(math.dist(a,b) for a,b in lines):.2f} mm</div>
</div>
<svg width="1920" height="1080" style="position:absolute;left:0;top:0">
 <defs><filter id="g"><feGaussianBlur stdDeviation="4"/></filter></defs>
 <rect x="{VX}" y="{VY}" width="{VW}" height="{VH}" rx="14" fill="#0f141a" stroke="#2a333c"/>
 <g stroke="rgba(148,164,178,.12)" stroke-width="1">{grid}</g>
 <g stroke="#ff5a5a" stroke-width="2"><line x1="{o[0]}" y1="{o[1]}" x2="{o[0]+60}" y2="{o[1]}"/></g>
 <g stroke="#46b95c" stroke-width="2"><line x1="{o[0]}" y1="{o[1]}" x2="{o[0]}" y2="{o[1]-60}"/></g>
 <text x="{o[0]-12}" y="{o[1]+30}" font-family="JetBrains Mono,DejaVu Sans Mono" font-size="18" fill="#94a4b2">0,0</text>
 <path d="{pd}" fill="none" stroke="#e7eef4" stroke-width="4" stroke-linejoin="round"/>
 <g font-family="JetBrains Mono,DejaVu Sans Mono" font-size="26" font-weight="700" fill="#e0b44a">{tx}</g>
 {laser}
</svg></body></html>'''
N=45
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome")
    pg=b.new_page(viewport={"width":1920,"height":1080})
    for i in range(N+1):
        pg.set_content(page(i/N, False)); pg.screenshot(path=f"/home/claude/y02/cad/f{i:03d}.png")
    pg.set_content(page(1.0, True)); pg.screenshot(path="/home/claude/y02/cad/final.png")
    b.close()
print("ok", minx,maxx,miny,maxy)
