# Informe de calidad — preparado, pendiente de mediciones
Autor: Wilfredo Jose Cayoja Medina. Fecha de ejecución: pendiente.
No se han inventado puntuaciones Lighthouse, validaciones W3C ni pruebas con usuarios.

## 1. Lighthouse móvil
Anota versión del navegador/Lighthouse y fecha. Usa Live Server. Audita el sitio con tus img/video reales; emula tema en DevTools > Rendering > prefers-color-scheme y recarga.
Para el antes del sitio usa Lab 12; para la práctica usa practica-auditoria-antes.html. Después: Lab 13. Guarda HTML/JSON y captura de cada auditoría.

| Página | Tema | Fase | Rendimiento | Accesibilidad | Buenas prácticas | SEO | LCP | CLS | Peso |
|---|---|---|---|---|---|---|---|---|---|
| index | claro | antes | pendiente | pendiente | pendiente | pendiente | pendiente | pendiente | pendiente |
| index | claro | después | pendiente | pendiente | pendiente | pendiente | pendiente | pendiente | pendiente |
| index | oscuro | antes | pendiente | pendiente | pendiente | pendiente | pendiente | pendiente | pendiente |
| index | oscuro | después | pendiente | pendiente | pendiente | pendiente | pendiente | pendiente | pendiente |
| tours | claro | antes | pendiente | pendiente | pendiente | pendiente | pendiente | pendiente | pendiente |
| tours | claro | después | pendiente | pendiente | pendiente | pendiente | pendiente | pendiente | pendiente |
| tours | oscuro | antes | pendiente | pendiente | pendiente | pendiente | pendiente | pendiente | pendiente |
| tours | oscuro | después | pendiente | pendiente | pendiente | pendiente | pendiente | pendiente | pendiente |
| contacto | claro | antes | pendiente | pendiente | pendiente | pendiente | pendiente | pendiente | pendiente |
| contacto | claro | después | pendiente | pendiente | pendiente | pendiente | pendiente | pendiente | pendiente |
| contacto | oscuro | antes | pendiente | pendiente | pendiente | pendiente | pendiente | pendiente | pendiente |
| contacto | oscuro | después | pendiente | pendiente | pendiente | pendiente | pendiente | pendiente | pendiente |
| nosotros | claro | antes | pendiente | pendiente | pendiente | pendiente | pendiente | pendiente | pendiente |
| nosotros | claro | después | pendiente | pendiente | pendiente | pendiente | pendiente | pendiente | pendiente |
| nosotros | oscuro | antes | pendiente | pendiente | pendiente | pendiente | pendiente | pendiente | pendiente |
| nosotros | oscuro | después | pendiente | pendiente | pendiente | pendiente | pendiente | pendiente | pendiente |
| practica-auditoria | claro | antes | pendiente | pendiente | pendiente | pendiente | pendiente | pendiente | pendiente |
| practica-auditoria | claro | después | pendiente | pendiente | pendiente | pendiente | pendiente | pendiente | pendiente |
| practica-auditoria | oscuro | antes | pendiente | pendiente | pendiente | pendiente | pendiente | pendiente | pendiente |
| practica-auditoria | oscuro | después | pendiente | pendiente | pendiente | pendiente | pendiente | pendiente | pendiente |

## 2. Nueve correcciones implementadas en la práctica
| Hallazgo del código | Criterio | Corrección | Verificación real |
|---|---|---|---|
| Título genérico Promo | SEO: title descriptivo | Título específico | Pendiente de auditoría |
| Sin meta description | SEO: descripción | Descripción de la promoción | Pendiente de auditoría |
| Salto h1 a h4 | WCAG 1.3.1 | h2 dentro de section | Pendiente de auditoría |
| Imagen de cascada sin alt | WCAG 1.1.1 | Descripción de la imagen | Pendiente de auditoría |
| Imagen sin dimensiones | CLS | width y height | Pendiente de auditoría |
| Texto gris de poco contraste | WCAG 1.4.3 | Token color-texto | Pendiente de auditoría |
| Precio dorado sobre claro | WCAG 1.4.3 | Token color-tierra | Pendiente de auditoría |
| Enlace clic aquí sin propósito claro | WCAG 2.4.4 | Consultar la promoción de Las Cuevas | Pendiente de auditoría |
| Botón de icono sin nombre ni función | WCAG 4.1.2 / funcionalidad | Enlace al inicio con texto y alt vacío decorativo | Pendiente de auditoría |

## 3. W3C
Sube index.html y nosotros.html a validator.w3.org, luego revisa las ocho páginas. Sube css/estilos.css a jigsaw.w3.org/css-validator. Registra errores, advertencias, fecha y captura. No declares una advertencia falso positivo sin comprobar su causa.

## 4. Pruebas manuales (pendientes)
- Tab y Shift+Tab: salto de contenido, menú, formulario, FAQ; foco siempre visible.
- Enter y Espacio abren/cerran FAQ; Escape cierra el modal Bootstrap y devuelve el foco.
- Zoom 200 %, anchos 320, 390, 768 y 1280: sin desbordamiento de página (tabla con desplazamiento propio).
- NVDA/VoiceOver: regiones, títulos, imágenes y etiquetas del formulario.
- Modo oscuro y prefers-reduced-motion.

## 5. SEO y publicación
Canonical y Open Graph: configurados con marcador .example. Sitemap: seis páginas públicas. noindex: gracias y 404. JSON-LD: caso académico sin reseñas inventadas. URL real pendiente del Lab 14.

## 6. Conclusión provisional
Las correcciones de código están preparadas. La calidad final debe comprobarse con los medios reales y las auditorías anteriores. Prioridad: restaurar img/video, ejecutar Lighthouse en ambos temas y corregir cualquier hallazgo antes de publicar. Adjuntar evidencias antes de entregar este informe como completado.
