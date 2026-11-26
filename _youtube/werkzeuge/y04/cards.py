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
.want{width:1000px;font-size:40px;font-weight:600;line-height:1.5}
.url{display:inline-block;padding:26px 46px;border-radius:22px;background:linear-gradient(135deg,#34c3d4,#1f97a8);color:#0f141a;font-weight:800;font-size:58px;letter-spacing:-.01em;box-shadow:0 20px 60px rgba(52,195,212,.35)}
.small{font-size:32px;color:#94a4b2;font-weight:500} .small b{color:#e7eef4}
'''
BG='''<div style="position:absolute;inset:0;background:radial-gradient(1200px 800px at 75% 40%,#1c2a33 0%,#13171c 60%,#0f141a 100%)"></div>
<div style="position:absolute;inset:0;background-image:linear-gradient(rgba(148,164,178,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(148,164,178,.06) 1px,transparent 1px);background-size:48px 48px;-webkit-mask-image:radial-gradient(900px 700px at 70% 45%,#000 30%,transparent 100%)"></div>
<div style="position:absolute;left:0;top:0;bottom:0;width:10px;background:linear-gradient(#34c3d4,#1f97a8)"></div>'''
cards={
 "intro":{"bg":BG,"layers":[
   ('brand','<div class="L brand" style="left:140px;top:250px"><i></i>DT-ProfiPassung</div>'),
   ('title','<h1 class="L" style="left:136px;top:320px">Passung berechnen<br><em>nach ISO 286</em></h1>'),
   ('sub','<div class="L sub" style="left:140px;top:560px;width:960px">Spielpassung H7/g6 und Pressverband H7/s6 – mit vollständigem Rechenweg</div>'),
   ('tri','<div class="L" style="left:1180px;top:240px"><svg width="640" height="620" viewBox="-60 -320 640 620"> <line x1="-40" y1="0" x2="560" y2="0" stroke="#94a4b2" stroke-width="3" stroke-dasharray="14 8"/> <text x="560" y="-14" text-anchor="end" font-family="Inter" font-weight="600" font-size="24" fill="#94a4b2">Nulllinie</text> <rect x="0" y="-130" width="110" height="130" fill="rgba(70,185,92,.22)" stroke="#46b95c" stroke-width="5"/> <text x="55" y="-150" text-anchor="middle" font-family="Inter" font-weight="800" font-size="34" fill="#46b95c">H7</text> <rect x="150" y="80" width="110" height="80" fill="rgba(80,150,230,.25)" stroke="#5a9be6" stroke-width="5"/><text x="205" y="200" text-anchor="middle" font-family="Inter" font-weight="800" font-size="34" fill="#5a9be6">g6</text><rect x="300" y="-230" width="110" height="80" fill="rgba(80,150,230,.25)" stroke="#5a9be6" stroke-width="5"/><text x="355" y="-250" text-anchor="middle" font-family="Inter" font-weight="800" font-size="34" fill="#5a9be6">s6</text></svg></div>')]},
 "aufgabe":{"bg":BG,"layers":[
   ('lab1','<div class="L lab" style="left:140px;top:190px">Teil 1 · Gleitsitz</div>'),
   ('c1','<div class="L chip" style="left:140px;top:240px"><b>Ø25 H7/g6</b> – Spiel?</div>'),
   ('lab2','<div class="L lab" style="left:140px;top:390px">Teil 2 · Zahnrad-Schrumpfsitz</div>'),
   ('c2','<div class="L chip" style="left:140px;top:440px"><b>Ø60 H7/s6</b> · Stahl auf Stahl</div>'),
   ('c3','<div class="L chip" style="left:140px;top:555px">Fuge <b>50 mm</b> · Nabe <b>Ø120</b> · <b>M_t = 250 Nm</b></div>'),
   ('want','<div class="L want" style="left:140px;top:720px">Gesucht: Spiel bzw. Übermaß · Fugendruck · Drehmoment · Einpresskraft · Fügetemperatur</div>'),
   ('tri','<div class="L" style="left:1250px;top:240px"><svg width="640" height="620" viewBox="-60 -320 640 620"> <line x1="-40" y1="0" x2="560" y2="0" stroke="#94a4b2" stroke-width="3" stroke-dasharray="14 8"/> <text x="560" y="-14" text-anchor="end" font-family="Inter" font-weight="600" font-size="24" fill="#94a4b2">Nulllinie</text> <rect x="0" y="-130" width="110" height="130" fill="rgba(70,185,92,.22)" stroke="#46b95c" stroke-width="5"/> <text x="55" y="-150" text-anchor="middle" font-family="Inter" font-weight="800" font-size="34" fill="#46b95c">H7</text> <rect x="150" y="80" width="110" height="80" fill="rgba(80,150,230,.25)" stroke="#5a9be6" stroke-width="5"/><text x="205" y="200" text-anchor="middle" font-family="Inter" font-weight="800" font-size="34" fill="#5a9be6">g6</text><rect x="300" y="-230" width="110" height="80" fill="rgba(80,150,230,.25)" stroke="#5a9be6" stroke-width="5"/><text x="355" y="-250" text-anchor="middle" font-family="Inter" font-weight="800" font-size="34" fill="#5a9be6">s6</text></svg></div>')]},
 "outro":{"bg":BG,"layers":[
   ('brand','<div class="L brand" style="left:140px;top:220px"><i></i>DT-ProfiPassung</div>'),
   ('title','<h1 class="L" style="left:136px;top:290px">Jetzt <em>kostenlos</em> testen</h1>'),
   ('sub','<div class="L sub" style="left:140px;top:420px">Direkt im Browser · ohne Anmeldung · ohne Installation</div>'),
   ('url','<div class="L url" style="left:140px;top:530px">dietertepe.github.io/dt-profipassung-web</div>'),
   ('small','<div class="L small" style="left:140px;top:720px">Vollversion: <b>139 € einmalig</b> · kein Abo · läuft offline<br>dt-profidreieck.de</div>')]},
}
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome")
    pg=b.new_page(viewport={"width":1920,"height":1080})
    for name,c in cards.items():
        pg.set_content(f"<style>{CSS}</style>{c['bg']}"); pg.wait_for_timeout(200)
        pg.screenshot(path=f"/home/claude/y04/cards/{name}_bg.png")
        for lid,html in c["layers"]:
            pg.set_content(f"<style>{CSS}</style>{html}"); pg.wait_for_timeout(150)
            pg.screenshot(path=f"/home/claude/y04/cards/{name}_{lid}.png",omit_background=True)
        pg.set_content(f"<style>{CSS}</style>{c['bg']}{''.join(h for _,h in c['layers'])}"); pg.wait_for_timeout(200)
        pg.screenshot(path=f"/home/claude/y04/cards/{name}_full.png")
    b.close()
