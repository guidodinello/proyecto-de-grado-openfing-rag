# Revisión independiente — correcciones de comentarios de tutores

**Fecha:** 2026-08-31
**Revisor:** verificación independiente (no basada en el checklist de los autores)
**Versión final auditada:** `../Proyecto_de_Grado_INCO_InCo_FIng_UdelaR.pdf` (111 páginas, portada 31/08/2026)
**Fuentes de comentarios:**

- Luis Chiruzzo — `mine/comments/202608221438_..._comments.pdf` (autor "Luis", 38 anotaciones)
- Libertad Tansini — `mine/comments/20260823_..._260822_143804.pdf` (autor "Usuario", 31 anotaciones)

Método: se extrajeron todas las anotaciones (`/Annots`, tipos Highlight/Text) con pypdf, se recuperó el
texto anclado con `pdftotext`, y para cada una se ubicó el pasaje en la versión final (texto del PDF
compilado + fuentes `.tex` en HEAD). El PDF final corresponde al estado actual del repositorio
(verificado: "Libertad Tansini" en portada, figura de arquitectura apaisada, "cinco palabras" en el
caso AVL, anexo E de planificación presente, etc.).

---

## 1. Resumen ejecutivo

| Resultado | Cantidad (tras el audit del 2026-08-31) |
|---|---|
| **APLICADO OK** | 65 |
| **APLICADO PARCIAL** | 0 |
| **NO APLICADO** | 0 |
| **NO VERIFICABLE con impacto** | 0 |
| **Total anotaciones consideradas** | 65 accionables (de 69 marcas; 4 son *highlights* auxiliares sin contenido que acompañan a otra anotación) |

*Valores originales de esta review (antes del audit): 62 OK, 1 no aplicado (T10), 2 no verificables
(T27 + un highlight aux). Los tres se cerraron después: T10 con `43002fe`, T27 con `a15ea0c`,
y L18 resultó mal aplicada y se corrigió con `e86b65f`. Detalle en la sección 6.*

**Veredicto:** todas las correcciones concretas pedidas por ambos tutores están aplicadas y
correctamente aplicadas en la versión final. El único ítem no aplicado es una sugerencia de estilo
opcional ("se considera un conjunto de documentos confiables o corpus curado") sobre un párrafo de la
introducción que fue reescrito, por lo que la marca quedó sin objeto. No se detectaron cambios de
contenido ajenos a un comentario de los tutores o a las excepciones acordadas.

**El informe se puede entregar el 1/9** (ver sección 5), con dos pendientes conocidos que dependen de
los autores y no de correcciones de redacción: el párrafo sobre Gemini (`% TODO (Diego)`) y la
validación de los porcentajes de las dos tablas del anexo E.

---

## 2. Tabla por comentario

### Luis Chiruzzo

> **Actualización 2026-08-31 (post-review):** ver la sección "6. Correcciones tras el audit
> de anclaje" al final. Cambian: L18 (se aplicó en el lugar equivocado, ya corregido),
> T10 (cerrado con una aposición), T27 (frase acortada). Conteo final: 65 OK, 0 parciales,
> 0 no aplicados, 0 no verificables con impacto.

| # | Pág. | Qué pedía | Qué se encontró en la versión final | Estado |
|---|---|---|---|---|
| L1 | 1 | Apellido de la cotutora: "Tansini" (una n) | Portada: "Libertad Tansini"; `Estructura.tex` y `main.tex` unificados | OK |
| L2 | 20 | La cita de Russell & Norvig debe decir solo "Russell and Norvig" | `referencias.bib`: `author = "{Russell and Norvig}"`; el PDF renderiza "Según Russell and Norvig (2020)" | OK |
| L3 | 22 | Borrar "Vaswani et al." redundante, dejar la `\cite` | Cap. 2: "La arquitectura *Transformer* fue introducida en \cite{vaswani2017attention}" | OK |
| L4 | 38 | "señalizan" → "indican" | Cap. 3 §Análisis Cuantitativo: "estadísticas objetivas que indican cuán cercana es una transcripción" | OK |
| L5 | 38 | "cercano" → "cercana" (concordancia) | mismo pasaje: "cuán cercana es una transcripción" | OK |
| L6 | 38 | Mover `\cite{Morris2004}` al final de la definición en texto de MER | Cap. 3: "...combina sustituciones, eliminaciones e inserciones \cite{Morris2004}." antes de la fórmula | OK |
| L7 | 40 | "UEFI(" → "UEFI (" (espacio) | Cap. 3: "reuniones con la UEFI (Unidad de Enseñanza de Facultad de Ingeniería...)" | OK |
| L8 | 40 | "Por lo tanto,se" → "Por lo tanto, se" (coma y espacio) | Cap. 3: "Por lo tanto, se debe mencionar qué información toma de cada uno de los segmentos" | OK |
| L9 | 46 | Referenciar el anexo B.2 (prompt de transcripción) | Cap. 4 §Módulo Transcriptor: "El texto completo de este prompt se detalla en el \autoref{section:A-1-prompt-transcripcion}"; `\label` existe en `1-Prompting.tex:49` | OK |
| L10 | 48 | "esta no va" sobre "evita el 'ruido' visual de agregar fuentes y referencias..." | La frase fue eliminada en Cap. 4 §Decisión de recuperación | OK |
| L11-12 | 48 | Comillas de apertura rectas → `` `` `` en "¿Por qué?", "¿Algún ejemplo?" | La oración que contenía esas comillas fue eliminada (L10); observación sin objeto | OK |
| L13 | 49 | Referenciar el anexo B.1 (prompt del asistente) en "Construcción del prompt" | Cap. 4: "...el *system prompt* del asistente educativo (\autoref{section:A-1-prompt-asistente})" | OK |
| L14 | 51 | "cuatro" → "cinco" | Cap. 4, caso AVL: "La consulta tiene cinco palabras y no hay historial" (¿Qué/es/un/árbol/AVL? = 5) | OK |
| L15 | 68 | Notas al pie de la tabla del dataset quedaron mal ancladas | Tabla convertida a `threeparttable` con `tablenotes` a–d dentro de la propia tabla | OK |
| L16 | 68 | "posee" → "poseen" (sujeto plural) | Cap. 6: "las primeras clases del curso de Computación 1 poseen una temática similar" | OK |
| L17 | 68 | Primera aparición de "PLN": expandir a "Procesamiento de Lenguaje Natural (PLN)" | Cap. 6 §6.1: "Introducción al Procesamiento de Lenguaje Natural (PLN) están a cargo de..." en la primera mención del cuerpo | OK |
| L18 | 73 | Caret de inserción después de "introducirían", nota "sesgos o" → insertar ahí | **Se había aplicado mal** (se pluralizó "el sesgo del juez" al final del párrafo, que Luis no marcó). Corregido en `e86b65f`: "...potencialmente introducirían **sesgos o** evaluaciones incorrectas..." y revertido el cambio no marcado | OK (corregido post-review) |
| L19 | 73/74 | Inconsistencia 24 vs 16 (la tabla tiene 16) | Cap. 6: "el volumen de la muestra, de 16 preguntas únicas evaluadas en 24 consultas"; y "las 16 preguntas dieron lugar a 24 consultas evaluadas, ya que las ocho preguntas sobre el corpus completo se ejecutaron con ambas variantes de prompt" | OK |
| L20 | 74 | "tabla,(respuesta, contexto, etc)" → "tabla (respuesta, contexto, etc.)" | Cap. 6: "más detalles que en la tabla (respuesta, contexto, etc.)" | OK |
| L21 | 78 | Falta espacio antes del paréntesis ("consulta(30 de mayo") | El texto se movió al `\caption`: "al momento de la consulta (30 de mayo de 2026)"; la frase del cuerpo se acortó | OK |
| L22 | 79 | (*highlight* auxiliar sobre la fila de notas de precios) | Resuelto junto con L23 vía `tablenotes` | OK |
| L23 | 79 | Tabla 6.4 y 6.5 son dos `\caption` para una sola tabla; unificar | Una sola tabla con un `\caption` (descripción de precios y método fusionada), `\label{6-Precios-Tabla}` único | OK |
| L24 | 80 | El anexo de IdeM "ahora es la sección 6.6"; corregir cross-refs | Cap. 6: "tal como se describe en la Sección 6.6" y "(véase Sección 6.6)"; `\label{section:6-IngenieriaMuestra}` creado; el PDF renderiza "Sección 6.6" | OK |
| L25 | 82 | Puntuación: "se celebro Ingeniería de Muestra. Una instancia" | Cap. 6 §6.6: "se celebró Ingeniería de Muestra, una instancia donde se comparten..." | OK |
| L26 | 82 | Forma verbal ("hubo" / zona de "esta") | Zona reescrita: "se celebró", "Esta presentación permitió recoger..." | OK |
| L27 | 82 | "prototipo": aclarar que lo mostrado en IdeM era un prototipo | Cap. 6 §6.6: "el grupo compartió con el público un prototipo del chatbot asistente" | OK |
| L28 | 82 | ", el": serie "evaluar el entusiasmo alcance, la viabilidad..." | Cap. 6 §6.6: "evaluar el entusiasmo, el alcance, la viabilidad y el potencial impacto" | OK |
| L29 | 82 | "poster" → "póster"; "Ingenieria" → "Ingeniería" | Cap. 6 §6.6: "un póster presentado por el grupo en Ingeniería de Muestra" | OK |
| L30 | 83 | "no es un impedimento" → "no son un impedimento" | Cap. 7: "...el tiempo que demanda el preprocesamiento de las clases no son un impedimento" | OK |
| L31 | 84 | "El proyecto valida... son" — redacción | Cap. 7: "El proyecto muestra que las barreras para implementar herramientas educativas... son principalmente metodológicas, no económicas, lo que abre posibilidades para..." | OK |
| L32 | 85 | ", desarrollando": fragmento de oración suelto | Cap. 7 §Trabajo a futuro: "...subir sus clases de manera online, desarrollando herramientas similares a OpenFing." | OK |
| L33 | 85 | "garantizaría" → "se garantiza" (modo verbal) | Cap. 7: "La integración institucional aporta la sostenibilidad, estabilidad y el respaldo necesario a largo plazo." (reformulado a indicativo) | OK |
| L34 | 86 | **Error conceptual**: la similitud vectorial sí es semántica; lo que no garantiza es relevancia, y hay que medirlo | Cap. 7 §Trabajo a futuro, párrafo de Re-Ranking totalmente reescrito: "esos *embeddings* se entrenan justamente para que la cercanía entre vectores refleje cercanía semántica... esa cercanía semántica general no garantiza que un fragmento sea el más pertinente... El impacto de esta técnica debe medirse de forma empírica... construir un conjunto de consultas con los fragmentos relevantes anotados, en la línea del conjunto de preguntas de evaluación..." | OK |
| L35 | 86 | Agregar a trabajo a futuro: con un corpus grande de preguntas/vectores relevantes se podría *fine-tunear* | Cap. 7: párrafo nuevo: "Ese mismo conjunto de consultas con fragmentos relevantes anotados habilitaría además un ajuste fino del modelo de *embeddings* sobre el dominio de OpenFing..." | OK |
| L36 | 93 | El anexo de IdeM ahora debería ser solo "Póster utilizado en Ingeniería de Muestra" | `0-IDM.tex`: `\chapter{Póster utilizado en Ingeniería de Muestra}`; el anexo quedó solo con el póster (el relato está en §6.6) | OK |
| L37 | 99 | El anexo de estimaciones no está referenciado en el cuerpo | Cap. 3 §Requisitos: "...surgió además un documento con las estimaciones de infraestructura... que se incluye en el \autoref{chapter:A-2-Estimaciones Para Open Fing}" (PDF: "Apéndice C"). También citado desde Cap. 7 (Subsección C.1.4) | OK |
| L38 | 99 | Confirmar nombres UEFI / URI | UEFI = Unidad de Enseñanza de Facultad de Ingeniería; URI = Unidad de Recursos Informáticos (sigla "(URI)" agregada en Cap. 3; el huérfano con "Unidad de Repositorios Institucionales" fue borrado) | OK |

### Libertad Tansini

| # | Pág. | Qué pedía | Qué se encontró en la versión final | Estado |
|---|---|---|---|---|
| T1 | 6 | Anexo corto al final: Gantt inicial/final, % por tarea-macro, estimación de horas, comentario de demoras | Anexo E "Planificación y ejecución del proyecto" (`5-Planificacion.tex`): tabla cronograma planificado vs. real, tabla de % de dedicación por tarea macro, sección "Comentario sobre las demoras". Referenciado desde Cap. 7. **Nota:** los % son estimación pendiente de validación de los autores (excepción acordada) | OK |
| T2 | 9 | "existen falencias en los LLMs" → "cajas negras / riesgos" | Resumen: "los modelos comerciales funcionan como cajas negras y su uso conlleva ciertos riesgos... una solución personalizada que mitigue esos riesgos" | OK |
| T3 | 9 | "distintas posibles arquitecturas las cuales se decidieron dejar de lado" → "alternativas y los motivos" | Resumen: "la arquitectura final del sistema junto con las alternativas consideradas y los motivos por los que se dejaron de lado" | OK |
| T4 | 9 | Párrafo de pipeline: datos de corpus + conclusión + IdeM 2025 | Resumen, párrafo nuevo: "239 cursos y 4.339 clases, utilizando faster-whisper con CTranslate2, lo que redujo los tiempos de procesamiento entre dos y cuatro veces...", WER < 0,05, Llama 3.1 8B; y "se mostró a estudiantes y docentes en la jornada Ingeniería de Muestra 2025, instancia que aportó una validación cualitativa" | OK |
| T5 | 9 | El resumen va antes del índice | `main.tex`: `\input{...0-Resumen}` ahora precede a `\tableofcontents`; en el PDF el Resumen aparece antes del índice | OK |
| T6 | 15 | Falta cita para "tendencia conocida a las alucinaciones" | Cap. 1: "...tendencia conocida a las alucinaciones \cite{ji2023survey}" (entrada bib nueva, survey ACM CSUR 2023) | OK |
| T7 | 15 | Falta cita / "riesgo" para el contexto educativo | Cap. 1: "...puede consolidar conceptos erróneos en el estudiante \cite{kasneci2023chatgpt}" | OK |
| T8 | 15 | Primera mención de RAG: "(RAG por sus siglas en inglés)" | Cap. 1: "Generación Aumentada por Recuperación (RAG, por sus siglas en inglés) \cite{lewis2020retrieval}" | OK |
| T9 | 15 | Falta cita / nota al pie para OpenFing | Cap. 1: "...transcripciones automáticas del contenido educativo de OpenFing \cite{misc_OpenFing}" | OK |
| T10 | 15 | Sugerencia: "un conjunto de documentos confiables o corpus curado de información académica" | Cerrado post-review (`43002fe`): "...utilizando como base de conocimiento un corpus curado de material académico, las transcripciones automáticas del contenido educativo de OpenFing..." | OK (post-review) |
| T11 | 15 | "evitando así..." → considerar "mitigando..." | La frase "evitando así" ya no está en la introducción reescrita; observación sin objeto | OK |
| T12 | 16 | Primera mención de ASR: "(ASR por sus siglas en inglés)" | Cap. 1, objetivo 2: "reconocimiento automático de voz (ASR, por sus siglas en inglés) \cite{SpeechandLanguageProcessing}" | OK |
| T13 | 16 | Falta cita para ASR | idem T12, `\cite{SpeechandLanguageProcessing}` | OK |
| T14 | 16 | Oración mal ensamblada "...en OpenFing pipeline implementado procesó los 239 cursos..." | Cap. 1: "...cubrir la totalidad del contenido disponible en OpenFing. El pipeline implementado procesó los 239 cursos y 4.339 clases..." | OK |
| T15 | 19 | "concentra miles de horas... y miles de clases" — "¿específicamente?" | Cap. 2 §OpenFing: "concentra miles de horas de video en 239 cursos y 4.339 clases" | OK |
| T16 | 22 | "ajuste iterativo de pesos matemáticos" → "pesos en funciones matemáticas" | Cap. 2: "aprenden patrones complejos a través del ajuste iterativo de pesos en funciones matemáticas" | OK |
| T17 | 27 | "no es aconsejable ni deseado" → "deseable" | Cap. 2 §Alucinaciones: "no es aconsejable ni deseable que los estudiantes confíen ciegamente" | OK |
| T18 | 33 | "En los capitulos ... y se explican las cuestiones planteadas en este capitulos" — "no va esta frase" | Cap. 3: la oración fue eliminada | OK |
| T19 | 33 | "para fundamentar las decisiones" → "para respaldar adecuadamente la toma de decisiones" | Cap. 3 §Objetivos: "...realizó para respaldar adecuadamente la toma de decisiones de diseño del sistema" | OK |
| T20 | 34 | Falta cita: API REST | Cap. 3: "una \Gls{api} \Gls{rest} \cite{fielding2000rest}" (tesis doctoral de Fielding, 2000) | OK |
| T21 | 34 | Falta cita: pgvector | Cap. 3: "\textbf{pgvector} \cite{misc_pgvector}" | OK |
| T22 | 34 | Falta cita: FAISS | Cap. 3: "librería... por Meta \cite{douze2025faiss}" (además se descomentó la frase que estaba rota) | OK |
| T23 | 34 | Falta cita: Elasticsearch | Cap. 3: "\textbf{Elasticsearch} \cite{gormley2015elasticsearch}" | OK |
| T24 | 37 | "existen estudios... . Los ASR son mayoritariamente entrenados en inglés" — "¿ya que?" (nexo causal) | Cap. 3: "...a pesar de que existen estudios y métricas publicadas al respecto, ya que los ASR son mayoritariamente entrenados en inglés..." | OK |
| T25 | 40 | "afinamiento" → "refinamiento" | Cap. 3: "para el refinamiento de estos requisitos" | OK |
| T26 | 43 | "¿se puede agrandar la figura?" (Figura 4.1, overview) | Cap. 4: la figura se movió a página apaisada (`landscape`, `[p]`, `width=\linewidth`) | OK |
| T27 | 71 | *Highlight* sobre la palabra "optimizar" en "línea de mejora futura para optimizar aún más el procesamiento" (vago) | Cerrado post-review (`a15ea0c`): "Una cuantificación sistemática de este efecto queda como línea de trabajo futuro." | OK (post-review) |
| T28 | 79 | "¿achicar tamaño de letra?" (tabla de precios) | Cap. 6: `\footnotesize` aplicado a la tabla de comparación de modelos | OK |
| T29 | 83 | "Algo de esto se evidenció en Ingeniería de Muestra..." (párrafo del estudiante) | Cap. 7: "Estas ventajas también se manifestaron en la retroalimentación recogida durante la jornada Ingeniería de Muestra (Sección 6.6), donde estudiantes del interior del país y de otras facultades destacaron el valor del asistente como herramienta de equidad educativa." | OK |
| T30 | 84 | "educativas basadas en IA" → agregar "de tipo RAG" | Cap. 7: "herramientas educativas de tipo RAG basadas en IA" | OK |

*Highlights auxiliares sin contenido propio (acompañan a otra anotación, ya cubiertos): T p.16 y≈186 (junto a T14), T p.40 y≈600 (junto a T25), L p.79 y≈643 (junto a L23), L p.48 (las dos marcas de comillas, junto a L10).*

---

## 3. Detalle de los ítems que NO están OK

### T p.15 — "corpus curado" (NO APLICADO, menor)

- **Qué pedía:** la tutora subrayó parte de la definición de RAG en la introducción y anotó la
  formulación alternativa "que se considera un conjunto de documentos confiables o corpus curado de
  información académica".
- **Qué se encontró:** el párrafo de la introducción fue reescrito por completo. La versión final dice
  "utilizando como base de conocimiento las transcripciones automáticas del contenido educativo de
  OpenFing". No aparece la expresión "corpus curado" ni "documentos confiables". Sí se conserva la idea
  equivalente ("ancla sus respuestas en el material de los cursos", "fuentes verificables" en Cap. 2).
- **Impacto:** nulo a efectos de corrección. Es una sugerencia de redacción sobre un texto que ya fue
  mejorado por otra vía. Se puede dejar así; si se quisiera cerrar formalmente, bastaría con una
  aposición de una línea en la introducción.

### T p.71 — highlight sin texto (NO VERIFICABLE)

- La anotación es un subrayado sin comentario, sobre la subsección cualitativa de errores de
  transcripción (muletillas, nombres propios, errores de grabación). No hay `/Contents`, no hay una
  corrección obvia asociada y el `diff` de Cap. 6 no toca esa subsección. No es posible determinar qué
  se pedía. Dado que el resto de las marcas de la tutora en esa zona no tienen contenido tampoco,
  probablemente sea una marca de lectura y no un pedido de cambio.

---

## 4. Cambios no ligados a comentarios

No se detectó ningún cambio de contenido o redacción fuera de: (a) un comentario concreto de los
tutores, (b) las excepciones acordadas, o (c) limpieza cosmética dentro del mismo pasaje que un tutor
marcó. Detalle:

### 4.1 Excepciones ya acordadas (correcto que estén)

1. **Sección "Declaración de Uso de Herramientas de IA"** (Cap. 1, entre "Aportes del Proyecto" y
   "Organización del Documento"). Requisito del PG (documento del EVA), no un comentario de PDF.
   Contiene un `% TODO (Diego)` para un párrafo sobre Gemini que queda pendiente **a propósito**.
2. **Anexo E "Planificación y ejecución del proyecto"** (`5-Planificacion.tex`). Responde a T p.6.
   Los porcentajes de sus dos tablas son estimación (tiempo de calendario + distribución de commits),
   **pendientes de validación de los autores**.
3. **Borrado de `7-TrabajoAFuturo.tex` y `8-Conclusiones.tex`** (huérfanos, no compilaban, contenido
   duplicado en `7-Conclusiones.tex`).
4. **Link de Trello** en el anexo Recursos: de link de invitación a URL de board público
   (`https://trello.com/b/D0HvvzSZ/backlog`).
5. **Tres typos de duplicación** corregidos sin marca de tutor (autorizados por los autores):
   - Cap. 2: "(UdelaR) OpenFing" → "(UdelaR)" (se eliminó el "OpenFing" repetido).
   - Cap. 6: "Let's EncryptLet's Encrypt" → "Let's Encrypt".
   - Cap. 6: encabezado "Preguntas que carecen relación con el dominio académico." → "Preguntas sin
     relación con el dominio académico".

### 4.2 Limpieza cosmética dentro de pasajes marcados (aceptable, se señala para transparencia)

- **Cap. 3 §Requisitos del Sistema:** además de agregar "(URI)" y la referencia al anexo de
  estimaciones (L p.99), se reescribió la oración vecina ("está unidad es la actual encargada de
  mantener el sistema de OpenFing funcionando" → "La UEFI está en contacto directo diario con la
  Unidad de Recursos Informáticos (URI), que es la unidad encargada de mantener el sistema de OpenFing
  en funcionamiento") y se cambió la URL de la nota al pie de la URI de
  `https://idm.fing.edu.uy/es/sysadmin` a `https://www.fing.edu.uy/es/sysadmin`. Ligado a la
  identificación de la URI que pidió Luis; la corrección de la URL es razonable.
- **Cap. 6 §6.1:** al introducir la sigla "PLN" (L p.68) se reconstruyó una oración que estaba rota
  ("Ambas clases de Computación son presentadas por Martín Pedemonte, en cuanto a las clases de
  Guillermo Moncecchi y Luis Chiruzzo." → "...mientras que las clases de Introducción al Procesamiento
  de Lenguaje Natural (PLN) están a cargo de Guillermo Moncecchi y Luis Chiruzzo. El orador de las
  clases de Computación presenta un discurso pausado, en tanto que ambos docentes de PLN..."). El
  arreglo de la oración rota no fue pedido explícitamente, pero es la misma frase de la marca.
- **Cap. 6 §6.4 (tabla de precios):** al fusionar los dos `\caption` (L p.79) el nuevo `\caption`
  incorpora texto explicativo nuevo sobre el significado de las columnas ("para un volumen proyectado
  de 1000 consultas con las métricas de tokens promedio (P Prom, R Prom) y máximas..."). Va algo más
  allá de "unificar lo que dicen", pero mejora la tabla y no introduce datos nuevos.
- **Cap. 6:** "A remarcar, los valores de la tabla ... representan el precio a la fecha de consulta
  (30 de mayo de 2026)." → "Los valores de la ... representan el precio a la fecha de consulta." (la
  fecha se movió al `\caption`). Estilo, dentro de la zona de L p.78.
- **Cap. 7 §Trabajo a futuro:** "Mi Nube" pasó de comillas rectas a `\textit{}`; "Por lo que permitir
  segmentar la información por facultad, se garantiza que..." → "Segmentar la información por facultad
  permite que..." (ligado a L p.85, "se garantiza"). Se agregó una oración que remite al anexo E en el
  párrafo de autocrítica de las conclusiones (ligado a T p.6).
- **`referencias.bib`:** entradas nuevas para las citas agregadas (`ji2023survey`, `kasneci2023chatgpt`,
  `fielding2000rest`, `gormley2015elasticsearch`) y cambio del string de autor de `RussellNorvig2020`
  (L p.20). Todo ligado a comentarios.
- **`main.tex`:** al mover el Resumen antes del índice (T p.9) también se reordenó el bloque de
  Agradecimientos (placeholder, sin cambio de contenido).

### 4.3 Nota — dato no tocado a propósito

`2-EstimacionesParaOpenFing.tex:66` ("2835 videos" / estimación de 1 TB) es un hallazgo de revisiones
internas, no un comentario de tutor. Se dejó intacto, en línea con la regla de alcance. Correcto.

---

## 5. Conclusión: ¿se puede entregar el 1/9?

**Sí.** Todas las correcciones solicitadas por Luis Chiruzzo y Libertad Tansini están aplicadas y
correctamente aplicadas en la versión final del PDF. Incluye:

- el error conceptual de fondo (L p.86, similitud vectorial / relevancia / medición) reescrito de
  forma técnicamente correcta;
- las inconsistencias numéricas (24 vs 16 preguntas) resueltas y explicadas;
- todas las citas faltantes agregadas con entradas `.bib` reales;
- las referencias cruzadas a los anexos (prompts, estimaciones, IdeM → §6.6) corregidas y con `\label`
  existentes;
- el anexo de planificación creado;
- los typos, la puntuación y las concordancias marcadas.

**Pendientes que no bloquean la entrega de correcciones pero conviene cerrar antes de la versión al
tribunal:**

1. **Párrafo sobre Gemini** de Diego (`% TODO (Diego)` en `1-Introduccion.tex`). Si no corresponde,
   eliminar el comentario TODO para que no quede en el fuente.
2. **Validar los porcentajes** de las dos tablas del anexo E (`5-Planificacion.tex`). Hoy son
   estimación declarada como tal en el propio texto del anexo.

*(El punto 3 original — cerrar T p.15 — ya se hizo, ver sección 6.)*

Recomendación: compilar una última vez y revisar que `\autoref{chapter:A-Planificacion}` y
`\autoref{section:A-1-prompt-transcripcion}` / `\autoref{section:A-1-prompt-asistente}` resuelvan sin
`??` en el PDF final (en el PDF auditado resuelven correctamente).

---

## 6. Correcciones tras el audit de anclaje (2026-08-31)

Después de esta review se revisaron a mano, con el usuario mirando el PDF con zoom, todas las
marcas cortas donde la posición exacta del `QuadPoint` determina qué palabra se corrige. Resultado:

| Marca | Estado en la review | Qué pasó |
|---|---|---|
| **T10 p.15** ("corpus curado") | NO APLICADO (menor) | Cerrado con `43002fe`: aposición en la definición de RAG de la intro, "...utilizando como base de conocimiento un corpus curado de material académico, las transcripciones automáticas...". |
| **T27 p.71** (highlight sin texto sobre "optimizar") | NO VERIFICABLE | El resaltado estaba sobre la palabra "optimizar" en "línea de mejora futura para optimizar aún más el procesamiento" (vago + redundante). Acortado con `a15ea0c`: "Una cuantificación sistemática de este efecto queda como línea de trabajo futuro.". |
| **L18 p.73** ("sesgos o") | OK (falso positivo) | **Estaba mal aplicada.** La review verificó que el PDF final decía "los sesgos del juez" y lo dio por bueno, pero esa pluralización (al final del párrafo) no fue lo que Luis marcó. Su caret estaba después de "introducirían". Corregido con `e86b65f`: "...introducirían sesgos o evaluaciones incorrectas..." y revertida la pluralización no marcada. |
| p.16 y p.40 (highlights sin texto) | aux de T14 / T25 | Confirmados como auxiliares de comentarios ya resueltos. |
| p.51 "cinco", p.82 "." / "hubo" | OK | Confirmados correctos contra el PDF (p.51 sobre "cuatro" en el ejemplo AVL; p.82 son puntuación/flujo de "con el público, entre ellos, varios estudiantes", cubierto por la reescritura de §6.6). |

**Lección:** la review independiente usó el mismo método de extracción por coordenadas
(`pypdf` + `pdftotext -bbox`) que el trabajo original, así que comparte el punto ciego para
las marcas de una palabra o los caret de inserción. Para ese tipo de marca, el chequeo confiable
es abrir el PDF y mirar el resaltado. De 69 marcas, ese chequeo encontró 1 mal aplicada (L18).
