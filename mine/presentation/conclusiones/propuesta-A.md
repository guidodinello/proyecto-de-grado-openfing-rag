# Propuesta A — "Conclusiones" (narrativa minimalista)

Ángulo, mínima densidad de texto en pantalla, una idea por bloque, el guion
oral carga el detalle y los matices. La lámina se lee en cinco segundos, la
voz hace el resto.

**Tiempo objetivo:** 2 minutos.

---

## Título

**Conclusiones**

Bajada en tipografía menor, sin dos puntos como conector:
Una prueba de concepto viable, evaluada contra sus propios objetivos

---

## Estructura visual

Una sola columna, tres bloques apilados, mucho espacio en blanco entre
ellos. Nada de tablas ni bullets largos.

### Bloque 1, arriba, el más grande visualmente — fila de 5 objetivos

Cinco íconos en fila horizontal, uno por objetivo específico del Cap. 1, sin
nombrar cada objetivo en pantalla (eso ya está en la diapo 5). Cuatro con
check lleno, uno con un ícono distinto, ej. medio relleno o un símbolo de
"en curso", no una cruz ni nada que lea como fallo.

```
  ✓        ✓        ✓        ◐        ✓
Pipeline  ASR    Chatbot  Evaluación  Código
                  RAG      QA        abierto
```

Debajo de la fila, una sola línea, chica, centrada:
> 4 de 5 objetivos específicos cumplidos, evaluación conversacional completa
> sobre el corpus, la principal tarea pendiente.

El ícono distinto sobre "Evaluación QA" es la única pieza que necesita
explicarse en voz, el resto de la fila se lee sola.

### Bloque 2, centro — declaración de viabilidad

Una frase sola, grande, centrada, sin bullet:

> La solución es viable y funciona como se esperaba.

Caption chico debajo, la autocrítica resumida en una línea, conectada
explícitamente con el objetivo parcial del bloque 1:

> El alcance real del procesamiento del corpus completo superó lo estimado,
> eso achicó el tiempo disponible para la evaluación conversacional.

### Bloque 3, abajo — cierre

Frase de cierre, en cursiva o con un tratamiento tipográfico distinto al
resto de la diapo, como si fuera una cita:

> "Las barreras para este tipo de herramientas son metodológicas, no
> económicas."

---

## Sin footer de Ingeniería de Muestra como bullet

La conexión con la retro de Ingeniería de Muestra no ocupa espacio en
pantalla, va solo en el guion oral, un puente hacia el bloque 2, no una
pieza visual nueva que compita con Despliegue y Validación.

---

## Notas del orador (guion, ~2 minutos)

Arranque, conectando con lo que ya se mostró en Despliegue y Validación.

"Ya vimos que el sistema funciona en producción y que los usuarios reales lo
valoraron en Ingeniería de Muestra. La pregunta que queda es más de fondo,
¿el proyecto cumplió lo que se propuso al principio?"

Bloque 1 (objetivos).

"De los cinco objetivos específicos que planteamos en la introducción,
cuatro los cumplimos completamente, el pipeline automatizado, la evaluación
de herramientas de transcripción, el chatbot con referencia al instante
exacto del video, y la arquitectura de código abierto extensible. El quinto,
evaluar la calidad del pipeline conversacional con experimentos de
pregunta-respuesta, lo abordamos parcialmente. La evaluación de
transcripción quedó completa y documentada, pero la evaluación del
componente conversacional sobre el corpus completo es la principal tarea que
nos queda pendiente."

Bloque 2 (viabilidad y autocrítica).

"Con eso dicho, la conclusión central es que la solución es viable y
funciona como esperábamos. Pero vale la autocrítica, el alcance real de
procesar el corpus completo de OpenFing, casi 4.340 clases, terminó siendo
mayor al que habíamos estimado en la planificación, y eso achicó el tiempo
que nos quedaba para la fase de evaluación conversacional. Si tuviéramos que
volver a planificar el proyecto, invertiríamos más tiempo inicial en
estimar el costo computacional del preprocesamiento."

Bloque 3 (cierre).

"A pesar de eso, creemos que el proyecto muestra algo importante, las
barreras para llevar este tipo de herramientas educativas a la práctica son
principalmente metodológicas, no económicas. Todo esto lo construimos sin
GPU propia, con inferencia como servicio y con la infraestructura que ya
tiene la facultad."

---

## Cobertura de preguntas del archivo 03

**Cubiertas en el guion:**

- **A, ¿el objetivo 4 incompleto preocupa?** El guion encuadra explícitamente
  "profundidad distinta entre componentes", no objetivo incumplido.
- **B, ¿por qué no estimaron mejor el tiempo?** La autocrítica del guion lo
  dice directamente, con el número de clases como referencia concreta.
- **C, ¿"viable" es "ya en producción"?** El guion no usa la palabra
  "producción" ni sugiere despliegue institucional, solo remite a lo ya
  mostrado en Despliegue y Validación.

**Solo en el Q&A:**

- **D, ¿la conclusión de barreras metodológicas es una afirmación fuerte?**
  Respuesta lista en `03`, remite a Infraestructura y Costos si insisten.
- **E, ¿la retro de estudiantes es representativa?** Ya resuelto en el Q&A
  de Despliegue y Validación, no se repite acá.
