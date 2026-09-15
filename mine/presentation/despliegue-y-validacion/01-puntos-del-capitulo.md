# ¿Cuáles son los puntos del capítulo?

Fuente: `6-Experimentacion.tex` §6.8 (intro, sin latencia ni self-hosting, ya
usadas en diapo 19) y §6.9. Más contexto técnico de
`mine/data/deployment-minube-antel.md`.

---

## 1. Contexto del despliegue (§6.8, líneas 321-328)

- Sistema desplegado en un entorno real y accesible públicamente, como
  complemento a los experimentos de laboratorio.
- **VPS de Mi Nube ANTEL**, cedido sin costo al proyecto como apoyo
  institucional durante un período acotado.
- Disponible en `openfingchat.duckdns.org`, accesible desde cualquier
  navegador durante el período de evaluación.
- Todos los servicios **containerizados con Docker**, orquestados con
  **Docker Compose**.
- Arquitectura de red, tráfico externo separado del acceso a la base de
  datos mediante redes internas de Docker. **PostgreSQL nunca expuesto al
  exterior**, solo el backend puede conectarse.
- **Nginx** como punto de entrada único, terminación TLS con certificados de
  **Let's Encrypt**, enruta hacia el backend FastAPI y el frontend React.
- El despliegue es una **validación cualitativa en condiciones reales**,
  complementaria a las métricas de evaluación de las secciones anteriores.
  Permitió recoger retroalimentación de usuarios reales, estudiantes de la
  FING y actores académicos.

## 2. Contexto técnico ampliado (no está en el informe con este nivel de
detalle, `mine/data/deployment-minube-antel.md`)

Útil para el guion oral y para el Q&A, no todo entra en la lámina:

- Servicios: backend (FastAPI, Python 3.12 + uv), frontend (React, servido
  por nginx), nginx (proxy reverso + TLS), database (Postgres), certbot
  (emisión y renovación automática de TLS cada 12 h), migration (Alembic,
  one-shot).
- DNS con **DuckDNS** (gratuito).
- Hardening de seguridad, varias capas independientes:
  - SSH en puerto no estándar (2222), solo autenticación por clave ED25519,
    root deshabilitado, `AllowUsers` restringido a un solo usuario.
  - Firewall UFW, política deny-all por defecto, SSH restringido a rangos de
    IP de Antel Uruguay únicamente.
  - Fail2Ban, baneo automático tras 3 intentos fallidos en 10 minutos.
  - **Dato llamativo:** se registraron más de **533.000 intentos de conexión
    SSH** desde atacantes de todo el mundo durante el período de despliegue.
    Ningún incidente exitoso.
- El VPS no se renovó al terminar el período gratuito, todo el código estaba
  en control de versiones, no se perdió nada.

## 3. Experiencia en Ingeniería de Muestra (§6.9, líneas 350-364)

- **10 y 11 de octubre de 2025**, instancia donde se comparten proyectos de
  grado e investigación de la FING. El grupo mostró un prototipo del chatbot
  al público, estudiantes, profesores y actores académicos.
- Permitió recoger perspectivas sobre entusiasmo, alcance, viabilidad e
  impacto potencial del proyecto.
- **Dos perspectivas destacadas por el informe:**
  1. **Estudiantes del interior del país**, que no pueden asistir
     regularmente a la facultad. El proyecto tiene valor como **herramienta
     de equidad educativa**, un chatbot especializado con el material del
     curso puede ser un recurso decisivo para sostener rendimiento académico
     comparable al de pares presenciales.
  2. **Estudiantes de UdelaR de otras facultades**, que a partir de la
     pandemia tienen acceso a clases grabadas de sus propias facultades. La
     herramienta podría extenderse más allá de FING, ampliando el alcance
     institucional. Solo requeriría un filtrado por facultad.
- Hay un póster del grupo presentado en Ingeniería de Muestra, en el Anexo A
  del informe.

## 4. Vínculo con la muestra de latencia (ya usada en diapo 19, no repetir)

La muestra de 272 consultas de latencia (diapo 19) proviene de este mismo
despliegue, 166 de esas 272 se concentran justo en la jornada de Ingeniería
de Muestra. Es el mismo evento visto desde dos ángulos, infraestructura
(latencia) vs. validación con usuarios (feedback cualitativo). Vale la pena
una frase de conexión en el guion, pero no repetir el número de latencia acá.
