"""Eigene, lizenzfreie Tonspur: ruhige Hintergrundmusik + dezente Bediengeräusche."""
import json
import numpy as np
from scipy.signal import fftconvolve, butter, sosfilt
from scipy.io import wavfile

SR = 48000
ev = json.load(open("/home/claude/y04/out/events.json"))
DUR = ev["dur"]
N = int(DUR * SR)
rng = np.random.default_rng(7)


def note(n):  # MIDI -> Hz
    return 440.0 * 2 ** ((n - 69) / 12)


def env_adsr(n, a, r, sus=1.0):
    e = np.ones(n) * sus
    na, nr = int(a * SR), int(r * SR)
    e[:na] = np.linspace(0, sus, na)
    if nr > 0:
        e[-nr:] *= np.linspace(1, 0, nr)
    return e


def lp(x, f, order=2):
    return sosfilt(butter(order, f, "low", fs=SR, output="sos"), x)


def bp(x, lo, hi):
    return sosfilt(butter(2, [lo, hi], "band", fs=SR, output="sos"), x)


L = np.zeros(N)
R = np.zeros(N)


def add(sig, t, gain=1.0, pan=0.0):
    i = int(t * SR)
    if i >= N:
        return
    s = sig[: N - i] * gain
    L[i:i + len(s)] += s * np.sqrt(0.5 * (1 - pan))
    R[i:i + len(s)] += s * np.sqrt(0.5 * (1 + pan))


# ---------------- Musik ----------------
BPM = 88
beat = 60 / BPM
bar = 4 * beat
# D-Dur, ruhig: Dmaj9 – Bm9 – Gmaj7(#11) – Asus4/A
chords = [[50, 57, 61, 64, 66, 69], [47, 54, 57, 61, 62, 66], [43, 50, 54, 57, 61, 62], [45, 52, 57, 59, 62, 64]]
roots = [38, 35, 31, 33]
t, k = 0.0, 0
while t < DUR + bar:
    ch = chords[k % 4]
    dur = 2 * bar
    n = int((dur + 2.5) * SR)
    tt = np.arange(n) / SR
    pad = np.zeros(n)
    for m in ch[1:]:
        for det in (-0.06, 0.06):
            f = note(m + det)
            pad += np.sin(2 * np.pi * f * tt) + 0.25 * np.sin(4 * np.pi * f * tt) + 0.08 * np.sin(6 * np.pi * f * tt)
    pad = lp(pad, 2200) * env_adsr(n, 1.6, 2.6) * 0.022
    add(pad, t, 1.0, -0.25 if k % 2 else 0.25)
    add(pad, t + 0.013, 0.8, 0.25 if k % 2 else -0.25)
    # Bass
    b = np.sin(2 * np.pi * note(roots[k % 4]) * tt) + 0.3 * np.sin(4 * np.pi * note(roots[k % 4]) * tt)
    add(lp(b, 400) * env_adsr(n, 0.4, 2.0) * 0.06, t)
    # Arpeggio (ab dem 2. Takt), Achtel, sanfte Zupfklänge
    if t > bar * 0.9:
        pat = [ch[1] + 12, ch[3] + 12, ch[2] + 12, ch[4] + 12, ch[3] + 12, ch[5] + 12, ch[4] + 12, ch[3] + 12]
        for j in range(16):
            m = pat[j % 8]
            nn = int(1.2 * SR)
            ts = np.arange(nn) / SR
            f = note(m)
            pl = (np.sin(2 * np.pi * f * ts) + 0.35 * np.sin(4 * np.pi * f * ts) * np.exp(-ts * 9)) * np.exp(-ts * 4.2)
            pl[: int(0.004 * SR)] *= np.linspace(0, 1, int(0.004 * SR))
            add(pl * (0.018 if j % 2 else 0.024), t + j * beat / 2, 1.0, 0.35 * np.sin(j))
    # leichte Rhythmik (nicht im Vorspann)
    if 5.0 < t < DUR - 6:
        for j in range(8):
            tb = t + j * beat
            if j % 2 == 0:  # weicher Kick
                nn = int(0.35 * SR)
                ts = np.arange(nn) / SR
                kk = np.sin(2 * np.pi * (55 + 70 * np.exp(-ts * 30)) * ts) * np.exp(-ts * 9)
                add(kk * 0.10, tb)
            nn = int(0.09 * SR)  # Shaker auf Offbeat
            sh = bp(rng.standard_normal(nn), 6000, 11000) * np.exp(-np.arange(nn) / SR * 45)
            add(sh * 0.010, tb + beat / 2, 1.0, 0.4)
    t += dur
    k += 1

# Hall
ir_n = int(2.8 * SR)
ir_t = np.arange(ir_n) / SR
irL = rng.standard_normal(ir_n) * np.exp(-ir_t * 2.4)
irR = rng.standard_normal(ir_n) * np.exp(-ir_t * 2.4)
irL, irR = lp(irL, 5000), lp(irR, 5000)
irL /= np.sqrt(np.sum(irL ** 2)); irR /= np.sqrt(np.sum(irR ** 2))
wetL = fftconvolve(L, irL)[:N]
wetR = fftconvolve(R, irR)[:N]
L = L * 0.75 + wetL * 0.45
R = R * 0.75 + wetR * 0.45

# Ein- und Ausblenden der Musik
fi, fo = int(1.2 * SR), int(3.5 * SR)
L[:fi] *= np.linspace(0, 1, fi); R[:fi] *= np.linspace(0, 1, fi)
L[-fo:] *= np.linspace(1, 0, fo) ** 1.5; R[-fo:] *= np.linspace(1, 0, fo) ** 1.5

# ---------------- Geräusche ----------------
def sfx(kind):
    if kind == "click":
        nn = int(0.06 * SR); ts = np.arange(nn) / SR
        s = np.sin(2 * np.pi * 1900 * ts) * np.exp(-ts * 90) * 0.5 + bp(rng.standard_normal(nn), 2500, 7000) * np.exp(-ts * 160) * 0.35
        return s * 0.55
    if kind == "type":
        nn = int(0.04 * SR); ts = np.arange(nn) / SR
        return bp(rng.standard_normal(nn), 2000, 6000) * np.exp(-ts * 180) * 0.25
    if kind == "pop":
        nn = int(0.18 * SR); ts = np.arange(nn) / SR
        f = 620 + 380 * (1 - np.exp(-ts * 40))
        return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-ts * 22) * 0.22
    if kind == "chime":
        nn = int(2.2 * SR); ts = np.arange(nn) / SR
        s = np.zeros(nn)
        for m, g in [(81, 1.0), (85, 0.6), (88, 0.45), (93, 0.25)]:
            s += g * np.sin(2 * np.pi * note(m) * ts) * np.exp(-ts * (2.2 + m / 60))
        s[: int(0.003 * SR)] *= np.linspace(0, 1, int(0.003 * SR))
        return s * 0.09
    if kind in ("whoosh", "swish"):
        d = 0.7 if kind == "whoosh" else 0.5
        nn = int(d * SR); ts = np.arange(nn) / SR
        nz = rng.standard_normal(nn)
        out = np.zeros(nn)
        seg = nn // 8
        for i in range(8):  # Bandpass wandert nach oben
            c = 400 * 2 ** (i * 0.5)
            out[i * seg:(i + 1) * seg] = bp(nz, c, c * 2.5)[i * seg:(i + 1) * seg]
        e = np.sin(np.pi * ts / d) ** 2
        return out * e * (0.06 if kind == "whoosh" else 0.035)
    return np.zeros(1)


for kind, t in ev["events"]:
    add(sfx(kind), max(0, t - (0.15 if kind in ("whoosh", "swish") else 0)), 1.0, 0.1)

st = np.stack([L, R], 1)
st /= max(1e-9, np.abs(st).max()) / 0.8
wavfile.write("/home/claude/y04/out/ton_roh.wav", SR, (st * 32767).astype(np.int16))
print("ok", round(DUR, 2), "s")
