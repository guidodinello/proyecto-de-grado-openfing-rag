# Propuesta final — diapo 19 "Análisis de Infraestructura"

Híbrida. Estructura y narrativa de la propuesta A, con el bullet del RNF5 traído a
pantalla desde la propuesta B y la tabla de contraste self-hosting vs. servicio
reservada como diapo de respaldo (backup slide).

**Formato:** una sola diapositiva. No se divide en 19a/19b, el deck ya tiene
cinco láminas vacías y dedicar dos a una de seis secciones es mala asignación de
espacio y de tiempo de exposición.

**Mensaje central:** el sistema es sostenible en producción y cada decisión de
infraestructura tiene una justificación concreta.

**Tiempo objetivo:** 2 a 3 minutos.

---

## Nota sobre el dato de costo (leer antes de armar el gráfico)

El informe está aceptado y congelado, se usa su valor tal como aparece.

- El §6.8.2 afirma "el costo promedio por cada mil consultas con Llama 3.1 8B a
  través del proveedor Novita es de aproximadamente 0,047 USD".
- Ese 0,047 coincide con la columna **P Prom** de la tabla 6.x, que es el costo
  proyectado de los tokens de entrada con el volumen promedio. La columna de
  tokens de salida (R Prom) para ese modelo es 0,016.
- El informe **no declara en ningún lado que el análisis considere solo tokens de
  entrada**. La tabla separa entrada y salida en columnas distintas y nunca las
  suma en una columna de total. El 0,047 del §6.8.2 se usa de forma laxa como
  "costo promedio". Estrictamente, el promedio entrada más salida es del orden de
  0,063 USD, pero los tokens de entrada dominan el costo en una arquitectura RAG,
  así que 0,047 es una aproximación razonable del costo operativo.
- **Decisión para la diapo:** se usa 0,047 USD como cifra ancla, citando el
  informe. El gráfico compara todos los modelos por su costo de tokens de entrada
  (columna P Prom), así la lámina es internamente consistente. La aclaración sobre
  entrada más salida queda preparada para el Q&A (ver archivo 03, punto H).
- **Comparación cuantificada que el informe sí respalda:** Llama es "hasta 10
  veces más barato que Qwen2.5-72B" (§6.7.1) y "sustancialmente menor que el resto
  de los modelos".

---

## Título

**Análisis de Infraestructura**

Bajada en tipografía menor:
Viabilidad operativa en costos, latencia y modelo de inferencia

---

## Bullets (texto para pegar en Slides)

- El costo de operar el modelo adoptado es de aproximadamente 0,047 USD por cada
  mil consultas, hasta diez veces menor que el de otros modelos abiertos de mayor
  tamaño y muy por debajo de los modelos propietarios de frontera. Un semestre de
  uso intensivo de un curso se sostiene con centavos de dólar.

- La generación de respuestas se delega a un servicio de inferencia gestionada
  porque el servidor de despliegue no disponía de GPU y el modelo requiere del
  orden de 16 GB de memoria de video. En CPU la inferencia local llevaba varios
  minutos por consulta.

- El self-hosting sigue siendo la vía para satisfacer plenamente el requisito de
  privacidad y autonomía. El modelo adoptado es de pesos abiertos, así que ese
  cambio no exige rediseñar la arquitectura y queda planteado como trabajo a
  futuro con hardware dedicado.

- La latencia se midió sobre 272 consultas reales en el servidor de producción,
  con una mediana de 5,4 segundos de extremo a extremo.

- La dependencia de un proveedor externo se asume como un costo conocido.
  Cualquier alternativa basada en modelos de pesos abiertos mantiene el gasto en
  el mismo orden de magnitud.

---

## Figura / visual sugerido

Gráfico de barras horizontales, **escala logarítmica en el eje de costo**, con el
costo proyectado de tokens de entrada por cada mil consultas (columna P Prom de la
tabla 6.x del informe) para cuatro modelos representativos:

| Modelo | Costo aprox. por 1.000 consultas (tokens de entrada) |
|---|---|
| Llama 3.1 8B (inferencia gestionada) | 0,047 USD |
| Qwen2.5 72B (inferencia gestionada) | 0,45 USD |
| GPT-4.1 | 2,36 USD |
| GPT-5 Pro | 17,7 USD |

La barra de Llama 3.1 8B resaltada con color de acento. Encima del gráfico, un
número grande como ancla visual, **≈ 0,047 USD / 1.000 consultas**. Nota al pie
chica, "tarifas de mayo de 2026, el mercado es dinámico, los órdenes de magnitud
se mantienen".

Alternativa si no se quiere gráfico, la misma tabla de cuatro filas con la fila
del modelo elegido resaltada.

---

## Diapo de respaldo (backup slide, no se muestra salvo que pregunten)

**Título:** Ejecución del modelo, inferencia como servicio frente a self-hosting

Tabla de contraste, se saca solo si el tribunal pregunta por el RNF5 de
privacidad o por qué no se alojó el modelo localmente.

| Dimensión | Inferencia como servicio | Self-hosting |
|---|---|---|
| Hardware requerido | Ninguno propio | GPU con 16 GB de VRAM |
| Latencia por consulta | Segundos | Minutos en CPU, segundos en GPU |
| Privacidad de datos | Las consultas salen a un tercero | Datos en servidores propios |
| Mantenimiento | A cargo del proveedor | A cargo del equipo |
| Costo | Proporcional al uso | Fijo, más predecible a largo plazo |

---

## Notas del orador (guion, 2 a 3 minutos)

Arranque con el mensaje central.

"Una herramienta que se propone para uso institucional tiene que demostrar que se
puede mantener en el tiempo. Analizamos tres dimensiones, cuánto cuesta operarla,
cuánto tarda en responder y qué modelo de inferencia conviene usar."

Costos.

"Sobre la muestra de preguntas del capítulo de evaluación medimos el consumo de
tokens de una consulta promedio, alrededor de mil doscientos de entrada y
cuatrocientos de salida. Proyectamos ese consumo a mil consultas y lo cruzamos
con las tarifas de los proveedores. El modelo que elegimos, Llama 3.1 de ocho mil
millones de parámetros servido por inferencia gestionada, cuesta menos de cinco
centavos de dólar cada mil consultas. Es hasta diez veces más barato que otro
modelo abierto más grande que también evaluamos, y en el gráfico se ve la
distancia contra los modelos propietarios de frontera, que están cientos de veces
por encima. Para el volumen de un entorno académico el costo es despreciable."

Aclaración sobre los precios.

"Estos precios son de mayo, el mercado se mueve rápido, es probable que los
números exactos ya cambiaron. Lo que se mantiene es la distancia entre un modelo
abierto servido de forma gestionada y un modelo propietario grande."

Modelo de inferencia.

"La decisión de usar un servicio de inferencia en lugar de alojar el modelo
nosotros no fue una preferencia de diseño. En los requisitos no funcionales
planteamos que lo ideal era alojar el modelo en la facultad, por privacidad de
los datos de los estudiantes y por costo predecible a largo plazo. Evaluamos las
dos opciones. La restricción fue de hardware, el servidor que nos cedió Antel no
tenía GPU y este modelo necesita del orden de dieciséis gigas de memoria de
video. En CPU la respuesta tardaba minutos, incompatible con una conversación. El
modelo que elegimos es de pesos abiertos, así que el self-hosting sigue siendo
posible el día que haya hardware dedicado, y lo dejamos planteado como trabajo a
futuro."

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

**Cubiertas por la lámina o el guion:**

- **A, por qué inferencia externa y no self-hosting.** Bullet 2 y 3 en pantalla,
  más el bloque de guion "Modelo de inferencia". La diapo de respaldo con la tabla
  de contraste está lista para profundizar.
- **B, cold start.** Se menciona en el guion de forma proactiva, sin poner el
  número en la lámina.
- **D, precios desactualizados.** Nota al pie del gráfico y bloque de guion sobre
  el mercado dinámico.
- **F, contraste de costos.** Es el visual central.
- **E, dependencia del proveedor.** Bullet 5 y cierre del guion, a nivel titular.

**Solo en el Q&A:**

- **C, representatividad de la muestra de latencia.** La lámina dice "272 consultas
  reales", no entra en que 166 son de un solo día. Respuesta en 03.
- **G, alcanza un modelo de 8B.** Se remite a la diapo 18.
- **H, el 0,047 es costo de tokens de entrada.** Nueva entrada en 03. Si preguntan,
  la tabla del informe separa entrada y salida, el promedio total es del orden de
  0,063 USD, y la conclusión de viabilidad no cambia.
