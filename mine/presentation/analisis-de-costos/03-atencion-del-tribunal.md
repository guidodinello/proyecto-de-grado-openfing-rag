# ¿Qué le puede llamar más la atención al tribunal?

La mayoría de las preguntas de fondo sobre esta cifra ya están tratadas en
`../analisis-de-infraestructura/03-atencion-del-tribunal.md` (puntos D, F, H,
I). Acá solo lo específico de presentar la tabla o el gráfico de costos.

---

## A. "¿Por qué eligieron 1.000 consultas como volumen de referencia?"

Es una elección arbitraria de escala para poder comparar, no una proyección de
uso real esperado.

Respuesta, es una unidad de medida cómoda para expresar el costo, no una
predicción de cuántas consultas va a recibir el sistema. La proyección real
depende de cuántos estudiantes lo usen, pero como el costo escala linealmente
con el volumen, el número por cada 1.000 alcanza para razonar sobre cualquier
escala.

---

## B. "Esa tabla mezcla modelos muy distintos en capacidad, ¿es justo compararlos solo por precio?"

Cierto, un GPT-5 Pro y un Llama 3.1 8B no rinden igual en tareas generales.

Respuesta, la comparación es válida para esta tarea puntual, generación de
respuestas dentro de un pipeline RAG, donde el modelo sintetiza fragmentos ya
recuperados en vez de recordar conocimiento propio. La evaluación de calidad
(§6, experimentación de modelos de lenguaje) ya validó que el modelo elegido
rinde adecuadamente para ese rol específico. La tabla de costos no dice "este
modelo es mejor", dice "para la tarea que necesitamos, este es el más barato
entre los que ya probamos que funcionan".

---

## C. Ver puntos D, F, H, I en el archivo de infraestructura

- **D.** Precios de mayo 2026 en una defensa de septiembre, el mercado
  fluctúa, los órdenes de magnitud se mantienen.
- **F.** El contraste de costos es justamente el contenido central de esta
  lámina.
- **H.** El 0,047 USD es costo de tokens de entrada, no el total. Respuesta
  lista si alguien mira la tabla con atención.
- **I.** Nombre del modelo, usar "Llama 3.1 8B" de forma consistente, aunque la
  fila de la tabla diga "Meta-Llama-3-8B-Instruct".

---

## D. "¿De dónde sale que sea 10 veces más barato exactamente?"

Si alguien pide que se justifique el "10 veces" en el momento.

Respuesta, comparando la columna de costo de tokens de entrada de la tabla,
Llama 3.1 8B da 0,047 USD contra 0,448 USD de Qwen2.5-72B por cada 1.000
consultas, una razón de aproximadamente 9,5, que el informe redondea a "hasta
10 veces". Si se suma también el costo de salida la razón da prácticamente
igual, 0,063 contra 0,610, porque ambos modelos tienen tarifas de entrada y
salida similares entre sí.
