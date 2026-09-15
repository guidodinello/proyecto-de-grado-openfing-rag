# Propuesta final — "Análisis de Costos"

Híbrida entre A (número ancla minimalista) y B (riesgo visible), revisada con
advisor. Estructura de A porque es la correcta para una lámina de 1,5-2 min;
de B se toma solo el bullet de riesgo, promovido de opcional a fijo, y la
decisión de qué hacer con la diapo 21 existente.

**Diapo 20 (esta propuesta):** número ancla + gráfico simple de 3 modelos.
**Diapo 21 (ya existe, no se edita):** la tabla completa de 9 modelos, se
demota a **material de respaldo**, no se recorre en la exposición oral, se usa
solo si preguntan el detalle completo.

---

## Título

**Análisis de Costos**

Bajada en tipografía menor:
Costo de inferencia proyectado sobre 1.000 consultas

---

## Bullets (texto para pegar en Slides, 3 líneas, cada una corta)

- El modelo adoptado cuesta aproximadamente 0,047 USD por cada 1.000 consultas,
  hasta diez veces menos que Qwen2.5 72B, la otra alternativa abierta evaluada.

- Frente a los modelos propietarios de mayor escala del mercado, el costo de
  HuggingFace resulta sustancialmente menor para el mismo volumen de uso.

- El costo depende de un proveedor externo. Migrar a otra alternativa de pesos
  abiertos mantendría el gasto en el mismo orden de magnitud.

**Corrección hecha al consolidar (marcada por el advisor):** la propuesta A
original decía "varios órdenes de magnitud" en el segundo bullet. Nuestro
propio archivo `01-puntos-del-capitulo.md` ya advertía que el informe no
cuantifica esa distancia. En la columna que graficamos (costo de tokens de
entrada), 0,047 contra 17,69 de GPT-5 Pro es ~376 veces, entre dos y tres
órdenes de magnitud, no "varios". Se usa en su lugar la frase textual del
informe (línea 316), "sustancialmente menores a los precios del resto de los
modelos", que es citable sin que nadie pueda objetar la aritmética.

---

## Visual

**Número ancla, tercio superior de la diapo:**

> ## ≈ 0,047 USD
> ### por cada 1.000 consultas

Debajo, gráfico de barras horizontales, 3 modelos:

| Modelo | Costo por 1.000 consultas (tokens de entrada) |
|---|---|
| **Llama 3.1 8B** (elegido) | 0,047 USD |
| Qwen2.5 72B | 0,45 USD |
| GPT-5 Pro | 17,7 USD |

Barra de Llama 3.1 8B en el color de acento, con el valor impreso al final de
cada barra.

**Corrección hecha al consolidar:** la propuesta A pedía sacar la grilla y los
ejes numerados para que "la barra se vea corta". El advisor lo marcó como el
único tipo de gráfico que no se puede presentar sin etiqueta de escala. Sin
indicar que el eje es logarítmico, una diferencia real de ~376 veces se ve
como una barra apenas 3 o 4 veces más corta, y si alguien pregunta por qué la
barra de GPT-5 Pro no es "376 veces más larga" la única respuesta honesta es
"la escala es logarítmica", que ya no estaría en pantalla.

**Dos formas válidas de resolverlo, elegir una:**
- Mantener escala logarítmica pero agregar una etiqueta chica "escala
  logarítmica" cerca del eje, además del valor al final de cada barra.
- Usar escala lineal simple. La barra de Llama queda como una línea casi
  invisible al lado de las otras dos, lo cual de hecho refuerza el punto sin
  necesitar ninguna aclaración de escala.

Nota al pie, chica: "Tarifas de mayo de 2026."

---

## Notas del orador (guion, 1,5 a 2 minutos)

"Sobre la muestra de preguntas de la evaluación, medimos cuánto cuesta
responder con el modelo que elegimos. El resultado es este número, menos de
cinco centavos de dólar cada mil consultas. Para un curso que reciba miles de
preguntas en un semestre, el costo de mantener el sistema corriendo es
despreciable."

"Es hasta diez veces más barato que el otro modelo abierto de mayor tamaño que
evaluamos, y sustancialmente menor que los modelos propietarios más grandes
del mercado, que están pensados para tareas mucho más generales que la
nuestra."

"Esta comparación es específica para la tarea que resuelve el sistema, generar
una respuesta a partir de fragmentos ya recuperados, no una afirmación general
de que el modelo elegido rinda igual que un modelo de frontera en cualquier
contexto."

"Como contrapartida, dependemos de un proveedor externo. Si cambia las
condiciones o discontinúa el modelo, migramos a otra alternativa abierta, el
orden de magnitud del costo se mantiene."

"Estos precios son de mayo de este año, el mercado de modelos de lenguaje
cambia rápido, pero la distancia entre un modelo abierto chico servido de
forma gestionada y un modelo propietario grande no depende del número exacto."

---

## Diapo 21 (ya existe, no se toca su contenido)

Se deja como está, tabla completa de 9 modelos con las 8 columnas del informe.
Rol en la exposición, **material de respaldo**, no se explica línea por línea.
Se navega ahí solo si preguntan "¿con qué otros modelos compararon?" o piden
ver el detalle de tokens promedio vs. máximos.

---

## Cobertura de preguntas de los archivos 03

**Cubiertas en pantalla o en el guion:**

- **F (infraestructura), contraste de costos.** Número ancla + gráfico.
- **D (infraestructura), precios de mayo 2026.** Nota al pie y guion.
- **E (infraestructura), dependencia del proveedor.** Bullet 3, fijo en
  pantalla, no condicionado al tiempo.
- **B (costos), es justo comparar modelos tan distintos.** Tercer párrafo del
  guion, dicho de forma proactiva.

**Solo en Q&A:**

- **H (infraestructura), el 0,047 es costo de tokens de entrada.** Respuesta
  lista en el archivo 03 de infraestructura.
- **I (infraestructura), nombre del modelo.** "Llama 3.1 8B" usado de forma
  consistente en toda la lámina.
- **A (costos), por qué 1.000 consultas.** Respuesta lista si preguntan el
  porqué exacto de la unidad de referencia.
- **D (costos), de dónde sale el "10 veces".** Cálculo exacto preparado.
- **G (infraestructura), si un 8B alcanza.** Remite a la diapo de
  experimentación de modelos de lenguaje.

---

## Confirmado con el usuario

La diapo 20 real del deck tenía el layout de dos tarjetas con bullets viejos
("Costo único de compra de equipo" / "Costo de electricidad" y "Costo de VM
virtual" / "Costo de inferencia"), heredados de antes de la limpieza de la
diapo 19. Confirmado que eran placeholder de copy-paste, no contenido a
preservar. Se reemplazan por completo por el número ancla y el gráfico de
arriba.
