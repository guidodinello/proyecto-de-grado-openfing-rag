# ¿Cuáles son los puntos del capítulo?

Fuente: `6-Experimentacion.tex` §6.7.1 "Costos de Inferencia" (líneas ~251-318).
Es la sección que ya se relevó en detalle en
`../analisis-de-infraestructura/01-puntos-del-capitulo.md` (sección 1); acá se
repite y se ordena en función específica de la lámina de costos.

---

## Metodología

- Parte de la muestra de preguntas de §6.6 (evaluación QA).
- Consulta promedio: **1.179,25 tokens de entrada**, **405,125 de salida**.
- Peor caso de la muestra: **1.268 de entrada**, **702 de salida** (cota máxima).
- En una arquitectura RAG los tokens de entrada incluyen la consulta del
  usuario, las instrucciones del sistema y todos los fragmentos recuperados de
  la base vectorial. Los de salida incluyen la respuesta visible y, en modelos
  que lo usan, los tokens de razonamiento interno.
- Proyección a un volumen de **1.000 consultas**.
- El informe aclara que el costo real no depende solo del volumen de tokens,
  algunos modelos aplican optimizaciones internas que podrían bajar los costos
  presentados.

## La tabla (Tabla 6.x, tarifas al 30/05/2026)

Columnas: Modelo, Proveedor, Entrada ($/1M tok), Salida ($/1M tok), **P Prom**
(costo de tokens de entrada a volumen promedio), **R Prom** (costo de tokens de
salida a volumen promedio), P Máx, R Máx (mismo criterio con el peor caso). El
informe no suma P+R en una columna de total, ver
`../analisis-de-infraestructura/03-atencion-del-tribunal.md` punto H.

| Modelo | Proveedor | Entrada $/1M | Salida $/1M | P Prom | R Prom |
|---|---|---|---|---|---|
| Meta-Llama-3-8B-Instruct (Llama 3.1 8B en el texto) | HuggingFace | 0,04 | 0,04 | **0,047** | 0,016 |
| Qwen2.5-72B-Instruct | HuggingFace | 0,38 | 0,40 | 0,448 | 0,162 |
| GPT-5.4 Nano | OpenAI | 0,20 | 1,25 | 0,236 | 0,506 |
| Gemini 2.5 Pro | Google | 1,25 | 10,00 | 1,474 | 4,051 |
| Gemini 3.5 Flash | Google | 1,50 | 9,00 | 1,769 | 3,646 |
| GPT-4.1 | OpenAI | 2,00 | 8,00 | 2,358 | 3,241 |
| Claude Sonnet 4.6 | Anthropic | 3,00 | 15,00 | 3,538 | 6,077 |
| Claude Opus 4.1 | Anthropic | 15,00 | 75,00 | 17,689 | 30,384 |
| GPT-5 Pro | OpenAI | 15,00 | 120,00 | 17,689 | 48,615 |

## Lecturas explícitas del informe (§6.7.1, líneas 314-318)

- El mercado es dinámico, alta fluctuación de tarifas, los valores pueden
  cambiar.
- Gran varianza de precios entre los modelos comerciales evaluados.
- Los modelos servidos por HuggingFace son sustancialmente más baratos que el
  resto.
- El modelo elegido (Llama 3.1 8B) sería **hasta 10 veces más barato que
  Qwen2.5-72B**, el otro modelo abierto evaluado.
- **Riesgo operativo:** los proveedores pueden retirar, discontinuar o
  modificar el acceso a un modelo sin previo aviso. Migrar altera las
  proyecciones económicas y puede traer problemas técnicos, reconfiguración de
  arquitectura, recalibración de prompts, variaciones de rendimiento.

## Lo que el informe NO dice explícitamente (cuidado al presentar)

- No dice "consideramos solo tokens de entrada" en ningún lado, pero el 0,047
  USD que se repite en §6.8.2 como "costo promedio" es numéricamente la columna
  P Prom (entrada) de Llama, no un total. Total derivado ≈ 0,063 USD.
- No cuantifica la distancia contra los modelos propietarios de frontera en
  órdenes de magnitud ni en un múltiplo exacto, la única comparación numérica
  que da es el "10 veces" contra Qwen. Cualquier "1.400x" o "mil veces" contra
  GPT-5 Pro es una derivación nuestra, no una cita del informe.
