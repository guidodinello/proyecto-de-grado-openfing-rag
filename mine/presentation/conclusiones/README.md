# Conclusiones

Workflow completo en [`../WORKFLOW.md`](../WORKFLOW.md). Acá solo lo específico
de esta diapo. No se referencia por número, ver `../README.md`.

## Alcance de esta diapo

Es la diapo 21 en `slides.md` (orientativo). Cubre el cuerpo principal del
Cap. 7, **no** la sección "Trabajo a futuro" del mismo capítulo, que
corresponde a las diapos 22-23 ("Trabajo a Futuro"), ya en `slides.md`.

## Ojo con la superposición con otras diapos

- **Ingeniería de Muestra / equidad educativa:** el Cap. 7 (párrafo 3) cita la
  retroalimentación de Ingeniería de Muestra como evidencia de valor para el
  estudiante. **Ese contenido ya se usó en la diapo de Despliegue y
  Validación** (`../despliegue-y-validacion/`). Acá se menciona como mucho de
  pasada, no se repite el bullet de equidad educativa ni el de alcance
  institucional.
- **WER de Whisper y elección de Llama 3.1 8B:** el Cap. 7 (párrafo 2) resume
  estos resultados, pero el detalle numérico completo le corresponde a las
  diapos de Experimentación (16, "Modelos de Transcripción") y de Modelo LLM
  (15), ambas todavía placeholder en `slides.md`. Si esta diapo se cierra
  antes de que existan esas dos, usar los números tal como están en el
  informe (WER < 0.05, Llama 3.1 8B vía API de HuggingFace) solo como
  respaldo breve de "la PoC funciona", no como contenido nuevo a desarrollar
  acá. Cuando se armen esas diapos, revisar que no quede el mismo dato
  repetido en dos láminas.
- **Objetivos (diapos 5 y 6):** el Cap. 1 define **5 objetivos específicos**
  (no 6, la nota de `slides.md` en la diapo 21 dice "6 objetivos de la diapo
  5-6" pero eso suma los 5 específicos con el objetivo general o con algo de
  la diapo 6 de no funcionales, no es una cifra que venga del informe). Esta
  diapo tiene que cerrar explícitamente contra los 5 objetivos específicos
  del Cap. 1, con el mismo balance que usa el informe, 4 cumplidos y 1
  parcial, no presentar los 5 como 100% logrados.

## Fuentes

- `Nuestro/Capitulos/7-Conclusiones.tex`, párrafos 1-9 (antes de la sección
  "Trabajo a futuro"), el cuerpo de conclusiones completo.
- `Nuestro/Capitulos/1-Introduccion.tex`, sección "Aportes del Proyecto"
  (líneas ~9-32), objetivo general y los 5 objetivos específicos contra los
  que el Cap. 7 evalúa el cumplimiento.
- Anexo A, "Planificación" (`Anexos/5-Planificacion.tex`), referenciado desde
  el párrafo de autocrítica del Cap. 7, cronograma planeado vs. real. No
  relevado en detalle acá, mencionar solo si el tribunal pregunta.

## Estado

- [x] 01 puntos del capítulo
- [x] 02 puntos más importantes
- [x] 03 atención del tribunal
- [x] validación de énfasis con el usuario (paso 3 del workflow, obligatorio)
- [x] propuestas A y B (dos forks) + `propuesta-final.md` (híbrida, revisada
  con advisor, correcciones aplicadas)
- [ ] pasada a Google Slides
