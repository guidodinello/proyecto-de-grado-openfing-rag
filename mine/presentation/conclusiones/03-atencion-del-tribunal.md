# Qué puede saltar el tribunal, preguntas probables y cómo responderlas

## A. "¿El objetivo 4 quedó incompleto, no debería preocupar eso?"

El Cap. 7 mismo lo dice, "abordado parcialmente". La evaluación de
transcripción (objetivo 2, en rigor) quedó completa y documentada con
métricas concretas (WER). Lo que falta es la evaluación del componente
conversacional sobre el corpus completo, no la evaluación en general, ya
existe evaluación cualitativa de respuestas (ver Cap. 6) y la retro de
Ingeniería de Muestra. Encuadrar la respuesta como "profundidad distinta
entre componentes", no como objetivo incumplido sin más.

## B. "¿Por qué no hicieron una estimación de tiempo mejor si sabían que el
preprocesamiento sería costoso?"

Respuesta honesta ya está en la autocrítica del Cap. 7, el alcance real del
procesamiento del corpus completo (239 cursos, 4.339 clases) resultó mayor a
lo estimado en la planificación inicial. El Anexo A (Planificación) tiene el
detalle de cronograma planeado vs. real si preguntan por números concretos.

## C. "¿'Viable' significa que ya está en producción?"

No, la solución es una prueba de concepto validada, no un sistema en
producción institucional. El VPS de Mi Nube ANTEL (ver diapo Despliegue y
Validación) fue una solución provisional. La integración institucional con
la URI es justamente el primer punto de Trabajo a Futuro, no algo ya
resuelto. Importante no dejar que la diapo de conclusiones suene a "ya está
desplegado y en uso", el informe no dice eso.

## D. "¿La conclusión de que las barreras son 'metodológicas, no económicas'
no es una afirmación fuerte para una PoC de este tamaño?"

Es una conclusión textual del Cap. 7, respaldada por el hecho de que el
proyecto se hizo sin GPU propia (inferencia como servicio) y con recursos ya
disponibles en la infraestructura de la facultad. Si el tribunal empuja
sobre esto, remitir a la diapo de Análisis de Infraestructura (self-hosting
vs. servicio) y a la de Análisis de Costos, ambas ya muestran por qué el
costo no fue la barrera principal.

## E. "¿Qué tan representativa es la retroalimentación de estudiantes que
mencionan como evidencia de valor?"

Ya cubierto en el Q&A de la diapo de Despliegue y Validación (`archivo 03`
de esa carpeta), la validación es cualitativa, no busca representatividad
estadística. Si esta diapo menciona esa retro de pasada, no hace falta
repetir la respuesta acá, remitir mentalmente a esa diapo.

## Riesgo de redacción a evitar

No convertir la diapo en una lista plana de logros sin matices, el valor de
esta lámina frente al tribunal está justamente en mostrar que el equipo
puede evaluar su propio trabajo con criterio, no en maximizar la cantidad de
cosas que salieron bien.
