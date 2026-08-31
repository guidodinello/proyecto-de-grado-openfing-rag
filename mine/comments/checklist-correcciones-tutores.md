# Checklist de correcciones — comentarios de tutores (entrega 2026-08-22)

Fuente: anotaciones extraídas de los dos PDF en `mine/comments/`.

- **L** = Luis Chiruzzo (`202608221438_..._comments.pdf`)
- **T** = Libertad Tansinni (`20260823_...-5_...pdf`), aparece como autor "Usuario"

`p.` = página del PDF. Los números de línea `.tex` son del estado del repo al momento de generar este checklist; verificar antes de editar.


## Alcance de las correcciones (2026-08-30, revisado)

Regla acordada con los autores: **solo se aplican cambios ligados a un comentario concreto de
los tutores.** Nada de mejoras de `mine/todos.md` ni de iniciativa propia. Ver también la
sección "Verify before assuming" del `CLAUDE.md`.

Revertido tras salirse de esa regla:
- `2-EstimacionesParaOpenFing.tex` — rewrite completo (los tutores solo pidieron referenciarlo).
- Agradecimientos de `main.tex` — restaurado el placeholder (solo se mantiene el reorden Resumen/índice de T p.9).
- `0-IDM.tex` — solo se renombró el `\chapter` (L p.93); se revirtió el rename del label, `fig:placeholder`, el caption y la oración agregada.
- Cap. 2 §OpenFing y Cap. 3 §ASR — recortados a la marca literal del tutor.

Se mantienen (avalados por los autores): reescrituras chicas en Cap. 3 §Requisitos y Cap. 6 §6.6,
el Resumen ampliado, y tres arreglos de typos claros no marcados por nadie ("OpenFing OpenFing",
"Let's EncryptLet's Encrypt", heading "carecen relación").

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

## ESTADO al 2026-08-30 (post sesión 2, ya subido a Overleaf)

### ✅ Resueltos (18)

| Coment. | Qué era |
|---|---|
| L p.1 | Apellido "Tansinni" → "Tansini" (main.tex + Estructura.tex) |
| T p.9 | "falencias" → "cajas negras / riesgos" (Resumen) |
| T p.9 | "distintas posibles arquitecturas las cuales…" reescrito (Resumen) |
| T p.16 | Oración mal ensamblada "OpenFing pipeline implementado procesó" → punto y seguido (Intro) |
| L p.20 | Cita Russell & Norvig: autor en bib → "{Russell and Norvig}" (verificar render) |
| L p.22 | Borrado "Vaswani et al." redundante (Cap. 2) |
| T p.22 | "pesos matemáticos" → "pesos en funciones matemáticas" (Cap. 2) |
| L p.38 | "señalizan" → "indican" (Cap. 3) |
| L p.38 | "cercano es" → "cercana es" (Cap. 3) |
| L p.38 | `\cite{Morris2004}` movido al final de la definición (Cap. 3) |
| T p.33 | Frase "En los capitulos… y se explican…" eliminada (Cap. 3) |
| T p.33 | "para fundamentar las decisiones" → "para respaldar adecuadamente la toma de decisiones" (Cap. 3) |
| L p.40 | "UEFI(" → "UEFI (" (Cap. 3) |
| T p.40 | "afinamiento" → "refinamiento" (Cap. 3) |
| L p.40 | "Por lo tanto,se" → "Por lo tanto, se" (Cap. 3) |
| L p.46 | `\autoref` al anexo del prompt de transcripción (Cap. 4) |
| L p.48 | Comillas rectas → `` ``…'' `` en la línea del "ruido visual" (Cap. 4) |
| L p.49 | `\autoref` al anexo del prompt del asistente en "Construcción del prompt" (Cap. 4) |
| L p.68 | "posee" → "poseen" (Cap. 6) |
| L p.74 | "tabla,(respuesta, contexto, etc)" → "tabla (respuesta, contexto, etc.)" (Cap. 6) |
| L p.78 | "consulta(30 de mayo" → "consulta (30 de mayo" (Cap. 6) |
| L p.82 | "poster" → "póster", "Ingenieria" → "en Ingeniería" (Cap. 6) |
| L p.83 | "no es un impedimento" → "no son un impedimento" (Cap. 7) |
| L p.84 | "El proyecto valida… abriendo" → "El proyecto muestra… lo que abre" (Cap. 7) |
| T p.84 | "educativas basadas en IA" → "educativas de tipo RAG basadas en IA" (Cap. 7) |
| L p.85 | "de manera online. Desarrollando" → "…online, desarrollando" + "UDELAR" → "UdelaR" (Cap. 7) |
| L p.85 | "La integración garantizaría…" y "Por lo que permitir segmentar…, se garantiza que…" reescritas (Cap. 7) |
| L p.48 | Cortada la frase "evita el ruido visual de agregar fuentes y referencias…" (Cap. 4) |
| T p.15 | Cita para alucinaciones → `\cite{ji2023survey}` (Intro) |
| T p.15 | Cita para riesgo en contexto educativo → `\cite{kasneci2023chatgpt}` (Intro) |
| T p.15 | "(RAG, por sus siglas en inglés)" + `\cite{lewis2020retrieval}` en la primera mención (Intro) |
| T p.15 | Cita para OpenFing → `\cite{misc_OpenFing}` (Intro) |
| T p.16 | "(ASR, por sus siglas en inglés)" + `\cite{SpeechandLanguageProcessing}` (Intro) |
| T p.34 | Citas en la lista de tecnologías: `fielding2000rest` (API REST), `misc_pgvector`, `douze2025faiss` (FAISS, además se descomentó la frase que estaba rota), `gormley2015elasticsearch` (Cap. 3) |
| T p.15 | "conjunto de documentos confiables / corpus curado" y "evitando así"→"mitigando": N/A, esas frases ya no están en la intro reescrita |
| L p.86 | Reescrito el párrafo de Re-Ranking: los embeddings SÍ capturan semántica; lo que no garantizan es relevancia para la consulta puntual, y eso hay que medirlo con el set de preguntas anotadas (Cap. 7) |
| L p.86 | Agregado párrafo: el mismo set de preguntas habilita ajuste fino del modelo de embeddings sobre el dominio de OpenFing (Cap. 7) |
| Nuevo | Sección "Declaración de Uso de Herramientas de IA" agregada en Cap. 1 |

(La tabla cuenta ~28 líneas porque varios comentarios de Luis marcaban varias cosas en la
misma página. El requisito de la declaración de IA cuenta aparte.)

### ✅ Resueltos — 2ª tanda (2026-08-30, sesión 3)

| Coment. | Qué se hizo |
|---|---|
| T p.9 | Resumen movido antes del índice; agradecimientos activados; Resumen ampliado (corpus 239/4.339, faster-whisper 2–4×, WER < 0,05, Llama 3.1 8B, IdeM 2025) |
| T p.19 | "concentra miles…" → cifras concretas (239 cursos, 4.339 clases) |
| T p.27 | "no es aconsejable ni deseado" → "…ni deseable" (estaba en Cap. 2) |
| T p.37 | Nexo causal explícito en el párrafo de ASR en inglés |
| T p.43 | Figura 4.1 (overview) en página apaisada para legibilidad |
| T p.79 | `\footnotesize` en la tabla de precios |
| T p.83 | Referencia a la retroalimentación de IdeM en el párrafo del estudiante (Cap. 7) |
| L p.51 | "cuatro palabras" → "cinco palabras" en el caso del árbol AVL (era conteo, no WER) |
| L p.68 | Tabla del dataset con `threeparttable`/`tablenotes`; label reubicado |
| L p.68 | "Procesamiento de Lenguaje Natural (PLN)" en su primera aparición + fragmento arreglado |
| L p.73 | "el sesgo del juez" → "los sesgos del juez" |
| L p.73/74 | 24 vs 16 aclarado: 16 preguntas únicas → 24 consultas (8 de corpus completo × 2 prompts) |
| L p.79 | Tabla 6.4/6.5 fusionadas en un `\caption`; fuentes de precios como `tablenote`; `adjustwidth` anidado arreglado |
| L p.80 | Cross-refs de IdeM en Cap. 6 → `\autoref{section:6-IngenieriaMuestra}` (label nuevo) |
| L p.82 | En §6.6: "se celebro"→"celebró", "Este presentación"→"Esta", "entusiasmo alcance"→"entusiasmo, el alcance", fragmento unido |
| L p.99 | UEFI/URI: nombres correctos confirmados (UEFI = Unidad de Enseñanza de FIng; URI = Unidad de Recursos Informáticos). El compilado ya los usa bien. |
| — | Bugs de duplicación: "UdelaR) OpenFing", "Let's EncryptLet's Encrypt", frase de FAISS comentada, heading "carecen relación", `"Mi Nube"` comillas rectas |

### 🔲 Pendientes

**Necesitan input / datos de ustedes:**
- **T p.6 — anexo de planificación**: Gantt inicial y final, % de dedicación por tarea-macro, estimación de horas, comentario sobre las demoras. Yo armo el `.tex` y el `\input`, ustedes ponen los datos. Es el ítem más grande que queda.
- **Diego — párrafo de Gemini** (hay `% TODO (Diego)` en `1-Introduccion.tex`).
- **Diego — párrafo de tests automatizados**: lo borró él a propósito el 19/7. Preguntarle el motivo. Si va: `git revert b7d4e26`.
- **Dato "2835 videos"** en el Anexo de Estimaciones: chequear de dónde salió (¿videos vs. clases? el corpus final son 4.339 clases / 239 cursos). No lo toqué.

**Menores que puedo hacer:**
- Anexo de Estimaciones: el footnote a Wikipedia sobre WER (`es.wikipedia.org`) no es fuente académica; se podría reemplazar por `\cite{ASR_Accuracy}` o `\cite{itoh2015metric}`.
- Renombrar `\label{chapter:8-Conclusiones}` en `7-Conclusiones.tex:2` (cosmético, funciona igual).

### ✅ Cerrados en esta ronda (sesión 4)
- **L p.93** — Anexo IdeM renombrado a "Póster utilizado en Ingeniería de Muestra", dejado con solo el póster (el relato está en §6.6), `\autoref` ajustados, `fig:placeholder` → `fig:IDM-poster`.
- **L p.99** — Anexo de Estimaciones ahora referenciado también desde Cap. 3 (reuniones con la UEFI).
- **"(URI)"** — sigla agregada en `3-Requisitos` + footnote URL corregida a la página oficial de la URI.
- **L p.82** — "." y "hubo": N/A, esa zona se reescribió y movió a §6.6.
- **Anexo de Estimaciones** — pase completo: comillas rectas → `` ``…'' ``, tildes, oraciones incompletas, listas de métricas/config normalizadas, tabla y caption traducidos al español.
- Huérfanos borrados; forensics del párrafo de tests completo; 24 vs 16 resuelto.

---

## Notas de estructura detectadas al cruzar (importante)

- El capítulo de conclusiones que compila es **`Nuestro/Capitulos/7-Conclusiones.tex`** (único `\input`). Contiene además `\section{Trabajo a futuro}`.
- **`8-Conclusiones.tex` y `7-TrabajoAFuturo.tex` fueron BORRADOS** el 2026-08-30 (commit `7aca49e`). Eran huérfanos (no compilaban, no estaban en Overleaf). Su contenido está en `7-Conclusiones.tex`.
- **Párrafo de tests automatizados** (§Trabajo a futuro): agregado el 2026-06-01 a `7-TrabajoAFuturo.tex`. La fusión de capítulos del 2026-07-11 (Diego, Overleaf) SÍ lo trajo a `7-Conclusiones.tex`. **Diego lo BORRÓ deliberadamente el 2026-07-19 ~13:23 (Overleaf v8036→v8041)**, en la misma edición en que agregó la frase del anexo de Estimaciones. Fue una edición dirigida, no un accidente. Verificado con el diff API de Overleaf. Mi re-add quedó revertido (`b7d4e26`). **NO re-agregar sin preguntarle a Diego por qué lo sacó.** Recuperable si hace falta: `git revert b7d4e26`.
- `7-Conclusiones.tex:2` usa `\label{chapter:8-Conclusiones}` (herencia histórica). El `\autoref` de la intro resuelve bien igual. Renombrar es opcional.

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
