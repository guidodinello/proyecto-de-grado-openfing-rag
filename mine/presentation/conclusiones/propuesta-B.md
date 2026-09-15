# Propuesta B — "Conclusiones" (ángulo: rigor técnico, objetivo por objetivo)

Versión centrada en una rendición de cuentas literal contra los 5 objetivos
específicos del Cap. 1, para que el tribunal pueda mapear cada objetivo a su
resultado de un vistazo, en vez de una narrativa suelta.

**Tiempo objetivo:** 2 minutos.

---

## Título

**Conclusiones**

Bajada en tipografía menor:
Cumplimiento de objetivos y balance del proyecto

---

## Estructura: checklist de 5 objetivos + franja de cierre

### Bloque superior — Checklist de objetivos específicos

Una fila por objetivo, cinco filas, cada una con ícono de estado a la
izquierda y el objetivo resumido en pocas palabras (no la frase completa del
Cap. 1, una versión corta reconocible):

```
✓  Pipeline automatizado de extracción, transcripción e indexación
✓  Evaluación de ASR para español académico rioplatense
✓  Chatbot RAG con referencia a curso, lección e instante exacto
◐  Evaluación de calidad del pipeline con experimentos de pregunta-respuesta
✓  Software de código abierto, arquitectura extensible
```

El símbolo `◐` (medio relleno, no una tilde ni una equis) marca el objetivo
parcial, visualmente distinto de los otros cuatro sin sugerir fallo. Color
del check en teal (mismo acento que "cumplido" en otras diapos del deck),
el medio círculo en un gris neutro, no en naranja o rojo, para no leerse
como una alerta.

Debajo del checklist, una línea de resumen numérico corta:
> 4 de 5 objetivos específicos cumplidos, 1 abordado parcialmente.

### Bloque inferior — dos columnas cortas

**Columna izquierda, "¿Por qué parcial?"**
Una oración, tomada de la autocrítica del Cap. 7, sin repetir el checklist:
"La evaluación de transcripción quedó completa. La evaluación del
componente conversacional sobre el corpus completo es la principal área
pendiente, el tiempo priorizó estabilizar el pipeline completo sobre la
fase experimental."

**Columna derecha, "Viabilidad de la PoC"**
"La solución es viable y funciona como se esperaba. La retroalimentación
recogida en Ingeniería de Muestra reforzó esta conclusión."
(Una sola línea de conexión con Ingeniería de Muestra, sin retomar los
bullets de equidad educativa ni de alcance institucional, ya mostrados en
Despliegue y Validación.)

### Franja de cierre, ancho completo

Una línea, tipografía algo mayor que el cuerpo, centrada, en el color de
acento del deck:
> "Las barreras para implementar herramientas educativas RAG son
> principalmente metodológicas, no económicas."

---

## Notas del orador (guion, ~2 minutos)

Arranque, apoyado en el checklist mientras aparece en pantalla.

"Volviendo a los cinco objetivos específicos que planteamos al inicio,
cuatro se cumplieron en su totalidad. El pipeline automatizado de
extracción, transcripción e indexación, la evaluación de modelos de ASR
para español académico rioplatense, el chatbot RAG con trazabilidad al
instante exacto del video, y la arquitectura de código abierto extensible."

Objetivo parcial.

"El cuarto objetivo, evaluar la calidad del pipeline mediante experimentos
de pregunta-respuesta, lo abordamos parcialmente. La evaluación de la
transcripción quedó completa y documentada con métricas concretas. Lo que
no llegamos a profundizar fue la evaluación del componente conversacional
sobre el corpus completo, priorizamos el tiempo en estabilizar el pipeline
de punta a punta antes que en esa fase experimental adicional."

Viabilidad y cierre.

"Con ese balance, la conclusión central del proyecto es que la solución es
viable y funciona como esperábamos, algo que también se reflejó en la
devolución que recibimos en Ingeniería de Muestra. Y a nivel más general,
el proyecto muestra que las barreras para este tipo de herramientas
educativas basadas en IA son principalmente metodológicas, no económicas."

---

## Por qué este ángulo

El checklist explícito responde de forma directa a la pregunta que un
tribunal de proyecto de grado hace casi por reflejo frente a una diapo de
conclusiones, "¿cumplieron lo que dijeron que iban a hacer?". Al mostrar el
balance real (4 de 5, con el motivo del parcial ya integrado en pantalla)
se adelanta la pregunta A de `03-atencion-del-tribunal.md` antes de que haga
falta preguntarla, en vez de esperar a que surja en el Q&A. El costo es que
la diapo tiene más densidad visual que una narrativa suelta, se compensa
con la brevedad de cada fila del checklist (título corto, no la oración
completa del Cap. 1) y dejando el resto del contenido (viabilidad, conexión
con Ingeniería de Muestra, cierre) en bloques mínimos de una o dos líneas.

## Riesgos a vigilar (de `03-atencion-del-tribunal.md`)

- Que el checklist se lea como "todo cumplido" a primera vista si el ícono
  parcial no es lo bastante distinto de los otros cuatro, de ahí la
  elección deliberada de `◐` en vez de reusar el mismo tilde con otro color.
- Que la frase de viabilidad se malinterprete como "ya está en producción",
  por eso la columna de viabilidad no menciona el despliegue ni el VPS, ya
  cubierto aparte en Despliegue y Validación, y evita cualquier palabra que
  sugiera continuidad operativa.
