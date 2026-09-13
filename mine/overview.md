# Tesis — Overview

**Proyecto de Grado, FING/UdelaR**
Autores: Diego Amorena y Guido Dinello
Supervisores: Luis Chiruzzo y Libertad Tansini

El documento describe el desarrollo de un **asistente de IA generativa para estudiantes de la FING**, basado en arquitectura RAG (Retrieval-Augmented Generation) sobre el contenido educativo de OpenFing.

---

## Secciones

**Resumen**
Plantea el problema: los LLMs comerciales alucinan y no fueron entrenados con contenido educativo local. Como solución, se desarrolló un chatbot RAG que usa las transcripciones de OpenFing como base de conocimiento, orientado a dar respuestas fiables y contextualizadas al estudiante de la FING.

**Cap. 1 — Introducción**
Motiva el trabajo desde las limitaciones del aprendizaje con video (lento, poco denso). Define objetivos, resultados y estructura del documento. Incluye la sección "Declaración de Uso de Herramientas de IA" (agregada 2026-08 por requisito nuevo del PG), con un `% TODO (Diego)` para el párrafo de Gemini.

**Cap. 2 — Marco Teórico**
Explica OpenFing (5000+ horas de video, pilar del aprendizaje digital en FING) y los conceptos base: IA generativa, LLMs, NLP (subsección agregada). La sección de Segmentos ahora distingue dos estrategias: *Segmentos Semánticos* y *Segmentos Recursivos* (Recursive Character Splitting), con parámetros concretos del proyecto: chunks de 1200 caracteres, overlap de 200, separadores adaptados al español académico, y metadatos de temporalización por chunk. Aún quedan algunos TODOs (Whisper, Prompt/fuentes).

**Cap. 3 — Requisitos** *(antes "Requisitos del Sistema")*
Se divide en dos secciones principales. **Requisitos del Sistema**: no funcionales (código abierto, mantenibilidad, confiabilidad, trazabilidad, extensibilidad hacia OpenUDELAR) y funcionales (chatbot RAG con corpus OpenFING, base de conocimiento dinámica, referencias con timestamp en cada respuesta). **Requisitos del Proyecto**: cuatro RPs que documentan las investigaciones que justifican las decisiones de diseño — (1) Arquitecturas de sistemas (pgvector vs FAISS vs Elasticsearch), (2) Infraestructura (self-hosting vs inference-as-a-service, con análisis de Mistral 7B), (3) Comparación de LLMs, (4) Evaluación de herramientas de transcripción (WER, MER, WIL, WIP, CER + análisis cualitativo).

**Cap. 4 — Arquitectura y Diseño**
Describe la arquitectura en frontend y backend. El backend sigue microservicios con componentes especializados: Scraper (extrae metadatos de OpenFing), Downloader, Transcriber, Generator, Shared. Incluye diagramas UML.

**Cap. 5 — Implementación**
Detalla el stack tecnológico elegido (todo open source). Frontend: React, TypeScript, TailwindCSS, JWT. Entorno: Docker, Uvicorn. Backend: Python + FastAPI. Base de datos: PostgreSQL + PGVector. LLM: Mistral + LangChain. Transcripción: Whisper.

**Cap. 6 — Experimentación**
Evalúa los métodos de transcripción (Whisper) usando WER, MER, WIL, WIP, CER sobre ~5 horas de audio transcriptas manualmente como ground-truth. También cubre experimentos de QA sobre el pipeline RAG.

**Cap. 7 — Trabajo a Futuro**
Plantea integración con la URI y OpenFing para sostenibilidad institucional, actualización automática de contenido, y extensión a otras facultades de UdelaR.

**Cap. 8 — Conclusiones**
Valida que el prototipo es viable y funcional. Concluye que las barreras son metodológicas, no económicas, y que el proyecto tiene potencial transformador para democratizar el acceso a educación en la FING.

**Anexos**
Póster de Ingeniería de Muestra (IDM), técnicas de prompting, estimaciones entregadas para el pasaje de conocimiento, recursos, y planificación y ejecución del proyecto (`5-Planificacion.tex`, agregado 2026-08-31 por el comentario de Libertad p.6). El manual de usuario (`3-Manual_De_Usuario.tex`) está comentado en `main.tex`.

---

## Estado de la ronda de correcciones de tutores (entrega 2026-08-22)

Todos los comentarios aplicados. Ver `mine/comments/checklist-correcciones-tutores.md` (sección "ESTADO FINAL").
Pendiente solo de los autores: validar los % del anexo de planificación y el párrafo de Gemini de Diego.
Los capítulos 7-TrabajoAFuturo.tex y 8-Conclusiones.tex (huérfanos) fueron borrados; el capítulo de
conclusiones y trabajo a futuro es `7-Conclusiones.tex`.

---




