# TODOs Pendientes

> **Ronda de correcciones de tutores (entrega 2026-08-22):** tracker propio en
> `mine/comments/checklist-correcciones-tutores.md`. Al 2026-08-31 todo aplicado salvo:
> (1) validar los % del nuevo `Nuestro/Anexos/5-Planificacion.tex` — autores;
> (2) párrafo de Gemini en la Declaración de IA de Cap. 1 — Diego.


## Cap. 0 — Resumen
- [x] **Errores gramaticales corregidos en texto**: "en las respuestas" (✓), "Facultad de Ingeniería" (✓), "una herramienta" (✓) — verificado en texto actual 2026-04-26.
- [x] **Typo "pausible"**: corregido a "plausible" — verificado 2026-05-17.
- [x] **Typo "Desde ahora en"**: corregido a "Desde ahora en adelante se denomina" — verificado 2026-05-17.
- [x] **Keywords ampliadas**: `\keywords{RAG, LLM, OpenFing, ASR, Whisper, embeddings, chatbot, educación}` — verificado presente.
- [ ] **Contenido incompleto**: según lineamientos el resumen debe describir la solución Y su evaluación. No menciona WER obtenido (~0.05 con medium), modelo LLM (Llama 3.1 8B), estadísticas corpus (239 cursos, 4339 clases).

## Cap. 1 — Introducción
- [x] **CRÍTICO — contradicción fine-tuning/RAG**: reescrito con descripción correcta de RAG y motivación desde alucinaciones.
- [x] **CRÍTICO — Instrucciones de draft VISIBLES**: eliminadas — verificado 2026-05-17, no existen en el tex actual.
- [x] **Referencia rota**: `\autoref{chapter:4-Arquitura y Diseño}` corregida a `chapter:4-Arquitectura y Diseño`.
- [x] Escribir sección **Objetivos del Proyecto**: objetivo general + 5 específicos redactados.
- [x] Completar sección **Organización del Documento**: reescrita con formato `\textbf{\autoref{}}` y descripción de cada capítulo.
- [x] **CRÍTICO — Sección Conclusiones Resumidas AUSENTE**: creada — 2026-05-17.
- [x] **CRÍTICO — Completar sección Resultados Esperados** (solo contiene `%TODO`): completada con WER, corpus stats, Llama 3.1 8B — 2026-05-17.
- [x] **Em dash en línea 21**: corregido — verificado 2026-05-17, el texto usa coma.

## Cap. 2 — Marco Teórico
- [x] **§ OpenFING — estadísticas sin citar**: suavizado a "miles de horas de video y miles de clases" (sin cifras concretas). Cita innecesaria — la página oficial no publica estadísticas (ver `mine/citation-audits/2026-04-28-openfing-stats/resumen.md`); `\cite{OpenFing}` ya está en la oración anterior del mismo párrafo.
- [x] Corregir sección **2.2.5 Segmentos**: justificación corregida (contexto del LLM + granularidad de recuperación); chunking semántico → Recursive Character Splitting con parámetros reales; texto duplicado eliminado; labels arreglados.
- [x] Corregir estrategia de chunking: reescrita con parámetros reales del código (`chunk_size=1200`, `chunk_overlap=200`, separadores en español académico, metadatos de temporización).
- [ ] Arreglar **problema con las referencias** (afecta todas las referencias del documento)
- [x] **`Hallucination_Abogado` y `Hallucinations_in_LLMs`**: presentes en `referencias.bib` (root) — migradas del bib de capítulos que fue eliminado. Sin problema de compilación.
- [ ] **ALTA — `Prompts_y_estrategia_de_prompts`**: blog de Tiendanube — NO citada en el tex de Cap. 2 (verificado). Entrada huérfana. Eliminar del bib o reemplazar con Brown et al. 2020 (GPT-3) si se va a usar.
- [ ] **ALTA — `Modelos_De_Lenguage`**: blog de `automatizapro.com.ar` — NO citada en el tex (verificado). Entrada huérfana. Eliminar del bib.
- [ ] **ALTA — `Diferencia_LLMS_y_Modelos_De_Lenguaje`**: blog de NextBrain AI — NO citada en el tex (verificado). Entrada huérfana. Eliminar del bib.
- [ ] **MEDIA — `InteligenciaArificialGenerativa`**: duplicado Jurafsky mal renombrado — NO citada en tex (verificado). Huérfana. Eliminar del bib.
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
- [x] **NUEVO (2026-04-28) — ALTO — Segmentos Recursivos: parámetros de implementación en Cap. 2**: eliminados — el tex actual solo describe el enfoque conceptual sin `chunk_size` ni separadores.
- [x] **NUEVO (2026-04-28) — ALTO — Embedding: nombres de modelos en Cap. 2**: eliminados — el tex actual dice "modelo de embedding multilingüe" sin nombrar modelos específicos.
- [x] **NUEVO (2026-04-28) — ALTO — Whisper: detalles de arquitectura interna demasiado técnicos**: simplificado — el tex actual usa la descripción funcional sin espectrograma ni atención cruzada.
- [x] **NUEVO (2026-04-28) — ALTO — Whisper: detalles de entrenamiento demasiado técnicos**: simplificado — el tex actual describe diversidad de datos y capacidades multilingues sin mencionar 680k horas ni supervisión débil.
- [x] **NUEVO (2026-04-28) — MEDIO — RAG: "El presente proyecto implementa Naive RAG"**: no aparece en el tex actual.
- [x] **NUEVO (2026-04-28) — MEDIO — Embedding: "redes siamesas"**: eliminado — SBERT dice "aptas para una comparación eficiente".
- [x] **NUEVO (2026-04-28) — BAJO — Alucinaciones: párrafo de 3 causas sin cita directa**: `\cite{Hallucinations_in_LLMs}` al final del párrafo de causas presente en el tex.
- [x] **NUEVO (2026-04-28) — BAJO — LLMs: "miles de millones de parámetros" sin cita**: `\cite{SpeechandLanguageProcessing}` agregado.
- [x] **NUEVO (2026-04-28) — BAJO — One-Shot Prompting: paráfrasis presentada como cita directa**: reescrito como paráfrasis con cita al final.

## Cap. 2 — Marco Teórico (nuevos issues 2026-06-01)
- [x] **ALTO — "en en" duplicado (l.139)**: corregido a "se basa en la información semántica" — 2026-06-15.

## Cap. 2 — Marco Teórico (nuevos issues 2026-05-31)
- [x] **Palabras duplicadas (l.34)**: "modelos modelos" → "modelos", "se se distinguen" → "se distinguen" — 2026-05-31.
- [x] **Colon como conector (l.60)**: reemplazado con punto — 2026-05-31.
- [x] **Cita flotante FINGChat (l.196)**: `\cite{sastre2024derivation}` integrado al final de la primera oración de la subsección — 2026-05-31.

## Cap. 2 — Marco Teórico (nuevos issues 2026-04-28)
- [x] **Cap. 2, Red Neuronal, línea 47**: reescrito — "Goodfellow et al. \cite{Goodfellow-et-al-2016} presentan una referencia exhaustiva..." con "deep learning" como dos palabras.
- [x] **Cap. 2, Tokenización, línea 57**: `\cite{Jurafsky2023}` reemplazado por `\cite{SpeechandLanguageProcessing}` integrado en la oración.

## Cap. 2 — Marco Teórico (citation audit 2026-04-28)
- [x] **ALTA — `chunks` (blog no académico)**: reemplazado — `gao2023retrieval` y `langchain`.
- [x] **ALTA — `Hallucinations_in_LLMs`**: instancias de RAG → `lewis2020retrieval`; causa → `Hallucinations_in_LLMs`.
- [x] **ALTA — `openTutorAI2025`**: título corregido; texto reescrito con contenido real del abstract.
- [x] **MEDIA — `SpeechandLanguageProcessing` para chunking semántico**: reemplazado por `gao2023retrieval`.
- [x] **BAJA — `RussellNorvig2020` campo `volume`**: eliminado del bib.
- [x] **BAJA — `ASR_Accuaracy` (venue incorrecto)**: renombrado a `ASR_Accuracy` en bib, venue corregido.
- [x] **`ASR_Accuaracy` en tex**: verificado 2026-05-17 — Cap. 3 línea 177 usa `\cite{ASR_Accuracy}` (key correcto). Resuelto.
- [x] **BAJA — `One_Shot_Prompting` (año)**: corregido a 2025 en bib.
- [x] **Cap. 2, `InteligenciaArificialGenerativa`**: entrada eliminada del bib — verificado 2026-05-17.
- [x] **CRÍTICO — `Prompts_y_estrategia_de_prompts` AUSENTE del bib**: entrada `@misc` re-agregada al bib (Tiendanube, 2024) — 2026-05-17. URL requiere verificación.

## Cap. 3 — Requisitos del Sistema
- [x] **Typos REGRESIÓN**: `\item Performance y Escalabilidad` (bullet list) y "nombres propios" — corregidos 2026-05-31.
- [x] **Oración cortada** (línea 99): completa — verificado.
- [x] **RPs en tiempo futuro**: todos los RPs de la sección "Objetivos del Proyecto" pasados a tiempo pasado (Cap. 3) — 2026-05-31.
- [ ] **Diego**: añadir foto de ejemplo para RNF1 (Confiabilidad y Trazabilidad)
- [ ] Encontrar artículo que respalde las estadísticas de uso
- [x] **CRÍTICO — LaTeX roto (l.65)**: `\textit{\textbf{Mistral 7B}}` cerrado correctamente — 2026-05-31.
- [x] **MEDIO — typo "qué si bien" (l.102)**: corregido a "que si bien" — 2026-05-31.
- [x] **BAJO — typo "scrapping" (l.16)**: corregido a "scraping" — 2026-05-31.

## Cap. 3 — Requisitos (nuevos issues 2026-06-01)
- [x] **ALTO — em dash en §3.1.1 (l.16)**: corregido a "generación de respuestas, resulta necesario" — 2026-06-15.

## Cap. 4 — Arquitectura (nuevos issues 2026-06-01)
- [x] **ALTO — step de vectorización/chunking no documentado**: descripción del módulo Shared actualizada para mencionar `shared/vectors` como responsable de fragmentación y vectorización — 2026-06-15.

## Cap. 5 — Implementación (nuevos issues 2026-06-01)
- [x] **MEDIO — configuración chunking producción ausente**: añadida nueva subsección §5-Fragmentación con Semantic Chunking (`multilingual-e5-base`, `threshold_type: "percentile"`, `semantic_threshold: 0.6`, `min_chunk_size: 400`) y alternativa RecursiveCharacterTextSplitter — 2026-06-15.

## Cap. 4 — Arquitectura (nuevos issues 2026-04-28)
- [x] **Cap. 4, posición del diagrama de Backend**: reposicionado al inicio de la subsección "Componentes del Backend" — verificado 2026-05-17.

## Cap. 4 — Arquitectura
- [x] **Frontend incompleto**: completado con descripción de React/TS/Vite/Zustand/TanStack/JWT.
- [x] **Labels incorrectos**: todos los prefijos `5-` corregidos a `4-` (Scrapper, Descargas, Transcriptor, Generator, Shared).
- [x] **Falta justificación de decisión**: agregada subsección "Base de Datos" con justificación de pgvector (cohesión del modelo de datos + inserciones incrementales sin reconstrucción de índice vs FAISS).
- [x] **Generator menciona OpenAI**: corregido — proveedores reales son HuggingFace Inference API y Ollama.
- [x] **Downloader describe descarga de video**: corregido — descarga audio con yt-dlp, reintentos, sin rate limiting ni validación de integridad.
- [x] **Diagramas de arquitectura/flujo** — ambos resueltos.

  **Diagrama A — Overview de componentes (pipeline completo)**: `mine/arquitectura.mermaid` reescrito con datos reales (Llama 3.1 8B, multilingual-e5-base, faster-whisper) y reorganizado en dos filas (Ingesta / Consulta) para evitar el bug de nesting de Mermaid y lograr una proporción imprimible (1568×560px). Exportado con `mmdc` a `Nuestro/Imagenes/Arquitectura/Overview.png`, insertado al inicio de `\section{Arquitectura}` en `4-Arquitectura.tex` (antes de `\section{Frontend}`) como figura introductoria, label `fig:Arquitectura_Overview` — 2026-06-30. Verificado en PDF compilado (Figura 4.1): tamaño legible, `\autoref` y glosario resuelven correctamente — 2026-06-30.

  **Diagrama B — Flujo de una consulta RAG end-to-end**: ya resuelto desde 2026-05-19 (ver entrada en "Reunión tutores 2026-05-17" más abajo) y expandido en profundidad el 2026-06-30 (ver "Sacar jugo en flujo" en "Reunión tutores 2026-06-24").

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

## Cap. 6 — Experimentación (nuevos issues 2026-05-31)
- [x] **CRÍTICO — §6.4.1 oración incompleta (l.218)**: párrafo reescrito eliminando la oración cortada; Context Caching integrado como oración completa — 2026-05-31.
- [x] **CRÍTICO — §6.4.1 referencia rota (l.218-219)**: "en )" corregido a `\autoref{tab:modelos_llm}` — 2026-05-31.
- [x] **FALSA ALARMA — tabla precios §6.4.1**: los nombres Diego usó son correctos según las páginas oficiales de precios verificadas 2026-06-15. Claude Opus 4.1 (deprecated, $15/$75), GPT-5.4 Nano ($0.20/$1.25), GPT-4.1 ($2/$8), GPT-5 Pro ($15/$120), Gemini 3.5 Flash y Gemini 2.5 Pro — todos confirmados. Las "correcciones" previas estaban basadas en conocimiento desactualizado (corte agosto 2025). La tabla NO requiere cambios.
- [x] **CRÍTICO — cita errónea PLN Clase 2 (l.21)**: `OpenFing_Comp1_Clase2_2024` → `OpenFing_PLN_Clase2_2016` — 2026-05-31.

## Cap. 6 — Experimentación (nuevos issues 2026-04-28)
- [x] **"Por que utilizamos faster whisper y whisper cpp."**: renombrado a "Justificación de faster-whisper" con contenido real — verificado 2026-05-17.
- [x] **QA modelos "Mistral y Meta"**: corregido — subsección Modelos usa Llama 3.1 8B + Qwen2.5-72B — verificado 2026-05-17.

## Cap. 6 — Experimentación
- [x] Sección duplicada "MIO Modelos de Transcripción" eliminada.
- [x] **RNF5 — Latencia en producción**: redactada con datos reales de 272 requests (logs VPS ANTEL ago–oct 2025), análisis en dos fases (retrieval+embed vs LLM), distribución bimodal por cold start — 2026-05-31.
- [x] **RNF5 — Comparación self-hosting vs inferencia gestionada**: redactada con requerimientos GPU de Llama 3.1 8B, contexto del VPS sin GPU, ventajas/riesgos del modelo gestionado — 2026-05-31. Citas: `touvron2023llama2`, `jiang2023mistral`.
- [ ] **RNF5 — Costos de inferencia**: §6.4.1 tiene oración truncada al final ("Los precios de HuggingFace" sin completar, l.281-282). La referencia rota "en )" del sprint anterior fue corregida pero esta oración nueva quedó incompleta. Completar con conclusión sobre varianza de precios de HuggingFace vs otros proveedores.
- [x] **Añadir modelo Whisper `large`**: N/A — las transcripciones de Enrique corresponden al modelo medium; "large" no aparece en el capítulo.
- [x] **CRÍTICO — `\section{Modelo de Vectorización}` vacía**: redactada con multilingual-e5-base vs all-MiniLM-L6-v2 — 2026-05-17.
- [x] **CRÍTICO — QA `\subsection{Resultados}` vacía**: redactada con evaluación cualitativa de Llama 3.1 8B y Qwen2.5-72B — 2026-05-17.
- [x] **CRÍTICO — QA `\subsection{Conclusión}` vacía**: redactada con conclusiones y trabajo futuro — 2026-05-17.
- [ ] Presentar **dataset completo**: cantidad de videos, horas, tokens, chunks — separado por curso.
- [x] **Referencia rota**: verificada resuelta 2026-04-28.
- [x] **`\todo` block de Luis visible**: eliminado — verificado 2026-05-17.
- [x] **`\label` antes de `\caption` en tabla**: corregido — verificado 2026-05-17 (caption en línea 71, label en línea 72).
- [x] **Análisis cuantitativo incompleto (Pnl-1 y Pnl-2)**: ahora cubre los 4 conjuntos de prueba — verificado 2026-05-17.

## Cap. 7 — Trabajo a Futuro (nuevos issues 2026-06-01)
- [x] **CRÍTICO — oración corrupta (l.5)**: corregida a "Durante el transcurso del proyecto, el sistema estuvo alojado en la plataforma 'Mi Nube' de Antel como solución provisional" — 2026-06-01.

## Cap. 7 — Trabajo a Futuro
- [ ] Contactar a Clara (URI) para evaluar integración institucional
- [ ] Precisar "requeriría un esfuerzo acotado" con detalles concretos (qué módulos, qué cambios) para evitar percepción de subestimación técnica
- [x] Añadir sección sobre **testing automatizado**: redactada — tests unitarios chunking/embedding/retrieval + regresión pipeline RAG — 2026-06-01.
- [x] **Typo "asumí"**: corregido a "asumir" — verificado 2026-05-17.
- [x] **`\todo` markers visibles**: eliminados — verificado 2026-05-17, no existen en el tex actual.
- [x] **Reordenar párrafo de filtrado por facultad**: verificado 2026-06-15 — en el tex actual el párrafo de filtrado por facultad aparece inmediatamente después del párrafo de expansión a otras facultades, en colocación lógica. Resuelto.
- [x] **Nueva sección — Multimodalidad**: redactada — diapositivas/pizarra no capturadas en transcripciones, modelos de visión y lenguaje como extensión — 2026-06-01.
- [x] **Nueva sección — Búsqueda híbrida (sparse + dense)**: redactada — recuperación densa + BM25, fortalezas complementarias — 2026-06-01.
- [x] **Nueva sección — Feedback explícito del usuario**: redactada — valoraciones de calidad, datos etiquetados para monitoreo y fine-tuning — 2026-06-01.
- [x] **Nueva sección — Fine-tuning del modelo**: redactada con LoRA/QLoRA, Llama 3.1 8B, datos de interacciones etiquetadas. Citas `hu2022lora` y `dettmers2023qlora` añadidas al bib — 2026-06-01.
- [x] **MEDIO — sintaxis Markdown en `*Re-Ranking*` REGRESIÓN**: reemplazado con `\textit{Re-Ranking}` en ambas instancias — 2026-06-01.

## Cap. 8 — Conclusiones
- [x] **Typo "quel el" REGRESIÓN**: corregido restaurando commit perdido 7012e64 — 2026-05-31.
- [x] **Resultados concretos REGRESIÓN**: WER, Llama 3.1 8B, 239 cursos/4.339 clases restaurados desde commit perdido 7012e64 — 2026-05-31.
- [x] **Contraste planificado vs realizado REGRESIÓN**: sección con evaluación por objetivo y autocrítica restaurada desde commit perdido 7012e64 — 2026-05-31.

## Reunión tutores 2026-05-17 — Action items

### main.tex / Documento general
- [x] **CRÍTICO — Restaurar tabla de contenidos (índice)**: `\tableofcontents` restaurado en `main.tex` — 2026-05-17.

### Cap. 3 — Requisitos (feedback tutores)
- [x] **Invertir orden RF / RNF**: poner Requisitos Funcionales antes de Requisitos No Funcionales en Cap. 3 — 2026-05-19.
- [x] **RNFs más concretos y orientados al usuario**: reescritos con criterios observables/verificables (acceso público al repo, trazabilidad con clase/lección/minuto, confiabilidad con aviso explícito, extensibilidad como esfuerzo de integración mínimo) — 2026-05-26.
- [x] **Mencionar otros tipos de usuario**: agregado párrafo del usuario administrador/operador al final de Requisitos Funcionales (pipeline de sync, visibilidad de estado via Prefect, corrección de fallas) — 2026-05-26.
- [x] **Renombrar "Requisitos del Proyecto" → "Objetivos del Proyecto"**: renombrado y movido al inicio del capítulo (antes de RF/RNF), acordado con Diego — 2026-05-26.

### Cap. 4 — Arquitectura y Diseño (feedback tutores)
- [x] **Añadir subsección del flujo principal (RAG end-to-end)**: subsección "Flujo de una Consulta" añadida al final de `\section{Arquitectura}` en Cap. 4 — 2026-05-19. Diagrama Mermaid en `mine/flujo-consulta.mermaid`. Exportar a `Nuestro/Imagenes/Arquitectura/FlujoPipeline.png` con `mmdc` o mermaid.live.

### Cap. 5 — Implementación (feedback tutores)
- [x] **Mencionar alternativas de Whisper**: sección Herramienta Audio a Texto en Cap. 5 consolidada (duplicado eliminado); whisper.cpp y faster-whisper presentados como los dos candidatos evaluados con descripción de cada uno; configuración en \paragraph{} con \begin{itemize} — 2026-05-26.

### Cap. 6 — Experimentación (feedback tutores)
- [x] **Mencionar deploy en Mi Nube Antel**: añadida sección `\section{Despliegue y Validación Operacional}` en Cap. 6 — 2026-05-17.
- [x] **Armar estructura de secciones vacías aunque sea con contenido provisional**: Modelo de Vectorización, QA Resultados, QA Conclusión ya tienen contenido completo — 2026-05-17. Sección "Análisis de Infraestructura" (RNF5) añadida con esqueleto de 3 subsecciones (Costos, Latencia, Self-hosting) — 2026-05-19.

### Transversal (feedback tutores)
- [x] **Verificar "Ilustración propia." en todas las figuras**: revisados todos los `\caption{}`. Cap. 4 (UML frontend/backend) y Cap. 5 (JWT) ya tenían "Ilustración propia." Añadido en Anexo IDM (poster). Corregido typo "Ilustracción" → "Ilustración" en Cap. 2. Las capturas de pantalla de OpenFing en Anexo 2 no aplican. — 2026-05-19.

## Transversal — Todo el documento
- [x] **"En está sección"** → verificado en Cap. 2: todas las instancias actuales leen "En esta sección" correctamente. Hacer búsqueda global antes de entrega para cubrir otros capítulos.
- [x] **Em dashes en Cap. 2 línea 89**: verificado — texto actual usa comas ("saltos de párrafo, saltos de línea"). Resuelto.
- [x] **Em dash en Cap. 1**: verificado — texto actual usa "la alucinación, generando afirmaciones" (coma). Resuelto.

## Cap. 4 — Arquitectura (nuevos issues 2026-05-31)
- [ ] **BAJA — inconsistencia jerárquica**: `\subsection{Scrapper}` debería ser `\subsubsection{}` dentro de "Componentes del Backend" para ser consistente con el nivel de Módulo de Descargas, Transcriptor, etc.

## referencias.bib
- [x] **Entradas duplicadas CitekeyXXX resueltas**: solo quedan `CitekeyArticle/Book/Misc` como ejemplos del template — no causan error pero son ruido.
- [x] **`vite` — autor corregido**: "VoidZero Inc. and Vite contributors".
- [x] **`React_JS_Coderhouse`**: verificado 2026-05-17 — entrada ya NO existe en el bib. Resuelta.
- [x] **Entrada `ibm`**: ya no existe. Resuelta.
- [x] **`Modelos_De_Lenguage`, `Diferencia_LLMS_y_Modelos_De_Lenguaje`, `InteligenciaArificialGenerativa`**: verificadas eliminadas del bib — 2026-05-17.
- [x] **CRÍTICO — `Prompts_y_estrategia_de_prompts`**: entrada re-agregada al bib (Tiendanube, 2024). Verificado presente en referencias.bib.
- [x] **MEDIO — entradas de ejemplo del template**: CitekeyArticle, etc. — NO APLICA: BibTeX solo incluye en el PDF entradas citadas con \cite{}. Las entradas sin citar son invisibles en la entrega. No requieren limpieza.
- [x] **BAJO — entradas huérfanas**: `ollama_gemma3_1b_it_qat`, `zheng2023mtbench`, `chiang2024chatbotarena` — NO APLICA: mismo motivo, no aparecen en el PDF si no están citadas.
- [x] **MEDIO — inconsistencia "Accessed"/"Accedido"**: unificado a "Accedido: AAAA-MM-DD" en todas las entradas del bib — 2026-06-15.
- [ ] **MEDIO — `Hallucinations_in_LLMs`**: `journal = {ResearchGate preprint}` no es nombre de journal válido — cambiar a `howpublished` con URL o encontrar publicación formal.
- [x] **`workshopOpenFing`**: tiene `note = "Accessed: 2026-05-03"` — cumple requisito INCO. Resuelto.
- [x] **`RussellNorvig2020`**: campo `volume` ya no está presente en el bib — verificado 2026-06-15. Resuelto.

## Anexos

### Nuevos issues 2026-06-15
- [ ] **MEDIO — Anexo 1: solo Tipo 1 prompt documentado**: el Anexo solo incluye el prompt Tipo 1 (que combina contexto con conocimiento general). El prompt Tipo 2 (que instruye al modelo a reconocer cuándo el contexto es insuficiente) fue evaluado en §6-QA y produjo mejores resultados. Documentar ambas variantes o aclarar cuál es el prompt de producción.
- [ ] **MEDIO — Anexo 3: falta declaración `\chapter{}`**: el archivo comienza con `\section{Introducción}` pero tiene `\label{chapter:A-3-Manual de Usuario}` sin `\chapter{}` previo. Verificar si se declara en main.tex; si no, añadir `\chapter{Anexo III-Manual de Usuario}` al inicio.
- [ ] **MEDIO — Anexo 3: falta guía de UI**: el manual solo documenta la API REST. Añadir descripción de cómo usar la interfaz web (chatbot UI) para el usuario final no técnico.
- [x] **BAJO — Cap. 6 l.284: gramática awkward**: corregido a "a los precios del resto de los modelos" — 2026-06-15.
- [x] **BAJO — Cap. 3 l.160: gramática awkward**: corregido a "se llevaron a cabo reuniones con la" — 2026-06-15.

- [x] **Anexo IDM — primera persona**: reescrito en impersonal/tercera persona; también corregidos typos de tildes y gramática ("específico", "imposibilitó", "sería"); label `fig:placeholder` → `fig:IDM-poster` — 2026-06-15.
- [ ] **Anexo IDM — `\label{fig:placeholder}`**: renombrar a algo descriptivo como `fig:IDM-poster`.
- [x] **Anexo 1 — typo en título**: corregido "Propmting" → "Prompting". Prompts reales incluidos. Completo.
- [ ] **Anexo 2 — discrepancia de videos**: dice "2835 videos públicos" pero el código registra 4.339 lecciones en 239 cursos. Corregir con datos reales. *(2026-08-31: verificado que NINGÚN tutor comentó este número; queda fuera del alcance de la ronda de correcciones de ago 2026. Sigue pendiente como mejora interna.)*
- [ ] **Anexo 2 — Wikipedia ref**: usa `\cite{WORD_ERROR_RATE}` apuntando a `es.wikipedia.org/wiki/Word_Error_Rate` — no es fuente académica válida. Reemplazar con `\cite{ASR_Accuracy}` o `\cite{itoh2015metric}`.
- [ ] **Anexo 2 — tabla en inglés**: encabezados "Model / Test Set / Lang" → traducir a español.
- [x] **Anexo 2 — oraciones incompletas**: eliminadas las dos oraciones truncadas ("Los archivos m4a pesan alrededor de" y "Realizar una conversión demora alrededor.") — 2026-06-15. La oración de contexto siguiente ("Estas transcripciones pueden ser eliminadas...") se preservó.
- [x] **Anexo 4 — `//` visible**: corregido a `%` — verificado 2026-05-17.
- [x] **Anexo 4 — URL Trello con token**: Trello URL comentada con `%` — verificado 2026-05-17.

## Reunión tutores 2026-06-24 — Pendientes (cross-check 2026-06-30)

### Bugs críticos en el diff actual (rompen el PDF)
- [ ] **CRÍTICO — oración truncada en Cap. 6**: "Si bien ya no se cuentan con datos formales del tiempo demorado a partir de cada uno de los modelos, en las primeras ite" — completar o eliminar.
- [ ] **CRÍTICO — typo fusión en Cap. 1**: "disponible en OpenFingi peline implementado" → "disponible en OpenFing. El pipeline implementado".
- [ ] **CRÍTICO — texto duplicado en items de Cap. 6**: cada item de la lista de clases repite el nombre dos veces (una sin footnote y una con), e.g., "Computación 1, Clase 1 - Teórico 2024. Computación 1, Clase 1 - Teoría 2024 \footnote{...}" — eliminar la primera instancia.
- [ ] **ALTO — títulos de librerías expuestos en cuerpo del texto (Cap. 4 y 5)**: la conversión de `\cite{}` a `\footnote{}` dejó el título del recurso escrito como texto plano antes del `\footnote{}`, e.g., "Zustand: A small, fast and scalable bearbones state-management solution \footnote{\url{...}}" — el título debe eliminarse del cuerpo o integrarse de otra forma.

### Contenido pendiente de las notas de reunión
- [x] **Sacar jugo en flujo (todo lo que pasa en el backend, 3-4 screenshots, varios casos)**: `\section{Flujo de una Consulta}` en Cap. 4 reestructurada en 7 subsecciones (Recepción y sesión, Decisión de recuperación, Recuperación y contexto, Construcción del prompt, Generación y errores, Persistencia y trazabilidad, Recorrido por casos representativos). Se documentaron reglas de negocio no cubiertas antes: rama autenticado (PostgreSQL) vs anónimo (caché en memoria, TTL 1h), toggle `NEVER_SKIP_RETRIEVAL`, truncamiento de historial en dos capas, guardrails de input y ownership de conversación, degradación ante errores del LLM. Se agregaron 3 capturas reales con casos trazados (consulta normal autenticada, follow-up que omite retrieval, consulta fuera de dominio con la pregunta de la paella valenciana ya usada en Cap. 6) — 2026-06-30. Nueva cita `openai_prompt_guide` agregada a `referencias.bib` para la afirmación sobre ubicación del contexto en el turno humano. Pendiente aparte: Diagrama A (overview estático de componentes, línea 116 de este archivo) sigue sin implementar.
- [ ] **Buenos Aires — representación en tokens**: agregar sección/párrafo sobre cómo se representan los nombres propios de Buenos Aires en tokens (tarea de Diego).
- [ ] **Mejorar explicación del descarte de Qwen**: la justificación actual solo dice "mayor capacidad" — desarrollar con argumento de costo y/o latencia.
- [ ] **Costo como argumento de elección del modelo final (Llama)**: agregar explícitamente en Cap. 5 o Cap. 6 por qué se eligió Llama en términos de costo de inferencia.
- [ ] **Referencia vacía `[??]` en §6.3.3**: identificar y corregir la cita rota.
- [ ] **Cap. 1 — Resultados Esperados → Aportes**: renombrar sección y reformatear como entregables concretos (nota de Luis).
- [ ] **Cap. 6 — Explicar Tipo 1 y Tipo 2 de prompts**: describir las dos variantes del system prompt y sus diferencias observadas.
- [ ] **Cap. 6 — Estimativos de tiempo de transcripción**: completar la oración truncada con datos reales (o aproximados) del tiempo por modelo.
- [ ] **Cap. 0 — Reescribir Resumen**: el contenido actual es motivación, no resumen. Reescribir como descripción del proyecto, arquitectura, experimentos y resultados (ver comentario agregado en el .tex).
- [ ] **Unificar Cap. 7 y Cap. 8**: fusionar en un solo capítulo con dos subsecciones — primero Conclusiones y luego Trabajo a Futuro.
- [ ] **Rótulo "Ingeniería de Muestra" → "Experimentación"** en el nombre del Anexo A (o adecuarlo al contenido real).
- [ ] **Borrar Anexo A / arreglar que todo el contenido quedó adentro del Anexo A**: revisar estructura de anexos en main.tex.
