# Timeline reconstruido del proyecto (para el anexo de Planificación — T p.6)

Fuente: historiales git de los 4 repos de código + mtimes del POC sin versionar + Cronograma Tentativo.

## Repos de código (en orden cronológico)

| Repo | Ruta | Rango | Qué fue |
|---|---|---|---|
| ProyectoDeGrado | `../ProyectoDeGrado/` | ago 2024 – oct 2024 (31 commits) | Exploración inicial de Diego. Scraping de OpenFing, descarga de videos, transcripción con Whisper (tiny/base/small/medium), script para cluster con GPU, primeras métricas WER con transcripciones manuales como ground truth (metn-2023, comp1-2024, pln). Commit "roadmap" el 16/8/2024. |
| repo-proygrado | `../repo-proygrado/` | nov 2024 – dic 2024 (2 commits) | Stub en GitHub. Solo gitignore/license + "tmp commit to another pc". Intento de migración. |
| download_and_transcript | `../download_and_transcript/` | feb 2025 + may 2025 (sin versionar, por mtime) | POC. feb 2025: `transcribe.py`, `get_txt_from_json.py`, transcripciones medium/tiny de 5 cursos, txts "custom" (manuales). may 2025: sub-proyecto `openfing-audio-dl/` (CLI de descarga con Prefect, pyproject propio). |
| tesis | `../tesis/` | jul 2025 – may 2026 (50 commits) | El sistema final. GitLab de FIng. |

## Actividad en `tesis/` por mes

- **jul 2025** (8): frontend routes, docker build args, backend container network, OAuth2 password bearer, middlewares, filtrados frontend, "contenido total en horas de openfing".
- **ago 2025** (10): filtrado frontend, memory to chat, register dialog, skip transcripciones sin segmentos, api route rewriting.
- **sep 2025** (21, pico): docker logs, mover prompts a archivos, soporte modelos locales con Ollama, markdown/codeblocks rendering, `NEVER_SKIP_RETRIEVAL`, deploy files, organización de deps, anonymous chat.
- **oct 2025** (6): preload del modelo de embeddings al startup, tree-shake icons, JWT auth con cookies, integración Sentry, endpoint admin de listado de usuarios.
- **nov 2025** (1): ajuste de Sentry. — luego pausa —
- **abr 2026** (2): `.env.example`, tweaks de system prompt.
- **may 2026** (2): fix de sources (start/end time), **fix del scraper por rediseño del sitio de OpenFing**.

## Repo del informe

- `Proyecto_de_Grado_INCO...`: primer commit **may 2026**. Redacción intensiva may–ago 2026. Primera entrega a tutores **22/8/2026**. Correcciones **1/9/2026**. Defensa **17/9/2026**.

## Plan (Cronograma Tentativo)

- Creado **7/7/2025**, última modificación **5/10/2025**. O sea: escrito a mitad de proyecto, planifica la fase de construcción final.
- Dice: 8 meses (mar–oct 2025), 15 h/sem por estudiante (estimadas, sin registro).
- Hito: "Evaluación del 4º mes" ubicada en junio 2025.

## Comparación plan vs. real

| | Plan | Real |
|---|---|---|
| Duración | 8 meses (mar–oct 2025) | ~25 meses (ago 2024 – sep 2026), con fase intensiva jul–oct 2025 |
| Fase exploratoria | (no contemplada) | ago 2024 – jun 2025, intermitente, 3 repos / POCs |
| Construcción del sistema | mar–oct 2025 | jul–oct 2025 (comprimida en 4 meses) |
| Experimentación + informe | sep–oct 2025 | may–ago 2026 |
| Pausa | — | nov 2025 – mar 2026 |

## Preguntas abiertas para los autores

1. Fase ago 2024 – jun 2025: ¿cómo describirla? ¿Exploración / definición de alcance / cambios de enfoque? ¿Hubo pausa por cursos y exámenes?
2. Pausa nov 2025 – mar 2026: motivo (redacción, otros compromisos, exámenes).
3. ¿Cuándo fue efectivamente la evaluación intermedia / del 4º mes con los tutores?
4. % de dedicación por tarea-macro: confirmar la tabla propuesta.
