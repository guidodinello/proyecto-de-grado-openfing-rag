# Lectura final antes de mandar a los tutores (1/9/2026)

Objetivo: leer el informe completo con los dos PDF de comentarios al lado y confirmar que
nada quedó afuera. Después mandar a Luis y Libertad.

## Documentos de apoyo para la lectura

 
- `mine/comments/checklist-correcciones-tutores.md` — sección "⭐ ESTADO FINAL" + tabla por comentario.
- `mine/reviews/review-independiente-correcciones-tutores.md` — tabla comentario → estado con la
  cita textual de lo que quedó en la versión final. Sirve para ir tildando contra los PDF.

## Chequeos concretos sobre el PDF compilado (recomendación del reviewer)

1. **`\autoref` a anexos sin `??`** — verificar en el PDF final que resuelvan bien las referencias a:
   - Anexo de planificación (`\autoref{chapter:A-Planificacion}`)
   - Prompt de transcripción (`\autoref{section:A-1-prompt-transcripcion}`)
   - Prompt del asistente (`\autoref{section:A-1-prompt-asistente}`)
   - Anexo de estimaciones (`\autoref{chapter:A-2-Estimaciones Para Open Fing}`)
   (en el PDF que auditó el reviewer resolvían bien, pero conviene reconfirmar tras los últimos cambios)

2. **Anexo E — ancho de las dos tablas** — confirmar que las tablas de `5-Planificacion.tex`
   (cronograma plan vs real, y % por tarea macro) entren en el ancho de página sin `Overfull`.
   Se ajustaron con `\small` + `\tabcolsep` reducido; el margen real de la clase `prgrado` solo
   lo confirma la compilación en Overleaf. Mirar que no se corten columnas ni se desborden.

3. **Compilar una última vez en Overleaf** antes de mandar, y revisar el log:
   0 errores; los warnings conocidos (inputenc ignorado, `h`→`ht`, overfull del título en portada,
   underfull en Marco Teórico L151) son pre-existentes y no bloquean.

## Pendientes reales antes del envío

- Ninguno de contenido. Ronda de correcciones cerrada (69/69).
- Solo la lectura final + los 3 chequeos de arriba.

## Al mandar

- Pedir a Claude una última verificación del zip contra el repo (diff) antes del envío.
- Mandar por WhatsApp y/o mail a Luis y Libertad. Deadline: martes 1/9.
- Defensa: jueves 17/9 18:30, salón 701. Tribunal: Guillermo Moncecchi, Raquel Sosa, Ignacio Sastre.
