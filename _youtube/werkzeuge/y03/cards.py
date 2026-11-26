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
   ('brand','<div class="L brand" style="left:140px;top:250px"><i></i>DT-ProfiSchraube</div>'),
   ('title','<h1 class="L" style="left:136px;top:320px">Schraube M16 10.9<br><em>nach VDI 2230</em></h1>'),
   ('sub','<div class="L sub" style="left:140px;top:560px;width:960px">Vorspannkraft · Anziehdrehmoment · Sicherheiten – mit vollständigem Rechenweg</div>'),
   ('tri','<div class="L" style="left:1200px;top:230px"><svg width="560" height="620" viewBox="-280 -310 560 620"> <defs><pattern id="h" width="14" height="14" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="14" stroke="#4a5866" stroke-width="3"/></pattern></defs> <rect x="-230" y="-110" width="460" height="110" fill="url(#h)" stroke="#e7eef4" stroke-width="4"/> <rect x="-230" y="0" width="460" height="110" fill="url(#h)" stroke="#e7eef4" stroke-width="4"/> <rect x="-44" y="-112" width="88" height="224" fill="#13171c"/> <rect x="-34" y="-150" width="68" height="300" fill="rgba(52,195,212,.18)" stroke="#34c3d4" stroke-width="5"/> <path d="M-80,-150 L-70,-205 L70,-205 L80,-150 Z" fill="rgba(52,195,212,.25)" stroke="#34c3d4" stroke-width="5"/> <path d="M-80,112 L80,112 L80,168 L-80,168 Z" fill="rgba(52,195,212,.25)" stroke="#34c3d4" stroke-width="5"/> <line x1="0" y1="-240" x2="0" y2="240" stroke="#94a4b2" stroke-width="2" stroke-dasharray="18 8 4 8"/> <g stroke="#caa04a" stroke-width="7" fill="#caa04a">  <line x1="0" y1="-215" x2="0" y2="-285"/><path d="M-14,-270 L0,-300 L14,-270 Z" stroke-width="2"/>  <line x1="0" y1="178" x2="0" y2="248"/><path d="M-14,233 L0,263 L14,233 Z" stroke-width="2"/>  <line x1="-250" y1="-55" x2="-180" y2="-55"/><path d="M-195,-69 L-165,-55 L-195,-41 Z" stroke-width="2"/> </g> <g font-family="Inter" font-weight="800" font-size="34" fill="#caa04a" stroke="#13171c" stroke-width="8" paint-order="stroke">  <text x="22" y="-262">F_A</text><text x="-260" y="-75">F_Q</text></g> <text x="110" y="-170" font-family="Inter" font-weight="700" font-size="30" fill="#34c3d4" stroke="#13171c" stroke-width="8" paint-order="stroke">M16 · 10.9</text></svg></div>')]},
 "aufgabe":{"bg":BG,"layers":[
   ('lab1','<div class="L lab" style="left:140px;top:200px">Gegeben</div>'),
   ('c1','<div class="L chip" style="left:140px;top:255px">Schraube <b>M16</b> · Festigkeit <b>10.9</b></div>'),
   ('c2','<div class="L chip" style="left:140px;top:370px">Durchsteckverbindung · <b>l_K = 40 mm</b></div>'),
   ('c3','<div class="L chip" style="left:140px;top:485px"><b>F_A = 12 kN</b> axial · <b>F_Q = 4 kN</b> quer</div>'),
   ('lab2','<div class="L lab" style="left:140px;top:660px">Gesucht</div>'),
   ('want','<div class="L want" style="left:140px;top:705px">Vorspannkraft · Anziehdrehmoment M<sub>A</sub> · Sicherheiten S<sub>F</sub>, S<sub>P</sub>, S<sub>G</sub></div>'),
   ('tri','<div class="L" style="left:1240px;top:230px"><svg width="560" height="620" viewBox="-280 -310 560 620"> <defs><pattern id="h" width="14" height="14" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="14" stroke="#4a5866" stroke-width="3"/></pattern></defs> <rect x="-230" y="-110" width="460" height="110" fill="url(#h)" stroke="#e7eef4" stroke-width="4"/> <rect x="-230" y="0" width="460" height="110" fill="url(#h)" stroke="#e7eef4" stroke-width="4"/> <rect x="-44" y="-112" width="88" height="224" fill="#13171c"/> <rect x="-34" y="-150" width="68" height="300" fill="rgba(52,195,212,.18)" stroke="#34c3d4" stroke-width="5"/> <path d="M-80,-150 L-70,-205 L70,-205 L80,-150 Z" fill="rgba(52,195,212,.25)" stroke="#34c3d4" stroke-width="5"/> <path d="M-80,112 L80,112 L80,168 L-80,168 Z" fill="rgba(52,195,212,.25)" stroke="#34c3d4" stroke-width="5"/> <line x1="0" y1="-240" x2="0" y2="240" stroke="#94a4b2" stroke-width="2" stroke-dasharray="18 8 4 8"/> <g stroke="#caa04a" stroke-width="7" fill="#caa04a">  <line x1="0" y1="-215" x2="0" y2="-285"/><path d="M-14,-270 L0,-300 L14,-270 Z" stroke-width="2"/>  <line x1="0" y1="178" x2="0" y2="248"/><path d="M-14,233 L0,263 L14,233 Z" stroke-width="2"/>  <line x1="-250" y1="-55" x2="-180" y2="-55"/><path d="M-195,-69 L-165,-55 L-195,-41 Z" stroke-width="2"/> </g> <g font-family="Inter" font-weight="800" font-size="34" fill="#caa04a" stroke="#13171c" stroke-width="8" paint-order="stroke">  <text x="22" y="-262">F_A</text><text x="-260" y="-75">F_Q</text></g> <text x="110" y="-170" font-family="Inter" font-weight="700" font-size="30" fill="#34c3d4" stroke="#13171c" stroke-width="8" paint-order="stroke">M16 · 10.9</text></svg></div>')]},
 "outro":{"bg":BG,"layers":[
   ('brand','<div class="L brand" style="left:140px;top:220px"><i></i>DT-ProfiSchraube</div>'),
   ('title','<h1 class="L" style="left:136px;top:290px">Jetzt <em>kostenlos</em> testen</h1>'),
   ('sub','<div class="L sub" style="left:140px;top:420px">Direkt im Browser · ohne Anmeldung · ohne Installation</div>'),
   ('url','<div class="L url" style="left:140px;top:530px">dietertepe.github.io/dt-profischraube-web</div>'),
   ('small','<div class="L small" style="left:140px;top:720px">Vollversion: <b>159 € einmalig</b> · kein Abo · läuft offline<br>dt-profidreieck.de</div>')]},
}
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome")
    pg=b.new_page(viewport={"width":1920,"height":1080})
    for name,c in cards.items():
        pg.set_content(f"<style>{CSS}</style>{c['bg']}"); pg.wait_for_timeout(200)
        pg.screenshot(path=f"/home/claude/y03/cards/{name}_bg.png")
        for lid,html in c["layers"]:
            pg.set_content(f"<style>{CSS}</style>{html}"); pg.wait_for_timeout(150)
            pg.screenshot(path=f"/home/claude/y03/cards/{name}_{lid}.png",omit_background=True)
        pg.set_content(f"<style>{CSS}</style>{c['bg']}{''.join(h for _,h in c['layers'])}"); pg.wait_for_timeout(200)
        pg.screenshot(path=f"/home/claude/y03/cards/{name}_full.png")
    b.close()
