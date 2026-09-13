# Detalles Técnicos Extraídos del Código

Relevados el 2026-04-25 desde `/home/guido/Desktop/fac/2024/proyecto-grado/tesis`.
Usar como fuente de verdad para completar/corregir el documento LaTeX.

---

## Corrección urgente — Cap. 5

El documento describe `uvicorn` como "gestor de paquetes y entornos virtuales para Python escrito en Rust". **Eso es incorrecto** — esa descripción corresponde a `uv`. Son dos herramientas distintas:
- **uv**: gestor de paquetes y entornos virtuales, reemplazo de pip/venv, escrito en Rust
- **uvicorn**: servidor ASGI para Python (ejecuta la API FastAPI)

Ambas están en uso en el proyecto.

---

## Stack tecnológico completo

### Backend
- Python 3.12+
- FastAPI + Uvicorn (servidor ASGI)
- uv (gestor de paquetes, reemplazo de pip/venv, escrito en Rust)
- SQLAlchemy 2.0+ (ORM) + Alembic (migraciones)
- Prefect 3.4.1 (orquestación de workflows del pipeline)
- LangChain (cadenas LCEL: `prompt | llm`)
- Typer (CLI para los servicios)

### Frontend
- React 19.1.0 + TypeScript (modo estricto)
- Vite (bundler)
- pnpm 10.18.2 (gestor de paquetes)
- Tailwind CSS 4.1.11
- Radix UI (componentes accesibles: dialog, dropdown, tooltip, etc.)
- Zustand (estado global)
- TanStack React Query v5 + Axios (fetching)
- `@llm-ui/react` + `@llm-ui/markdown` + `@llm-ui/code` (streaming de respuestas del LLM)
- react-markdown + remark-gfm + shiki (renderizado de markdown con syntax highlighting)
- React Hook Form (formularios)
- Sentry (error tracking)

### Base de datos
- PostgreSQL + pgvector
- Schema `rag`: tablas `courses`, `lessons`, `transcriptions`, `chunks`
- Schema `public`: tablas `conversations`, `messages`, `message_sources`

### Entorno / Despliegue
- Docker + Docker Compose
- VPS con DuckDNS (dominio) + Let's Encrypt (SSL)

---

## Componentes del Backend (`/backend/services/`)

| Componente | Responsabilidad |
|---|---|
| `scraper` | Crawlea OpenFing con BeautifulSoup4 + aiohttp (concurrente) |
| `downloader` | Descarga videos con yt-dlp |
| `transcriber` | Transcribe audio con faster-whisper |
| `generator` | Endpoint RAG + chat (FastAPI) |
| `shared` | Modelos DB, config, vectores, prompts, utilidades comunes |

---

## Transcripción — Whisper

- **Librería**: `faster-whisper` (no el Whisper original de OpenAI)
- **Modelos disponibles**: tiny, base, small, medium, large, turbo
- **Default en `.env.example`**: `WHISPER__MODEL="tiny"`
- **Dispositivo**: CUDA o CPU (autodetect), configurable con `WHISPER__DEVICE`
- **Parámetros clave**:
  - `word_timestamps=True`
  - `vad_filter=True` (Voice Activity Detection — filtra silencio)
  - `task="transcribe"`
  - Prompt inicial de dominio: *"Esta es una clase de la Facultad de Ingeniería de la Universidad de la República (UDELAR), Uruguay"* — incluye terminología de ingeniería, algoritmos, programación, matemática, física, ML, y español rioplatense con términos técnicos en inglés
- **Salida**: texto completo + segmentos con `start`, `end`, `text`, `tokens`, `avg_logprob`, `no_speech_prob`, timestamps por palabra

**Archivo**: `/backend/services/transcriber/core/asr/faster_whisper.py`

---

## Embeddings

Dos modelos configurables:

| Modelo | Dimensiones | Uso |
|---|---|---|
| `sentence-transformers/all-MiniLM-L6-v2` | 384 | Modelo base (default) |
| `intfloat/multilingual-e5-base` | 768 | Alternativa multilingüe |

- Librería: LangChain HuggingFace Embeddings
- Thread-safe con RLock, lazy loading, normalize embeddings habilitado
- Configurable con `EMBEDDINGS__MODEL` y `EMBEDDINGS__DIMENSION`

**Archivo**: `/backend/shared/vectors/embedding/embedder.py`

---

## Chunking

- **Estrategia**: Semantic Chunking (confirmado: los 217.986 chunks en producción usan `chunk_strategy: "semantic"`)
- **Librería**: LangChain HuggingFace (`langchain_huggingface` 0.2.0) con embedder `intfloat/multilingual-e5-base` (normalize_embeddings=True)
- **Parámetros**: `threshold_type: "percentile"`, `semantic_threshold: 0.6`, `min_chunk_size: 400`
- **Estrategia alternativa disponible**: `RecursiveCharacterTextSplitter` (1200 chars, 200 overlap, separadores en español)
- **Metadatos por chunk**: `start_time`, `end_time`, `duration`, `educational_score` (0.0–1.0), `word_count`, `sentence_count`, `timing_accuracy`, `chunk_size`

**Archivos**: `/backend/shared/vectors/chunking/chunker.py`, `semantic.py`, `recursive.py`

### Mecanismo de asignación de timestamps a chunks

El proceso se divide en dos fases ejecutadas en `BaseChunker.chunk()`:

**Fase 1 — Construcción del mapa de posiciones** (`_create_timestamp_mapping()`):
Para cada segmento Whisper (que ya tiene `start` y `end` en segundos), se busca su texto dentro del transcript completo mediante `str.find()`. Si no hay coincidencia exacta, se intenta fuzzy matching (normalización de espacios/puntuación). El resultado es una lista de objetos `TimestampMapping`:
```
{ char_start, char_end, time_start, time_end, segment_ids, confidence_score }
```
Este mapa vincula rangos de caracteres en el texto completo a intervalos de tiempo del video.

**Fase 2 — Cálculo del timestamp de cada chunk** (`_calculate_chunk_timing()`):
Una vez que el splitter genera los chunks, se determina la posición de cada chunk en el texto original (`_find_chunk_position()`) y se calcula su timestamp:

| Caso | Método | `timing_accuracy` |
|---|---|---|
| El rango de caracteres del chunk se solapa con uno o más segmentos | `min(time_start)` y `max(time_end)` de los segmentos solapados | `"precise"` |
| El chunk cae en un hueco entre segmentos | Interpolación lineal proporcional a la posición de caracteres entre los dos segmentos vecinos | `"interpolated"` |
| No hay datos de segmentos disponibles | `None` / `None` | `"no_segments"` |

El resultado es que cada chunk queda anotado con el segundo exacto de inicio y fin dentro del video original, lo que permite al frontend enlazar directamente la respuesta del asistente con el momento preciso de la clase.

---

## Pipeline RAG — Generator

- **Retrieval**: búsqueda por similitud vectorial vía pgvector + LangChain
- **k = 4** chunks recuperados por consulta (default)
- **Filtrado opcional** por `course_ids` o `lessons_ids`
- **Optimización de follow-up**: si hay historial y la query tiene ≤3 palabras → se omite el retrieval (configurable con `NEVER_SKIP_RETRIEVAL`)
- **Formato de contexto**: agrupa fuentes por clase para evitar repetición: *"En la clase '[Curso] - [Subtítulo] - [Título de clase]' se menciona: [contenido]"*
- **Historial de conversación**: máximo 4000 tokens (últimos N mensajes), con `trim_messages(strategy="last")`
- **Cadena LangChain LCEL**: `prompt_template | llm`
- **Respuestas solo en español** (instrucción explícita en el system prompt)

**Archivo**: `/backend/services/generator/core/chat_service.py`

---

## LLM

- **Proveedores soportados**: HuggingFace Inference API, Ollama (local)
- **Modelo principal**: `meta-llama/Meta-Llama-3.1-8B-Instruct`
- **Modelo anterior** (deprecated): `mistralai/Mistral-7B-Instruct-v0.3`
- **Modelo alternativo**: `Qwen/Qwen2.5-72B-Instruct`
- **Parámetros de inferencia**:
  - `max_new_tokens: 2048`
  - `temperature: 0.1`
  - `top_p: 0.9`, `top_k: 10`
  - `typical_p: 0.95`
  - `repetition_penalty: 1.05`

**Archivo**: `/backend/services/generator/core/llm_factory.py`

---

## Dataset — Estadísticas

- **Cursos en OpenFing**: 239
- **Videos (lecciones)**: 4,339
- **Metadatos**: `openfing_content.json` (10,318 líneas), `video_durations.json` (4,339 entradas)
- **Duración promedio de video**: entre ~33 y ~100 minutos

---

## Schema de Base de Datos

### Schema `rag`
- **courses**: `id`, `code` (UNIQUE), `name`, `subtitle`, `course_metadata` (JSONB)
- **lessons**: `id`, `title`, `number`, `video_url`, `lesson_metadata` (JSONB), `course_id` (FK)
- **transcriptions**: `id`, `content` (TEXT), `transcription_metadata` (JSONB), `lesson_id` (FK)
  - Metadata incluye: `transcriber_model_size`, `language`, `duration_seconds`, `segments_count`, `vectorized`
- **chunks**: gestionado por langchain-postgres — `uuid` (determinístico: transcription_id + chunk_index), `embedding` (vector), `metadata` (JSONB), `content` (TEXT)

### Schema `public`
- **conversations**: `id`, `user_id` (FK), `title`
- **messages**: `id`, `conversation_id` (FK), `role` (user/assistant/system), `content`, `message_order`
- **message_sources**: `id`, `message_id` (FK), `chunk_id` (UUID), `confidence_score` (FLOAT), `source_order`

---

## Prompts del sistema

- **Asistente educativo** (`educational_assistant.yaml`): actuar como asistente educativo, integrar contexto de clases naturalmente, responder solo en español
- **Transcripción** (`educational_transcription.yaml`): hint de dominio FING/UdelaR, terminología técnica de ingeniería, español rioplatense + términos técnicos en inglés

**Directorio**: `/backend/shared/prompts/`
