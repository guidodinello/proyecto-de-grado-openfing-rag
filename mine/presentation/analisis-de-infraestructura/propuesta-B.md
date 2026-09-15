# Propuesta B — Análisis de Infraestructura (diapo 19)

**Enfoque:** rigor técnico, estructura por las tres dimensiones que plantea §6.7
del informe (costos, latencia, modelo de ejecución). Pensada para un tribunal
técnico que va a pedir números y va a preguntar por el RNF5 de privacidad.

**Recomendación de formato:** dividir en dos sub-láminas. Una sola diapo con las
tres dimensiones y sus datos concretos queda sobrecargada y obliga a leer texto
en pantalla. La partición natural es costos por un lado, y latencia más decisión
de ejecución por el otro, porque esas dos comparten la misma causa raíz, la
ausencia de GPU en el entorno de despliegue. En el contador de tiempo de la
charla son unos 3 minutos combinados.

---

## Diapo 19a — Costos de Inferencia

### Título
Análisis de Infraestructura. Costos de Inferencia

### Bullets (texto para Slides)

- La estimación parte de la muestra de evaluación de preguntas y respuestas, con
  una consulta promedio de 1.179 tokens de entrada y 405 de salida, proyectada a
  un volumen de 1.000 consultas.
- Con el modelo adoptado, Llama 3.1 8B servido mediante inferencia gestionada, el
  costo es de aproximadamente 0,047 USD por cada 1.000 consultas.
- Los modelos propietarios de frontera se ubican entre dos y tres órdenes de
  magnitud por encima, hasta unos 66 USD por el mismo volumen.
- El costo por consulta resulta despreciable para una base de usuarios de escala
  académica, de modo que la viabilidad económica del despliegue queda establecida.
- El riesgo asumido es la dependencia del proveedor, que puede modificar tarifas
  o discontinuar el modelo. Una migración a otra alternativa de pesos abiertos
  mantendría el mismo orden de magnitud de costo.

### Visual sugerido

Gráfico de barras horizontales en escala logarítmica, eje en USD por cada 1.000
consultas, con cuatro modelos representativos para no saturar.

| Modelo | USD / 1.000 consultas |
|---|---|
| Llama 3.1 8B (HuggingFace) | ~0,06 |
| Qwen2.5 72B (HuggingFace) | ~0,61 |
| GPT-4.1 (OpenAI) | ~5,6 |
| GPT-5 Pro (OpenAI) | ~66 |

La barra de Llama 3.1 8B en color de acento. Nota al pie con la fecha de las
tarifas, 30 de mayo de 2026.

### Notas del orador (~1.5 min)

Para cerrar la viabilidad del sistema necesitábamos saber cuánto cuesta operarlo.
Tomamos la muestra de preguntas del experimento de evaluación, medimos el consumo
real de tokens de una consulta típica, promedio de mil ciento setenta y nueve de
entrada y cuatrocientos cinco de salida, y lo proyectamos a mil consultas. Con
esos números comparamos las tarifas vigentes de los modelos más usados del
mercado.

El resultado es el gráfico. En escala logarítmica, porque si no las barras de la
izquierda no se ven. El modelo que elegimos, Llama tres punto uno de ocho mil
millones de parámetros a través de inferencia gestionada, cuesta cuatro centavos
y medio de dólar cada mil consultas. Un curso entero con miles de preguntas al
semestre cuesta menos de un dólar. Los modelos propietarios de frontera, un GPT-5
Pro, están hasta mil cuatrocientas veces más caros para exactamente la misma
tarea.

Una aclaración honesta. Estos precios son de mayo, el mercado se mueve rápido, es
muy probable que los números exactos ya cambiaron. Lo que no cambia es la
distancia entre un modelo abierto servido de forma gestionada y un modelo
propietario grande, que se mantiene en dos o tres órdenes de magnitud. La
conclusión de viabilidad no depende del número fino.

El costo de esto es la dependencia del proveedor, que puede subir la tarifa o
dejar de servir el modelo. Si eso pasa migramos a otro proveedor de modelos
abiertos, el orden de magnitud del costo se mantiene.

---

## Diapo 19b — Latencia y Modelo de Ejecución

### Título
Análisis de Infraestructura. Latencia y Decisión de Ejecución

### Bullets (texto para Slides)

- La latencia se midió sobre 272 consultas reales del despliegue público en el
  VPS de Mi Nube ANTEL, con una mediana de 5,4 s y un promedio de 8,8 s.
- El tiempo total se descompone en dos fases, la recuperación vectorial con una
  mediana de 2,9 s y la generación del modelo de lenguaje con una mediana de
  2,4 s.
- Tras períodos de inactividad, la carga inicial del modelo de embeddings en CPU
  extiende la primera fase hasta 75 s, un efecto de arranque en frío que se
  amortiza con el uso sostenido.
- Se optó por inferencia como servicio en lugar de self-hosting porque el entorno
  de despliegue no disponía de GPU y Llama 3.1 8B requiere unos 16 GB de memoria
  de video. La ejecución local sobre CPU habría implicado varios minutos por
  consulta.
- El self-hosting sigue siendo técnicamente viable con hardware dedicado y es la
  vía para satisfacer plenamente el requisito de privacidad y autonomía. El
  modelo adoptado es de pesos abiertos, así el cambio no exige rediseñar la
  arquitectura.

### Visual sugerido

Opción 1, barra apilada de la latencia mediana por fase, 2,9 s de recuperación
más 2,4 s de generación, con una marca lateral que señale el peor caso de
arranque en frío de 75 s.

Opción 2, tabla compacta de contraste entre las dos alternativas de ejecución.

| Dimensión | Inferencia como servicio | Self-hosting |
|---|---|---|
| Hardware requerido | Ninguno propio | GPU con 16 GB de VRAM |
| Latencia por consulta | Segundos | Minutos en CPU, segundos en GPU |
| Privacidad de datos | Consultas salen a un tercero | Datos en servidores propios |
| Mantenimiento | A cargo del proveedor | A cargo del equipo |
| Costo | Proporcional al uso | Fijo, predecible a largo plazo |

Recomiendo la Opción 2, porque es la que responde de antemano la pregunta del
RNF5.

### Notas del orador (~1.5 min)

La segunda dimensión es la latencia, y la medimos en producción, no en
laboratorio. Doscientas setenta y dos consultas reales de gente que usó el
sistema mientras estuvo público en el servidor de Antel. La mediana fue cinco
segundos y medio.

Separamos ese tiempo en dos partes. Primero la recuperación, vectorizar la
pregunta y buscar los fragmentos relevantes en la base, mediana de tres segundos.
Después la generación del modelo de lenguaje, otros dos segundos y medio. Hay un
caso feo que conviene que lo cuente yo antes de que lo pregunten. Cuando el
sistema estuvo inactivo un rato largo, el modelo de embeddings se descarga de
memoria y el primer pedido siguiente tiene que recargarlo en CPU, y eso puede
llevar hasta setenta y cinco segundos. Es solo la primera consulta después de un
período muerto. Con uso sostenido, que es el escenario de un curso, el modelo
queda caliente y no se nota. Se soluciona con un warm-up periódico.

Y acá está la decisión de infraestructura más importante del proyecto, y quiero
adelantarme a la pregunta. En los requisitos no funcionales planteamos que lo
ideal era alojar el modelo en la facultad, por privacidad de los datos de los
estudiantes y por costo predecible. Evaluamos las dos opciones en serio. La
restricción fue de hardware. El servidor que nos cedió Antel no tenía placa de
video, y este modelo necesita unos dieciséis gigas de memoria de video. En CPU
la respuesta tardaba minutos, incompatible con una conversación. Por eso elegimos
inferencia gestionada. El modelo que usamos es de pesos abiertos, así que el día
que haya una GPU dedicada el sistema se puede self-hostear sin tocar la
arquitectura. Eso queda como trabajo a futuro.

---

## Cobertura de las preguntas del archivo 03

**Cubiertas por la lámina (el tribunal ve la respuesta en pantalla o en la nota):**

- **A, RNF5 de privacidad.** Bullet explícito en 19b más nota del orador que se
  adelanta a la pregunta. Es la principal razón de recomendar la tabla de
  contraste como visual.
- **B, cold start de 75 s.** Bullet explícito en 19b y guion que lo nombra
  proactivamente.
- **D, precios de mayo 2026.** Nota al pie en el visual de 19a y aclaración en el
  guion sobre órdenes de magnitud.
- **F, contraste de costos.** Es directamente el gráfico logarítmico de 19a.
- **E, dependencia del proveedor.** Cubierta a nivel de titular por el último
  bullet de 19a. El detalle de a qué proveedor se migraría queda para el Q&A.

**Se responden solo en el Q&A (no entran en la lámina para no saturar):**

- **C, representatividad de la muestra de latencia.** El hecho de que 166 de 272
  consultas sean de un solo día no va en pantalla. Respuesta oral, es validación
  cualitativa en condiciones reales, un estudio de carga sistemático es trabajo a
  futuro.
- **G, si un modelo de 8B alcanza.** Se remite a la diapo 18 de experimentación
  de modelos de lenguaje. En RAG el modelo sintetiza los fragmentos recuperados,
  no necesita el conocimiento memorizado.
- **E en detalle.** Qué proveedores alternativos existen y cuál sería el costo de
  la transición.

**Fuera de alcance de esta diapo (van en la diapo 20, Despliegue):** hardening del
VPS, TLS, Fail2Ban, aislamiento de red de Docker.
