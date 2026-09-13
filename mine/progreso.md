# Progreso del Documento

> **NOTA 2026-08-31:** Este archivo quedó desactualizado (data del 2026-06-15). Desde entonces
> se procesaron dos entregas a tutores (jun y ago 2026) y todas sus correcciones. El estado
> vigente de la ronda de correcciones está en `mine/comments/checklist-correcciones-tutores.md`.
> Cambios estructurales posteriores: Cap. 7 y 8 unificados en `7-Conclusiones.tex` (los otros
> dos borrados); nuevo `Nuestro/Anexos/5-Planificacion.tex`; sección de Declaración de IA en Cap. 1.

Estimación al 2026-06-15 (revisión holística completa).

**Overall: ~74% completo** (actualizado 2026-06-15 — REGRESIÓN tabla precios Cap. 6 sigue sin corregir; pendientes: "en en" Cap. 2, em dash Cap. 3, chunking producción Cap. 5, Resumen sin resultados cuantitativos, bib entries de template, Anexo 2 datos incorrectos. Resuelto: filtrado párrafo Cap. 7 en posición correcta; RussellNorvig2020 sin campo volume incorrecto.)

---

## Por capítulo

| Capítulo | Estado | % |
|---|---|---|
| Resumen | Typos corregidos; falta descripción de evaluación/resultados concretos | 85% |
| Cap. 1 — Introducción | Completo: Objetivos, Resultados Esperados, Organización y Conclusiones Resumidas presentes | 90% |
| Cap. 2 — Marco Teórico | "en en" duplicado en l.139 sigue presente (nuevo issue 2026-06-01) | 95% |
| Cap. 3 — Requisitos | Em dash en l.16 (nuevo issue 2026-06-01); pendientes menores | 88% |
| Cap. 4 — Arquitectura | Componentes, BD, Flujo de una Consulta (7 subsecciones + 3 casos con capturas) y diagrama overview (Diagrama A) completos | 96% |
| Cap. 5 — Implementación | Stack completo; falta configuración chunking de producción | 96% |
| Cap. 6 — Experimentación | REGRESIÓN: tabla precios sigue con modelos incorrectos; oración truncada "Los precios de HuggingFace" | 72% |
| Cap. 7 — Trabajo a Futuro | Completo: fine-tuning, búsqueda híbrida, feedback explícito, multimodalidad y testing añadidos; bugs críticos corregidos | 92% |
| Cap. 8 — Conclusiones | Restaurado desde commit perdido 7012e64: typo corregido, WER/LLM/stats presentes, contraste por objetivo y autocrítica incluidos | 92% |
| Anexo IDM | Sin `\todo` visible; primera persona informal; `\label{fig:placeholder}` | 55% |
| Anexo Prompting | Ambos prompts reales incluidos; completo | 95% |
| Anexo Estimaciones | Dato 2835 videos incorrecto (real: 4339); oraciones incompletas; Wikipedia URL con typo; tabla en inglés | 28% |
| Anexo Manual de Usuario | API bien documentada; falta guía de UI | 75% |
| Anexo Recursos | Comentarios corregidos a `%`; Trello comentado; contenido muy escueto | 70% |

---

## Lo más crítico que falta (actualizado 2026-06-15 post-review)

1. **REGRESIÓN Cap. 6** — tabla precios l.262-266: "Claude Opus 4.1", "GPT-5.4 Nano", "GPT-5 Pro", "Gemini 3.5 Flash" siguen incorrectos (confirmado en revisión 2026-06-15)
2. **Anexo Estimaciones** — "2835 videos" incorrecto (real: 4.339); oraciones incompletas l.71-72; tabla en inglés; Wikipedia como fuente
3. **Bib** — entradas de template (CitekeyArticle/Book/Inproceedings/Manual/Misc) siguen presentes; huérfanas (ollama_gemma3_1b_it_qat, zheng2023mtbench, chiang2024chatbotarena); Hallucinations_in_LLMs con journal inválido; inconsistencia "Accessed"/"Accedido"
4. **Cap. 0** — Resumen no menciona resultados de evaluación (WER < 0.05, Llama 3.1 8B, 239 cursos / 4.339 clases / 217.986 chunks)
5. **Cap. 2** — "en en" duplicado en l.139
6. **Cap. 3** — em dash en l.16
7. **Cap. 4 / Cap. 5** — step de vectorización/chunking semántico de producción no documentado
8. **Anexo IDM** — primera persona informal; `\label{fig:placeholder}`
9. **Anexo 1** — solo Tipo 1 prompt documentado; falta Tipo 2
10. **Anexo 3** — falta `\chapter{}` o verificar main.tex; falta guía de UI
11. **Cap. 6 l.284** — gramática "al resto de los precios modelos"
