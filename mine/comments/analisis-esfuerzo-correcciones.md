# Análisis de esfuerzo — correcciones de tutores

Complemento de `checklist-correcciones-tutores.md`. Estima qué tan complejo es corregir cada comentario.

## Resumen

- **Total de comentarios con texto: 69** (Luis 38, Libertad 31).
- 4 subrayados sin nota adicionales (Luis p.79; Libertad p.16, p.40, p.71).
- Si se agrupan los repetidos literales: ~30 acciones distintas de Luis, ~24 de Libertad.
- **~85% es trabajo mecánico** (una tarde). El peso real está en 3–4 ítems de contenido.
- Nada es técnicamente difícil: no hay que rehacer experimentos ni tocar código del sistema.

---

## Mecánicos triviales (~45) — minutos cada uno

- Typos y concordancia: Luis p.38 "señalizan"→"indican" y "cercano"→"cercana", p.68 "posee"→"poseen", p.83 "son", p.84 "muestra", p.85 "desarrollando", p.82 varios.
- Puntuación / espacios: Luis p.40 "UEFI(", p.40 "tanto,se", p.74 "tabla,(", p.78 espacio antes de paréntesis, comillas `` ``...'' `` en p.48.
- Mover un `\cite`: Luis p.38 (Morris2004), p.22 (borrar "Vaswani et al." redundante).
- Agregar `\autoref` a un anexo existente: Luis p.46 (B.2), p.49 (B.1), p.99 (Estimaciones).
- Cambios de palabra sugeridos: Libertad "riesgos" por "falencias", "pesos en funciones matemáticas", "de tipo RAG", "mitigando".
- Renombrar `\chapter{}`: Luis p.93 (título del anexo IdeM).

## Mecánicos con algo de trabajo (~15) — ~media hora cada uno

- **Las ~11 "ref" de Libertad** (p.15, p.16, p.34): mecánico si las fuentes ya están en `referencias.bib`. Si hay que buscar el paper/URL correcto de FAISS, pgvector, Elasticsearch, ASR y crear la entrada bib, se alarga.
- Reordenar el Resumen antes del índice (Libertad p.9): mover `\input` en `main.tex`, revisar que no rompa el formato de `prgrado.cls`.
- Fusionar Tabla 6.4 + 6.5 en un solo caption (Luis p.79): reestructurar el `table`, cuidar que entre en la página.
- Notas al pie en tablas que no renderizan (Luis p.68): usar `\footnotemark`/`\footnotetext` o `tablefootnote`, compilar y verificar.
- Agrandar / rotar Figura 4.1 (Libertad p.43): probar apaisada, regenerar si hace falta.
- Corregir cross-refs a "sección 6.6" (Luis p.80): decidir a qué apunta cada `\autoref` (anexo IdeM vs §6.6).
- Achicar letra de la tabla de modelos (Libertad p.79): `\scriptsize` o `\resizebox`.

## Requieren decisión o contenido nuevo (~9) — lo que lleva tiempo real

1. **Error conceptual p.86 (Luis)** — reescribir el párrafo de Re-Ranking en `7-Conclusiones.tex:30`. El punto: la similitud vectorial SÍ es semántica (los embeddings se entrenan para eso); lo que no garantiza es *relevancia*, y eso hay que medirlo (p. ej. rankeando con el set de preguntas del grupo). Corto pero hay que pensarlo bien. El texto erróneo está triplicado (`7-Conclusiones.tex`, `7-TrabajoAFuturo.tex`, `8-Conclusiones.tex`); solo compila el primero.
2. **Anexo de planificación nuevo (Libertad p.6)** — Gantt inicial y final, % de dedicación por tarea-macro, estimación de horas, comentario de demoras. Es material a **producir**, no a corregir. El ítem más pesado.
3. **Ampliar el Resumen (Libertad p.9)** — datos del corpus (239 cursos, 4.339 clases, faster-whisper + CTranslate2, 2–4x) y mención a evaluación con estudiantes en IdeM 2025. La tutora ya dio el texto base.
4. **Inconsistencia 24 vs 16 preguntas (Luis p.73/74)** — aclarar relación "preguntas únicas" vs "consultas evaluadas" y reescribir para que los números cierren en todo el Cap. 6.
5. **Unificar sigla UEFI / URI** — decisión de fondo (¿nombre correcto?) + pase global. Hoy aparece como "Unidad de Enseñanza...", "Unidad de Repositorios Institucionales" y "Unidad de Recursos Informáticos".
6. **"esta frase no va" (Libertad p.33) / "esta no va" (Luis p.48)** — decidir si cortar y cómo reescribir el resto.
7. **Sugerencia de fine-tuning con corpus de preguntas (Luis p.86)** — párrafo nuevo en Trabajo a Futuro, conectando con `7-Conclusiones.tex:34`.
8. **Reestructurar Anexo IdeM → solo el póster (Luis p.93)** — mover el relato de experiencia a §6.6, ajustar `\autoref` que lo citan (`6-Experimentacion.tex:5,324,333,359`; `7-Conclusiones.tex:26`).
9. **Dudas de redacción de Libertad** — "¿específicamente?" (p.19), "¿deseable?" (p.27), "¿ya que?" (p.37), "¿refinamiento?" (p.40). Cada una chica pero implica repensar la frase.

---

## Orden sugerido para mañana

1. Arrancar por lo mecánico en bloque (typos, espacios, comillas, `\autoref`, `\cite`) — despeja ~45 ítems rápido y da sensación de avance.
2. Las "ref" de Libertad — juntar todas las fuentes de una.
3. Error conceptual p.86 + inconsistencia 24/16 — los dos de contenido que no se pueden postergar.
4. Anexo de planificación — bloque de tiempo dedicado, en paralelo si se reparte entre los dos.
5. Limpieza estructural: borrar `8-Conclusiones.tex` y `7-TrabajoAFuturo.tex`, revisar `\label{chapter:8-Conclusiones}`.
