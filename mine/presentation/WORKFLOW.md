# Workflow de preparación de diapositivas — defensa 17/9

Cómo se prepara el contenido de cada diapo de la defensa. Google Slides es la
**fuente de verdad del layout**; todo lo de acá es contenido y guion de apoyo,
se pasa a Slides a mano.

## Estructura de carpetas

```
mine/presentation/
  WORKFLOW.md              este archivo
  slides.md                índice de diapos, una por bloque (numeración orientativa)
  pdfs/
    Presentacion 17_9 Tesis.pdf                       export del deck
    Proyecto_de_Grado_INCO_InCo_FIng_UdelaR.pdf        informe completo compilado
  <slug-diapo>/             una carpeta por diapo que necesita desarrollo real
    README.md               fuentes de esa diapo + checklist de estado
    01-puntos-del-capitulo.md
    02-puntos-mas-importantes.md
    03-atencion-del-tribunal.md
    propuesta-A.md
    propuesta-B.md
    propuesta-final.md
    *.svg / *.png            diagramas o figuras propias de esa diapo, si hacen falta
```

No todas las diapos necesitan su carpeta, solo las que requieren desarrollo de
contenido real (las que estaban en placeholder o necesitan argumentación). Una
diapo que ya está resuelta en una línea se maneja directo en `slides.md`.

## Pasos por diapo

1. **Fuente.** Identificar qué sección del informe (.tex) y qué archivos de
   `mine/` respaldan la diapo. Se anota en el `README.md` de la carpeta.

2. **Preguntas de encuadre.** Antes de redactar la lámina se responden tres
   preguntas, un archivo cada una:
   - `01-puntos-del-capitulo.md` — todo lo que dice el capítulo, sin filtrar.
   - `02-puntos-mas-importantes.md` — qué entra sí o sí en la lámina y por qué.
   - `03-atencion-del-tribunal.md` — qué puede saltar el tribunal, preguntas
     probables y cómo responderlas.
   Si el contenido de fondo ya fue relevado en otra carpeta (por ejemplo dos
   diapos que cubren la misma sección del informe desde ángulos distintos),
   estos tres archivos pueden armarse directo sin forks, referenciando la
   carpeta hermana en vez de duplicar la investigación.

3. **Validación de énfasis con el usuario. Obligatorio, no se saltea.** Antes
   de lanzar los forks, se presenta el punteo de `01` y `02` y se le pregunta
   al usuario explícitamente qué puntos quiere que tengan énfasis en la
   lámina, o qué puntos del capítulo quiere que se traten y cuáles no. No se
   asume que el ranking de importancia armado en `02` es el que el usuario
   quiere ver reflejado en la diapo, es un punto de partida a confirmar, no
   una decisión ya tomada. Este paso existe porque en la diapo de Despliegue y
   Validación se avanzó directo a una propuesta con un dato (intentos de SSH
   bloqueados) que además resultó no estar en el informe, sin haber validado
   antes con el usuario si ese era el énfasis correcto.

4. **Propuesta de lámina, con dos forks en paralelo.** Siempre que haya margen
   de diseño real (no solo cuando es la primera diapo), se lanzan dos agentes
   fork con el mismo material de entrada (los tres archivos del paso 2 más la
   validación de énfasis del paso 3) pero un ángulo de diseño distinto cada
   uno, por ejemplo narrativa minimalista vs. rigor técnico denso. Cada uno
   escribe su propia `propuesta-A.md` / `propuesta-B.md`, sin tocar los demás
   archivos.

5. **Consolidación.** Se leen ambas propuestas y se arma un híbrido en
   `propuesta-final.md`, tomando la estructura que mejor sirve y las piezas
   sueltas que valga la pena rescatar de la otra.

6. **Chequeo con el advisor.** Antes de cerrar la propuesta final se llama al
   advisor para que revise el consolidado contra el resto de la conversación.
   Su valor principal históricamente fue detectar inconsistencias numéricas o
   afirmaciones no respaldadas por el informe que ninguno de los dos forks
   había notado (ver ejemplos en `analisis-de-infraestructura/propuesta-final.md`
   y `analisis-de-costos/propuesta-final.md`). Se aplican sus correcciones
   antes de dar la propuesta por cerrada.

7. **A Slides.** El usuario copia la propuesta final a Google Slides a mano.

8. **Revisión iterativa en Slides.** El usuario comparte capturas de pantalla
   a medida que arma la diapo, se da feedback puntual de formato (alineación,
   color, qué tabla vs. qué bullets, etc.) hasta que la diapo queda cerrada.

9. **Re-sync.** Después de cerrar una diapo en Slides, se re-exporta el PDF y
   se actualiza el bloque correspondiente en `slides.md` si hace falta.

## Regla de numeración

Las carpetas de diapo se nombran y se referencian **por sección, no por
número**. El número de diapo en Slides se corre cada vez que se inserta,
borra o reordena una lámina, y varias veces quedó desincronizado entre
`slides.md` y los README de cada carpeta. Para ubicar una carpeta en el deck
actual, mirar el panel de miniaturas de Slides por título de diapo.

## Reglas de contenido

- El informe (`Proyecto_de_Grado_INCO_InCo_FIng_UdelaR.pdf` / los `.tex`) está
  **aceptado y congelado**. No se "corrige" ni se cambian sus cifras aunque
  parezcan imprecisas, se usan tal como aparecen y cualquier aclaración va
  como nota de Q&A, no como corrección en la lámina.
- No se ponen en pantalla multiplicadores o comparaciones que el informe no
  cite textualmente. Si hace falta comparar y el informe no da un número
  exacto, se usa la frase cualitativa que el informe sí usa (ej. "sustancialmente
  menor"), no una derivación propia que un miembro del tribunal pueda
  recalcular y no coincidir.
- **No se usan datos o hechos que no estén en el `.tex` final**, aunque sean
  ciertos y estén documentados en archivos de trabajo de `mine/` (ej.
  `mine/data/deployment-minube-antel.md` tiene detalle operativo, estadísticas
  de ataques, que nunca entró al informe). Si el tribunal busca el dato en el
  capítulo que ya leyó y no lo encuentra, es peor que no haberlo mencionado.
  Ese tipo de información queda para el Q&A oral, aclarando que es
  conocimiento del equipo adicional al informe, no para la lámina.
- Estilo de redacción, el mismo del informe, prosa académica, sin em dash, sin
  dos puntos como conector de oraciones.

## Estado general

Ver el checklist en el `README.md` de cada carpeta de diapo. Diapos con
carpeta propia hasta ahora, ver [`../README.md`](README.md) para el listado
actualizado por nombre de sección, no por número.
