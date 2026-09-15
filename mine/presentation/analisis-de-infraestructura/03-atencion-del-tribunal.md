# ¿Qué le puede llamar más la atención al tribunal?

Puntos que probablemente salten, preguntas esperables y cómo responderlas.
Preparar respuesta oral para cada uno.

---

## A. "Un RNF era privacidad y autonomía. ¿Por qué terminaron con inferencia externa?"

**Es la pregunta más probable de toda la sección.** El RNF5 (§3.3.4) lista
privacidad, latencia y costo como ventajas del self-hosting, y el sistema hace lo
contrario.

Respuesta, se evaluaron las dos alternativas. El self-hosting era la opción
preferida por privacidad de datos estudiantiles y por costo predecible a largo
plazo. La restricción fue de hardware, el VPS cedido por ANTEL no tenía GPU y
Llama 3.1 8B necesita ~16 GB de VRAM. En CPU la inferencia daba varios minutos por
consulta. La opción de "código abierto y ejecutable localmente" se mantiene, el
modelo elegido es open-weight y el sistema puede self-hostearse el día que haya
GPU dedicada. Queda planteado como trabajo a futuro.

No decir, "no llegamos a probar self-hosting". Sí se analizó, el informe lo
documenta.

---

## B. El cold start de 75 segundos

Número feo y muy visible en cualquier gráfico de latencia.

Respuesta proactiva (mejor decirlo antes de que lo pregunten), es el arranque en
frío del modelo de embeddings, que corre en CPU en el VPS. Se carga en el primer
request tras un período de inactividad y después queda residente en memoria. La
mediana con modelo caliente es 2,9 s. Con uso sostenido, que es el escenario real
de un curso, no se percibe. Se mitiga con un warm-up o manteniendo el proceso
vivo.

---

## C. Representatividad de la muestra de latencia

272 consultas, de las cuales 166 son de un solo día (Ingeniería de Muestra).

Respuesta, es una validación cualitativa en condiciones reales, no un estudio de
carga controlado. Da una foto realista de los tiempos que experimentaron usuarios
reales. Un benchmark de carga sistemático queda como trabajo a futuro. El valor
acá es que son datos de producción, no de laboratorio.

---

## D. Precios de mayo 2026 en una defensa de septiembre

El mercado de LLM fluctúa rápido y la tabla ya tiene 4 meses.

Respuesta, el informe lo aclara explícitamente, los valores son a fecha de
consulta y el mercado es dinámico. Lo que se mantiene estable son los órdenes de
magnitud, un modelo open de 8B servido por inferencia gestionada cuesta 2 o 3
órdenes de magnitud menos que un modelo propietario de frontera. La conclusión de
viabilidad no depende del número exacto.

---

## E. "¿Qué pasa si HuggingFace o Novita dejan de servir el modelo gratis?"

Dependencia de un tercero para una pieza crítica.

Respuesta, el sistema migra a otro proveedor de modelos open (hay varios en el
mercado de inferencia gestionada) o, si hay hardware, a self-hosting. El costo de
la transición es operativo, recalibrar prompts y revalidar respuestas. No es un
riesgo de viabilidad económica, porque cualquier alternativa open mantiene el
costo bajo. Es el trade-off que se asume al elegir inference as a service y está
documentado en el informe.

---

## F. Contraste que conviene mostrar

**0,047 USD vs. 66 USD** para 1.000 consultas (Llama-3-8B vía HF contra GPT-5 Pro).
Es un factor ~1.400x. Una barra en escala logarítmica con 3 o 4 modelos vende la
idea sin que haya que explicarla.

Cuidado, no dar a entender que Llama-3-8B tiene la misma calidad que GPT-5 Pro. El
punto es que para esta tarea, RAG sobre un corpus acotado con recuperación que
aporta el contexto, un modelo chico alcanza, y la evaluación de calidad (§6.6) lo
respalda.

---

## G. Posible objeción sobre la calidad del modelo elegido

"¿Un 8B es suficiente para un asistente educativo?"

Respuesta, remitir a la experimentación de modelos de lenguaje (§6, diapo 18). En
RAG el modelo no tiene que saber el contenido, tiene que sintetizar los fragmentos
recuperados. Ahí un modelo mediano rinde bien. La tabla de costos solo muestra que
además es barato.

---

## H. "El 0,047 USD, ¿incluye los tokens de salida?"

Un miembro del tribunal que mire la tabla 6.x del informe puede notar que tiene
columnas separadas de entrada (P Prom) y salida (R Prom), y que 0,047 es solo la
de entrada.

Respuesta, correcto, la cifra de 0,047 USD que aparece en el análisis de
despliegue (§6.8.2) corresponde al costo de los tokens de entrada, que en una
arquitectura RAG dominan el consumo porque incluyen la consulta, las instrucciones
del sistema y todos los fragmentos recuperados. Sumando los tokens de salida el
costo promedio total es del orden de 0,063 USD por cada mil consultas. La
diferencia no cambia ninguna conclusión, sigue siendo una fracción de centavo por
consulta y el modelo elegido sigue siendo cerca de diez veces más barato que la
alternativa abierta más grande que se evaluó. El informe presenta ambas columnas
por separado y no las suma en una sola cifra.

No decir, "es un error del informe". El informe está aceptado, la tabla está
completa, y 0,047 es una aproximación defendible del costo operativo.

---

## I. Seam de nombre del modelo, "Llama-3-8B" vs "Llama 3.1 8B"

La tabla 6.x del informe etiqueta la fila como Meta-Llama-3-8B-Instruct servido
por HuggingFace. El §6.8.2 habla de Llama 3.1 8B servido por Novita. Son etiquetas
distintas para lo que en la práctica es el mismo modelo de despliegue.

Decisión para la presentación, usar **"Llama 3.1 8B"** de forma consistente en
todas las láminas y en el guion, que es el nombre del modelo efectivamente
desplegado y el que referencia el dato de VRAM. Si el gráfico de costos se arma
con datos de la tabla, igual etiquetarlo "Llama 3.1 8B" para no mostrar dos
nombres.

Si preguntan por la diferencia, es la misma familia de modelos de 8B parámetros,
la variante desplegada. La cita bibliográfica de la afirmación de VRAM en el
informe apunta a Llama 2, conviene saberlo por si alguien lo chequea.
