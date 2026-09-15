# Propuesta final — "Conclusiones"

Híbrida entre la propuesta A (narrativa minimalista) y la B (rigor técnico,
objetivo por objetivo). Se toma de A la fila de objetivos con íconos y
etiquetas cortas (no la oración completa del Cap. 1) y el tratamiento del
cierre como cita. Se toma de B la estructura en dos columnas para el bloque
inferior (autocrítica y viabilidad separadas, corto cada una), que además es
consistente con el patrón de dos tarjetas ya usado en Despliegue y
Validación y Análisis de Costos.

**Tiempo objetivo:** 2 minutos.

---

## Título

**Conclusiones**

Sin bajada de subtítulo propia, ver "Bloque de cierre" más abajo, esa línea
absorbió el rol de la bajada.

---

## Historial de cambios sobre esta consolidación (armado en vivo en Slides)

Esta sección se armó a mano en Slides con iteración directa del usuario, más
cambios de los habituales en una sola diapo. Lo que sigue documenta el
estado **final** después de esos cambios, no la primera consolidación de los
forks A/B. Cambios de fondo respecto a la consolidación original:

- El orden de la fila de íconos se invirtió para el objetivo parcial, ahora
  va último (4 check seguidos, `◐` al final), no en la posición 4 del Cap. 1.
  Es una decisión de layout, no implica un orden distinto de objetivos en el
  informe.
- La tarjeta izquierda dejó de explicar "por qué el objetivo 4 quedó
  parcial" (generaba confusión, mezclaba sin aclararlo la evaluación de ASR
  ya completa con la evaluación de respuestas pendiente) y pasó a resumir en
  un solo párrafo la implementación completa del sistema. La explicación del
  parcial queda solo en la línea de resumen bajo la fila de íconos y en el
  guion oral.
- La tarjeta derecha **cambió de tema**, dejó de hablar de viabilidad de la
  PoC y de la conexión con Ingeniería de Muestra, y ahora habla de que más
  evaluación es el camino para seguir mejorando la herramienta. Decisión
  explícita del usuario, ver nota de riesgo más abajo.
- La declaración de viabilidad no desapareció del todo, se reubicó en la
  línea de cierre de abajo de la diapo ("prueba de concepto totalmente
  viable...").
- La conexión con Ingeniería de Muestra **sí desapareció de la pantalla**,
  ya no está en ningún bloque. Sigue cubierta en Despliegue y Validación,
  pero ya no hay puente explícito entre esa diapo y esta.

**Riesgo a vigilar:** la tarjeta derecha ahora se superpone en espíritu con
Trabajo a Futuro (diapos 22-23), que desarrolla con más detalle qué tipo de
evaluación adicional hace falta (re-ranking, ajuste fino, retroalimentación
explícita del usuario). Cuando se arme esa diapo, revisar que no quede el
mismo mensaje repetido dos veces seguidas, ahí sí puede convenir que
Conclusiones se quede con la idea genérica ("más evaluación") y Trabajo a
Futuro con el detalle técnico de cómo.

---

## Estructura visual

### Bloque superior — fila de 5 objetivos con estado

Cinco íconos en fila horizontal, uno por objetivo específico del Cap. 1
(los objetivos ya se nombraron completos en la diapo 5, acá van resumidos en
una o dos palabras, no la oración entera). Orden final, con el parcial al
final de la fila:

```
  ✓          ✓        ✓            ✓                ◐
Pipeline    ASR    Chatbot   Arquitectura    Evaluación extensiva
                    RAG        extensible       de respuestas
```

Etiqueta del quinto objetivo cambiada de "Código abierto" a "Arquitectura
extensible" (decisión del usuario), para poner el énfasis en la parte del
objetivo 5 sobre extensibilidad hacia otras bases de conocimiento académico,
no en la licencia del repositorio.

Etiqueta del cuarto objetivo (el parcial) cambiada de "Evaluación de
pregunta-respuesta" a "Evaluación extensiva de respuestas" (decisión del
usuario, iterada dos veces). Primero se agregó "extensiva" para comunicar
que la evaluación en sí existe pero no llegó a la profundidad prevista, no
que falte por completo. Después se cambió "pregunta-respuesta" (nombre del
método del experimento, no del objeto evaluado) por "respuestas" (lo que
efectivamente se evalúa, la calidad de las respuestas del chatbot, según el
Cap. 7 línea 12).

El símbolo `◐` (medio relleno) marca el objetivo parcial, distinto de los
otros cuatro sin leerse como fallo. Color del check en el acento teal del
deck, el medio círculo en gris neutro, no en naranja ni rojo, para no leerse
como una alerta. **Ojo al armar en Slides:** el carácter Unicode `◐` puede no
existir en la tipografía del deck, mejor construir el ícono como una forma
(círculo con la mitad rellena) en vez de depender del glifo de texto.

Debajo de la fila, una línea centrada, chica, con la misma frase cualitativa
del Cap. 7 (línea 12, "el proyecto los abordó en su totalidad aunque con
distinta profundidad"), sin convertirla en una proporción numérica que el
informe no da textualmente:
> Los cinco objetivos fueron abordados, con distinta profundidad. La
> evaluación conversacional sobre el corpus completo es la principal tarea
> pendiente.

### Bloque inferior — dos columnas cortas

**Columna izquierda, acento teal, "Qué se logró"**
> Quedó implementado un sistema que consolida el conocimiento impartido por
> el cuerpo docente y lo expone a los estudiantes mediante una interfaz
> simple y moderna, funcionando así como una herramienta de autoestudio
> acorde a los tiempos actuales.

(Fraseo del usuario, ajustado para evitar el gerundio suelto como oración
nueva, "Sirviendo como..." pasó a integrarse con "así" en la misma oración,
según la regla de estilo de conectores consecutivos del proyecto.)

**Columna derecha, acento naranja, "Más evaluación, el próximo paso"**
> Más evaluación es el principal camino para mejorar la herramienta y
> aprovechar todo su potencial.

(Corregido de "Mas evaluación es el principal camino a seguir, para la
mejorar la herramienta y lograr el mayor provecho de la misma", faltaba la
tilde de "Más" y sobraba un "la".)

### Cierre, ancho completo

Reemplaza tanto la bajada del título como la cita de cierre original de
"barreras metodológicas, no económicas" (esa frase queda solo como remate
oral en el guion, no en pantalla):

> "Una prueba de concepto totalmente viable y de potencial para la
> comunidad educativo-universitaria."

Nota de estilo, "totalmente" es un énfasis del usuario, el Cap. 7 dice
"la solución es viable y funciona como se esperaba" sin ese calificador. No
es un dato inventado, es tono, se deja a criterio del usuario.

"Comunidad educativo-universitaria" no es un término que aparezca en
comunicados institucionales reales (se buscó explícitamente), es
gramaticalmente correcto pero un compuesto armado para esta diapo. La
alternativa más segura seguía siendo "comunidad universitaria", el término
que usa la propia UdelaR en sus comunicados. Decisión final a criterio del
usuario, que mantuvo el compuesto en las últimas capturas.

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
transcripción quedó completa y documentada con métricas concretas. Lo que no
llegamos a profundizar fue la evaluación del componente conversacional
sobre el corpus completo, priorizamos el tiempo en estabilizar el pipeline
de punta a punta antes que en esa fase experimental adicional."

Qué se logró (tarjeta izquierda).

"Con ese balance, lo que queda implementado es un sistema que consolida el
conocimiento impartido en los cursos de OpenFing y lo expone a los
estudiantes en una interfaz simple y moderna, una herramienta de autoestudio
pensada para los tiempos actuales. La solución es viable y funciona como
esperábamos, algo que también se reflejó en la devolución que recibimos en
Ingeniería de Muestra."

Próximo paso (tarjeta derecha).

"Dicho esto, más evaluación es el principal camino para seguir mejorando la
herramienta y aprovechar todo su potencial, ese es justamente el punto de
partida de lo que viene en Trabajo a Futuro."

Cierre.

"En términos generales, el proyecto muestra que las barreras para este tipo
de herramientas educativas basadas en IA son principalmente metodológicas,
no económicas. La generación de respuestas, en particular, no requirió
infraestructura de GPU propia, se resolvió con inferencia como servicio."

---

## Nota sobre "valor para la facultad" (párrafo 4 del Cap. 7)

No tiene representación propia en pantalla ni en el guion, más allá de la
línea de conexión con Ingeniería de Muestra. Es intencional, el usuario
eligió la opción "una línea de conexión" (no una sección nueva) al validar
el énfasis en el paso 3, así que este párrafo del capítulo queda sin cubrir
en esta diapo, no es un olvido de la consolidación.

## Cobertura de preguntas del archivo 03

**Cubiertas en pantalla o en el guion:**

- **A, ¿el objetivo 4 incompleto preocupa?** El checklist y el guion
  encuadran explícitamente "profundidad distinta entre componentes", no
  objetivo incumplido, y el símbolo `◐` evita que se lea como fallo.
- **B, ¿por qué no estimaron mejor el tiempo?** La columna "¿Por qué
  parcial?" lo dice directamente.
- **C, ¿"viable" es "ya en producción"?** Ni la columna de viabilidad ni el
  guion mencionan despliegue o continuidad operativa, eso queda en
  Despliegue y Validación.

**Solo en el Q&A:**

- **D, ¿la conclusión de barreras metodológicas es una afirmación fuerte?**
  Respuesta lista en `03`, remite a Infraestructura y Costos si insisten.
- **E, ¿la retro de estudiantes es representativa?** Ya resuelto en el Q&A
  de Despliegue y Validación, no se repite acá.
