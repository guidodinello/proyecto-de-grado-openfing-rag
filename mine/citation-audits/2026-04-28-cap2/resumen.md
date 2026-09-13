# Auditoría de Citas — Cap. 2 Marco Teórico
Fecha: 2026-04-28

Total de claves únicas auditadas: 19 (≈35 instancias en texto)
✅ VALID:     14
⚠️  DUBIOUS:  5
❌ NOT_FOUND: 0

---

## Tabla de resultados

| Clave                    | Afirmación (extracto)                                   | Veredicto    |
|--------------------------|---------------------------------------------------------|--------------|
| `OpenFing`               | "plataforma de videos educativos de la FING..."         | ✅ VALID      |
| `RussellNorvig2020`      | "dos ejes en definiciones tradicionales de IA"          | ✅ VALID *    |
| `Goodfellow-et-al-2016`  | modelo generativo aprende distribución estadística      | ✅ VALID      |
| `Goodfellow-et-al-2016`  | deep learning aprende sin ingeniería manual             | ✅ VALID      |
| `Goodfellow-et-al-2016`  | referencia exhaustiva sobre redes neuronales            | ✅ VALID      |
| `Zhao2023LLMSurvey`      | LLMs aprenden estructuras del lenguaje                  | ✅ VALID      |
| `Zhao2023LLMSurvey`      | LLMs más complejos que modelos anteriores               | ✅ VALID      |
| `Zhao2023LLMSurvey`      | LLMs modelan relaciones semánticas complejas            | ✅ VALID      |
| `SpeechandLanguageProcessing` | definición de PLN (morfológico→pragmático)         | ✅ VALID      |
| `SpeechandLanguageProcessing` | tareas clásicas de NLP (1950–1960)                 | ✅ VALID      |
| `SpeechandLanguageProcessing` | variantes Transformer (encoder/decoder) + LLMs     | ✅ VALID      |
| `SpeechandLanguageProcessing` | tokenización: proceso de dividir texto en tokens   | ✅ VALID      |
| `SpeechandLanguageProcessing` | definición de modelo de lenguaje                   | ✅ VALID      |
| `SpeechandLanguageProcessing` | LLMs con millones/miles de millones de parámetros  | ✅ VALID      |
| `SpeechandLanguageProcessing` | chunking semántico: capturar idea completa por chunk | ⚠️ DUBIOUS  |
| `SpeechandLanguageProcessing` | definición de embedding vectorial denso            | ✅ VALID      |
| `vaswani2017attention`   | arquitectura Transformer introducida por Vaswani        | ✅ VALID      |
| `vaswani2017attention`   | embeddings basados en Transformer                       | ✅ VALID      |
| `vaswani2017attention`   | Whisper basado en arquitectura Transformer              | ✅ VALID      |
| `chunks`                 | ventana de contexto + granularidad de recuperación      | ⚠️ DUBIOUS   |
| `chunks`                 | Recursive Character Splitting con separadores           | ⚠️ DUBIOUS   |
| `Brown2020GPT3`          | definición de Few-Shot Prompting                        | ✅ VALID      |
| `One_Shot_Prompting`     | One-Shot generaliza desde un único ejemplo              | ⚠️ DUBIOUS   |
| `reimers2019sbert`       | SBERT produce embeddings de oraciones eficientes        | ✅ VALID      |
| `karpukhin2020dense`     | DPR supera métodos dispersos en búsqueda abierta        | ✅ VALID      |
| `Hallucinations_in_LLMs` | causas de alucinaciones en LLMs                         | ⚠️ DUBIOUS   |
| `Hallucinations_in_LLMs` | RAG ancla respuestas en fuentes verificables            | ⚠️ DUBIOUS   |
| `Hallucinations_in_LLMs` | RAG en contexto de motivación anti-alucinaciones        | ⚠️ DUBIOUS   |
| `Hallucination_Abogado`  | caso Varghese v. China Southern Airlines                | ✅ VALID      |
| `lewis2020retrieval`     | RAG como estrategia efectiva vs alucinaciones           | ✅ VALID      |
| `lewis2020retrieval`     | RAG genera a partir de información verificable          | ✅ VALID      |
| `gao2023retrieval`       | paradigmas Naive / Advanced / Modular RAG               | ✅ VALID      |
| `ASR_Accuaracy`          | definición de WER (sustituciones + inserciones + del.)  | ⚠️ DUBIOUS   |
| `radford2022robust`      | Whisper extremo-a-extremo sin alineación fonética       | ✅ VALID      |
| `radford2022robust`      | Whisper multilingüe desde audio web                     | ✅ VALID      |
| `radford2022robust`      | Whisper sin ajuste fino, varía por idioma               | ✅ VALID      |
| `faster_whisper`         | reimplementación con CTranslate2, VAD, timestamps       | ✅ VALID      |
| `openTutorAI2025`        | plataforma abierta de tutoría con IA                    | ✅ VALID      |
| `openTutorAI2025`        | incorpora motor RAG para anclar respuestas en materiales | ⚠️ DUBIOUS  |

\* `RussellNorvig2020`: el campo `volume` en el .bib contiene "Introduction, What is AI?" — uso incorrecto del campo volume.

---

## Issues de bib detectados (no son sobre la existencia de la fuente)

| Clave | Problema en el .bib |
|-------|---------------------|
| `RussellNorvig2020` | `volume` = "Introduction, What is AI?" — campo incorrecto |
| `One_Shot_Prompting` | `year = 2024` — artículo de IBM publicado en 2025 |
| `ASR_Accuaracy` | `journal` = "iJET" incorrecto — el paper está en AIP Conference Proceedings (vol. 3063, 2024); typo en key ("Accuaracy") |
| `openTutorAI2025` | `title` incorrecto: el título real es "Open TutorAI: An Open-source Platform for Personalized and Immersive Learning with Generative AI" |
| `Hallucinations_in_LLMs` | `journal = "ResearchGate preprint"` no es un journal real; autores "Pete Jano Meade Cleti" parecen ser dos personas distintas separadas |

---

Artefactos individuales: ver archivos `{key}.md` en este mismo directorio.
