# Publicación — realizar en tu cuenta
1. Copia img y video al lado de index.html. Abre SOLO esta carpeta en VS Code. No subas el ZIP completo ni las cuatro carpetas como si fueran un solo sitio.
2. Instala Git y verifica `git --version`. Configura tu nombre y correo de GitHub (puedes usar tu dirección noreply).
3. En la terminal de esta carpeta:
```sh
git init -b main
git config user.name "Wilfredo Jose Cayoja Medina"
git config user.email "TU-CORREO-DE-GITHUB"
git add .
git status
git commit -m "Preparar sitio de Senderos Samaipata para publicación"
```
Revisa que no aparezcan img/originales ni datos privados.
4. En GitHub crea senderos-samaipata, público y sin README inicial. Reemplaza TU-USUARIO:
```sh
git remote add origin https://github.com/TU-USUARIO/senderos-samaipata.git
git push -u origin main
```
Si ya existe repositorio local no repitas init ni remote add: consulta git status y git remote -v antes.
5. Settings > Pages > Deploy from a branch > main > /(root) > Save. Usa la URL que GitHub realmente muestre.
6. Actualiza las URL desde esta carpeta (Python instalado; en Windows puedes usar py):
```sh
python configurar-url.py https://TU-USUARIO.github.io/senderos-samaipata/
```
Alternativa sin Python: reemplaza `https://senderossamaipata.example/` por la URL real en todos los HTML, sitemap y robots; en 404.html agrega después de meta charset `<base href="/senderos-samaipata/">`. Si usas otro repositorio o dominio, ajusta el prefijo.
7. Completa la URL del README y crea el segundo commit:
```sh
git add .
git diff --cached
git commit -m "Configurar URL pública y página 404 para GitHub Pages"
git push
git log --oneline
```
8. En el celular con datos móviles: portada, todas las páginas, imágenes, menú, formulario de prueba. Abre /senderos-samaipata/no/existe/pagina.html: debe mostrar 404 con estilos y enlaces correctos. Ejecuta PageSpeed Insights y guarda resultados reales. Revisa la imagen Open Graph antes de compartir.

No se ha creado ni publicado un repositorio por vos. Los dos commits y las evidencias deben existir en tu cuenta.
