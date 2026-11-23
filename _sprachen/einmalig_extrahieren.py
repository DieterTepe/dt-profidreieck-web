"""EINMALIG (bereits ausgefuehrt): holt das Woerterbuch aus der alten index.html,
stellt Portugiesisch auf Brasilien (pt-BR) um und speichert es als
_sprachen/uebersetzungen.json. Danach wird nur noch die JSON-Datei gepflegt."""
import json, re, subprocess, sys
from pathlib import Path

repo = Path(__file__).resolve().parent.parent
s = (repo / "index.html").read_text(encoding="utf-8")
i = s.index("var I18N = {"); k = s.index("var I18N_TITLE = {"); e = s.index("(function(){", k)
js = s[i:e] + "\nconsole.log(JSON.stringify({I18N, I18N_HTML}))"
Path("/tmp/_i18n.js").write_text(js, encoding="utf-8")
d = json.loads(subprocess.run(["node", "/tmp/_i18n.js"], capture_output=True, text=True, check=True).stdout)

# Portugal -> Brasil (Reihenfolge wichtig: lange Ausdruecke zuerst)
BR = [
    ("Verifica-se a si próprio – e diz-o", "Ele mesmo se verifica – e informa isso"),
    ("Qual a ferramenta certa para si?", "Qual é a ferramenta certa para você?"),
    ("Destina-se expressamente a ser partilhada – com colegas, formandos ou o gabinete ao lado.",
     "Pode ser compartilhada à vontade – com colegas, aprendizes ou o escritório ao lado."),
    ("O botão de compra leva-o", "O botão de compra leva você"),
    ("Ao clicar num botão de compra sai deste site; passam a aplicar-se",
     "Ao clicar em um botão de compra, você sai deste site; passam a valer"),
    ("A quem me dirijo em caso de dúvidas?", "Com quem falo em caso de dúvidas?"),
    ("Numa nave sem rede não ajudam de todo.", "Em um galpão sem rede, não ajudam em nada."),
    ("O refugo custa a dobrar", "O refugo custa em dobro"),
    ("enche facilmente uma tarde", "ocupa facilmente uma tarde"),
    ("logo a seguir", "logo em seguida"),
    ("pronto a importar", "pronto para importar"),
    ("não nas letras pequenas", "não nas letras miúdas"),
    ("Escreva «Ø50 H7/g6» – segundos depois tem", "Digite “Ø50 H7/g6” – segundos depois você tem"),
    ("pressuposto de preço", "premissa de preço"),
    ("Telemóvel", "Celular"), ("telemóvel", "celular"),
    ("Captura de ecrã", "Captura de tela"), ("no ecrã", "na tela"),
    ("Descarregamento imediato", "Download imediato"), ("para descarregar", "para download"),
    ("Após a transferência", "Após o download"),
    ("corre no browser", "roda no navegador"), ("no browser", "no navegador"),
    ("Introdução rápida", "Entrada rápida"), ("introdução rápida", "entrada rápida"),
    ("Da introdução ao resultado", "Da entrada ao resultado"), ("da introdução ao resultado", "da entrada ao resultado"),
    ("Introduza", "Digite"), ("introduzidos", "inseridos"),
    ("num único ficheiro", "em um único arquivo"), ("Um ficheiro", "Um arquivo"), ("um ficheiro", "um arquivo"),
    ("ficheiro", "arquivo"),
    ("num relance", "de relance"), ("num toque", "com um toque"), ("numa", "em uma"), ("num ", "em um "),
    ("rastreio", "rastreamento"), ("Porquê", "Por que"), ("fiáveis", "confiáveis"), ("poupam", "economizam"),
    ("não chegam", "não bastam"),
    ("soldadura", "soldagem"), ("Serralharia", "Serralheria"), ("Controlo", "Controle"),
    ("encurvadura", "flambagem"), ("gabinetes técnicos", "escritórios técnicos"),
    ("utilizadores", "usuários"), ("utilizador", "usuário"), ("não utiliza", "não usa"),
    ("binário", "torque"), ("veio-base", "eixo-base"), ("do veio", "do eixo"), ("veio", "eixo"),
    ("ligação por interferência", "ajuste por interferência"), ("Ligação por interferência", "Ajuste por interferência"),
    ("aparafusadas", "parafusadas"), ("afastamentos", "desvios"), ("Afastamentos", "Desvios"),
    ("com visto em cada passo", "com marca de verificação em cada passo"),
    ("um visto por passo", "uma marca de verificação por passo"), ("Um visto em falta", "Uma marca de verificação ausente"),
    ("guardar e abrir", "salvar e abrir"), ("Guardar e abrir", "Salvar e abrir"), ("guardar", "salvar"),
    ("guardados", "armazenados"), ("que guarda", "que salva"),
    ("registo", "cadastro"), ("Contacto", "Contato"), ("panorâmica", "visão geral"),
    ("formação", "treinamento"), ("face à norma", "em relação à norma"), ("face às normas", "em relação às normas"),
    ("Prefere experimentar primeiro?", "Prefere testar primeiro?"),
    ("A verificação aplica-se", "A verificação se aplica"),
    ("«", "“"), ("»", "”"),
]
def br(t):
    for a, b in BR:
        t = t.replace(a, b)
    return t

texte = {de: {"en": v[0], "pt": br(v[1])} for de, v in d["I18N"].items()}
html = {k: {"en": v["en"], "pt": br(v["pt"])} for k, v in d["I18N_HTML"].items()}
out = {"_hinweis": "Schluessel = deutscher Text aus index.html. Werte: en = Englisch (international), pt = Portugiesisch (Brasilien). Nach Aenderungen: python3 _sprachen/sprachen.py",
       "texte": texte, "html": html}
(repo / "_sprachen/uebersetzungen.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
geaendert = [(v[1], br(v[1])) for v in d["I18N"].values() if br(v[1]) != v[1]]
print("Texte:", len(texte), "| pt-BR angepasst:", len(geaendert))
