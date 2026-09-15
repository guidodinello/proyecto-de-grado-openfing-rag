# Propuesta A — "Despliegue y Validación"

**Enfoque:** arquitectura primero. La lámina lidera con la arquitectura técnica
del despliegue (contenedores, aislamiento de red, TLS, el dato de seguridad) y
cierra con la validación de Ingeniería de Muestra como bloque más chico al
final. Pensada para transmitir rigor de ingeniería antes de pasar a lo humano.

**Tiempo objetivo:** 2 minutos.

No repite latencia (mediana 5,4 s, cold start) ni la comparación self-hosting
vs. servicio, ambas ya cerradas en la diapo 19.

---

## Título

**Despliegue y Validación**

Bajada en tipografía menor:
Arquitectura de producción y validación con usuarios reales

---

## Bullets (texto para pegar en Slides)

- El sistema se desplegó en un servidor virtual de Mi Nube ANTEL, cedido sin
  costo como apoyo institucional, y estuvo accesible públicamente durante el
  período de evaluación.

- Todos los servicios se containerizaron con Docker y se orquestaron con
  Docker Compose. Nginx opera como único punto de entrada, con terminación TLS
  mediante certificados de Let's Encrypt.

- La base de datos nunca se expone a internet. El tráfico externo y el acceso
  a PostgreSQL viajan por redes internas separadas de Docker, solo el backend
  puede conectarse a la base.

- Durante el período de despliegue se registraron más de 533.000 intentos de
  conexión SSH bloqueados, sin ningún incidente de seguridad.

- El despliegue se validó de forma cualitativa en Ingeniería de Muestra, con
  devolución de estudiantes, docentes y actores académicos de la FING.

---

## Visual sugerido

**Diagrama de arquitectura simple** (2/3 superiores de la diapo), cajas y
flechas, no un diagrama de red exhaustivo:

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

Todo el bloque de Backend + Frontend + PostgreSQL encerrado en un rectángulo
punteado etiquetado "Docker Compose", para comunicar que es un stack
containerizado de punta a punta.

Al costado o debajo del diagrama, un recuadro chico de acento (mismo estilo
que el número ancla de la diapo de costos) con el dato de seguridad:

> ## 533.000+
> ### intentos de SSH bloqueados, 0 incidentes

**Bloque inferior, más chico** (1/3 de la diapo): dos íconos o bullets cortos
para Ingeniería de Muestra, sin gráfico, es contenido cualitativo:

- Estudiantes del interior → equidad educativa
- Estudiantes de otras facultades de UdelaR → alcance institucional

---

## Notas del orador (guion, 2 minutos)

"Además de los experimentos de laboratorio, desplegamos el sistema en un
entorno real. Antel nos cedió un servidor virtual sin costo, como apoyo
institucional, y el sistema estuvo público durante el período de evaluación."

"Todo corre containerizado con Docker. Nginx es el único punto de entrada,
con TLS de Let's Encrypt, y la base de datos nunca se expone a internet, solo
el backend puede conectarse a ella por una red interna separada."

"Exponer un sistema con datos de estudiantes a internet real implica
responsabilidad. Durante el período de despliegue bloqueamos más de
quinientos mil intentos de conexión SSH de atacantes automatizados, sin
ningún incidente."

"Este mismo despliegue nos permitió una validación distinta a las métricas de
laboratorio, mostramos el prototipo en Ingeniería de Muestra y recibimos
devolución cualitativa de estudiantes, docentes y actores académicos. Dos
perspectivas se repitieron, estudiantes del interior del país, para quienes
la herramienta es un recurso de equidad educativa, y estudiantes de otras
facultades de la universidad, que verían valor en extenderla más allá de
FING."

"Este despliegue es también la fuente de los datos de latencia en producción
que vimos antes."

---

## Cobertura de las preguntas del archivo 03

**Cubiertas en pantalla o en el guion:**

- **C, por qué importa el dato de SSH.** Es el visual de acento central de la
  mitad superior, y el guion lo conecta explícitamente a la responsabilidad de
  exponer datos de estudiantes.
- **E, relación con la latencia de la diapo 19.** Última frase del guion,
  cierre explícito.

**Solo en Q&A:**

- **A, si el sistema sigue funcionando hoy.** No entra en la lámina, la
  bajada dice "producción" en tiempo pasado implícito, pero no aclara que se
  dio de baja. Respuesta lista en 03 si preguntan.
- **B, tipo de validación.** El bullet dice "cualitativa" explícitamente, lo
  cual cubre parcialmente la objeción, pero el detalle de que no es un
  estudio formal con métricas queda para el Q&A.
- **D, si la extensión a otras facultades está diseñada o es una idea suelta.**
  El bullet final del diagrama la presenta como hallazgo de la validación, no
  como funcionalidad. El detalle de que requeriría filtrado por facultad
  queda para el Q&A.
