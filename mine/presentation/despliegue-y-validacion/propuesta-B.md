# Propuesta B — diapo 21 "Despliegue y Validación"

**Enfoque:** el humano primero. La lámina lidera con la validación en
Ingeniería de Muestra y las dos perspectivas de usuarios reales, equidad para
estudiantes del interior y extensión a otras facultades de UdelaR, como
mensaje central. La arquitectura técnica queda reducida a un par de bullets
de apoyo al final. Pensada para el momento de la charla donde el proyecto
conecta con el impacto real, no solo con la ingeniería.

**Restricciones respetadas:** no repite latencia (5,4 s, cold start) ni la
comparación self-hosting vs. servicio, ambas ya cerradas en la diapo 19. No
presenta Ingeniería de Muestra como estudio de usuario formal, se nombra
explícitamente como validación cualitativa.

**Tiempo objetivo:** 2 minutos.

---

## Título

**Despliegue y Validación**

Bajada en tipografía menor:
El sistema en producción real, visto por sus usuarios

---

## Bullets (texto para pegar en Slides)

- El sistema estuvo desplegado públicamente durante un período de evaluación,
  con tráfico real de estudiantes y actores académicos de la FING, no solo en
  condiciones de laboratorio.

- Durante Ingeniería de Muestra, instancia donde la FING comparte proyectos de
  grado con la comunidad académica, el grupo mostró el prototipo y recogió
  devolución cualitativa de estudiantes, docentes y actores académicos.

- Los estudiantes del interior del país, que no siempre pueden asistir de
  forma presencial, señalaron el valor del sistema como herramienta de equidad
  educativa, un chatbot entrenado con el material del curso puede sostener su
  rendimiento académico frente a la falta de acceso continuo a clase.

- Estudiantes de otras facultades de la Universidad de la República plantearon
  que la herramienta podría extenderse más allá de OpenFing, ampliando su
  alcance institucional mediante un filtrado por facultad.

- El despliegue se hizo sobre un VPS cedido por Mi Nube de ANTEL, con todos los
  servicios containerizados y expuestos con buenas prácticas de seguridad, sin
  incidentes durante el período de evaluación.

---

## Visual sugerido

Dos bloques lado a lado, no una tabla, esto no es una comparación de
dimensiones sino dos citas de impacto.

**Bloque izquierdo, "Equidad educativa":** ícono o silueta simple de un mapa
del interior del país, con una frase corta como cita, "sostener el
rendimiento académico frente a la falta de acceso continuo a clase".

**Bloque derecho, "Alcance institucional":** ícono simple de UdelaR o de
varias facultades, con la frase "extender la herramienta más allá de
OpenFing, a otras facultades de la Universidad".

Debajo de los dos bloques, una franja angosta con los datos duros de
respaldo, en tipografía menor, "VPS de Mi Nube ANTEL, Docker, TLS, sin
incidentes de seguridad durante el despliegue".

Si no hay tiempo de armar los dos bloques con íconos, alcanza con dos
recuadros de texto simple, uno por perspectiva, en vez de una lista de
bullets plana, para que las dos citas no se lean como un ítem más de una
lista.

---

## Notas del orador (guion, ~2 minutos)

Arranque, conectando con la diapo anterior sin repetir el dato de latencia.

"El despliegue que mencionamos recién, el que usamos para medir latencia,
también nos sirvió para algo más importante, saber si esto le importa a
alguien."

Contexto del evento.

"En octubre de 2025 participamos de Ingeniería de Muestra, la instancia donde
la facultad comparte los proyectos de grado con toda la comunidad académica.
Mostramos el prototipo funcionando en vivo y hablamos con estudiantes,
docentes y otros actores de la FING."

Perspectiva 1, equidad.

"La devolución que más nos marcó vino de estudiantes que viven en el interior
del país. Para ellos, no poder asistir de forma regular a la facultad genera
una desconexión real con el curso, y las vías tradicionales para resolver
dudas, foros, consultas informales, no siempre alcanzan. Un chatbot entrenado
específicamente con el material de su curso no es solo una comodidad, puede
ser un recurso que sostenga su rendimiento a la par de sus compañeros que
cursan en Montevideo."

Perspectiva 2, alcance.

"La segunda devolución vino de estudiantes de otras facultades de la
Universidad de la República, que después de la pandemia tienen sus propias
clases grabadas disponibles. Nos plantearon que la herramienta podría
servirles igual, extendiéndose más allá de OpenFing con solo un filtrado por
facultad."

Cierre técnico, breve.

"Todo esto corrió sobre un servidor que nos cedió Antel, containerizado con
Docker y expuesto con buenas prácticas de seguridad, sin ningún incidente
durante el período que estuvo activo."

---

## Cobertura de preguntas del archivo 03

**Cubiertas en pantalla o en el guion:**

- **B, ¿es un estudio de usuario formal?** El bullet 2 y el guion usan
  explícitamente "devolución cualitativa" y "recogió comentarios", no se habla
  de encuestas ni métricas, evita la sobreventa desde la propia lámina.
- **D, ¿la extensión a otras facultades está diseñada o es una idea suelta?**
  El bullet 4 dice "plantearon que podría extenderse", tiempo condicional, no
  se presenta como funcionalidad entregada.
- **E, ¿cómo se relaciona con la latencia de la diapo de infraestructura?** La
  frase de arranque del guion conecta ambas diapos sin repetir el número.

**Solo en el Q&A:**

- **A, ¿el sistema sigue funcionando hoy?** No entra en la lámina, la
  respuesta preparada en el archivo 03 explica que el VPS era temporal y el
  código está versionado.
- **C, ¿esta validación es representativa?** La lámina ya dice "cualitativa"
  para curarse en salud, pero si insisten en profundidad, la respuesta de que
  no busca representatividad estadística está lista en el archivo 03.
- **C (de esta carpeta, la de seguridad), ¿por qué contar los intentos de SSH
  bloqueados si no habla del RAG?** Esta propuesta B no incluye el dato de los
  533.000 intentos en la lámina, a diferencia de una propuesta más técnica, por
  eso esta pregunta ni se dispara desde la pantalla, pero si el tribunal
  pregunta por la seguridad del despliegue en general, la respuesta está en el
  archivo 03.

**Nota de diseño:** esta propuesta sacrifica el dato llamativo de los 533.000
intentos de SSH (que sí aparece fuerte en `02-puntos-mas-importantes.md` punto
3) a cambio de que la lámina completa quede dedicada al impacto humano sin
diluirlo con una cifra de seguridad. Si se quiere ese dato en pantalla,
conviene la propuesta A o un híbrido que lo sume como bullet técnico final.
