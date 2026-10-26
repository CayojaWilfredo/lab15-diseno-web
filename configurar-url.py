#!/usr/bin/env python3
"""Actualiza una copia local; no hace push ni publica."""
from pathlib import Path
from urllib.parse import urlsplit
import sys,re,json
root=Path(__file__).resolve().parent
if len(sys.argv)!=2: raise SystemExit('Uso: python configurar-url.py https://usuario.github.io/repositorio/')
url=sys.argv[1].rstrip('/')+'/'
u=urlsplit(url)
if u.scheme!='https' or not u.netloc or u.query or u.fragment or any(c in url for c in '<>"\' '): raise SystemExit('Usa una URL HTTPS pública válida, sin consulta ni fragmento.')
config=root/'publicacion.json'
old=json.loads(config.read_text())['url'] if config.exists() else 'https://senderossamaipata.example/'
for p in root.rglob('*'):
 if '.git' in p.parts or not p.is_file() or p.suffix not in ('.html','.xml','.txt'): continue
 text=p.read_text(encoding='utf-8');text=text.replace(old,url)
 if p==root/'404.html':
  text=re.sub(r'<base\s+[^>]*>\s*','',text)
  text=text.replace('<meta charset="UTF-8">','<meta charset="UTF-8">\n  <base href="'+u.path+'">')
 p.write_text(text,encoding='utf-8')
config.write_text(json.dumps({'url':url},indent=2),encoding='utf-8')
print('Metadatos actualizados. Revisa cambios, completa README y crea tu segundo commit.')
