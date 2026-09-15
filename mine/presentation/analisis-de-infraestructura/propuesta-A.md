# Propuesta A — diapo 19 "Análisis de Infraestructura"

**Enfoque:** narrativa de viabilidad. Un solo mensaje central, pocos bullets, el
peso visual puesto en el contraste de costos. La lámina se defiende sola en 2 a 3
minutos.

**Mensaje central que se lleva el tribunal:** el sistema es sostenible en
producción y las decisiones de infraestructura tienen una justificación concreta.

---

## Título

**Análisis de Infraestructura**

Subtítulo o bajada (opcional, en tipografía menor):
Viabilidad operativa en costos, latencia y modelo de inferencia

---

## Bullets (texto para pegar en Slides)

- El costo de operación del modelo elegido es de aproximadamente 0,05 USD por cada
  mil consultas. Un semestre de uso intensivo de un curso se sostiene con centavos
  de dólar.

- La generación de respuestas se delega a un servicio de inferencia gestionada
  porque el entorno de despliegue no disponía de GPU y el modelo requiere del
  orden de 16 GB de memoria de video. El self-hosting local queda planteado para
  una etapa con hardware dedicado.

- La latencia se midió sobre 272 consultas reales en el servidor de producción,
  con una mediana de 5,4 segundos de extremo a extremo.

- La dependencia de un proveedor externo se asume como un costo conocido. Cualquier
  alternativa basada en modelos de pesos abiertos mantiene el gasto en el mismo
  orden de magnitud.

---

## Figura / visual sugerido

Gráfico de barras horizontales, **escala logarítmica en el eje de costo**, con el
costo estimado por cada mil consultas para cuatro modelos representativos:

| Modelo | Costo aprox. por 1.000 consultas |
|---|---|
| Llama 3.1 8B (inferencia gestionada) | 0,06 USD |
| Qwen2.5 72B (inferencia gestionada) | 0,61 USD |
| GPT-4.1 | 5,6 USD |
| GPT-5 Pro | 66 USD |

La barra del modelo elegido se resalta con color de acento. Encima del gráfico, un
número grande como ancla visual, por ejemplo **≈ 0,05 USD / 1.000 consultas**.
Nota al pie chica, tarifas de mayo de 2026, el mercado es dinámico.

Alternativa si no se quiere gráfico, la misma tabla de cuatro filas con la fila
del modelo elegido resaltada.

---

## Notas del orador (guion, 2 a 3 minutos)

Arranque con el mensaje central.

"Una herramienta que se propone para uso institucional tiene que demostrar que se
puede mantener en el tiempo. Analizamos tres dimensiones, cuánto cuesta operarla,
cuánto tarda en responder y qué modelo de inferencia usar."

Costos.

"Sobre la muestra de preguntas del capítulo de evaluación medimos el consumo de
tokens de una consulta promedio, alrededor de mil doscientos de entrada y
cuatrocientos de salida. Proyectamos ese consumo a mil consultas y lo cruzamos con
las tarifas de los proveedores. El modelo que elegimos, Llama 3.1 de ocho mil
millones de parámetros servido por inferencia gestionada, cuesta unos cinco
centavos de dólar cada mil consultas. En el gráfico se ve la diferencia contra
modelos propietarios de frontera, que están dos o tres órdenes de magnitud más
arriba. Para el volumen de un entorno académico el costo es despreciable."

Modelo de inferencia.

"La decisión de usar un servicio de inferencia en lugar de alojar el modelo
nosotros no fue una preferencia de diseño. El servidor que nos cedió Antel no
tenía GPU, y este modelo necesita del orden de dieciséis gigas de memoria de
video. En CPU la inferencia daba varios minutos por consulta, incompatible con un
chat. El modelo que elegimos es de pesos abiertos, así que el self-hosting sigue
siendo posible el día que haya hardware dedicado. Lo dejamos planteado como
trabajo a futuro."

Latencia.

"El tiempo de respuesta lo medimos con tráfico real, doscientas setenta y dos
consultas de usuarios durante el período de despliegue. La mediana fue de cinco
segundos y medio de extremo a extremo, repartidos entre la recuperación de
fragmentos y la generación. Hay un caso de arranque en frío que puede llegar a
más, cuando el modelo de embeddings se carga por primera vez tras un rato de
inactividad, pero con uso sostenido queda residente y no se percibe."

Cierre.

"El costo de esta arquitectura es la dependencia de un proveedor externo, que
puede cambiar tarifas o discontinuar un modelo. Lo asumimos como un riesgo
conocido, porque migrar a otro modelo abierto mantiene el gasto en el mismo orden
y no compromete la viabilidad económica del sistema."

---

## Cobertura de las preguntas del archivo 03

**Cubiertas por la lámina o por el guion:**

- **A (por qué inferencia externa y no self-hosting).** El bullet 2 y el bloque de
  guion "Modelo de inferencia" lo explican de frente, con la restricción de
  hardware y el self-hosting como trabajo a futuro.
- **B (cold start de 75 s).** Se menciona en el guion de forma proactiva sin poner
  el número feo en la lámina.
- **D (precios desactualizados).** Nota al pie del gráfico y frase del guion sobre
  el mercado dinámico y los órdenes de magnitud.
- **F (contraste de costos).** Es el visual central de la diapo.

**Se responden solo en el Q&A:**

- **C (representatividad de la muestra de latencia).** La lámina dice "272
  consultas reales", no entra en si son representativas. Respuesta preparada en 03.
- **E (qué pasa si el proveedor discontinúa el modelo).** El bullet 4 lo insinúa,
  el detalle de la migración va al Q&A.
- **G (alcanza un modelo de 8B).** Se remite a la diapo 18 de experimentación de
  modelos de lenguaje.
