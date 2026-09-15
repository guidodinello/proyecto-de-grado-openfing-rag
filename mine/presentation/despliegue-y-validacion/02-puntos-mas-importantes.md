# ¿Cuáles son los más importantes?

Cuatro ideas, en orden de prioridad. Esta diapo tiene dos mitades naturales,
la arquitectura de despliegue (técnica) y la validación con usuarios
(humana), y la segunda es la que más impacto tiene en una defensa.

---

## 1. El sistema corrió en producción real, no solo en laboratorio

Está desplegado, accesible públicamente, con tráfico real de usuarios reales
durante un período. No es un prototipo que solo corrió en la notebook del
equipo.

Por qué importa, distingue este proyecto de uno puramente experimental.
Valida que la arquitectura (Docker, FastAPI, React, Postgres) funciona como
sistema integrado, no solo como piezas sueltas.

---

## 2. La validación con usuarios reales en Ingeniería de Muestra es el punto más fuerte de toda la diapo

Dos perspectivas concretas y con nombre, equidad educativa para estudiantes
del interior, y extensión institucional a otras facultades de UdelaR. Estas
no son opiniones genéricas de "les gustó", son casos de uso articulados por
la gente que los vive.

Por qué importa, es el momento de la charla donde el proyecto deja de ser
"funciona técnicamente" y pasa a "importa para alguien". Un tribunal
valora mucho ver que el equipo salió a mostrar el trabajo y escuchó
devolución real, no solo hizo benchmarks internos.

---

## 3. La seguridad del despliegue, un dato llamativo y concreto

Más de 533.000 intentos de conexión SSH bloqueados, cero incidentes. Es un
número que se recuerda y demuestra que se tomó en serio exponer el sistema
al internet real, no es un detalle menor de infraestructura.

Por qué importa, un proyecto de grado que además hizo hardening de
producción real (no solo "funciona en mi máquina") suma seriedad. Y es un
dato fácil de decir en una frase, no requiere que el tribunal entienda
Docker.

---

## 4. Conexión con la diapo de infraestructura, sin repetirla

Esta diapo y la 19 vienen del mismo despliegue, la muestra de latencia de la
diapo 19 se recolectó acá. Basta una frase que conecte ambas, no hace falta
repetir el número de latencia.

---

## Lo que NO entra en esta lámina

- El detalle de latencia (mediana 5,4 s, cold start), ya está en la diapo 19.
- La comparación self-hosting vs. servicio, ya está en la diapo 19.
- El detalle completo de hardening (SSH, Fail2Ban, UFW, capas de defensa),
  demasiado técnico para la lámina, el dato de los 533.000 intentos alcanza,
  el resto queda para el Q&A si preguntan cómo se aseguró el sistema.
- Las especificaciones exactas de los contenedores Docker (versiones,
  imágenes base), es demasiado detalle de implementación para una diapo de
  defensa.
