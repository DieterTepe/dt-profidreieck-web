"""Y02 – Vom Werkstück zur DXF (Knotenblech, Vollversion). Rendert jede Szene als eigene MP4 (1920x1080, 30 fps)
und schreibt events.json (Zeitpunkte für Klicks, Tippen, Übergänge) für die Tonspur."""
import json, math, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1920, 1080, 30
BG = (19, 23, 28)
ACC = (52, 195, 212)
FG = (231, 238, 244)
MUTED = (148, 164, 178)
D = "/home/claude/y02/"
CAP = D + "cap/"
CARDS = D + "cards/"
OUT = D + "out/"
os.makedirs(OUT, exist_ok=True)
F_SEMI = ImageFont.truetype("/usr/share/fonts/opentype/inter/Inter-SemiBold.otf", 40)
F_SMALL = ImageFont.truetype("/usr/share/fonts/opentype/inter/Inter-Bold.otf", 22)
TL = json.load(open(CAP + "timeline.json"))
TILES = TL["tiles"]


def ease(x):
    x = max(0.0, min(1.0, x))
    return x * x * (3 - 2 * x)


def ease_out(x):
    x = max(0.0, min(1.0, x))
    return 1 - (1 - x) ** 3


class Scene:
    def __init__(self, name, dur):
        self.name, self.dur, self.events = name, dur, []

    def frames(self):
        raise NotImplementedError

    def render(self):
        n = round(self.dur * FPS)
        tmp = OUT + self.name + ".part.mp4"
        p = subprocess.Popen(
            ["ffmpeg", "-loglevel", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24",
             "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "veryfast",
             "-crf", "18", "-pix_fmt", "yuv420p", "-r", str(FPS), tmp], stdin=subprocess.PIPE)
        fade = 0.35
        bgimg = Image.new("RGB", (W, H), BG)
        for i in range(n):
            t = i / FPS
            im = self.frame(t).convert("RGB")
            a = min(1.0, t / fade, (self.dur - t) / fade)
            if a < 1:
                im = Image.blend(bgimg, im, ease(max(0, a)))
            p.stdin.write(im.tobytes())
        p.stdin.close()
        if p.wait() != 0:
            sys.exit("ffmpeg failed " + self.name)
        os.replace(tmp, OUT + self.name + ".mp4")


# ---------- Bildunterschrift (unten links) ----------
def caption(im, text, alpha, pos="bl"):
    if not text or alpha <= 0:
        return im
    layer = Image.new("RGBA", im.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    tw = d.textlength(text, font=F_SEMI)
    x0, y0 = 96, H - 168
    if pos == "br":
        x0 = W - 96 - (tw + 76)
    box = (x0, y0, x0 + tw + 76, y0 + 84)
    d.rounded_rectangle(box, 18, fill=(15, 20, 26, int(232 * alpha)), outline=(50, 62, 73, int(255 * alpha)), width=2)
    d.rounded_rectangle((x0, y0, x0 + 9, y0 + 84), 4, fill=ACC + (int(255 * alpha),))
    d.text((x0 + 40, y0 + 42), text, font=F_SEMI, fill=FG + (int(255 * alpha),), anchor="lm")
    return Image.alpha_composite(im.convert("RGBA"), layer)


def cap_alpha(t, t0, t1, k=0.25):
    return min(ease((t - t0) / k), ease((t1 - t) / k) if t1 is not None else 1)


# ---------- Karten mit Ebenen ----------
class Card(Scene):
    def __init__(self, name, dur, layers, events=None):
        super().__init__(name, dur)
        self.bg = Image.open(CARDS + name + "_bg.png").convert("RGBA")
        self.layers = [(Image.open(CARDS + f"{name}_{lid}.png").convert("RGBA"), t0, kind) for lid, t0, kind in layers]
        self.events = [("whoosh", 0.05)] + (events or [])

    def frame(self, t):
        # sanfte Kamerafahrt: 1.00 -> 1.03
        im = self.bg.copy()
        for lay, t0, kind in self.layers:
            x = ease_out((t - t0) / 0.7)
            if x <= 0:
                continue
            if kind == "wipe":  # Dreieck von links nach rechts aufdecken
                mask = Image.new("L", lay.size, 0)
                ImageDraw.Draw(mask).rectangle((0, 0, int(W * x), H), fill=255)
                l2 = lay.copy()
                l2.putalpha(Image.composite(lay.getchannel("A"), mask, mask))
                im.alpha_composite(l2)
            else:
                l2 = lay.copy()
                l2.putalpha(lay.getchannel("A").point(lambda v, a=x: int(v * a)))
                im.alpha_composite(l2, (0, int(28 * (1 - x))))
        z = 1 + 0.03 * (t / self.dur)
        if z > 1.0005:
            cw, ch = W / z, H / z
            im = im.resize((W, H), Image.BICUBIC, box=((W - cw) / 2, (H - ch) / 2, (W + cw) / 2, (H + ch) / 2))
        return im


# ---------- Eingabe: Bildschirmfotos mit Kamera ----------
class Eingabe(Scene):
    def __init__(self, name, shots):
        super().__init__(name, sum(s["hold"] for s in shots))
        self.items, t = [], 0.0
        self.src = {}
        for s in shots:
            if s["f"] not in self.src:
                self.src[s["f"]] = Image.open(CAP + s["f"])
            z = s["z"]
            cw, ch = 1920 / z, 1080 / z
            cx = min(max(s["fx"], cw / 2), 1920 - cw / 2)
            cy = min(max(s["fy"], ch / 2), 1080 - ch / 2)
            box = tuple(v * 2 for v in (cx - cw / 2, cy - ch / 2, cx + cw / 2, cy + ch / 2))
            img = self.src[s["f"]].resize((W, H), Image.LANCZOS, box=box).convert("RGBA")
            self.items.append((t, t + s["hold"], img, s["cap"], box, s["f"], s.get("pan")))
            if s["ev"] in ("click", "pop", "chime"):
                self.events.append((s["ev"], t))
            if s["ev"] == "type":
                self.events.append(("type", t - 0.05))
            t += s["hold"]
        self.events.append(("whoosh", 0.05))
        self.caps = []
        for it in self.items:
            t0, t1, c = it[0], it[1], it[3]
            if self.caps and self.caps[-1][2] == c:
                self.caps[-1][1] = t1
            else:
                self.caps.append([t0, t1, c])

    def frame(self, t):
        for i, it in enumerate(self.items):
            if it[0] <= t < it[1]:
                break
        t0, t1, img, _, box, f, pan = it
        im = img
        if pan and i > 0 and self.items[i - 1][5] == f and t - t0 < 0.7:
            pb = self.items[i - 1][4]
            k = ease((t - t0) / 0.7)
            bx = tuple(a + (b - a) * k for a, b in zip(pb, box))
            im = self.src[f].resize((W, H), Image.BICUBIC, box=bx).convert("RGBA")
        for c0, c1, c in self.caps:
            if c0 <= t < c1:
                im = caption(im, c, cap_alpha(t, c0, c1, 0.18), "br")
        return im


# ---------- Ergebnis-Karte mit Hervorhebungen ----------
class Ergebnis(Scene):
    def __init__(self):
        super().__init__("s4_ergebnis", 8.0)
        self.cards = {k: Image.open(CAP + f).convert("RGBA") for k, f in
                      [("n", "erg_card.png"), ("h", "erg_card_hov.png"), ("p", "erg_card_prs.png")]}
        cw, ch = self.cards["n"].size
        self.s = min((W - 80) / cw, (H - 200) / ch)
        self.size = (round(cw * self.s), round(ch * self.s))
        self.off = ((W - self.size[0]) // 2, 24)
        self.bg = Image.open(CARDS + "intro_bg.png").convert("RGBA")
        self.base = {k: self._place(v) for k, v in self.cards.items()}
        self.hl = [(1.0, ["Seite c"], "Dritte Kante c = 392,55 mm"),
                   (2.9, ["Winkel α", "Winkel β"], "Winkel α = 73,24° · β = 36,76°"),
                   (4.5, ["Fläche"], "Fläche A = 46.984,63 mm²")]
        self.events = [("whoosh", 0.05)] + [("pop", t) for t, _, _ in self.hl] + [("click", 6.95)]

    def _place(self, c):
        im = self.bg.copy()
        im.alpha_composite(c.resize(self.size, Image.LANCZOS), self.off)
        return im

    def frame(self, t):
        key = "n" if t < 6.5 else ("h" if t < 6.95 else "p")
        im = self.base[key].copy()
        cap = "Alle Werte auf einen Blick"
        k = 2 * self.s
        for i, (t0, names, label) in enumerate(self.hl):
            t1 = self.hl[i + 1][0] if i + 1 < len(self.hl) else 6.4
            if t0 <= t < t1:
                a = cap_alpha(t, t0, t1, 0.25)
                lay = Image.new("RGBA", im.size, (0, 0, 0, 0))
                d = ImageDraw.Draw(lay)
                for nm in names:
                    x, y, w, h = TILES[nm]
                    bx = (self.off[0] + x * k - 6, self.off[1] + y * k - 6, self.off[0] + (x + w) * k + 6, self.off[1] + (y + h) * k + 6)
                    d.rounded_rectangle(bx, 16, outline=ACC + (int(255 * a),), width=6)
                glow = lay.filter(ImageFilter.GaussianBlur(10))
                im = Image.alpha_composite(Image.alpha_composite(im, glow), lay)
                cap = label
        if t >= 6.4:
            cap = "Rechenweg aufklappen"
        return caption(im, cap, 1.0)


# ---------- Rechenweg: ruhige Kamerafahrt ----------
class Rechenweg(Scene):
    def __init__(self):
        tr = Image.open(CAP + "trace.png").convert("RGBA")  # 1820 breit (2x)
        bg = Image.open(CARDS + "intro_bg.png").convert("RGBA")
        self.img = Image.new("RGBA", (W, tr.height + 260), BG + (255,))
        self.img.alpha_composite(bg.resize((W, self.img.height)))
        self.img.alpha_composite(tr, ((W - tr.width) // 2, 130))
        self.maxy = self.img.height - H
        st = {s["t"]: s for s in TL["steps"]}

        def at(title, frac=0.5):
            s = st[title]
            return min(self.maxy, max(0, 130 + (s["y"] + s["h"] * frac) * 2 - H / 2))
        self.stops = [(at("Seite c (Kosinussatz)"), 4.4, "Dritte Kante mit dem Kosinussatz: c = 392,55 mm"),
                      (at("Winkel α (Kosinussatz)"), 3.6, "Winkel α = 73,24°"),
                      (at("Probe: Winkelsumme"), 3.6, "Winkel β = 36,76° – Probe: Summe 180°"),
                      (at("Fläche A (Heron)"), 4.2, "Fläche nach Heron: A = 46.984,63 mm²")]
        self.move = 1.3
        dur = sum(s[1] for s in self.stops) + self.move * (len(self.stops) - 1)
        super().__init__("s5_rechenweg", dur)
        self.plan, t = [], 0.0
        for i, (y, hold, c) in enumerate(self.stops):
            self.plan.append((t, t + hold, y, c))
            t += hold
            if i + 1 < len(self.stops):
                self.events.append(("swish", t))
                t += self.move
        self.events.append(("whoosh", 0.05))

    def frame(self, t):
        y, cap, ca = 0, None, 0
        for i, (t0, t1, yy, c) in enumerate(self.plan):
            if t < t0:
                p0 = self.plan[i - 1]
                y = p0[2] + (yy - p0[2]) * ease((t - p0[1]) / self.move)
                break
            if t0 <= t < t1:
                y, cap, ca = yy, c, cap_alpha(t, t0, t1, 0.3)
                break
        else:
            y = self.plan[-1][2]
        y = round(y)
        im = self.img.crop((0, y, W, y + H))
        return caption(im, cap, ca, "br")


# ---------- DXF-Vorschau ----------
class CAD(Scene):
    def __init__(self):
        super().__init__("s8_dxf", 7.5)
        self.fr = [Image.open(D + f"cad/f{i:03d}.png").convert("RGBA") for i in range(46)]
        self.fin = Image.open(D + "cad/final.png").convert("RGBA")
        self.events = [("whoosh", 0.05), ("swish", 0.6), ("pop", 2.4)]

    def frame(self, t):
        if t < 0.5:
            im = self.fr[0]
        elif t < 2.0:
            im = self.fr[min(45, int((t - 0.5) / 1.5 * 45))]
        elif t < 2.4:
            im = Image.blend(self.fr[45], self.fin, ease((t - 2.0) / 0.4))
        else:
            im = self.fin
        if t < 2.3:
            return caption(im, "Inhalt der DXF-Datei: die Kontur – so fährt der Laser", cap_alpha(t, 0.2, 2.3))
        return caption(im, "Echte Millimeter, getrennte Ebenen – direkt für CAD und CNC", cap_alpha(t, 2.4, None))


def build():
    sh = TL["shots"]
    k = next(i for i, x in enumerate(sh) if x["f"] == "in_done.jpg") + 1
    scenes = [
        Card("intro", 5.5, [("brand", 0.3, "f"), ("title", 0.55, "f"), ("sub", 0.95, "f"), ("tri", 0.6, "wipe")]),
        Card("aufgabe", 6.0, [("lab1", 0.2, "f"), ("c1", 0.45, "f"), ("c2", 0.7, "f"), ("c3", 0.95, "f"),
                              ("lab2", 1.5, "f"), ("want", 1.7, "f"), ("tri", 0.4, "wipe")],
             [("pop", 0.45), ("pop", 0.7), ("pop", 0.95)]),
        Eingabe("s3_eingabe", sh[:k]), Ergebnis(), Rechenweg(), Eingabe("s7_zeichnung_dxf", sh[k:]), CAD(),
        Card("outro", 8.0, [("brand", 0.3, "f"), ("title", 0.5, "f"), ("sub", 0.9, "f"), ("url", 1.3, "f"), ("small", 1.8, "f")],
             [("chime", 1.3)]),
    ]
    only = sys.argv[1:]  # z. B. "s4_ergebnis"
    ev, t0, lst = [], 0.0, []
    for s in scenes:
        if not only or s.name in only:
            print("render", s.name, round(s.dur, 2), flush=True)
            s.render()
        ev += [(k, round(t0 + t, 3)) for k, t in s.events]
        lst.append(f"file '{OUT}{s.name}.mp4'")
        t0 += round(s.dur * FPS) / FPS
    open(OUT + "list.txt", "w").write("\n".join(lst) + "\n")
    json.dump({"events": sorted(ev, key=lambda e: e[1]), "dur": t0}, open(OUT + "events.json", "w"), indent=1)
    print("total", round(t0, 2))


if __name__ == "__main__":
    build()
