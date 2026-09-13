# Auditoría de Citas — Estadísticas de OpenFing
Fecha: 2026-04-28

## Afirmaciones auditadas

### Ocurrencia 1 — Cap. 2, sección OpenFing (línea 11)
> "Hoy en día, cuenta con más de 5000 horas de video, más de 3000 clases subidas."

**Estado**: Sin `\cite{}` en esa oración. La entrada `\cite{OpenFing}` aparece en la oración anterior ("OpenFing es una plataforma...") y apunta a `https://open.fing.edu.uy/about/`.

### Ocurrencia 2 — Cap. 1, Introducción (línea 21)
> "plataforma que concentra más de 5000 horas de clases grabadas de la FING"

**Estado**: Sin `\cite{}`.

---

## Verificación de la fuente `\cite{OpenFing}`

- **URL**: `https://open.fing.edu.uy/about/`
- **URL resuelta**: sí
- **¿Publica las estadísticas?**: **NO**. La página describe historia, estructura y tecnología, pero no incluye ningún dato cuantitativo sobre horas de video ni cantidad de clases.

## Veredicto: ❌ NOT_FOUND (para las cifras concretas)

**Razonamiento**: Las cifras "más de 5000 horas" y "más de 3000 clases" aparecen sin cita en ambos capítulos. Incluso si se añadiera `\cite{OpenFing}`, la página oficial no contiene esos números, por lo que la cita no respaldaría la afirmación. La fuente no existe de forma verificable en ningún lugar accesible.

---

## Recomendación

**Opción A (preferida)**: Suavizar la afirmación, eliminando las cifras concretas:
> "Hoy en día concentra miles de horas de video y miles de clases, abarcando casi todos los cursos de la institución."

**Opción B**: Buscar si OpenFing publica esas cifras en otro lugar (noticias institucionales, informes anuales de FING/UdelaR, etc.) y añadir la cita correspondiente con fecha de acceso.

**Opción C**: Citar el catálogo directamente y derivar las cifras de lo que el propio sistema procesó (p. ej. en Cap. 6 o el Anexo de estimaciones), mencionando que el conteo proviene del procesamiento propio.
