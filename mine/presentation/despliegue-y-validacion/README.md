# Despliegue y Validación

Workflow completo en [`../WORKFLOW.md`](../WORKFLOW.md). Acá solo lo específico
de esta diapo. No se referencia por número, la numeración del deck real se
corre cada vez que se inserta o borra una lámina, ver `../README.md`.

## Ojo con la superposición con Análisis de Infraestructura

§6.8 del informe mezcla tres cosas: arquitectura de despliegue, latencia en
producción, y comparación self-hosting vs. servicio. **La latencia y la
comparación self-hosting ya se usaron en la diapo de Análisis de
Infraestructura**. Para no repetirnos, esta diapo se enfoca en lo que falta,
la arquitectura de despliegue en sí y la validación con usuarios reales en
Ingeniería de Muestra. Si hace falta mencionar latencia acá, es de pasada,
no como contenido nuevo.

## Fuentes

- `Nuestro/Capitulos/6-Experimentacion.tex` §6.8 "Despliegue y Validación
  Operacional", intro y contexto del VPS (líneas ~321-328), no las
  subsecciones de latencia (330-339) ni self-hosting (341-348), esas ya están
  cubiertas en Análisis de Infraestructura.
- `Nuestro/Capitulos/6-Experimentacion.tex` §6.9 "Experiencia en Ingeniería de
  Muestra" (líneas ~350-364), la validación cualitativa con usuarios reales.
- `mine/data/deployment-minube-antel.md`, contexto técnico completo del
  despliegue (stack Docker, seguridad, estadísticas de ataques), más detallado
  que lo que entró en el informe. Fuente de contexto, no todo entra en la
  diapo.
- Anexo A, "Ingeniería de Muestra" (referenciado en el informe, pôster del
  grupo), no relevado en detalle acá.

## Estado

- [x] 01 puntos del capítulo
- [x] 02 puntos más importantes
- [x] 03 atención del tribunal
- [x] propuestas A y B (dos forks) + `propuesta-final.md` (híbrida, revisada con advisor)
- [x] diagrama de arquitectura como imagen (`arquitectura-despliegue.png`,
  con logos oficiales de Docker y Nginx, generado desde
  `arquitectura-despliegue.svg`)
- [x] pasada a Google Slides, revisada y aprobada por el usuario
