# ¿Qué le puede llamar más la atención al tribunal?

Preguntas probables y respuesta preparada. La latencia y self-hosting ya
están cubiertos en `../analisis-de-infraestructura/03-atencion-del-tribunal.md`,
acá solo lo específico de despliegue y validación.

---

## A. "¿El sistema sigue funcionando hoy?"

El VPS de ANTEL era temporal y no se renovó.

Respuesta, el VPS se dio de baja al terminar el período de cesión gratuita,
fue un despliegue de validación por tiempo acotado, no una promesa de
disponibilidad permanente. Todo el código está versionado (GitLab), no se
perdió nada, y el sistema puede volver a desplegarse en cualquier
infraestructura equivalente, la arquitectura está containerizada
específicamente para eso.

---

## B. "¿Qué validación es esta, encuestas formales o comentarios sueltos?"

Es fundamental no sobrevender la Ingeniería de Muestra como si fuera un
estudio de usuario riguroso.

Respuesta, es una validación cualitativa, no un estudio de usuario
formal con métricas de satisfacción. Fue una instancia de exhibición donde
el grupo mostró el prototipo y recogió comentarios espontáneos de
estudiantes, docentes y actores académicos presentes. El valor está en que
son perspectivas de gente real, con casos de uso concretos (equidad para el
interior, extensión a otras facultades), no en que sea estadísticamente
representativo. Un estudio de usuarios formal queda como trabajo a futuro.

---

## C. "¿Por qué contar los intentos de SSH bloqueados, eso prueba algo sobre el sistema en sí?"

Podría verse como un dato de relleno, no relacionado al RAG.

Respuesta, no prueba nada sobre la calidad del chatbot, prueba que el
equipo asumió la responsabilidad de exponer un sistema con datos de
estudiantes a internet real y lo hizo con buenas prácticas de seguridad, no
es un detalle menor cuando se habla de desplegar algo institucional. Es
relevante para el RNF de privacidad y autonomía que se planteó en los
requisitos.

---

## D. "La propuesta de extender a otras facultades, ¿está diseñada o es una idea suelta?"

Cuidado con sonar como que ya está implementado.

Respuesta, es una perspectiva que surgió del intercambio con el público, no
una funcionalidad implementada. Requeriría, como mínimo, un sistema de
filtrado por facultad sobre el corpus, que es un cambio de alcance, no de
arquitectura, la base ya es extensible (RNF de extensibilidad, ver diapo de
objetivos). Queda como línea de trabajo a futuro, no como algo entregado.

---

## E. "¿Cómo se relaciona esto con la latencia de la diapo de infraestructura?"

Si preguntan por qué la latencia se separó de esta diapo.

Respuesta, es el mismo despliegue visto desde dos ángulos. La muestra de
latencia (272 consultas, diapo de infraestructura) se recolectó durante este
mismo período, de hecho 166 de esas 272 son justo del día de Ingeniería de
Muestra. Acá el foco es la arquitectura y la devolución humana, allá el foco
es el rendimiento medido.
