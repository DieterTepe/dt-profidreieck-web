import render as R
TL=R.TL; sh=TL["shots"]; k=next(i for i,x in enumerate(sh) if x["f"]=="in_done.jpg")+1
cues=[]
def add(t0,t1,txt):
    if cues and cues[-1][2]==txt and abs(cues[-1][1]-t0)<0.05: cues[-1][1]=t1
    else: cues.append([t0,t1,txt])
T=0
add(0.3,5.4,"Vom Werkstück zur DXF – Knotenblech mit DT-ProfiDreieck berechnen, Kontur prüfen und als DXF in echten Millimetern an Laser oder CNC"); T=5.5
add(T+0.1,T+5.9,"Werkstück: Knotenblech. Kante a = 400 mm, Kante b = 250 mm, Winkel dazwischen γ = 70°. Gesucht: dritte Kante c, Winkel α und β, Fläche – und die DXF für den Zuschnitt"); T+=6.0
def shots(lst,T):
    for s in lst:
        if s["cap"]: add(T,T+s["hold"],s["cap"])
        T+=s["hold"]
    return T
T=shots(sh[:k],T)
E=R.Ergebnis(); add(T,T+1.0,"Alle Werte auf einen Blick")
for i,(t0,_,lab) in enumerate(E.hl):
    t1=E.hl[i+1][0] if i+1<len(E.hl) else 6.4; add(T+t0,T+t1,lab)
add(T+6.4,T+E.dur,"Rechenweg aufklappen"); T+=E.dur
Rw=R.Rechenweg()
for (t0,t1,y,c) in Rw.plan:
    if c: add(T+t0,T+t1,c)
T+=Rw.dur
T=shots(sh[k:],T)
add(T,T+2.3,"Inhalt der DXF-Datei: die Kontur – so fährt der Laser"); add(T+2.4,T+7.5,"Echte Millimeter, getrennte Ebenen – direkt für CAD und CNC"); T+=7.5
add(T+0.3,T+8.0,"Jetzt kostenlos testen: dietertepe.github.io/test-dreieck – Vollversion 69 € einmalig, mit DXF-, SVG- und PDF-Export"); T+=8.0
f=lambda t:f"{int(t//3600):02d}:{int(t%3600//60):02d}:{t%60:06.3f}"
o=["WEBVTT",""]
for i,(a,b,t) in enumerate(cues,1): o+= [str(i),f"{f(a)} --> {f(b)}",t,""]
open("out/y02.de.vtt","w",encoding="utf-8").write("\n".join(o))
print(round(T,2)); [print(round(a,1),round(b,1),t) for a,b,t in cues]
