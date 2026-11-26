import math
from playwright.sync_api import sync_playwright
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
   ('brand','<div class="L brand" style="left:140px;top:250px"><i></i>DT-ProfiSchweissnaht</div>'),
   ('title','<h1 class="L" style="left:136px;top:320px">Schweißnaht am Rohr<br><em>unter Torsion</em></h1>'),
   ('sub','<div class="L sub" style="left:140px;top:560px;width:980px">Kehlnaht nach EN 1993-1-8 – mit vollständigem Rechenweg</div>'),
   ('tri','<div class="L" style="left:1180px;top:220px"><svg width="640" height="640" viewBox="-320 -320 640 640"> <defs><marker id="ah" markerUnits="userSpaceOnUse" markerWidth="30" markerHeight="30" refX="14" refY="15" orient="auto"><path d="M0,3 L28,15 L0,27 z" fill="#caa04a"/></marker></defs> <circle r="200" fill="none" stroke="#34c3d4" stroke-width="22" opacity=".95"/> <circle r="178" fill="rgba(52,195,212,.06)" stroke="#e7eef4" stroke-width="5"/> <circle r="157" fill="#13171c" stroke="#e7eef4" stroke-width="5"/> <line x1="-280" y1="0" x2="280" y2="0" stroke="#94a4b2" stroke-width="2" stroke-dasharray="18 8 4 8"/> <line x1="0" y1="-280" x2="0" y2="280" stroke="#94a4b2" stroke-width="2" stroke-dasharray="18 8 4 8"/> <path d="M 236 -150 A 280 280 0 0 1 236 150" fill="none" stroke="#caa04a" stroke-width="8" marker-end="url(#ah)"/> <text x="268" y="-150" font-family="Inter" font-weight="800" font-size="40" fill="#caa04a">T</text> <text x="0" y="-232" text-anchor="middle" font-family="Inter" font-weight="700" font-size="28" fill="#34c3d4" stroke="#13171c" stroke-width="10" paint-order="stroke">Kehlnaht a = 4</text> <text x="0" y="12" text-anchor="middle" font-family="Inter" font-weight="700" font-size="30" fill="#e7eef4" stroke="#13171c" stroke-width="12" paint-order="stroke">⌀ 114,3 × 6</text></svg></div>')]},
 "aufgabe":{"bg":BG,"layers":[
   ('lab1','<div class="L lab" style="left:140px;top:200px">Gegeben</div>'),
   ('c1','<div class="L chip" style="left:140px;top:255px">Rundrohr <b>114,3 × 6</b> auf Platte</div>'),
   ('c2','<div class="L chip" style="left:140px;top:370px">umlaufende Kehlnaht <b>a = 4 mm</b></div>'),
   ('c3','<div class="L chip" style="left:140px;top:485px">Stahl <b>S235</b> · Torsion <b>T = 9 kNm</b></div>'),
   ('lab2','<div class="L lab" style="left:140px;top:660px">Gesucht</div>'),
   ('want','<div class="L want" style="left:140px;top:705px">Schubspannung τ<sub>∥</sub> · Vergleichsspannung σ<sub>v</sub> · Nachweis</div>'),
   ('tri','<div class="L" style="left:1220px;top:220px"><svg width="640" height="640" viewBox="-320 -320 640 640"> <defs><marker id="ah" markerUnits="userSpaceOnUse" markerWidth="30" markerHeight="30" refX="14" refY="15" orient="auto"><path d="M0,3 L28,15 L0,27 z" fill="#caa04a"/></marker></defs> <circle r="200" fill="none" stroke="#34c3d4" stroke-width="22" opacity=".95"/> <circle r="178" fill="rgba(52,195,212,.06)" stroke="#e7eef4" stroke-width="5"/> <circle r="157" fill="#13171c" stroke="#e7eef4" stroke-width="5"/> <line x1="-280" y1="0" x2="280" y2="0" stroke="#94a4b2" stroke-width="2" stroke-dasharray="18 8 4 8"/> <line x1="0" y1="-280" x2="0" y2="280" stroke="#94a4b2" stroke-width="2" stroke-dasharray="18 8 4 8"/> <path d="M 236 -150 A 280 280 0 0 1 236 150" fill="none" stroke="#caa04a" stroke-width="8" marker-end="url(#ah)"/> <text x="268" y="-150" font-family="Inter" font-weight="800" font-size="40" fill="#caa04a">T</text> <text x="0" y="-232" text-anchor="middle" font-family="Inter" font-weight="700" font-size="28" fill="#34c3d4" stroke="#13171c" stroke-width="10" paint-order="stroke">Kehlnaht a = 4</text> <text x="0" y="12" text-anchor="middle" font-family="Inter" font-weight="700" font-size="30" fill="#e7eef4" stroke="#13171c" stroke-width="12" paint-order="stroke">⌀ 114,3 × 6</text></svg></div>')]},
 "outro":{"bg":BG,"layers":[
   ('brand','<div class="L brand" style="left:140px;top:220px"><i></i>DT-ProfiSchweissnaht</div>'),
   ('title','<h1 class="L" style="left:136px;top:290px">Jetzt <em>kostenlos</em> testen</h1>'),
   ('sub','<div class="L sub" style="left:140px;top:420px">Direkt im Browser · ohne Anmeldung · ohne Installation</div>'),
   ('url','<div class="L url" style="left:140px;top:530px">dietertepe.github.io/dt-profischweissnaht-web</div>'),
   ('small','<div class="L small" style="left:140px;top:720px">Vollversion: <b>169 € einmalig</b> · kein Abo · läuft offline<br>dt-profidreieck.de</div>')]},
}
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome")
    pg=b.new_page(viewport={"width":1920,"height":1080})
    for name,c in cards.items():
        pg.set_content(f"<style>{CSS}</style>{c['bg']}"); pg.wait_for_timeout(200)
        pg.screenshot(path=f"/home/claude/y05/cards/{name}_bg.png")
        for lid,html in c["layers"]:
            pg.set_content(f"<style>{CSS}</style>{html}"); pg.wait_for_timeout(150)
            pg.screenshot(path=f"/home/claude/y05/cards/{name}_{lid}.png",omit_background=True)
        pg.set_content(f"<style>{CSS}</style>{c['bg']}{''.join(h for _,h in c['layers'])}"); pg.wait_for_timeout(200)
        pg.screenshot(path=f"/home/claude/y05/cards/{name}_full.png")
    b.close()
