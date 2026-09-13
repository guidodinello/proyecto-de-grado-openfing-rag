# Datos de Experimentación — Chunks y Dataset

Relevados el 2026-05-03 mediante consultas SQL directas a la base de datos de producción.
Usar como fuente de verdad para completar Cap. 6 (Experimentación).

---

## Estadísticas generales del dataset de chunks

- **Total de chunks**: 217.986
- **Tabla**: `rag.chunks`

---

## Estrategia de chunking

```sql
SELECT metadata->>'chunk_strategy' AS chunk_strategy, COUNT(*) AS count
FROM rag.chunks GROUP BY metadata->>'chunk_strategy' ORDER BY count DESC;
```

| chunk_strategy | count   |
|----------------|---------|
| semantic       | 217.986 |

**Conclusión**: el 100% de los chunks en producción fueron generados con la estrategia semántica. No se usó Recursive Character Splitting en ningún chunk del dataset final.

**Parámetros del chunker semántico** (extraídos del campo `metadata->>'splitter_config'`):
- `strategy`: `"semantic"`
- `threshold_type`: `"percentile"`
- `semantic_threshold`: `0.6`
- `min_chunk_size`: `400`
- Embedder: `intfloat/multilingual-e5-base` (via `langchain_huggingface` 0.2.0, `normalize_embeddings: true`)

---

## Precisión de timestamps

```sql
SELECT metadata->>'timing_accuracy' AS timing_accuracy, COUNT(*) AS count
FROM rag.chunks GROUP BY metadata->>'timing_accuracy' ORDER BY count DESC;
```

| timing_accuracy | count   |
|-----------------|---------|
| precise         | 217.986 |

**Conclusión**: el 100% de los chunks tiene timestamps de precisión `"precise"`, es decir, su rango de caracteres se solapó directamente con segmentos Whisper y los tiempos de inicio/fin son exactos (no interpolados ni proporcionales).

---

## Educational score

```sql
SELECT
  MIN((metadata->>'educational_score')::float) AS min_score,
  MAX((metadata->>'educational_score')::float) AS max_score,
  AVG((metadata->>'educational_score')::float) AS avg_score
FROM rag.chunks WHERE metadata->>'educational_score' IS NOT NULL;
```

| min_score | max_score | avg_score          |
|-----------|-----------|--------------------|
| 0.0       | 1.0       | 0.2662037929041425 |

### Interpretación cualitativa

**Chunks con score = 1.0** (máximo): fragmentos extremadamente densos y ricos en contenido educativo. Ejemplos observados: clases completas de teoría de información (DUD denoiser), liderazgo organizacional, historia de la computación, diseño de circuitos secuenciales. Típicamente son los chunks más largos del dataset.

**Chunks con score = 0.0** (mínimo): fragmentos con contenido nulo desde el punto de vista educativo. Ejemplos observados:
- *"Las clases se retoman el siguiente lunes. Vamos a seguir viendo los lunes básicamente."*
- *"Me tienen que justificar la vez que viene por qué."*
- *"Nosotros vamos a testearlo con este simulador."*
- *"Nacimiento de noche... Va a quedar publicada..."* (artefacto de transcripción)

**Promedio ~0.27**: la mayoría de los chunks tiene contenido educativo moderado, lo que es esperable dado que las clases incluyen transiciones, comentarios administrativos y fragmentos de diálogo además del contenido sustantivo.

### Implicación para el sistema RAG

El `educational_score` puede usarse como filtro de recuperación para evitar retornar chunks de relleno como contexto. Un umbral de corte (ej. score > 0.1) eliminaría los fragmentos puramente administrativos sin descartar contenido educativo relevante.

---

## Pendientes / preguntas abiertas

- [ ] Distribución completa del educational_score (histograma por rangos: 0–0.1, 0.1–0.3, etc.)
- [ ] ¿Se aplica algún filtro por educational_score en el retrieval actual? Verificar en `chat_service.py`
- [ ] Cantidad de chunks por curso y por lección (distribución)
- [ ] Tamaño promedio de chunk en caracteres y palabras
- [ ] ¿Cuántas transcripciones tienen chunks? ¿Hay lecciones sin chunks?
