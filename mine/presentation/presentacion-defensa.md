# Presentación — Defensa de Tesis

**Borrador de outline, para iterar.** Estructura sugerida por Libertad (WhatsApp 2026-08-29): problema abordado → proceso seguido → diseño+implementación → pruebas+resultados → conclusiones y trabajos futuros.

Tiempo total: 40-45 min presentación (Luis, WhatsApp). Preguntas del tribunal: 20 min - 1 hora.

**Criterio de asignación de tiempo**: minimizar lo que el tribunal ya leyó en el informe (Marco Teórico general, "qué es RAG"), maximizar lo que solo existe como decisión/evidencia y genera preguntas (los RPs de Cap. 3, los resultados de Cap. 6).

---

## 1. Problema y motivación (~3-4 min) — Cap. 1

**Hook** (comportamiento real de estudiante, no la escala del corpus completo):
> "Cuando repasás para un parcial, no volvés a ver todo el curso: volvés al video puntual de la clase que te generó dudas, o al práctico donde se resolvió un ejercicio parecido al que estás trabajando ahora. El problema es que el video es un formato secuencial, sabés que la respuesta está en algún lugar de esa clase de 40-90 minutos, pero encontrar el momento exacto es lento."

**Segundo punto** (no como aparte, sino como "ya que estamos pensando en soluciones tipo LLM..."):
- Los LLMs comerciales (ChatGPT, etc.) no conocen el contenido específico de los cursos de FING y alucinan cuando se les pregunta por temas puntuales de una clase, con lo cual no resuelven el problema anterior por sí solos.

- Objetivo general: diseñar, implementar y evaluar un asistente conversacional RAG que responda sobre el contenido real de OpenFing, con referencias verificables (timestamp exacto en el video).

Nota: la escala del corpus (5000+ horas, 239 cursos, 4.339 clases) NO va acá — es un dato de alcance/dataset, se usa en la Sección 3 (diseño/implementación), no como parte del hook personal, porque describe todo OpenFing (todas las carreras) y ningún estudiante consume ese total.

**Slide(s)**: 1 título, 1 problema (hook de repaso + práctico), 1 problema (LLM genérico no alcanza), 1 objetivo.

---

## 2. Proceso — decisiones de diseño (~5-6 min) — Cap. 3 (Requisitos del Proyecto)

Esta es la parte que más conviene desarrollar: son decisiones justificadas con investigación propia, no solo "elegimos X".

**DECIDIDO**: se mencionan las 4, pero con énfasis desparejo — las dos que más preguntas generan (infraestructura, LLM) llevan más tiempo/detalle; las otras dos van resumidas.

- **Arquitecturas de sistemas** (resumida, 1 línea): pgvector vs. FAISS vs. Elasticsearch → pgvector, integra con Postgres ya usado, evita infra adicional.
- **Infraestructura** (énfasis): self-hosting vs. inference-as-a-service → análisis de costo/latencia, terminó en HuggingFace Inference API (evolucionó de Mistral 7B a Llama 3.1 8B).
- **Comparación de LLMs** (énfasis): criterios de elección del modelo final (Llama 3.1 8B Instruct sobre Mistral 7B y Qwen2.5-72B).
- **Evaluación de herramientas de transcripción** (resumida, 1 línea): por qué Whisper (faster-whisper) y con qué métricas se lo validó (WER, MER, WIL, WIP, CER) — conecta directo con los resultados de Cap. 6.

**Slide(s)**: 1 slide combinada para las 2 resumidas, 1 slide cada una para las 2 con énfasis (formato "opciones consideradas → criterio → elegido").

---

## 3. Diseño e implementación (~10-12 min) — Caps. 4-5

- **Arquitectura**: diagrama de microservicios (Scraper → Downloader → Transcriber → Generator, + Shared). Un diagrama, no cinco.
- **Flujo de una consulta** (el corazón de la demo): recepción → decisión de recuperación (¿hace falta buscar o es follow-up corto?) → recuperación de chunks (k=4, pgvector) → armado del contexto agrupado por clase → generación (LangChain LCEL, prompt+llm) → respuesta con fuentes y timestamp.
  - Usar 2-3 screenshots reales del flujo, no solo texto.
- **Stack** (una sola slide resumen, no enumerar todo): React/TS + FastAPI/Python + PostgreSQL/pgvector + Llama 3.1 8B vía HuggingFace + faster-whisper. Todo open source.
- **Chunking semántico**: mencionar que el pipeline de producción usa chunking semántico (no solo recursivo por caracteres) con metadata de timestamp por chunk — es lo que permite el link exacto al video.
- **Idempotencia en re-vectorización**: UUID determinístico por chunk (`transcription_id + chunk_index`), lo que permite re-transcribir/re-vectorizar sin duplicar datos (upsert limpio). Precisión de lenguaje para el tribunal: esto es *idempotencia*, no "versionado" (no hay historial de versiones ni rollback).
- **Metadata de procedencia/reproducibilidad** (esto sí conviene mencionar, no está en el informe): cada transcripción y cada chunk guarda el package version + modelo + configuración exacta que lo generó — para transcripciones: versión de `faster-whisper`, tamaño de modelo, `initial_prompt` usado, `vad_filter`/`word_timestamps`; para embeddings: nombre del modelo + versión del package. Esto permite trazar cualquier resultado a exactamente qué lo produjo (relevante para reproducibilidad de la evaluación de Cap. 6, y para distinguir contenido viejo vs. re-procesado con un modelo más nuevo).
- **Dataset resultante**: 239 cursos, 4.339 clases, 217.986 chunks vectorizados (acá va el dato de 5000+ horas del corpus, ver nota en Sección 1).

**Slide(s)**: 1 arquitectura, 2-3 flujo de consulta (con capturas), 1 stack, 1 dataset/escala + procedencia.

---

## 4. Pruebas y resultados (~8-10 min) — Cap. 6

**Nota sobre visuales**: no hace falta cargar esta sección de screenshots nuevos — reusar diagramas/capturas de la Sección 3, y dejar la demostración visual fuerte para la demo en vivo (Sección 6). Acá el foco es números/tablas, no pantallas.

Lo más "objetivo" y lo que más preguntas genera. Ir con números, no adjetivos.

- **Evaluación de transcripción** (ground truth manual, ~5h de audio; Cap. 6 §6.1):
  - Modelos comparados: `base`, `small`, `medium` (WhisperModelLanguage con español explícito).
  - `medium` (elegido para producción): WER promedio **< 0.05** en todos los conjuntos de prueba, menos de 5 errores cada 100 palabras — suficiente para que los fragmentos recuperados sean semánticamente correctos aun con errores menores.
  - `small`: WER entre 2 y 4 veces mayor que `medium`, alternativa más barata pero puede degradar la relevancia de lo indexado.
  - `base`: no adecuado para el dominio (WER 0.203).
  - Detalle de rigor operativo: en las primeras iteraciones, transcribir una sola clase con `small` en CPU tardaba +12 horas; con GPU (infraestructura propia + colaboración UEFI) se logró `medium` en ~5 min/clase — vale mencionarlo, muestra que la elección del modelo no fue solo por calidad sino también viable en tiempo/infraestructura real.
  - CER sistemáticamente menor que WER — errores de nivel léxico/terminológico, no de comprensión general del audio.

- **Evaluación QA del pipeline RAG — foco cualitativo, no solo la métrica** (Cap. 6 §Pregunta-Respuesta): 16 preguntas únicas / 24 consultas (8 sobre corpus completo evaluadas con 2 prompts, 8 sobre corpus restringido a una lección), con Llama 3.1 8B, k=4, historial hasta 4000 tokens. Las respuestas de un LLM son difíciles de reducir a un número (a diferencia de WER), así que el valor real está en lo cualitativo: qué observamos probando el sistema, qué problemas encontramos y cómo los resolvimos.

  **Tres ejemplos concretos ya documentados en el informe, listos para convertir en slides:**

  1. **Respuestas ancladas en el corpus, con fuente + timestamp** (in-domain): la pregunta sobre el resurgimiento de las redes neuronales obtuvo una respuesta precisa y bien fundamentada en los fragmentos recuperados, con referencia explícita a curso/lección/instante del video. Este es el caso "todo funciona como se diseñó" — bueno para abrir la sección.

  2. **El contraste Prompt 1 vs. Prompt 2 — la mejor historia de "encontramos un problema y lo arreglamos"**: con preguntas totalmente fuera de dominio (ej. "receta de la paella valenciana", "planetas habitables en la Vía Láctea"), el sistema con **Prompt 1** recuperó fragmentos vagamente relacionados (una mención incidental a "receta" en una clase de Microprocesadores, las leyes de Kepler en Física) y respondió mezclando eso con conocimiento del modelo entrenado, **sin advertir que la info no estaba en el corpus** — riesgo real de alucinación silenciosa. Al cambiar a **Prompt 2** (instrucción explícita de reconocer cuando el contexto no alcanza), el sistema reconoció correctamente en ambos casos que la consulta no correspondía al dominio de OpenFing. Es el ejemplo más fuerte de iteración real: detectamos el problema, entendimos la causa (falta de instrucción explícita en el prompt), lo corregimos, y verificamos que se corrigió.

  3. **Límite honesto: corpus restringido a una única clase** — incluso con el contexto acotado a una lección específica y la pregunta directamente sobre ese contenido, el modelo extendió respuestas con conocimiento externo de forma inconsistente, especialmente en preguntas técnicas (álgebra lineal, sistemas operativos). Caso de éxito dentro del mismo grupo: la pregunta sobre en qué año empezó el dictado virtual del curso se dedujo correctamente del contexto disponible. Buen ejemplo para mostrar honestidad científica: el sistema no es perfecto, y sabemos exactamente dónde falla.

  - **Reframe de la limitación de tamaño de muestra (16 preguntas / 24 consultas)**: no presentarlo como debilidad a esconder, presentarlo como decisión metodológica explícita (documentada en el propio Cap. 6) — se priorizó profundidad cualitativa por pregunta sobre volumen, y se descartó *LLM-as-a-judge* para acelerar la evaluación porque introduciría su propio riesgo de sesgo/ruido (citado en el informe, \cite{Chen2026Efficient}) que habría requerido validación cruzada humana de todos modos. Si el tribunal pregunta "¿por qué tan pocas preguntas?", esa es la respuesta, no una disculpa.

**Slide(s)**: 1 metodología+métricas de transcripción (WER medium/small/base + nota de tiempo GPU vs CPU), 1 metodología QA (16/24, 4 categorías, 2 prompts), 3 slides cualitativas (una por ejemplo arriba), sin necesidad de screenshots nuevos (reusar diagramas de Sección 3).

---

## 5. Conclusiones y trabajo a futuro (~5 min) — Caps. 7-8

**Gancho de apertura (retoma el throughline de la Sección 4)**: los límites que identificamos (dependencia de la calidad de transcripción, respuestas que a veces exceden el contexto recuperado) no son fallas del proyecto, son el resultado de haberlo evaluado en profundidad — y en al menos un caso (Prompt 1 → Prompt 2) ya los corregimos. Esto se dice en una frase antes de pasar al punto de viabilidad general, no como una sección aparte.

- El prototipo es viable y funcional; las barreras que quedan son metodológicas (curación de contenido, mantenimiento), no económicas (todo el stack es open source / gratuito o de bajo costo).
- Potencial: democratizar acceso a contenido educativo de FING, reduce dependencia del formato video puro.
- Trabajo a futuro: integración institucional con FING/OpenFing para sostenibilidad, actualización automática de contenido, extensión a otras facultades de UdelaR (OpenUDELAR), fine-tuning, búsqueda híbrida, feedback explícito, multimodalidad.

**Slide(s)**: 1 conclusión central, 1 trabajo a futuro (lista corta, 4-5 ítems máximo).

---

## 6. Demo (~5 min, si entra en el tiempo)

**DECIDIDO: demo en vivo**, corriendo localmente en la laptop (el sistema no está deployado en ningún lado accesible actualmente).

- Mostrar: pregunta real sobre un curso conocido → respuesta con fuente y timestamp → click en la fuente → salta al segundo exacto del video.
- Riesgos a mitigar antes del día de la defensa (por ser local, no hay "producción" de respaldo):
  - [ ] Tener el entorno completo levantado y probado el mismo día, no asumir que "andaba la semana pasada" (Docker Compose completo: backend, DB con pgvector, frontend).
  - [ ] Elegir 1-2 preguntas de backup ya probadas y funcionando de antemano (idealmente del mismo set de 16 preguntas de Cap. 6, para que la demo conecte directo con los resultados ya mostrados).
  - [ ] Tener igual una **grabación de respaldo** de la misma demo, por si falla wifi/laptop/lo que sea el día de la defensa — no reemplaza la demo en vivo, es el plan B silencioso.
  - [ ] Wifi de la universidad confirmado, no es un riesgo.
  - [ ] Verificar antes del día: la cuenta de HuggingFace está activa/con crédito disponible, y el modelo configurado en `.env` (Llama 3.1 8B Instruct) sigue disponible vía Inference API (a veces los proveedores rotan/deprecan modelos sin aviso).

---

## Preparación para Q&A (investigación fuera del informe)

No va en las slides, es prep para responder al tribunal si preguntan por qué elegimos este enfoque frente a otras variantes de RAG que existen en la literatura/industria y que el informe no discute explícitamente.

- **Taxonomía de tipos de RAG** (búsqueda "types of rag", ver detalle abajo): Naive/Standard, Conversational, Hybrid, HyDE, Multimodal, Adaptive, Corrective, Graph RAG, Agentic RAG.
- **Nuestro sistema encaja en "Conversational RAG"**: retrieval por similitud vectorial + manejo de historial de conversación (trim_messages, skip de retrieval en follow-ups cortos). No es Naive puro (tiene memoria de conversación) pero tampoco es Hybrid/Graph/Agentic.
- **Respuesta lista si preguntan "¿por qué no Hybrid/Graph/Agentic RAG?"**: alcance de un PG vs. complejidad de un sistema en producción; el informe (Cap. 7, Trabajo a Futuro) ya identifica **búsqueda híbrida** como próximo paso natural, así que no es un punto ciego, es una decisión de alcance explícita y ya documentada.
- Pendiente: revisar si conviene una slide de backup (no en el flujo principal, solo por si preguntan) con esta taxonomía y dónde cae el proyecto.

<details>
<summary>Taxonomía completa (fuente: búsqueda de Google, sin citar en la tesis, solo para prep de Q&A)</summary>

- Foundational: Naive/Standard RAG, Conversational RAG
- Advanced retrieval/processing: Hybrid RAG (dense + sparse/BM25), HyDE, Multimodal RAG
- Autónomas/inteligentes: Adaptive RAG, Corrective RAG, Graph RAG, Agentic RAG

</details>

---

## Pendiente de decidir con Diego

- [ ] Quién presenta qué sección (¿dividir por autor o por tema?).
- [ ] Formato final: Beamer (LaTeX, consistente con la tesis) vs. Google Slides/PowerPoint (más rápido de iterar visualmente).
- [ ] Si la demo va en vivo o grabada.
- [ ] Ensayo con Luis y Libertad (mencionado en el chat, coordinar fecha).
- [ ] Confirmar el volumen real del corpus de 16 preguntas QA — si el tribunal pregunta por qué tan chico, tener la respuesta lista (tiempo/recursos, no descuido).

## Siguiente paso

Con este outline validado, el siguiente paso es armar las slides (contenido concreto por slide, no solo bullets de tema) y después hacer una ronda de QA simulada con vos como si fueras del tribunal.
