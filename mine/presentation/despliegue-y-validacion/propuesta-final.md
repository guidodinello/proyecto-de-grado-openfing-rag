# Propuesta final — "Despliegue y Validación"

Versión 2, reequilibrada con el usuario después de revisar el peso real que
le da el capítulo a cada tema. La v1 (más abajo, en el historial de este
archivo antes de esta reescritura) ponía casi todo el peso en Ingeniería de
Muestra con la arquitectura reducida a una línea de footer, pero §6.8 del
informe le dedica desarrollo real a la arquitectura de despliegue, no solo de
paso. Esta versión balancea 50/50, una tarjeta por tema.

**Validado con el usuario antes de esto (paso 3 del workflow):** sacar el
dato de intentos de SSH bloqueados, no está en el `.tex`. Dar peso igual a
arquitectura y a validación humana, sin un footer de dato suelto.

**Tiempo objetivo:** 2 minutos.

No repite latencia (5,4 s, cold start) ni self-hosting vs. servicio, ya
cerrados en la diapo de Análisis de Infraestructura.

---

## Título

**Despliegue y Validación**

Bajada en tipografía menor:
Arquitectura de producción y validación con usuarios reales

---

## Estructura: dos tarjetas, mismo tamaño, mismo peso visual

### Tarjeta izquierda — "Arquitectura del despliegue"

Diagrama de cajas y flechas, no un diagrama de red exhaustivo. Ya armado como
imagen en [`arquitectura-despliegue.png`](arquitectura-despliegue.png)
(exportado desde `arquitectura-despliegue.svg`, mismo estilo visual que
`analisis-de-infraestructura/comparacion-ejecucion.svg`; se usa el PNG porque
Google Slides no soporta insertar SVG directamente). Cada caja lleva un ícono
simple a color, monitor/navegador para el usuario, ballena para Docker
Compose, marca de bloques para Nginx, átomo para React, rayo para FastAPI,
cilindro de base de datos para PostgreSQL, en vez de logos oficiales exactos
(evita depender de assets de marca externos). Sin subtítulos de texto dentro
de las cajas (se sacaron "TLS, único punto de entrada" y "red interna, nunca
expuesto"), el ícono y el color de borde ya comunican el rol de cada pieza.

**Corrección tras feedback del usuario:** Docker y Nginx pasaron a usar sus
logos oficiales reales (paths de [simple-icons](https://simpleicons.org),
`docker.svg` y `nginx.svg`), no una versión estilizada propia. Nginx pasó de
bloque naranja sólido a tarjeta neutra (como el resto de las cajas) con borde
naranja y el hexágono verde oficial, para que el color real del logo no
compitiera con el naranja del deck.

```
Usuario / Navegador
        │
        ▼
   Nginx (TLS, único punto de entrada)
    │              │
    ▼              ▼
Frontend React   Backend FastAPI
                     │
                     ▼
          PostgreSQL (red interna,
           nunca expuesto)
```

Frontend + Backend + PostgreSQL encerrados en un rectángulo punteado
etiquetado **"Docker Compose"**, para comunicar que es un stack
containerizado de punta a punta.

Caption chico debajo del diagrama:
> VPS de Mi Nube ANTEL, cedido sin costo institucional.

### Tarjeta derecha — "Validación en Ingeniería de Muestra"

Dos bullets cortos dentro de la misma tarjeta, no dos tarjetas separadas
como en la v1, para que ocupe el mismo espacio que la tarjeta de arquitectura
y no desequilibre la diapo hacia lo humano:

- **Equidad educativa.** Estudiantes del interior del país, que no siempre
  pueden asistir de forma presencial, sostienen su rendimiento académico con
  el material del curso.
- **Alcance institucional.** Estudiantes de otras facultades de la
  Universidad de la República plantearon extender la herramienta más allá de
  OpenFing.

Caption chico debajo, simétrico con el de la izquierda:
> Ingeniería de Muestra, octubre de 2025, devolución cualitativa de
> estudiantes, docentes y actores académicos.

**Corrección ya aplicada desde la v1 (marcada por el advisor):** el bullet de
equidad separa lo que los estudiantes reportaron (su situación, no pueden
asistir regularmente) de lo que el equipo concluye a partir de eso (valor
como herramienta de equidad educativa). El informe (línea 358) atribuye la
lectura de equidad a los autores, no a los estudiantes.

---

## Sin footer

La v1 tenía una franja inferior con datos duros. Se cae en esta versión, cada
tarjeta ya lleva su propio caption de contexto (VPS de ANTEL / fecha de
Ingeniería de Muestra), no hace falta una tercera franja.

---

## Notas del orador (guion, ~2 minutos)

Arranque, conectando con la diapo de infraestructura sin repetir el dato de
latencia.

"El mismo despliegue del que salieron los datos de latencia que vimos antes
también nos sirvió para dos cosas más, probar la arquitectura en producción
real y validar el sistema con usuarios reales."

Arquitectura (tarjeta izquierda).

"Todo corre containerizado con Docker Compose, sobre un servidor que nos
cedió Antel sin costo, como apoyo institucional. Nginx es el único punto de
entrada, con TLS de Let's Encrypt, y la base de datos nunca se expone a
internet, solo el backend puede conectarse a ella por una red interna
separada."

Validación (tarjeta derecha).

"En octubre de 2025 participamos de Ingeniería de Muestra, la instancia donde
la facultad comparte los proyectos de grado con toda la comunidad académica.
Mostramos el prototipo funcionando en vivo y recogimos devolución cualitativa
de estudiantes, docentes y actores académicos. Dos perspectivas se
repitieron. Estudiantes que viven en el interior del país nos contaron que no
poder asistir de forma regular genera una desconexión real con el curso, y
que las vías tradicionales para resolver dudas no siempre alcanzan, a partir
de esa conversación identificamos que un chatbot entrenado con el material de
su curso puede ser un recurso que sostenga su rendimiento a la par de sus
compañeros que cursan en Montevideo. La segunda perspectiva vino de
estudiantes de otras facultades de la Universidad de la República, que
plantearon que la herramienta podría extenderse más allá de OpenFing con un
filtrado por facultad."

---

## Cobertura de preguntas del archivo 03

**Cubiertas en pantalla o en el guion:**

- **B, ¿es un estudio de usuario formal?** El guion usa explícitamente
  "devolución cualitativa", no se habla de encuestas ni métricas.
- **D, ¿la extensión a otras facultades está diseñada o es una idea suelta?**
  El bullet dice "plantearon extender", tiempo condicional, no funcionalidad
  entregada.
- **E, ¿cómo se relaciona con la latencia de infraestructura?** Frase de
  arranque del guion.

**Solo en el Q&A:**

- **A, ¿el sistema sigue funcionando hoy?** Respuesta lista en `03`, el VPS
  era temporal, el código está versionado.
- **C, ¿esta validación es representativa?** La lámina ya dice "cualitativa",
  la respuesta de que no busca representatividad estadística está lista si
  insisten.
- **C (de infraestructura), sobre seguridad del despliegue.** Si preguntan
  por hardening más allá de lo que dice el informe (aislamiento de red, TLS),
  se puede mencionar oralmente el trabajo de hardening adicional (SSH,
  Fail2Ban, intentos bloqueados) aclarando que es conocimiento operativo del
  equipo, no contenido del informe.
