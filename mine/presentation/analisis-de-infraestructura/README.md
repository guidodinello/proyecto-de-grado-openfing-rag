# Análisis de Infraestructura

Workflow completo en [`../WORKFLOW.md`](../WORKFLOW.md). Acá solo lo específico
de esta diapo. Diapo: self-hosting vs. inferencia como servicio (tabla de
comparación). No se referencia por número, la numeración del deck real se
corre cada vez que se inserta o borra una lámina, ver `../README.md`.

## Fuentes

- `Nuestro/Capitulos/6-Experimentacion.tex` §6.7 "Análisis de Infraestructura"
  (líneas ~246-318) y §6.8 "Despliegue y Validación Operacional" (~321-348),
  que contiene latencia y comparación self-hosting.
- `Nuestro/Capitulos/3-RequisitosDelSistema.tex` §3.3.4 "Análisis de Requisitos
  de Infraestructura" (RNF5, líneas ~42-69).
- `Nuestro/Anexos/2-EstimacionesParaOpenFing.tex` (estimaciones de ingesta para
  todo OpenFing).
- `mine/data/deployment-minube-antel.md` (contexto del VPS de ANTEL).
- `mine/latency_analysis.py` (script del análisis de latencia).

## Estado

- [x] 01 puntos del capítulo
- [x] 02 puntos más importantes
- [x] 03 atención del tribunal (incluye puntos H y I sobre el dato de costo y el nombre del modelo)
- [x] propuestas A y B (dos forks) + `propuesta-final.md` (híbrida, revisada con advisor)
- [x] propuesta volcada al bloque correspondiente en `../slides.md`
- [x] armada y cerrada en Google Slides (tabla de comparación self-hosting vs. inferencia como servicio, borde naranja en la opción elegida, frase de cierre sobre la GPU)
- [x] latencia con GPU dedicada verificada (~1-3 s, benchmarks vLLM en A10/A100), reemplaza el "a chequear" de las notas del orador
