# TODOs Pendientes

## Cap. 0 — Resumen
- [x] **Errores gramaticales corregidos en texto**: "en las respuestas" (✓), "Facultad de Ingeniería" (✓), "una herramienta" (✓) — verificado en texto actual 2026-04-26.
- [x] **Nuevo typo**: "pausible" (línea 7) → "plausible"
- [x] **Nuevo typo**: "Desde ahora en se refiere al modulo" (línea 11) → "Desde ahora en adelante se denomina"
- [x] **Keywords ampliadas**: `\keywords{RAG, LLM, OpenFing, ASR, Whisper, embeddings, chatbot, educación}` — verificado presente.
- [ ] **Contenido incompleto**: según lineamientos el resumen debe describir la solución Y su evaluación. No menciona WER obtenido, modelo LLM utilizado, pgvector ni resultados obtenidos.

## Cap. 1 — Introducción
- [x] **CRÍTICO — contradicción fine-tuning/RAG**: reescrito con descripción correcta de RAG y motivación desde alucinaciones.
- [x] **CRÍTICO — Instrucciones de draft eliminadas**: líneas 13–17 de 1-Introduccion.tex eliminadas (2026-05-02).
- [x] **Referencia rota**: `\autoref{chapter:4-Arquitura y Diseño}` corregida a `chapter:4-Arquitectura y Diseño`.
- [x] Escribir sección **Objetivos del Proyecto**: objetivo general + 5 específicos redactados.
- [x] Completar sección **Organización del Documento**: reescrita con formato `\textbf{\autoref{}}` y descripción de cada capítulo.
- [x] Agregar sección **Conclusiones Resumidas**: creada con `%TODO` para completar al final del informe.
- [ ] Completar sección **Resultados Obtenidos** (vacía — pendiente de resultados finales de Whisper y QA)

## Cap. 1 — Introducción
- [x] **NUEVO (2026-04-26)** — Em dash línea 21: "la alucinación — generan afirmaciones" → reemplazado con coma (verificado 2026-05-03).
- [x] **NUEVO (2026-05-03)** — Em dash en línea 15: `de \Gls{OpenFing} — plataforma que concentra` → corregido a `, plataforma que concentra` — 2026-05-04.

## Cap. 2 — Marco Teórico
- [x] **§ OpenFING — estadísticas sin citar**: suavizado a "miles de horas de video y miles de clases" (sin cifras concretas). Cita innecesaria — la página oficial no publica estadísticas (ver `mine/citation-audits/2026-04-28-openfing-stats/resumen.md`); `\cite{OpenFing}` ya está en la oración anterior del mismo párrafo.
- [x] Corregir sección **2.2.5 Segmentos**: justificación corregida (contexto del LLM + granularidad de recuperación); texto duplicado eliminado; labels arreglados.
- [x] Corregir estrategia de chunking: verificado contra DB (217.986 chunks, todos `chunk_strategy: "semantic"`) — la estrategia real es **Semantic Chunking** con `intfloat/multilingual-e5-base`, threshold percentile 0.6, min_chunk_size 400. Las correcciones anteriores que decían "Recursive Character Splitting" eran incorrectas; revertido a semántico. `detalles-tecnicos-codigo.md` actualizado en 2026-05-03.
- [ ] Arreglar **problema con las referencias** (afecta todas las referencias del documento)
- [x] **`Hallucination_Abogado` y `Hallucinations_in_LLMs`**: presentes en `referencias.bib` (root) — migradas del bib de capítulos que fue eliminado. Sin problema de compilación.
- [x] **ALTA — `Prompts_y_estrategia_de_prompts`**: eliminada del bib — 2026-05-03.
- [x] **ALTA — `Modelos_De_Lenguage`**: eliminada del bib — 2026-05-03.
- [x] **ALTA — `Diferencia_LLMS_y_Modelos_De_Lenguaje`**: eliminada del bib — 2026-05-03.
- [x] **MEDIA — `InteligenciaArificialGenerativa`**: ya no existe en el bib (eliminada en sesión anterior).
- [x] **MEDIA — duplicado Jurafsky**: `Jurafsky2023` eliminado — queda solo `SpeechandLanguageProcessing` como entrada canónica.
- [x] **BAJA — `OpenFing`**: autor ya figura como "OpenFing" (institución) en bib — correcto.
- [ ] **BAJA — `One_Shot_Prompting`**: año incorrecto en bib: 2024 → 2025 (artículo de IBM Think publicado noviembre 2025).
- [ ] **BAJA — `ASR_Accuaracy`**: (1) typo en key: "Accuaracy" → "Accuracy"; (2) venue posiblemente incorrecto (puede ser AIP Conference Proceedings, no iJOE Vol. 20); (3) la cita está suelta en el tex sin ligarse a ninguna afirmación concreta.
- [x] Escribir **sección de NLP** — redactada 2026-04-28 (3 párrafos: definición, tareas clásicas, deep learning + relevancia para el proyecto)
- [x] Añadir explicación de redes neuronales (Jurafsky) y deep learning (Goodfellow) — subsección Red Neuronal presente con cita a Goodfellow et al.
- [x] Redactar `\subsubsection{Inteligencia Artificial Generativa}` — redactada 2026-04-28 (2 párrafos: discriminativo vs generativo + LLMs como representante, citas Goodfellow + Zhao2023)
- [x] Revisar sección sobre embeddings / modelos — redactada 2026-04-28 (all-MiniLM-L6-v2, multilingual-e5-base, DPR, SBERT)
- [x] Redactar `\subsection{Arquitectura Transformer}` — redactada 2026-04-28 (3 párrafos: autoatención vs recurrentes, codificador-decodificador y variantes, relevancia transversal para Whisper/embeddings/LLM)
- [x] Subsección Plataformas Análogas: Khanmigo reemplazado por Open TutorAI con contenido real y cita arXiv:2602.07176.
- [x] **Texto duplicado en Segmentos**: eliminado — cada subsubsección tiene ahora contenido propio y correcto.
- [x] **Estructura rota en sección RAG**: corregida — subsubsecciones duplicadas eliminadas, jerarquía arreglada.
- [x] **Sección RAG redactada**: intro (Naive RAG vs Advanced/Modular con `gao2023retrieval`), subsubsección Recuperación y subsubsección Generación con contenido real.
- [x] **Alucinaciones / RAG**: `\cite{Hallucinations_in_LLMs}` integrado en la intro de la subsección RAG; TODO resuelto.
- [x] **FINGChat oración cortada**: sección completa en el tex actual — describe corpus, enfoque RAG y diferencia con el proyecto.
- [x] **Plataformas Análogas intro cortada**: intro completa en el tex actual.
- [x] **Subsección Whisper vacía** (Cap. 2): redactada 2026-04-28 — ASR intro (2 párrafos: definición + WER) + Whisper (3 párrafos: arquitectura, entrenamiento, variantes/faster-whisper).
- [x] **Cita suelta**: `\cite{OpenFing}` integrado inline en la oración de descripción de la plataforma.
- [x] **NUEVO (2026-04-26) — Subsección OpenUdelar vacía**: redactada — tiene contenido real (descripción, diferencia con OpenFing, dirección de expansión futura).
- [x] **NUEVO (2026-04-26) — TODO raw visible en PDF**: eliminado — no aparece en el tex actual.
- [x] **NUEVO (2026-04-26) — \todo cyan visible en Alucinaciones**: eliminado — no aparece en el tex actual.
- [x] **NUEVO (2026-04-26) — Embedding completamente vacía**: redactada 2026-04-28 (3 párrafos con modelos del proyecto y pipeline de consulta).
- [x] **NUEVO (2026-04-28) — ALTO — Segmentos: parámetros de implementación en Cap. 2**: el tex describe el enfoque conceptual. Nota: la estrategia es semántica (confirmado por DB 2026-05-03), no recursiva como se asumió en esta sesión.
- [x] **NUEVO (2026-04-28) — ALTO — Embedding: nombres de modelos en Cap. 2**: eliminados — el tex actual dice "modelo de embedding multilingüe" sin nombrar modelos específicos.
- [x] **NUEVO (2026-04-28) — ALTO — Whisper: detalles de arquitectura interna demasiado técnicos**: simplificado — el tex actual usa la descripción funcional sin espectrograma ni atención cruzada.
- [x] **NUEVO (2026-04-28) — ALTO — Whisper: detalles de entrenamiento demasiado técnicos**: simplificado — el tex actual describe diversidad de datos y capacidades multilingues sin mencionar 680k horas ni supervisión débil.
- [x] **NUEVO (2026-04-28) — MEDIO — RAG: "El presente proyecto implementa Naive RAG"**: no aparece en el tex actual.
- [x] **NUEVO (2026-04-28) — MEDIO — Embedding: "redes siamesas"**: eliminado — SBERT dice "aptas para una comparación eficiente".
- [x] **NUEVO (2026-04-28) — BAJO — Alucinaciones: párrafo de 3 causas sin cita directa**: `\cite{Hallucinations_in_LLMs}` al final del párrafo de causas presente en el tex.
- [x] **NUEVO (2026-04-28) — BAJO — LLMs: "miles de millones de parámetros" sin cita**: `\cite{SpeechandLanguageProcessing}` agregado.
- [x] **NUEVO (2026-04-28) — BAJO — One-Shot Prompting: paráfrasis presentada como cita directa**: reescrito como paráfrasis con cita al final.

## Cap. 2 — Marco Teórico (nuevos issues 2026-04-28)
- [x] **Cap. 2, Red Neuronal, línea 47**: reescrito — "Goodfellow et al. \cite{Goodfellow-et-al-2016} presentan una referencia exhaustiva..." con "deep learning" como dos palabras.
- [x] **Cap. 2, Tokenización, línea 57**: `\cite{Jurafsky2023}` reemplazado por `\cite{SpeechandLanguageProcessing}` integrado en la oración.

## Cap. 2 — Marco Teórico (nuevos issues 2026-05-03)
- [ ] **NUEVO (2026-05-03) — Sección 2.2.5 Segmentos: estrategia incorrecta en el tex**: verificado 2026-05-04 — el tex actual describe ambas estrategias (Semántica y Recursiva) a nivel conceptual sin parámetros concretos de implementación. Parece correcto para Marco Teórico. Investigar si hay alguna afirmación residual incorrecta.
- [x] **NUEVO — Typo línea 120**: "lenguange" → "lenguaje" — 2026-05-04.
- [x] **NUEVO — Tildes línea 142**: "ocurrio" → "ocurrió"; "reafirmo" → "reafirmó" — 2026-05-04.
- [x] **NUEVO — Cita flotante línea 143**: `\cite{Hallucination_Abogado}` integrado al final de la oración — 2026-05-04.

## Cap. 2 — Marco Teórico (citation audit 2026-04-28)
- [x] **ALTA — `chunks` (blog no académico)**: reemplazado — `gao2023retrieval` y `langchain`.
- [x] **ALTA — `Hallucinations_in_LLMs`**: instancias de RAG → `lewis2020retrieval`; causa → `Hallucinations_in_LLMs`.
- [x] **ALTA — `openTutorAI2025`**: título corregido; texto reescrito con contenido real del abstract.
- [x] **MEDIA — `SpeechandLanguageProcessing` para chunking semántico**: reemplazado por `gao2023retrieval`.
- [x] **BAJA — `RussellNorvig2020` campo `volume`**: eliminado del bib.
- [x] **BAJA — `ASR_Accuaracy` (venue incorrecto)**: renombrado a `ASR_Accuracy` en bib, venue corregido.
- [x] **NUEVO — `ASR_Accuaracy` aún en tex**: verificado 2026-05-02 — el tex ya usa `\cite{ASR_Accuracy}` (key correcto). Resuelto.
- [x] **BAJA — `One_Shot_Prompting` (año)**: corregido a 2025 en bib.
- [x] **Cap. 2, `InteligenciaArificialGenerativa`**: no aparece citada en el tex actual.

## Cap. 3 — Requisitos del Sistema
- [x] **NUEVO (2026-04-26) — Typos**: "Performarmance y Escálabilidad" (línea 153) → "Performance y Escalabilidad"; "nobres propios" (línea 196) → "nombres propios" — 2026-05-03.
- [x] **NUEVO (2026-05-03) — Oración incompleta línea 108**: corregida — "el equipo se vio limitado en cuanto al tamaño de modelo a ejecutar." — 2026-05-04.

- [x] **Oración cortada** (línea 99): verificado — la oración "es preferible un modelo mayor no entrenado a un modelo pequeño altamente entrenado" está completa en el texto actual.
- [x] **RPs en tiempo futuro**: verbos principales cambiados a tiempo pasado en los 4 RPs (evaluará→evaluó, comparará→compararon, realizará→realizó, etc.) — 2026-05-04. Pendiente: documentar explícitamente las decisiones tomadas (pgvector, HuggingFace API, Llama 3.1 8B, faster-whisper).
- [ ] **Diego**: añadir foto de ejemplo para RNF1 (Confiabilidad y Trazabilidad)
- [ ] Encontrar artículo que respalde las estadísticas de uso

## Cap. 4 — Arquitectura (nuevos issues 2026-04-28)
- [x] **Cap. 4, posición del diagrama de Backend**: `fig:Arquitectura_Backend` movido al inicio de la subsección "Componentes del Backend" — 2026-05-03.

## Cap. 4 — Arquitectura
- [x] **Frontend incompleto**: completado con descripción de React/TS/Vite/Zustand/TanStack/JWT.
- [x] **Labels incorrectos**: todos los prefijos `5-` corregidos a `4-` (Scrapper, Descargas, Transcriptor, Generator, Shared).
- [x] **Falta justificación de decisión**: agregada subsección "Base de Datos" con justificación de pgvector (cohesión del modelo de datos + inserciones incrementales sin reconstrucción de índice vs FAISS).
- [x] **Generator menciona OpenAI**: corregido — proveedores reales son HuggingFace Inference API y Ollama.
- [x] **Downloader describe descarga de video**: corregido — descarga audio con yt-dlp, reintentos, sin rate limiting ni validación de integridad.
- [ ] **Diagramas de arquitectura/flujo pendientes** — bloqueado por respuesta de tutores (ver `mine/preguntas-tutores.md`: pregunta sobre qué va en Cap. 4 vs Cap. 5). Una vez recibida la respuesta, implementar lo siguiente:

  **Diagrama A — Overview de componentes (pipeline completo)**
  - Fuente: `mine/arquitectura.mermaid` (ya existe, sirve como punto de partida).
  - Muestra: OpenFing → Scraper → Downloader → Transcriber → Embeddings → PGVector / Backend FastAPI + Generator / Frontend React → Usuario.
  - Corresponde a una vista estática de qué componentes existen. Iría al inicio de `\section{Arquitectura}` como figura introductoria antes de las subsecciones de componentes.
  - El mermaid actual NO incluye el modelo de embeddings concreto — completar con el modelo real (ver `mine/detalles-tecnicos-codigo.md`).

  **Diagrama B — Flujo de una consulta RAG end-to-end**
  - No existe aún; hay que crearlo desde cero en Mermaid.
  - Flujo a documentar: consulta del usuario → (si hay historial y query ≤ 3 palabras, omitir retrieval) → búsqueda vectorial en pgvector (k=4 chunks) → ensamblado de contexto agrupado por clase → prompt template + historial (últimos 4000 tokens) → Llama 3.1 8B vía HuggingFace API → respuesta en español + fuentes con timestamp.
  - Es un diagrama de comportamiento dinámico (qué pasa en runtime), distinto al Diagrama A que es estructural.
  - Según la respuesta de los tutores, puede ir en Cap. 4 (Arquitectura) o Cap. 5 (Implementación).

  **Instrucciones de exportación** (una vez creados los `.mermaid`):
  - Con mermaid-cli: `mmdc -i mine/arquitectura.mermaid -o Nuestro/Imagenes/Arquitectura/Pipeline.png`
  - Alternativa sin instalar nada: pegar en mermaid.live y exportar PNG.
  - Incluir en LaTeX con `\includegraphics` dentro de un entorno `figure`, con caption descriptivo y label con prefijo `fig:Arquitectura_`.

## Cap. 5 — Implementación
- [x] **Estadísticas de herramientas** (sección LLM): contenido reasignado a Cap. 6 — RNF5 Análisis de infraestructura (costos, latencia, comparación self-hosting). No corresponde a Cap. 5.
- [x] **Downloader — corregir descripción**: Cap. 5 ya no menciona Downloader directamente; la descripción de descarga de audio está en Cap. 4.
- [x] **LangChain, FastAPI y Multilingual Embeddings duplicados**: eliminados — cada tecnología aparece una sola vez en su sección correspondiente.
- [x] **Whisper sin descripción**: reescrito con faster-whisper, parámetros reales, VAD, word_timestamps, prompt de dominio.
- [x] **PGVector sin cita**: agregado `\cite{pgvector}`.
- [x] **LLM principal desactualizado**: reescrito con Llama 3.1 8B como modelo principal; Mistral solo como alternativa evaluada.
- [x] **uvicorn no mencionado**: agregado en subsección Entorno con `\cite{uvicorn}`.
- [x] **Tecnologías ausentes**: Prefect, SQLAlchemy/Alembic, Zustand, TanStack, pnpm, Vite, Radix UI, Sentry — todos agregados con citas nuevas en `referencias.bib`.
- [x] **Sección LLM vacía**: redactada con Llama 3.1 8B, proveedores (HuggingFace/Ollama), parámetros de inferencia y alternativas evaluadas.

## Cap. 6 — Experimentación (nuevos issues 2026-04-28)
- [x] **Cap. 6, sección "Por que utilizamos faster whisper y whisper cpp."**: renombrada a "Justificación de faster-whisper" y redactada con justificación real (CTranslate2, velocidad 2-4x, corpus 4339 clases) — 2026-05-02.
- [x] **Cap. 6, sección QA modelos**: "Mistral y Meta" reemplazado por descripción correcta (Llama 3.1 8B principal, Qwen2.5-72B alternativo, Mistral deprecated) — 2026-05-02.

## Cap. 6 — Experimentación
- [x] Sección duplicada "MIO Modelos de Transcripción" eliminada.
- [x] **NUEVO (2026-05-03) — Intro gramaticalmente incorrecta**: reescrita — "En este capítulo se presentan los experimentos realizados para evaluar el desempeño del sistema, cuyos criterios de evaluación se establecieron en los capítulos anteriores." — 2026-05-04.
- [x] **NUEVO (2026-05-03) — Comentario de implementación visible**: eliminado — 2026-05-04.
- [ ] **RNF5 — Análisis de infraestructura (retomar de Cap. 3)**: en Cap. 3 se dejó el análisis en términos cualitativos (self-hosting vs inference-as-a-service, umbrales de VRAM). En la experimentación convendría incluir: (a) costos reales observados con el proveedor elegido (tokens procesados, costo por consulta), (b) latencias medidas en producción vs estimadas, (c) comparar contra la alternativa de self-hosting con los modelos concretos analizados (Llama 2 7B, Mistral 7B). Referencias ya disponibles: `touvron2023llama2`, `jiang2023mistral`, `zheng2023mtbench`, `chiang2024chatbotarena` (MT-Bench y Chatbot Arena como benchmarks de calidad conversacional).
- [ ] **Añadir modelo Whisper `large`**: Enrique pasó las transcripciones — agregar sus resultados a la tabla de evaluación.
- [ ] **Luis**: detallar evaluación de transcripciones manuales con análisis cualitativo (cuándo Whisper anda bien/mal) y conclusión
- [ ] Presentar **dataset completo**: cantidad de videos, horas, tokens, chunks — separado por curso; incluir versión pequeña (experimentos) y versión full
- [ ] Completar **experimentos QA**: N videos, 4 categorías de preguntas, análisis cuantitativo y cualitativo
- [ ] Añadir **volumen total de OpenFing** (estadísticas generales)
- [x] **Referencia rota**: verificado 2026-04-28 — Cap. 6 línea 20 usa `subsection:3-RNF6: Evaluación de Herramientas de Transcripción` que coincide con el label en Cap. 3 línea 145. Resuelta.
- [x] **Conclusión de transcripción**: redactada — recomienda medium+es (WER<0.05), descarta small y base — 2026-05-02.
- [x] **Título incorrecto**: "Por que utilizamos faster whisper y whisper cpp." → "Justificación de faster-whisper", con contenido real — 2026-05-02.
- [x] **\todo block de Luis**: no aparece en el tex actual (ya eliminado en sesión anterior).
- [x] **\label antes de \caption en tabla**: corregido — \label ahora va después del \caption — 2026-05-02.
- [x] **Análisis cuantitativo incompleto**: párrafo de Pnl-1/Pnl-2 agregado al análisis de resultados — 2026-05-02.
- [ ] **Secciones vacías restantes**: "Modelo de Vectorización", "Pregunta Respuesta → Resultados", "Pregunta Respuesta → Conclusión" — pendiente datos de experimentos QA.

## Cap. 7 — Trabajo a Futuro
- [ ] Contactar a Clara (URI) para evaluar integración institucional
- [ ] Reconsiderar redacción del párrafo sobre extensión a otras facultades — especialmente la frase "sería relativamente simple" (puede sonar arrogante al tribunal)
- [ ] Añadir sección sobre **testing automatizado**
- [x] **NUEVO (2026-05-03) — `\autoref` flotante línea 9**: integrado en oración — "Durante nuestra exposición en Ingeniería de Muestra (ver \autoref{...}), se nos comentó…" — 2026-05-04.
- [x] **NUEVO (2026-05-03) — Capitalización inconsistente**: "en ingeniería de muestra" → "en Ingeniería de Muestra" — 2026-05-04.
- [x] **Typo**: "asumí la responsabilidad" → "asumir la responsabilidad" — 2026-05-02.
- [x] **\todo markers visibles**: dos bloques `\todo[inline,color=orange]` eliminados; frase "sería relativamente simple" suavizada a "requeriría un esfuerzo acotado" — 2026-05-02.

## Cap. 8 — Conclusiones
- [x] **Typo**: "quel el alto volumen" → "que el alto volumen" — 2026-05-02.
- [x] **Resultados concretos ausentes**: agregados WER (medium <0.05), LLM (Llama 3.1 8B), dataset (239 cursos, 4339 clases) — 2026-05-03.
- [x] **Contraste planificado vs realizado**: agregado párrafo que mapea los 5 objetivos específicos contra lo realizado; agregado párrafo de autocrítica — 2026-05-03.

## Transversal — Todo el documento
- [x] **"En está sección"** → verificado en Cap. 2: todas las instancias actuales leen "En esta sección" correctamente. Hacer búsqueda global antes de entrega para cubrir otros capítulos.
- [x] **Em dashes en Cap. 2 línea 89**: verificado — texto actual usa comas ("saltos de párrafo, saltos de línea"). Resuelto.
- [x] **Em dash en Cap. 1**: verificado — texto actual usa "la alucinación, generando afirmaciones" (coma). Resuelto.

## referencias.bib
- [x] **Entradas duplicadas CitekeyXXX resueltas**: verificado 2026-04-26 — el archivo solo tiene una copia de cada entrada ejemplo. Error de compilación BibTeX ya no presente por esta causa.
- [x] **NUEVO (2026-05-03) — `chunks` huérfano**: eliminado del bib — 2026-05-04.
- [ ] **NUEVO (2026-05-03) — `React_JS_Coderhouse` huérfano**: ya no se cita en ningún .tex. Eliminar del bib.
- [ ] **NUEVO (2026-05-03) — Entradas de ejemplo**: `CitekeyArticle`, `CitekeyBook`, `CitekeyInproceedings`, `CitekeyManual`, `CitekeyMisc` solo aparecen en comentarios LaTeX de Cap. 1 (no en el PDF). Considerar eliminar del bib antes de la entrega final.
- [x] **`vite` — autor corregido**: cambiado de "Evan You and Vite Contributors" a "VoidZero Inc. and Vite contributors" (copyright oficial en vite.dev).
- [x] **`React_JS_Coderhouse` en Cap. 5**: eliminado el porcentaje "74,5%" del texto; la afirmación queda como "uno de los frameworks más utilizados" sin stat. Entrada `React_JS_Coderhouse` queda huérfana en el bib (ya no se cita en Cap. 5).
- [x] **Entrada `ibm` incorrecta**: verificado 2026-04-28 — entrada `ibm` ya no existe en `referencias.bib`. Resuelta.
- [x] **`whisper` entry**: entrada huérfana eliminada del bib (`radford2022robust` ya era la cita activa en el tex) — 2026-05-03.
- [x] **`workshopOpenFing`**: `note = "Accessed: 2026-05-03"` agregado — 2026-05-03.
- [x] **`RussellNorvig2020`**: campo `volume` ya eliminado en sesión anterior (verificado 2026-05-03).
- [ ] **`Hallucinations_in_LLMs`**: journal listado como "ResearchGate preprint" — no es un journal real.

## Anexos
- [x] **\todo visible eliminado** (0-IDM.tex, línea 3) — 2026-05-02.
- [ ] Revisar uso de primera persona en el Anexo IDM (0-IDM.tex).
- [x] **NUEVO (2026-05-03) — IDM typo**: "Este ultimo" → "Este último" — 2026-05-04.
- [x] **NUEVO (2026-05-03) — IDM "con con"**: "desconexión con con el curso" → "desconexión con el curso" — 2026-05-04.
- [x] **NUEVO (2026-05-03) — Recursos typo**: "Está sección esta dedicada" → "Esta sección está dedicada" — 2026-05-04.
- [x] **Anexo 1 — typo en título**: corregido "Propmting" → "Prompting" en `\chapter` y `\label`. Punto extra eliminado. Agregada sección del prompt de transcripción con el texto real del YAML.
- [ ] **Anexo 2 — discrepancia de videos**: dice "2835 videos públicos" pero el código registra 4,339 lecciones en 239 cursos. Corregir con datos reales.
- [x] **Anexo 2 — typos de borrador**: "Se realio", "dbido a que", "qe hay en totales", "OpenFig", "Pntalla inicial" (en captions), "sstituciones de una palabra porotra", "transormar" — corregidos 2026-05-04.
- [x] **Anexo 2 — Wikipedia ref URL**: `Word_eror_rate` → `Word_error_rate` — corregido 2026-05-04. (Nota: sigue siendo Wikipedia, no fuente académica.)
- [ ] **Anexo 2 — tabla en inglés**: encabezados "Model / Test Set / Lang" mientras Cap. 6 usa "Modelo / Conjunto de Prueba / Idioma". Unificar en español.
- [ ] **Anexo 2 — oraciones incompletas**: "Los archivos m4a pesan alrededor de" y "Realizar una conversión demora alrededor." — completar con datos reales.
- [x] **Anexo 4 — `//` visible en documento**: convertido a comentario LaTeX (`%`) — 2026-05-03.
- [x] **Anexo 4 — URL de Trello con token**: URL con token eliminada; reemplazada por comentario pendiente de readonly link — 2026-05-03.
