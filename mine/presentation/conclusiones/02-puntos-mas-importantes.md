# Qué entra sí o sí en la lámina, y por qué

Punto de partida a confirmar con el usuario (paso 3 del workflow), no una
decisión ya tomada.

## Entra sí o sí

1. **Cumplimiento de los 5 objetivos específicos, con el balance real (4
   cumplidos, 1 parcial).** `slides.md` ya marca esto como el eje de la
   diapo ("cerrar contra los objetivos de la diapo 5-6"). Es además lo que un
   tribunal de proyecto de grado más va a mirar en una diapo de conclusiones,
   no una lista de logros genérica sino la rendición de cuentas específica
   contra lo que se prometió en la introducción. Presentar los 5 como 100%
   logrados sería inexacto y el Cap. 7 mismo es explícito en que el cuarto
   quedó parcial.

2. **Declaración de viabilidad de la PoC.** "La solución es viable y
   funciona como se esperaba" es la frase que abre el capítulo, tiene que
   estar en algún lado de la diapo o del guion como conclusión central, no
   solo el detalle de objetivos.

3. **Autocrítica (estimación de tiempo/cómputo, evaluación QA incompleta).**
   Un tribunal valora que el equipo identifique sus propias limitaciones sin
   que se las señalen primero. Además conecta directamente con el objetivo 4
   parcial, no son dos temas separados, es la misma historia contada desde
   dos ángulos.

4. **Frase de cierre** ("las barreras son metodológicas, no económicas").
   Es la conclusión más "citable" del capítulo, funciona bien como última
   línea de la diapo o del guion oral antes de pasar a Trabajo a Futuro.

## Candidatos, a confirmar con el usuario

- **Resultados numéricos (WER < 0.05, Llama 3.1 8B sin GPU propia).** Ya
  tienen diapos propias asignadas más adelante en el deck (15 y 16, hoy
  placeholder). Usarlos acá en una versión mínima, una línea de respaldo, o
  no usarlos y dejar que esas diapos hagan todo el trabajo numérico, es una
  decisión de énfasis, no algo a decidir por default.
- **Valor para el estudiante / valor para la facultad (párrafos 3 y 4 del
  capítulo).** Se superponen parcialmente con Despliegue y Validación
  (equidad educativa, alcance institucional ya se mostraron ahí). Si entran
  acá, tendría que ser una mención de una línea que no repita esos bullets,
  no una sección nueva.
- **Áreas de mejora genéricas** (refinamiento de precisión, métricas de uso,
  integración con sistemas académicos, expansión de corpus). Se superponen
  en espíritu con Trabajo a Futuro (diapos 22-23), que ya cubre expansión de
  corpus y otras mejoras con más desarrollo. Riesgo de redundancia entre dos
  diapos consecutivas.

## Decisión de énfasis, validada con el usuario (paso 3 del workflow)

- **Números concretos (WER, Llama 3.1 8B):** no entran acá, quedan
  completamente para las diapos 15/16.
- **Valor para estudiante/facultad:** entra como una línea de conexión corta
  con la retro de Ingeniería de Muestra, sin repetir los bullets de equidad
  educativa / alcance institucional que ya están en Despliegue y Validación.
- **Áreas de mejora genéricas:** no entran acá, quedan para Trabajo a Futuro.

## No entra

- Todo el contenido de la sección "Trabajo a futuro" del mismo capítulo
  (integración institucional/URI, filtrado por facultad, re-ranking,
  fine-tuning, streaming, multimodalidad). Eso es contenido de las diapos
  22-23, ya armadas en `slides.md`.
- El detalle de Ingeniería de Muestra (equidad educativa, alcance
  institucional) más allá de una mención de pasada, ya está en Despliegue y
  Validación.
