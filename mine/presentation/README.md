# mine/presentation/ — preparación de la defensa oral

Todo lo relacionado a la presentación y al Q&A del 17/9/2026. El informe está
congelado, esto es trabajo nuevo, no edición del `.tex`.

## Por dónde empezar

- **Proceso de trabajo:** [`WORKFLOW.md`](WORKFLOW.md). Léelo antes de tocar
  cualquier diapo, describe cómo se prepara el contenido de cada una.
- **Estado del deck:** [`slides.md`](slides.md), un bloque por diapo
  (contenido actual, propuesta, notas del orador, pendientes). Se armó contra
  el conteo original de 23 diapos, el deck real ya tiene más y sigue
  cambiando, tratar los números de `slides.md` como orientativos, no exactos.
- **Guion general de la charla:** [`presentacion-defensa.md`](presentacion-defensa.md),
  estructura, timing por sección, contenido de cada capítulo, nota de
  taxonomía RAG para preguntas no cubiertas en el informe, checklist de demo.
- **Q&A simulado con el tribunal:** [`qa-simulacion-tribunal.md`](qa-simulacion-tribunal.md),
  pregunta, borrador de respuesta, feedback, versión refinada. Crece sesión a
  sesión.
- **Tips de los tutores sobre la presentación:** [`tips-tutores-presentacion.md`](tips-tutores-presentacion.md).

## Organización de carpetas

```
mine/presentation/
  README.md                     este archivo, índice general
  WORKFLOW.md                   proceso paso a paso para desarrollar una diapo
  slides.md                     índice de diapos (numeración orientativa, no exacta)
  presentacion-defensa.md       guion y estructura de la charla
  qa-simulacion-tribunal.md     Q&A simulado con el tribunal
  tips-tutores-presentacion.md  feedback de los tutores sobre cómo presentar
  pdfs/
    Presentacion 17_9 Tesis.pdf                     export del deck de Slides
    Proyecto_de_Grado_INCO_InCo_FIng_UdelaR.pdf      informe completo compilado
  <slug-diapo>/                 una carpeta por diapo que necesitó desarrollo real
    README.md                   fuentes de esa diapo + checklist de estado
    01-puntos-del-capitulo.md
    02-puntos-mas-importantes.md
    03-atencion-del-tribunal.md
    propuesta-A.md
    propuesta-B.md
    propuesta-final.md
    *.svg / *.png                diagramas propios de esa diapo, si hacen falta
```

## Carpetas de diapo existentes

Las carpetas se nombran y referencian por sección, no por número de diapo, el
número se corre cada vez que se inserta o borra una lámina en Slides y quedó
desincronizado entre archivos más de una vez. Para ubicar cada una en el
deck actual, mirar el panel de miniaturas de Slides por título, no por
posición.

- [`analisis-de-infraestructura/`](analisis-de-infraestructura/) —
  self-hosting vs. inferencia como servicio. Cerrada y armada en Slides.
- [`analisis-de-costos/`](analisis-de-costos/) — lámina principal (número
  ancla + gráfico de costos) cerrada y armada en Slides; lámina de respaldo
  (tabla completa de 9 modelos) marcada "Omitir diapositiva".
- [`despliegue-y-validacion/`](despliegue-y-validacion/) — validación en
  Ingeniería de Muestra + arquitectura de despliegue. Cerrada y armada en
  Slides, revisada y aprobada por el usuario.
- [`conclusiones/`](conclusiones/) — cumplimiento de los 5 objetivos
  específicos del Cap. 1 (4 cumplidos, 1 parcial), viabilidad de la PoC,
  autocrítica y frase de cierre. Propuesta final lista, pendiente de pasar a
  Slides.
- [`ingesta-scraping/`](ingesta-scraping/) — esquema `courses`/`lessons` con
  instancia real de ejemplo (Anexo 2, `actint2025`). Cerrada y armada en
  Slides.

No todas las diapos tienen o necesitan carpeta propia, solo las que
requirieron desarrollo de contenido real. Ver `WORKFLOW.md` para el criterio.
