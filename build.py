import csv, html, pathlib, datetime
ROOT=pathlib.Path(__file__).parent
OUT=ROOT/'docs'; OUT.mkdir(exist_ok=True)
rows=list(csv.DictReader((ROOT/'products.csv').open(encoding='utf-8')))
items=[]
for p in rows:
    if p['approved'].strip().lower()!='yes': continue
    if not p['url'].startswith('https://'): continue
    title=html.escape(p['title']); category=html.escape(p['category']); desc=html.escape(p['description']); url=html.escape(p['url'],quote=True)
    items.append(f'<article><h2>{title}</h2><p>{category}</p><p>{desc}</p><a href="{url}" rel="sponsored nofollow noopener" target="_blank">Zum Anbieter (Werbelink)</a></article>')
body='\n'.join(items) or '<p>Noch keine geprüften Angebote veröffentlicht.</p>'
page=f'''<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>FitProduktRadar</title><style>body{{font:17px system-ui;max-width:760px;margin:3rem auto;padding:0 1rem;line-height:1.6}}article{{border:1px solid #ddd;padding:1rem;margin:1rem 0;border-radius:12px}}a{{color:#075985}}</style></head><body><h1>FitProduktRadar</h1><p>Unabhängig zusammengestellte Produktinformationen für Heimtraining. Angebote sind keine medizinischen Empfehlungen.</p><p><strong>Werbehinweis:</strong> Mit gekennzeichneten Werbelinks können wir eine Provision erhalten. Für dich entstehen dadurch normalerweise keine zusätzlichen Kosten.</p>{body}<footer><p>Stand: {datetime.date.today().isoformat()}. Produktpreise und Verfügbarkeit bitte beim Anbieter prüfen.</p><p><strong>Vor öffentlicher Veröffentlichung erforderlich:</strong> Impressum und Datenschutzhinweise ergänzen.</p></footer></body></html>'''
(OUT/'index.html').write_text(page,encoding='utf-8')
print(f'Erstellt: {len(items)} freigegebene Produkte')
# Walking-Pad-Ratgeber einbinden
import shutil

ratgeber = ROOT / "walking-pad-mietwohnung.html"

if ratgeber.exists():
    shutil.copy2(
        ratgeber,
        OUT / "walking-pad-mietwohnung.html"
    )

    startseite = OUT / "index.html"
    inhalt = startseite.read_text(encoding="utf-8")

    link = (
        '<section><h2>Unsere Ratgeber</h2>'
        '<p><a href="walking-pad-mietwohnung.html">'
        'Walking Pad in der Mietwohnung: '
        'Lautstärke und Trittschall</a></p></section>'
    )

    inhalt = inhalt.replace("</body>", link + "</body>")
    startseite.write_text(inhalt, encoding="utf-8")
