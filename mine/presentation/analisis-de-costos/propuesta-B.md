# Propuesta B — "Análisis de Costos"

**Enfoque:** tabla curada con foco y riesgo visible. Lámina más densa que una
narrativa minimalista, pensada para un tribunal técnico que va a querer auditar
el número antes de aceptarlo. No repite la diapo 19 (self-hosting vs. servicio,
latencia), se concentra solo en costo.

---

## Título

**Análisis de Costos**

Bajada en tipografía menor:
Proyección de costo de inferencia para 1.000 consultas

---

## Bullets (texto para pegar en Slides)

- La proyección parte del consumo real medido en la muestra de evaluación, una
  consulta promedio consiste en 1.179 tokens de entrada y 405 de salida, y se
  escala a un volumen de referencia de 1.000 consultas.

- Con el modelo adoptado, Llama 3.1 8B servido por inferencia gestionada, el
  costo resultante es de aproximadamente 0,047 USD por cada 1.000 consultas.

- Esa cifra es hasta diez veces menor que la de Qwen2.5 72B, el otro modelo de
  pesos abiertos evaluado, y sustancialmente menor que la de los modelos
  propietarios de mayor escala del mercado.

- La comparación es válida para la tarea puntual de este sistema, generar una
  respuesta a partir de fragmentos ya recuperados, no una afirmación general de
  que el modelo elegido rinda igual que los demás en cualquier tarea.

- El costo depende de un proveedor externo. Una discontinuación o un cambio de
  tarifa obligaría a migrar, aunque cualquier alternativa de pesos abiertos
  mantiene el gasto en el mismo orden de magnitud.

---

## Tabla curada (para la lámina, 6 modelos en vez de los 9 del informe)

Columnas mínimas, sin exponer P Prom/R Prom como tal para no invitar a leer la
tabla como si fuera de precios por token. Se etiqueta directamente como costo
proyectado.

| Modelo | Proveedor | Costo por 1.000 consultas (USD) |
|---|---|---|
| **Llama 3.1 8B** ← elegido | HuggingFace | **0,047** |
| Qwen2.5 72B | HuggingFace | 0,45 |
| GPT-4.1 | OpenAI | 2,36 |
| Gemini 2.5 Pro | Google | 1,47 |
| Claude Sonnet 4.6 | Anthropic | 3,54 |
| GPT-5 Pro | OpenAI | 17,69 |

Fila de Llama 3.1 8B resaltada en el color de acento del deck, con un
indicador breve de "elegido". Valores tomados de la columna de costo de tokens
de entrada de la tabla del informe (ver nota de consistencia abajo). Nota al
pie de la lámina, en tipografía chica: "Tarifas al 30 de mayo de 2026, mercado
sujeto a variación."

**Nota de consistencia (no va en la lámina, es para quien arma el gráfico):**
todos los valores de esta tabla curada vienen de la misma columna del informe
(costo de tokens de entrada, P Prom), igual que en la diapo 19. No mezclar con
columnas de salida o de máximos, para que cualquier verificación cruzada con el
informe cierre.

---

## Bullet de riesgo, visible en la propia lámina

En vez de dejarlo solo en las notas del orador, va como línea de cierre debajo
de la tabla, en tipografía distinta (itálica o un tono más tenue), para que se
lea pero no compita con el mensaje principal:

> El proveedor puede modificar tarifas o discontinuar el modelo sin previo
> aviso. Migrar a otra alternativa abierta mantiene el orden de magnitud del
> costo.

---

## Diapo de respaldo (no se muestra salvo pedido explícito de detalle)

**Título:** Análisis de Costos, tabla completa

La tabla de 9 modelos tal como está hoy en la diapo 21 del deck, sin editar.
Se deja como backup slide, no como parte de la exposición oral. Si el
tribunal pide ver el resto de los modelos o las columnas de costo máximo, se
navega ahí en el momento.

---

## Notas del orador (guion, 1.5 a 2 minutos)

"Para saber si el sistema es sostenible en producción medimos el costo real de
operarlo. Tomamos el consumo de tokens de una consulta promedio de la muestra
de evaluación y lo proyectamos a mil consultas."

"Con el modelo que elegimos, Llama 3.1 de ocho mil millones de parámetros
servido por inferencia gestionada, el costo es de menos de cinco centavos de
dólar cada mil consultas. Es hasta diez veces más barato que Qwen, el otro
modelo abierto que evaluamos, y muy por debajo de los modelos propietarios más
grandes del mercado, que se ven en la tabla."

"Esta comparación es específica para la tarea que resuelve el sistema, generar
una respuesta a partir de fragmentos ya recuperados. No estamos diciendo que
este modelo rinda igual que un GPT-5 Pro en cualquier contexto, la evaluación
de calidad de la sección de experimentación ya validó que para esta tarea
puntual el modelo elegido responde bien."

"Como contrapartida, dependemos de un proveedor externo. Si cambia las
condiciones o discontinúa el modelo, migramos a otra alternativa abierta, el
orden de magnitud del costo se mantiene."

"Estos precios son de mayo de 2026 y el mercado se mueve rápido, pero la
distancia entre modelos abiertos servidos de forma gestionada y modelos
propietarios de frontera no depende del número exacto."

---

## Cobertura de preguntas de los archivos 03

**Cubiertas en pantalla:**

- **A (de esta carpeta), por qué 1.000 consultas.** Bullet 1 lo encuadra como
  proyección, no como estimación de uso real (aclaración completa queda para
  Q&A si insisten).
- **B (de esta carpeta), es justo comparar modelos tan distintos.** Bullet 4
  lo dice explícitamente, "válida para la tarea puntual", en pantalla.
- **F (infraestructura), contraste de costos.** Es la tabla curada completa.
- **E (infraestructura), dependencia del proveedor.** Visible como bullet de
  cierre, no solo en notas.
- **D (infraestructura), precios desactualizados.** Nota al pie de la tabla.

**Solo en Q&A:**

- **H (infraestructura), el 0,047 es costo de entrada.** No se expone la
  distinción P Prom/R Prom en la lámina para no complicarla, queda lista la
  respuesta si preguntan.
- **I (infraestructura), nombre del modelo.** Se usa "Llama 3.1 8B" en toda la
  lámina, consistente con la diapo 19.
- **D (esta carpeta), de dónde sale el "10 veces".** Respuesta preparada con
  el cálculo exacto si lo piden.
- **G (infraestructura), si un 8B alcanza.** Remite a la diapo de
  experimentación de modelos de lenguaje.

---

## Nota sobre el formato de dos diapos vs. una

Con esta cantidad de contenido (5 bullets + tabla + bullet de riesgo) la
lámina queda cargada pero entra en una sola diapo sin forzar demasiado el
tamaño de fuente, siempre que la tabla se limite a 6 filas y 3 columnas como
está arriba. No recomiendo dividir en dos láminas para costos, ya son
suficientes diapos nuevas entre infraestructura y costos, y el informe trata
esto como una sola sección (§6.7.1).
