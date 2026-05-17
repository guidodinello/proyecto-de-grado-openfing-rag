# Progreso del Documento

Estimación al 2026-05-03 (post `/thesis-review` holístico — ajustada a estado real observado).

**Overall: ~68% completo**

---

## Por capítulo

| Capítulo | Estado | % |
|---|---|---|
| Resumen | Typos corregidos; falta WER obtenido, modelo LLM, stats corpus y resultados de evaluación | 80% |
| Cap. 1 — Introducción | Resultados Obtenidos y Conclusiones Resumidas vacíos | 60% |
| Cap. 2 — Marco Teórico | Contenido completo; typos y cita flotante corregidos | 95% |
| Cap. 3 — Requisitos | RFs y RNFs con prosa limpia; RPs en tiempo pasado; oración incompleta corregida | 80% |
| Cap. 4 — Arquitectura | Componentes y BD correctos; falta mención de Prefect; diagramas pipeline/RAG ausentes | 80% |
| Cap. 5 — Implementación | **COMPLETO**. Stack íntegro con citas. | **100%** |
| Cap. 6 — Experimentación | Transcripción completa; QA resultados/Conclusión/Vectorización vacíos | 48% |
| Cap. 7 — Trabajo a Futuro | \todo eliminados; \autoref integrado; capitalización corregida; falta sección testing | 75% |
| Cap. 8 — Conclusiones | Completo: WER, LLM, dataset stats, contraste vs objetivos, autocrítica | 92% |
| Anexo IDM | Primera persona; typos corregidos; tono informal | 55% |
| Anexo Prompting | Ambos prompts reales incluidos; completo | 95% |
| Anexo Estimaciones | Dato 2835 incorrecto (real: 4339); 12+ typos de borrador; oraciones incompletas; tabla en inglés; chunk size desactualizado | 28% |
| Anexo Manual de Usuario | API bien documentada; falta guía de UI | 75% |
| Anexo Recursos | Typo corregido; Trello placeholder sin URL; contenido muy escaso | 42% |

---

## Lo más crítico que falta (actualizado 2026-05-03, post thesis-review)

1. **Cap. 6** — QA completamente vacía (experimento central): Resultados y Conclusión de QA + Modelo de Vectorización
2. **Cap. 1** — Resultados Obtenidos vacía (requerida por lineamientos INCO) — pendiente datos finales
3. **Cap. 1** — `Conclusiones Resumidas` vacía (completar cuando estén resultados finales)
4. **Cap. 3** — 4 RPs en tiempo futuro (cambiar a pasado) + oración incompleta línea 108
5. **Cap. 0** — Resumen no menciona WER obtenido, LLM, ni estadísticas del corpus (incumple lineamientos)
6. **Anexo Estimaciones** — dato 2835 incorrecto (real: 4339 lecciones) + 12+ typos de borrador + oraciones incompletas
7. **Cap. 7** — falta sección de testing automatizado; \autoref flotante sin oración
8. **Cap. 2** — 3 typos nuevos + cita flotante (correcciones menores pero necesarias)
