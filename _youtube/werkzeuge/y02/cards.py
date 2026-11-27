import math
from playwright.sync_api import sync_playwright
# echtes Dreieck a=7 b=5 c=6
S=1.2
c_=392.550597; A=(0,0);B=(c_*S,0);C=(72.09*S,239.38*S)
W=c_*S+330; H=C[1]+150
def P(p): return (220+p[0], H-90-p[1])
pa,pb,pc=P(A),P(B),P(C)
def mid(p,q,dx=0,dy=0): return ((p[0]+q[0])/2+dx,(p[1]+q[1])/2+dy)
def tri(show_vals):
    ma=mid(pb,pc,34,-6); mb=mid(pa,pc,-40,0); mc=mid(pa,pb,0,48)
    la=("a = 400 mm" if show_vals else "a = 400"); lb=("b = 250 mm" if show_vals else "b = 250"); lc=("c = ?" if show_vals else "c = ?")
    return f'''<svg width="{W:.0f}" height="{H:.0f}" viewBox="0 0 {W:.0f} {H:.0f}">
 <polygon points="{pa[0]},{pa[1]} {pb[0]},{pb[1]} {pc[0]},{pc[1]}" fill="rgba(52,195,212,.10)" stroke="#e7eef4" stroke-width="5" stroke-linejoin="round"/>
 <path d="M {pc[0]+34},{pc[1]+70} A 70 70 0 0 0 {pc[0]-14},{pc[1]+72}" fill="none" stroke="#34c3d4" stroke-width="4"/><text x="{pc[0]+8}" y="{pc[1]+118}" font-family="Inter" font-weight="800" font-size="32" fill="#34c3d4" text-anchor="middle">70°</text><g fill="#34c3d4">{''.join(f'<circle cx="{q[0]}" cy="{q[1]}" r="9"/>' for q in (pa,pb,pc))}</g>
 <g font-family="Inter" font-weight="700" font-size="34" fill="#caa04a">
  <text x="{ma[0]}" y="{ma[1]}">{la}</text><text x="{mb[0]}" y="{mb[1]}" text-anchor="end">{lb}</text><text x="{mc[0]}" y="{mc[1]}" text-anchor="middle">{lc}</text></g>
 <g font-family="Inter" font-weight="600" font-size="30" fill="#94a4b2">
  <text x="{pa[0]-30}" y="{pa[1]+12}" text-anchor="end">A</text><text x="{pb[0]+28}" y="{pb[1]+12}">B</text><text x="{pc[0]}" y="{pc[1]-26}" text-anchor="middle">C</text></g></svg>'''
CSS='''*{margin:0;box-sizing:border-box} html,body{width:1920px;height:1080px;background:transparent;font-family:Inter;color:#e7eef4}
.L{position:absolute} .brand{font-weight:700;letter-spacing:.18em;font-size:26px;color:#34c3d4;text-transform:uppercase;display:flex;align-items:center;gap:16px}
.brand i{display:inline-block;width:0;height:0;border-left:16px solid transparent;border-right:16px solid transparent;border-bottom:26px solid #34c3d4}
h1{font-family:"Inter Display";font-weight:800;font-size:96px;line-height:1.04;letter-spacing:-.02em}
h1 em{font-style:normal;color:#34c3d4}
.sub{font-size:38px;color:#94a4b2;font-weight:500}
.lab{font-size:26px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:#94a4b2}
.chip{display:inline-block;padding:18px 34px;border-radius:16px;background:#212a31;border:2px solid #323e49;font-family:"JetBrains Mono","DejaVu Sans Mono",monospace;font-size:46px;font-weight:700}
.chip b{color:#34c3d4}
.want{font-size:44px;font-weight:600;line-height:1.5}
.url{display:inline-block;padding:26px 46px;border-radius:22px;background:linear-gradient(135deg,#34c3d4,#1f97a8);color:#0f141a;font-weight:800;font-size:58px;letter-spacing:-.01em;box-shadow:0 20px 60px rgba(52,195,212,.35)}
.small{font-size:32px;color:#94a4b2;font-weight:500} .small b{color:#e7eef4}
'''
BG='''<div style="position:absolute;inset:0;background:radial-gradient(1200px 800px at 75% 40%,#1c2a33 0%,#13171c 60%,#0f141a 100%)"></div>
<div style="position:absolute;inset:0;background-image:linear-gradient(rgba(148,164,178,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(148,164,178,.06) 1px,transparent 1px);background-size:48px 48px;-webkit-mask-image:radial-gradient(900px 700px at 70% 45%,#000 30%,transparent 100%)"></div>
<div style="position:absolute;left:0;top:0;bottom:0;width:10px;background:linear-gradient(#34c3d4,#1f97a8)"></div>'''
cards={
 "intro":{"bg":BG,"layers":[
   ('brand','<div class="L brand" style="left:140px;top:250px"><i></i>DT-ProfiDreieck · Vollversion</div>'),
   ('title','<h1 class="L" style="left:136px;top:320px">Vom Werkstück<br><em>zur DXF</em></h1>'),
   ('sub','<div class="L sub" style="left:140px;top:560px;width:900px">Knotenblech berechnen, Kontur prüfen und als DXF in echten Millimetern an Laser oder CNC</div>'),
   ('tri',f'<div class="L" style="left:1000px;top:{520-H/2:.0f}px">{tri(False)}</div>')]},
 "aufgabe":{"bg":BG,"layers":[
   ('lab1','<div class="L lab" style="left:140px;top:200px">Werkstück: Knotenblech</div>'),
   ('c1','<div class="L chip" style="left:140px;top:255px">Kante <b>a = 400 mm</b></div>'),
   ('c2','<div class="L chip" style="left:140px;top:370px">Kante <b>b = 250 mm</b></div>'),
   ('c3','<div class="L chip" style="left:140px;top:485px">Winkel dazwischen <b>γ = 70°</b></div>'),
   ('lab2','<div class="L lab" style="left:140px;top:660px">Gesucht</div>'),
   ('want','<div class="L want" style="left:140px;top:705px;width:900px">Dritte Kante c · Winkel α, β · Fläche – und die DXF für den Zuschnitt</div>'),
   ('tri',f'<div class="L" style="left:960px;top:{500-H/2:.0f}px">{tri(True)}</div>')]},
 "outro":{"bg":BG,"layers":[
   ('brand','<div class="L brand" style="left:140px;top:220px"><i></i>DT-ProfiDreieck</div>'),
   ('title','<h1 class="L" style="left:136px;top:290px">Jetzt <em>kostenlos</em> testen</h1>'),
   ('sub','<div class="L sub" style="left:140px;top:420px">Direkt im Browser · ohne Anmeldung · ohne Installation</div>'),
   ('url','<div class="L url" style="left:140px;top:530px">dietertepe.github.io/test-dreieck</div>'),
   ('small','<div class="L small" style="left:140px;top:720px">Vollversion: <b>69 € einmalig</b> · mit DXF-, SVG- und PDF-Export · läuft offline<br>dt-profidreieck.de</div>')]},
}
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome")
    pg=b.new_page(viewport={"width":1920,"height":1080})
    for name,c in cards.items():
        pg.set_content(f"<style>{CSS}</style>{c['bg']}"); pg.wait_for_timeout(200)
        pg.screenshot(path=f"/home/claude/y02/cards/{name}_bg.png")
        for lid,html in c["layers"]:
            pg.set_content(f"<style>{CSS}</style>{html}"); pg.wait_for_timeout(150)
            pg.screenshot(path=f"/home/claude/y02/cards/{name}_{lid}.png",omit_background=True)
        pg.set_content(f"<style>{CSS}</style>{c['bg']}{''.join(h for _,h in c['layers'])}"); pg.wait_for_timeout(200)
        pg.screenshot(path=f"/home/claude/y02/cards/{name}_full.png")
    b.close()
