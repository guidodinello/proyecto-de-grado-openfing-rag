# Propuesta A — "Análisis de Costos"

**Enfoque:** número ancla minimalista. La lámina hace un solo trabajo, que en 5
segundos de mirarla el tribunal entienda "esto es barato", sin necesidad de leer
texto. Complementa la diapo 19 (ya cerrada), no repite su contenido de latencia
ni self-hosting.

**Tiempo objetivo:** 1,5 a 2 minutos.

---

## Título

**Análisis de Costos**

Bajada en tipografía menor:
Costo de inferencia proyectado sobre 1.000 consultas

---

## Bullets (texto para pegar en Slides, mínimos a propósito)

- El modelo adoptado cuesta aproximadamente 0,047 USD por cada 1.000 consultas,
  hasta diez veces menos que la alternativa abierta de mayor tamaño evaluada.

- Los modelos propietarios de mayor escala del mercado se ubican varios órdenes
  de magnitud por encima para el mismo volumen de uso.

(Dos bullets, no más. El peso de la diapo lo lleva el número y el gráfico, no el
texto.)

---

## Visual (elemento dominante de la diapo)

**Número ancla, ocupando el tercio superior de la diapo, tipografía grande:**

> ## ≈ 0,047 USD
> ### por cada 1.000 consultas

Debajo, gráfico de barras horizontales en escala logarítmica, solo 3 modelos
(menos es más para este enfoque):

| Modelo | Costo por 1.000 consultas (tokens de entrada) |
|---|---|
| **Llama 3.1 8B** (elegido) | 0,047 USD |
| Qwen2.5 72B | 0,45 USD |
| GPT-5 Pro | 17,7 USD |

Barra de Llama 3.1 8B en el color de acento del deck, mucho más corta que las
otras dos por ser escala log, con el valor impreso al final de la barra. Sin
grilla, sin ejes numerados, el eje logarítmico es un detalle técnico que no hace
falta mostrar, alcanza con que la barra se vea corta.

Nota al pie, chica: "Tarifas de mayo de 2026."

No usar tabla de 9 modelos acá, esa queda como material de respaldo si preguntan
(ver abajo).

---

## Notas del orador (guion, 1,5 a 2 minutos)

"Sobre la muestra de preguntas de la evaluación, medimos cuánto cuesta responder
con el modelo que elegimos. El resultado es este número, menos de cinco centavos
de dólar cada mil consultas. Para un curso que reciba miles de preguntas en un
semestre, el costo de mantener el sistema corriendo es despreciable."

"Es hasta diez veces más barato que el otro modelo abierto de mayor tamaño que
evaluamos, y varios órdenes de magnitud por debajo de los modelos propietarios
más grandes del mercado, que están pensados para tareas mucho más generales que
la nuestra."

"Estos precios son de mayo de este año, el mercado de modelos de lenguaje cambia
rápido, pero la distancia entre un modelo abierto chico servido de forma
gestionada y un modelo propietario grande se mantiene."

(Si el tiempo aprieta, cortar acá. Si sobra medio minuto, agregar la frase de
riesgo del proveedor abajo.)

Frase de cierre opcional, solo si hay tiempo:
"La contrapartida de este costo tan bajo es depender de un proveedor externo,
que puede cambiar sus tarifas. Cualquier alternativa abierta a la que migremos
se mantiene en el mismo orden de costo."

---

## Diapo de respaldo (no se muestra salvo que pidan el detalle)

La tabla completa de 9 modelos con las 8 columnas (P Prom, R Prom, P Máx, R Máx)
tal como está en el informe. Se usa solo si preguntan "¿y con qué otros modelos
compararon?" o piden ver la metodología completa de tokens promedio vs. máximos.

---

## Cobertura de preguntas del archivo 03 (esta carpeta + infraestructura)

**Cubiertas en pantalla o en el guion:**

- **F (infraestructura), contraste de costos.** Es el visual central completo.
- **D (infraestructura), precios de mayo 2026.** Nota al pie y frase del guion.
- **A (costos), por qué 1.000 consultas.** Implícito en el guion ("para un curso
  que reciba miles de preguntas"), no hace falta explicitarlo salvo que
  pregunten el porqué exacto de la unidad.

**Solo en el Q&A, no entran en esta lámina minimalista:**

- **H (infraestructura), el 0,047 es costo de tokens de entrada.** Con solo 2
  bullets y un número grande, no hay espacio para esta aclaración en pantalla.
  Respuesta lista en el archivo 03 de infraestructura si alguien mira la tabla
  con atención y pregunta.
- **I (infraestructura), nombre del modelo.** El gráfico y el guion ya usan
  "Llama 3.1 8B" de forma consistente, no requiere aclaración en pantalla.
- **B (costos), si es justo comparar modelos tan distintos por precio.**
  Respuesta lista en el archivo 03 de esta carpeta.
- **D (costos), de dónde sale el "10 veces".** Respuesta lista en el archivo 03
  de esta carpeta si piden que se justifique el número en el momento.
- El riesgo de dependencia del proveedor queda relegado a una frase de cierre
  opcional, condicionada al tiempo disponible, en vez de a un bullet fijo. Con
  este enfoque minimalista, meterlo como bullet fijo le resta impacto al número
  ancla, que es el objetivo central de la diapo.
