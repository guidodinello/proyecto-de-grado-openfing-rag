# Checklist de correcciones — comentarios de tutores (entrega 2026-08-22)

Fuente: anotaciones extraídas de los dos PDF en `mine/comments/`.

- **L** = Luis Chiruzzo (`202608221438_..._comments.pdf`)
- **T** = Libertad Tansinni (`20260823_...-5_...pdf`), aparece como autor "Usuario"

`p.` = página del PDF. Los números de línea `.tex` son del estado del repo al momento de generar este checklist; verificar antes de editar.

## Contexto y plazos (actualizado 2026-08-30)

- Veredicto de los tutores sobre esta entrega: "el informe está muy bien, casi terminado";
  los comentarios son errores chicos y correcciones de redacción. Corregirlos **todos**.
- **Entrega de correcciones: martes 1/9** (mandar la última versión a los tutores para que la
  revisen y la pasen al tribunal).
- **Defensa: jueves 17/9 18:30, salón 701.** Tribunal: Guillermo Moncecchi, Raquel Sosa,
  Ignacio Sastre. Habrá un ensayo antes.
- **Requisito nuevo (no está en los PDF de comentarios):** apartado obligatorio
  "Declaración de Uso de Herramientas de IA" en Cap. 1, antes de "Organización del Documento".
  Detalle completo en `mine/comments/declaracion-uso-ia.md`.
- Progreso de correcciones mecánicas: `mine/comments/cambios-aplicados-sesion1.md`
  (19 ítems, 2026-08-27) y `mine/comments/cambios-aplicados-sesion2.md` (2026-08-30).
  **OJO**: 10 de los 19 cambios de la sesión 1 se habían perdido (pisados por commits
  posteriores); se re-aplicaron en la sesión 2. Verificar todo en Overleaf.
- Apellido de Libertad: el correcto es **"Tansini"** (una n), como marcó Luis en su primer
  comentario. Unificado en `main.tex` y `Estructura.tex` (sesión 2).

## Notas de estructura detectadas al cruzar (importante)

- El capítulo de conclusiones que compila es **`Nuestro/Capitulos/7-Conclusiones.tex`** (único `\input` en `main.tex:247`). Contiene además `\section{Trabajo a futuro}`.
- **`Nuestro/Capitulos/8-Conclusiones.tex` y `Nuestro/Capitulos/7-TrabajoAFuturo.tex` NO se compilan** (no están en `main.tex`) pero tienen contenido casi idéntico. Todo cambio de conclusiones/trabajo a futuro va en `7-Conclusiones.tex`. Conviene borrar los archivos huérfanos o dejar constancia de que son obsoletos.
- `7-Conclusiones.tex:2` y `8-Conclusiones.tex:2` comparten `\label{chapter:8-Conclusiones}`. La numeración de capítulo/label quedó desalineada con el nombre de archivo.

---

## Cap. 0 — Resumen (`Nuestro/Capitulos/0-Resumen.tex`)

- [ ] **T p.9** — "el resumen va antes del índice". Verificar orden en `main.tex` (`\input{...0-Resumen}` en línea 231, después del TOC). Mover el resumen antes del `\tableofcontents`.
- [ ] **T p.9** — `0-Resumen.tex:5` "existen falencias en los LLMs populares". Reformular hacia: "Los modelos comerciales funcionan como cajas negras y su uso tiene ciertos riesgos asociados". Cambiar "falencias" por "riesgos".
- [ ] **T p.9** — `0-Resumen.tex:9` "distintas posibles arquitecturas las cuales se decidieron dejar de lado". Reescribir: "alternativas y los motivos por los que se dejaron de lado".
- [ ] **T p.9** — `0-Resumen.tex` (párrafo de pipeline). Agregar datos del corpus y una conclusión. Texto sugerido por la tutora: *"El pipeline de transcripción fue aplicado al corpus completo de OpenFing, que comprende 239 cursos y 4.339 clases, utilizando faster-whisper con CTranslate2, lo que redujo los tiempos de procesamiento entre dos y cuatro veces respecto a la implementación original de Whisper"*. Mencionar además que se mostró y evaluó con estudiantes en IdeM 2025.

## Cap. 1 — Introducción (`Nuestro/Capitulos/1-Introduccion.tex`)

- [ ] **T p.15** — `1-Introduccion.tex:4` "presentan una tendencia conocida a las alucinaciones". Falta **cita** para la afirmación sobre alucinaciones.
- [ ] **T p.15** — `1-Introduccion.tex:4` "Este riesgo se agrava en un contexto educativo". Falta **cita** / usar "riesgo".
- [ ] **T p.15** — `1-Introduccion.tex:6` primera mención de RAG: agregar "(RAG por sus siglas en inglés)" al expandir "Generación Aumentada por Recuperación". (Ya usa `\acrshort{rag}`; confirmar que el glossary imprime la forma larga + sigla en la primera aparición.)
- [ ] **T p.15** — `1-Introduccion.tex:6` "las transcripciones automáticas del contenido educativo de OpenFing". Falta **cita / nota al pie** para OpenFing.
- [ ] **T p.15** — reformular a: "un conjunto de documentos confiables o corpus curado de información académica".
- [ ] **T p.15** — "evitando así..." → considerar "mitigando..." como verbo.
- [ ] **T p.16** — `1-Introduccion.tex:22` objetivo ASR. Agregar "(ASR por sus siglas en inglés)" en la primera mención (línea 22 o donde se expanda "reconocimiento automático de voz").
- [ ] **T p.16** — `1-Introduccion.tex:22` falta **cita** para ASR.
- [ ] **T p.16** — `1-Introduccion.tex:44` "se proyectaba cubrir la totalidad del contenido disponible en OpenFing pipeline implementado procesó los 239 cursos...". Oración mal ensamblada (falta conector / punto). Corregir redacción. Comentario de la tutora: "refinamiento?" sobre "afinamiento".

## Cap. 2 — Marco Teórico (`Nuestro/Capitulos/2-MarcoTeorico.tex`)

- [x] **L p.1 / portada** — apellido de la tutora: el correcto es **"Tansini"** (una n). Unificado en `main.tex:57,235` y `Estructura.tex:27,64` — sesión 1 + sesión 2.
- [ ] **L p.20** — `2-MarcoTeorico.tex:26` `\cite{RussellNorvig2020}` con texto "Stuart J. Russell and Peter Norvig". La cita en el cuerpo debería decir solo "Russell and Norvig". Revisar el string en `referencias.bib` (entrada `RussellNorvig2020`) o cómo se renderiza el `\citeauthor`.
- [ ] **L p.22** — `2-MarcoTeorico.tex:56` "introducida por Vaswani et al. \cite{vaswani2017attention}". Borrar el "Vaswani et al." redundante en texto y dejar solo la referencia `\cite` de al lado.
- [ ] **T p.22** — `2-MarcoTeorico.tex:50` "ajuste iterativo de pesos matemáticos". Cambiar a "pesos en funciones matemáticas" (o "pesos", a secas).
- [ ] **L p.38** — typo: "señalizan" → **"indican"**. Buscar en `2-MarcoTeorico.tex` (sección de embeddings / recuperación, aprox. líneas 97–165). *(No localizado exacto por grep; buscar "señaliz".)*
- [ ] **L p.38** — typo: "cercano" → **"cercana"** (concordancia). Misma zona (`2-MarcoTeorico.tex:101` o `:163`, "los $k$ fragmentos más cercanos" — revisar cuál da el género incorrecto).
- [ ] **L p.38** — `\cite{Morris2004}` de MER: mover la referencia **hacia arriba**, al final de donde está la definición en texto de MER. Nota: la definición de MER con `\cite{Morris2004}` está en **`Nuestro/Capitulos/3-RequisitosDelSistema.tex:138-144`**, no en Cap. 2. Verificar en qué página del PDF cae (el comentario está sobre `C+S+D+I  Morris et al. (2004)`, que es la fórmula de `3-RequisitosDelSistema.tex:142`). Mover `\cite{Morris2004}` de línea 144 al final de la línea 138.

## Cap. 3 — Requisitos del Sistema (`Nuestro/Capitulos/3-RequisitosDelSistema.tex`)

- [ ] **T p.27** — comentario "deseable?" sobre "deseado" / "comportamiento esperado". *(No localizado por grep; revisar sección de requisitos no funcionales / criterios de evaluación.)*
- [ ] **T p.33** — `3-RequisitosDelSistema.tex:6` "En los capitulos \autoref{...5} y \autoref{...6} **y** se explican las cuestiones planteadas en este capitulos." La tutora marca "para mi no va esta frase". Además tiene errores: "capitulos" (x2, sin tilde y mal número), "y" duplicado. Eliminar o reescribir.
- [ ] **T p.33** — `3-RequisitosDelSistema.tex:11` "para fundamentar las decisiones de diseño". Sugerencia: "para respaldar adecuadamente la toma de decisiones".
- [ ] **T p.34** — `3-RequisitosDelSistema.tex` lista de tecnologías de búsqueda: falta **cita** en cada ítem:
  - "API REST" (línea ~24) — ref.
  - "FAISS (Facebook AI Similarity Search)" — ref.
  - "pgvector: extensión de PostgreSQL" (línea 28) — ref.
  - "Elasticsearch" (línea 33) — ref.
- [ ] **T p.37** — `3-RequisitosDelSistema.tex:109` "existen estudios y métricas publicadas al respecto. Los ASR son mayoritariamente entrenados en inglés...". Comentario "ya que?": hacer explícito el nexo causal entre ambas oraciones.
- [ ] **L p.40** — `3-RequisitosDelSistema.tex:187` "reuniones con la **UEFI( Unidad** de Enseñanza de Facultad de Ingeniería". Espacio mal puesto: "UEFI (Unidad". Corregir `UEFI(` → `UEFI (`.
- [ ] **T p.40** — mismo pasaje, "afinamiento de estos requisitos" — la tutora sugiere "refinamiento". Evaluar cambio de término.
- [ ] **L p.40** — "coma y espacio" sobre `3-RequisitosDelSistema.tex:193` "Por lo tanto,se debe mencionar". Falta espacio tras la coma: "Por lo tanto, se debe".
- [ ] **L p.99 / T** — nombre de la unidad: en `3-RequisitosDelSistema.tex:187` se expande UEFI como *"Unidad de Enseñanza de Facultad de Ingeniería"*; en `7-Conclusiones.tex:5` aparece *"URI (Unidad de Repositorios Institucionales)"* y en `8-Conclusiones.tex:24` *"URI (Unidad de Recursos Informáticos)"*. Unificar la sigla y su expansión en todo el documento.

## Cap. 4 — Arquitectura (`Nuestro/Capitulos/4-Arquitectura.tex`)

- [ ] **T p.43** — `4-Arquitectura.tex:9-10` Figura 4.1 (`Overview.png`, caption "Vista general del pipeline..."). "¿se puede agrandar la figura?". Aumentar tamaño / rotar apaisada / mejorar legibilidad.
- [ ] **L p.46** — `4-Arquitectura.tex:52` módulo de transcripción: "inicializa la transcripción con un prompt de dominio que incluye terminología de ingeniería y español rioplatense". Agregar `\autoref` al **Anexo B.2** (prompt de Whisper — está en `Nuestro/Anexos/1-Prompting.tex:49` y en `Nuestro/Anexos/2-EstimacionesParaOpenFing.tex:103`). Verificar/crear `\label` en ese anexo.
- [ ] **L p.48** — `4-Arquitectura.tex:86` "evita el \"ruido\" visual". La tutora/Luis marca "esta no va" sobre parte de esta frase. Revisar y probablemente recortar.
- [ ] **L p.48** — `4-Arquitectura.tex:86` comillas de apertura: `"¿Por qué?"`, `"¿Algún ejemplo?"` usan comillas rectas / de cierre. En LaTeX las de apertura deben ser `` `` ``. Reemplazar `"..."` por `` ``...'' `` (2 ocurrencias en la línea). Revisar la misma convención en `"ruido"` de esa línea.
- [ ] **L p.49** — `4-Arquitectura.tex:97` `\subsection{Construcción del prompt}`. El Anexo B.1 (`Nuestro/Anexos/1-Prompting.tex`) tiene detalles del prompt del sistema y **nunca se referencia**. Agregar `\autoref` a ese anexo en esta subsección.

## Cap. 5 — Implementación (`Nuestro/Capitulos/5-Implementacion.tex`)

- [ ] (Ver también L p.46 / p.49: las referencias a los anexos de prompting impactan Cap. 4; confirmar si Cap. 5 §transcripción `5-Implementacion.tex:142` también debería enlazar el Anexo B.2.)

## Cap. 6 — Experimentación (`Nuestro/Capitulos/6-Experimentacion.tex`)

- [ ] **L p.51** — `6-Experimentacion.tex:149` (o `7-Conclusiones.tex:6` / `8-Conclusiones.tex:6`) "entre dos y cuatro veces". Luis marca "cinco". Contexto: "WER ... equivalente a menos de **cinco** errores por cada cien palabras" está en `7-Conclusiones.tex:6` ("menos de cinco"). Verificar a qué número apunta exactamente el highlight (¿"cuatro" → "cinco"? ¿un conteo de componentes/modelos?). **Revisar contra dato real.**
- [ ] **L p.68** — `6-Experimentacion.tex:23-33` tabla del dataset (Computación 1 / PLN, `\footnote{\url{...}}`). Luis: "estas notas al pie quedaron mal, no se ve a dónde apuntan; poner los links como notas al pie dentro de esta página". Revisar que los `\footnote` dentro de `tabular`/`table` se rendericen (usar `\footnotemark`/`\footnotetext` o `tablefootnote`).
- [ ] **L p.68** — `6-Experimentacion.tex:36` "las primeras clases del curso de Computación 1 **posee** una temática similar" → "poseen" (concordancia; sujeto plural "las primeras clases").
- [ ] **L p.68** — primera aparición de "PLN" en el cuerpo: escribir "Procesamiento de Lenguaje Natural (PLN)" y luego usar solo "PLN". Primera mención como sigla suelta está aprox. en `6-Experimentacion.tex:113` ("curso de Procesamiento de Lenguaje Natural (PLN-1 y PLN-2)") — verificar si antes se usó "PLN" sin expandir.
- [ ] **L p.73** — `6-Experimentacion.tex:160` "validar la coherencia y el **sesgo** del juez". Comentario "sesgos o" — revisar redacción (¿"los sesgos"? ¿"sesgo o ..."?).
- [ ] **L p.73 y p.74** — **inconsistencia 24 vs 16**: `6-Experimentacion.tex:160` "el volumen de la muestra, de **24 preguntas**" y `6-Experimentacion.tex:169` "se evaluó mediante **24 consultas**", pero la tabla `table:preguntas_evaluacion` tiene **16 preguntas** (Luis: "en la tabla son 16"). Aclarar: ¿24 consultas totales sobre 16 preguntas únicas? Uniformar el texto y explicitar la diferencia entre "preguntas únicas" y "consultas evaluadas".
- [ ] **L p.74** — `6-Experimentacion.tex:184` "más detalles que en la tabla,(respuesta, contexto, etc)". Cambiar la coma por espacio: "tabla (respuesta, contexto, etc.)". (También cerrar con "etc.").
- [ ] **L p.78** — "espacio antes del paréntesis". Revisar zona pág. 78 del PDF (sección de comparación de modelos / costos, aprox. `6-Experimentacion.tex:240-265`) buscando `texto(` sin espacio.
- [ ] **L p.79** — `6-Experimentacion.tex:265` (`\caption{Comparación de modelos fundacionales...}`) y `6-Experimentacion.tex:303` (`\caption{Los precios corresponden...}`). Tabla 6.4 y Tabla 6.5 son **dos captions para una sola tabla**. Dejar un único `\caption` y unificar el texto (fusionar la descripción de precios dentro del caption principal o pasarla a nota de tabla). Revisar `6-Experimentacion.tex:300-305`.
- [ ] **T p.79** — misma tabla: "¿achicar tamaño de letra?" para que entre mejor. Ya usa `\footnotesize`; evaluar `\scriptsize` o `\resizebox`.
- [ ] **L p.80** — referencia a sección obsoleta: el highlight está sobre `6-Experimentacion.tex:333` ("período que incluye la jornada de Ingeniería de Muestra (véase \autoref{chapter:A-0-Anexo I-Ingeniería de Muestra})"). Luis: "ahora es en la sección 6.6" y "(ver sección 6.6)". Revisar que el `\autoref` apunte a `\section{Experiencia en Ingeniería de Muestra}` (`6-Experimentacion.tex:346`) y no solo al anexo; corregir el texto del cross-ref.
- [ ] **L p.80** — `6-Experimentacion.tex:80` (`\autoref{...}` sobre "Apéndice A" / "estudiantes"). Ajustar a "(ver sección 6.6)". Localizar el `\autoref{chapter:A-0-...}` cercano a la mención de "272 consultas" / "Apéndice A" y unificar con la sección 6.6.

## Cap. 7 — Conclusiones y Trabajo a Futuro (`Nuestro/Capitulos/7-Conclusiones.tex`)

> Las páginas 82–86 del PDF de Luis caen en este capítulo. Editar **`7-Conclusiones.tex`** (no `8-Conclusiones.tex` ni `7-TrabajoAFuturo.tex`).

- [ ] **L p.82** — typo "." (puntuación). Revisar `7-Conclusiones.tex` párrafos iniciales (líneas 4–14).
- [ ] **L p.82** — "hubo": corregir tiempo/forma verbal cerca de "esta" (`7-Conclusiones.tex`, zona de resultados/experiencia). Revisar.
- [ ] **L p.82** — "prototipo": `7-Conclusiones.tex:14` "Si bien el prototipo actual cumple su función demostrativa". Revisar concordancia/artículo ("el prototipo").
- [ ] **L p.82** — ", el": falta coma + artículo en alguna enumeración de `7-Conclusiones.tex:14` ("refinamiento de la precisión de respuestas, implementación de métricas de uso, integración..., y expansión..."). Revisar la serie.
- [ ] **L p.82** — "póster" (con tilde). Buscar "poster" sin tilde: `6-Experimentacion.tex:359` "un poster presentado por el grupo Ingenieria de Muestra" y `7-Conclusiones.tex` si aplica. Corregir "poster"→"póster" e "Ingenieria"→"Ingeniería".
- [ ] **L p.83** — "son": `7-Conclusiones.tex` "cómputo es" / concordancia. Revisar.
- [ ] **L p.84** — "muestra": `7-Conclusiones.tex` "valida IA son" — revisar redacción de esa oración.
- [ ] **T p.84** — "educativas basadas" → agregar "de tipo RAG" ("soluciones educativas **de tipo RAG** basadas en...").
- [ ] **L p.85** — ", desarrollando": `7-Conclusiones.tex:26` "Las otras facultades de la UDELAR están comenzando a subir sus clases de manera online. **Desarrollando** herramientas similares a OpenFing." Fragmento de oración: unir con coma ("..., desarrollando herramientas similares a OpenFing.").
- [ ] **L p.85** — "garantizaría": `7-Conclusiones.tex:5` "La integración garantizaría la sostenibilidad" — Luis marca "se garantiza". Revisar modo verbal (condicional vs presente) según el contexto.
- [ ] **L p.86** — ⚠️ **ERROR CONCEPTUAL** — `7-Conclusiones.tex:30` (`\section{Trabajo a futuro}`, párrafo de Re-Ranking): *"los documentos son recuperados en función de similitud matemática entre vectores, independiente de la similitud semántica que los vectores puedan tener. ... puede ocurrir que los vectores matemáticamente más similares, no sean semánticamente relevantes"*. Luis: los embeddings **sí** están entrenados para capturar similitud semántica; la afirmación es incorrecta. Lo correcto: traer vectores por similitud **no garantiza relevancia**, y eso hay que **medirlo** (p. ej. rankeando relevancia con un conjunto de preguntas como el que construyó el grupo). Reescribir el pasaje. Nota: el mismo texto erróneo está duplicado en `7-TrabajoAFuturo.tex:11` y `8-Conclusiones.tex:30` (archivos no compilados).
- [ ] **L p.86** — sugerencia de Luis para agregar a Trabajo a Futuro: *"si contamos con un corpus suficientemente grande de preguntas y vectores relevantes, podríamos fine-tunear un sistema que funcione mejor para nuestro caso particular"*. Ya hay una mención de fine-tuning en `7-Conclusiones.tex:34` (retroalimentación explícita → "ajuste fino posteriores"); ampliar conectando con el corpus de preguntas de evaluación.
- [ ] **T p.83** — `7-Conclusiones.tex:8` "Para el estudiante, la solución brinda respuestas mayoritariamente correctas...". Comentario: "Algo de esto se evidenció en Ingeniería de Muestra...". Añadir referencia a la evidencia cualitativa de IdeM (`\autoref{chapter:A-0-Anexo I-Ingeniería de Muestra}` o §6.6).

## Requisito nuevo — Declaración de Uso de Herramientas de IA

Ver detalle completo en `mine/comments/declaracion-uso-ia.md`.

- [x] Redactada `\section{Declaración de Uso de Herramientas de IA}` en `1-Introduccion.tex`, entre "Aportes del Proyecto" y "Organización del Documento" — 2026-08-30.
- [ ] Diego: párrafo sobre Gemini (hay `% TODO (Diego)` en el .tex).
- [ ] Pasada final a Conclusiones / Trabajo a Futuro / discusión de resultados con el criterio "secciones reflexivas de autoría del estudiante".

## Anexos

- [ ] **L p.93** — `Nuestro/Anexos/0-IDM.tex:1` `\chapter{Experiencia en Ingeniería de Muestra}`. Luis: este anexo ahora debería llamarse simplemente **"Poster utilizado en Ingeniería de Muestra"** (el relato de la experiencia ya está en §6.6 del Cap. 6). Renombrar el `\chapter{}` y ajustar su contenido para que sea solo el póster; actualizar todos los `\autoref{chapter:A-0-Anexo I-Ingeniería de Muestra}` que lo citen (`6-Experimentacion.tex:5,324,333,359`; `7-Conclusiones.tex:26`).
- [ ] **L p.99** — Anexo "C" (según el PDF; probablemente `Nuestro/Anexos/2-EstimacionesParaOpenFing.tex`, `\label{Estimaciones de lo que significaría para OpenFing}`) **no está referenciado** en el cuerpo. Único `\autoref` a ese label está en `8-Conclusiones.tex:24` (archivo NO compilado); `7-Conclusiones.tex` no lo referencia. Agregar la referencia en `7-Conclusiones.tex` (zona línea 5, integración institucional / recursos para OpenFing) y/o en `3-RequisitosDelSistema.tex` donde se habla de reuniones con la UEFI (líneas 73, 187) y de self-hosting.

## Anexo nuevo a crear

- [ ] **T p.6** — Agregar un anexo corto al final con: **diagrama de Gantt inicial y final**, **porcentaje de dedicación por tarea-macro**, **estimación de horas** (si existe) y un **comentario sobre las demoras**. Crear `Nuestro/Anexos/5-Planificacion.tex` (o similar), agregar `\input` en `main.tex` (tras línea 261) y referenciarlo desde el Cap. 1 o Cap. 7.

---

## Ítems transversales / limpieza sugerida

- [ ] Borrar o marcar como obsoletos `Nuestro/Capitulos/8-Conclusiones.tex` y `Nuestro/Capitulos/7-TrabajoAFuturo.tex` (no compilan, duplican contenido y ya causaron confusión con el error conceptual de p.86).
- [ ] Revisar el `\label{chapter:8-Conclusiones}` en `7-Conclusiones.tex:2` — el número de capítulo no coincide con el archivo ni con el orden real.
- [ ] Pase global de comillas: usar `` ``...'' `` en LaTeX (no `"..."`). Aparece en Cap. 4 y probablemente en otros.
- [ ] Pase global de tildes en "Ingeniería" / "Computación" dentro de tablas y captions.
