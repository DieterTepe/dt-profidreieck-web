from playwright.sync_api import sync_playwright
import json
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome")
    pg=b.new_page(viewport={"width":1920,"height":1080},device_scale_factor=2)
    pg.goto("file:///home/claude/dietertepe/test-dreieck/DT-ProfiDreieck_Test_1-1-0.html"); pg.wait_for_timeout(1200)
    for k,v in [("Länge a","7"),("Länge b","5"),("Länge c","6")]:
        pg.locator(f'#wizOverlay .pill[title="{k}"]').click(); pg.wait_for_timeout(300); pg.keyboard.type(v); pg.keyboard.press("Enter"); pg.wait_for_timeout(400)
    pg.wait_for_timeout(800); pg.evaluate("scrollTo(0,0)")
    d=pg.evaluate("""()=>{const c=document.querySelector('#resultCard').getBoundingClientRect();const o={};
      document.querySelectorAll('#resultCard .res').forEach(r=>{const k=r.querySelector('.k')?.textContent.trim();const b=r.getBoundingClientRect();o[k]=[b.left-c.left,b.top-c.top,b.width,b.height]});
      const t=document.querySelector('#traceToggle').getBoundingClientRect();o.toggle=[t.left-c.left,t.top-c.top,t.width,t.height];return o}""")
    json.dump(d,open("cap/tiles.json","w"),ensure_ascii=False); print(d)
    b.close()
