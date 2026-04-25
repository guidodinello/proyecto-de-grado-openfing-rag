# Tesis — Overview

**Proyecto de Grado, FING/UdelaR**
Autores: Diego Amorena y Guido Dinello
Supervisores: Luis Chiruzzo y Libertad Tansinni

El documento describe el desarrollo de un **asistente de IA generativa para estudiantes de la FING**, basado en arquitectura RAG (Retrieval-Augmented Generation) sobre el contenido educativo de OpenFing.

---

## Secciones

**Resumen**
Plantea el problema: los LLMs comerciales alucinan y no fueron entrenados con contenido educativo local. Como solución, se desarrolló un chatbot RAG que usa las transcripciones de OpenFing como base de conocimiento, orientado a dar respuestas fiables y contextualizadas al estudiante de la FING.

**Cap. 1 — Introducción**
Motiva el trabajo desde las limitaciones del aprendizaje con video (lento, poco denso). Define objetivos, resultados y estructura del documento. Algunas secciones aún están incompletas (Objetivos y Resultados están en blanco).

**Cap. 2 — Marco Teórico**
Explica OpenFing (5000+ horas de video, pilar del aprendizaje digital en FING) y los conceptos base: IA generativa, LLMs, NLP. Varias subsecciones tienen TODOs pendientes.

**Cap. 3 — Requisitos del Sistema**
Define requisitos funcionales y no funcionales. Los no funcionales enfatizan **código abierto, mantenibilidad, confiabilidad y trazabilidad**. Los funcionales centran en el chatbot RAG con referencias explícitas a las clases fuente.

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

**Anexos (0–4)**
Ingeniería de Muestra (IDM), técnicas de prompting, estimaciones para OpenFing, manual de usuario, y recursos.

---




