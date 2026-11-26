"""Y04 – Passung H7/g6 und Pressverband H7/s6. Rendert jede Szene als eigene MP4 (1920x1080, 30 fps)
und schreibt events.json (Zeitpunkte für Klicks, Tippen, Übergänge) für die Tonspur."""
import json, math, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1920, 1080, 30
BG = (19, 23, 28)
ACC = (52, 195, 212)
FG = (231, 238, 244)
MUTED = (148, 164, 178)
D = "/home/claude/y04/"
CAP = D + "cap/"
CARDS = D + "cards/"
OUT = D + "out/"
os.makedirs(OUT, exist_ok=True)
F_SEMI = ImageFont.truetype("/usr/share/fonts/opentype/inter/Inter-SemiBold.otf", 40)
F_SMALL = ImageFont.truetype("/usr/share/fonts/opentype/inter/Inter-Bold.otf", 22)
TL = json.load(open(CAP + "timeline.json"))



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
    def __init__(self):
        shots = TL["shots"]
        super().__init__("s3_ablauf", sum(s["hold"] for s in shots))
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


# ---------- Rechenweg: Aufklappen + ruhige Kamerafahrt ----------
class Rechenweg(Scene):
    def __init__(self):
        tr = Image.open(CAP + "weg.png").convert("RGBA")
        bg = Image.open(CARDS + "intro_bg.png").convert("RGBA")
        self.img = Image.new("RGBA", (W, tr.height + 260), BG + (255,))
        self.img.alpha_composite(bg.resize((W, self.img.height)))
        self.img.alpha_composite(tr, ((W - tr.width) // 2, 130))
        self.maxy = self.img.height - H

        def place(f):
            c = Image.open(CAP + f).convert("RGBA")
            im = bg.copy()
            im.alpha_composite(c, ((W - c.width) // 2, (H - 200 - c.height) // 2 + 20))
            return im
        self.hov, self.prs = place("weg_hov.png"), place("weg_prs.png")
        st = {s["t"]: s for s in TL["steps"]}

        def at(n, m=None):
            a = st[n]; b = st[m or n]
            c = (a["y"] + b["y"] + b["h"]) / 2
            return min(self.maxy, max(0, 130 + c * 2 - H / 2 + 60))
        self.pre = 1.6
        self.stops = [(at("6", "9"), 4.0, "Übermaß 23 … 72 µm → Übermaßpassung"),
                      (at("10", "13"), 3.6, "Rautiefen glätten: wirksames Übermaß 18,5 µm"),
                      (at("21", "23"), 4.0, "Fugendruck p = 24,3 … 88,6 N/mm²"),
                      (at("24", "27"), 3.6, "Sicherheit gegen Fließen S_F = 1,73"),
                      (at("28", "30"), 3.8, "Übertragbares Drehmoment M_t,max = 962 Nm"),
                      (at("31", "33"), 3.8, "Rutschsicherheit S_H = 3,85 · Einpresskraft 116,9 kN"),
                      (at("34", "36"), 4.0, "Fügen: Nabe auf 211,3 °C erwärmen")]
        self.move = 1.2
        dur = self.pre + sum(s[1] for s in self.stops) + self.move * (len(self.stops) - 1)
        super().__init__("s4_rechenweg", dur)
        self.plan, t = [], self.pre
        for i, (y, hold, c) in enumerate(self.stops):
            self.plan.append((t, t + hold, y, c))
            t += hold
            if i + 1 < len(self.stops):
                self.events.append(("swish", t))
                t += self.move
        self.events += [("whoosh", 0.05), ("click", 0.9)]

    def frame(self, t):
        if t < 0.9:
            return caption(self.hov, "Rechenweg aufklappen", cap_alpha(t, 0, 1.6))
        if t < self.pre:
            a = ease((t - 1.15) / 0.45)
            y0 = round(self.plan[0][2])
            im = self.prs if a <= 0 else Image.blend(self.prs, self.img.crop((0, y0, W, y0 + H)), a)
            return caption(im, "Rechenweg aufklappen", cap_alpha(t, 0, self.pre))
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
        if t < self.plan[0][0] + 0.001:
            y = self.plan[0][2]
        y = round(y)
        im = self.img.crop((0, y, W, y + H))
        return caption(im, cap, ca, "br")


def build():
    scenes = [
        Card("intro", 5.5, [("brand", 0.3, "f"), ("title", 0.55, "f"), ("sub", 0.95, "f"), ("tri", 0.6, "wipe")]),
        Card("aufgabe", 6.5, [("lab1", 0.2, "f"), ("c1", 0.45, "f"), ("lab2", 1.0, "f"), ("c2", 1.25, "f"), ("c3", 1.55, "f"),
                              ("want", 2.1, "f"), ("tri", 0.4, "wipe")],
             [("pop", 0.45), ("pop", 1.25), ("pop", 1.55)]),
        Eingabe(), Rechenweg(),
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
