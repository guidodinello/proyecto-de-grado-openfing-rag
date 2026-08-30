# Cambios aplicados — sesión 2 (2026-08-30)

Referencias: `checklist-correcciones-tutores.md`, `cambios-aplicados-sesion1.md`.
L = Luis · T = Libertad · `p.N` = página del PDF de comentarios.

## ⚠️ Regresión detectada

Al verificar el estado real de los `.tex` contra `cambios-aplicados-sesion1.md`, **10 de los 19
cambios de la sesión 1 no estaban en los archivos**. Se perdieron, probablemente pisados por
los commits `73aa5c9` ("last version before comments", 2026-08-27) y `36b3cd6` ("my changes",
2026-08-30).

- **Sobrevivieron**: #1, #2, #4, #6, #7, #8, #5 (bib), #19 (parcial, ver abajo) — Cap. 2, 3, 4 (comillas), bib, main.tex.
- **Se perdieron**: #9, #10 (Cap. 4 autorefs a anexos), #11, #12, #13, #14 (Cap. 6), #15, #16, #17, #18 (Cap. 7).

Todos los perdidos se re-aplicaron en esta sesión (abajo).

## Aplicados

| # | Coment. | Archivo | Antes → Después |
|---|---|---|---|
| 1 | T p.9 | `0-Resumen.tex:5` | "existen falencias en los LLMs populares … que mitigue estas falencias" → "los modelos comerciales funcionan como cajas negras y su uso conlleva ciertos riesgos … que mitigue esos riesgos" |
| 2 | T p.9 | `0-Resumen.tex:9` | "se presenta arquitectura final del sistema como también distintas posibles arquitecturas las cuales se decidieron dejar de lado" → "se presenta la arquitectura final del sistema junto con las alternativas consideradas y los motivos por los que se dejaron de lado" |
| 3 | T p.16 | `1-Introduccion.tex` | "disponible en OpenFing pipeline implementado procesó" → "disponible en OpenFing. El pipeline implementado procesó" (oración mal ensamblada) |
| 4 | T p.33 | `3-RequisitosDelSistema.tex:6` | eliminada la frase "En los capitulos \autoref{...5} y \autoref{...6} y se explican las cuestiones planteadas en este capitulos." (la tutora: "para mi no va esta frase"; además tenía "capitulos" x2 y "y" duplicado) |
| 5 | T p.33 | `3-RequisitosDelSistema.tex:11` | "para fundamentar las decisiones de diseño del sistema" → "para respaldar adecuadamente la toma de decisiones de diseño del sistema" |
| 6 | T p.40 | `3-RequisitosDelSistema.tex:182` | "para el afinamiento de estos requisitos" → "para el refinamiento de estos requisitos" |
| 7 | L p.68 (re-aplic. #11) | `6-Experimentacion.tex:36` | "las primeras clases del curso de Computación 1 posee" → "poseen" |
| 8 | L p.74 (re-aplic. #12) | `6-Experimentacion.tex:178` | "más detalles que en la tabla,(respuesta, contexto, etc)." → "en la tabla (respuesta, contexto, etc.)." |
| 9 | L p.78 (re-aplic. #13) | `6-Experimentacion.tex:310` | "el precio a la fecha de consulta(30 de mayo de 2026)" → "consulta (30 de mayo de 2026)" |
| 10 | L p.82 (re-aplic. #14) | `6-Experimentacion.tex:359` | "un poster presentado por el grupo Ingenieria de Muestra" → "un póster presentado por el grupo en Ingeniería de Muestra" |
| 11 | L p.83 (re-aplic. #15) | `7-Conclusiones.tex:4` | "el tiempo que demanda el preprocesamiento de las clases no es un impedimento" → "no son un impedimento" (sujeto compuesto) |
| 12 | L p.84 + T p.84 (re-aplic. #17/#18) | `7-Conclusiones.tex:18` | "El proyecto valida que las barreras … educativas basadas en \acrshort{ia} … abriendo posibilidades" → "El proyecto muestra que las barreras … educativas de tipo \acrshort{rag} basadas en \acrshort{ia} … lo que abre posibilidades" |
| 13 | L p.85 (re-aplic. #16) | `7-Conclusiones.tex:26` | "de manera online. Desarrollando herramientas similares a OpenFing." → "de manera online, desarrollando herramientas similares a OpenFing." (+ "UDELAR" → "UdelaR", doble espacio) |
| 14 | L p.85 | `7-Conclusiones.tex:24` | "La integración garantizaría la sostenibilidad, estabilidad y el respaldo necesario a largo plazo." → "La integración institucional aporta la sostenibilidad, estabilidad y el respaldo necesario a largo plazo." |
| 15 | L p.85 | `7-Conclusiones.tex:28` | "Por lo que permitir segmentar la información por facultad, se garantiza que el chatbot acceda …" → "Segmentar la información por facultad permite que el chatbot acceda …" (oración mal construida) |
| 16 | L p.46 (re-aplic. #9) | `4-Arquitectura.tex:52` | re-agregada "El texto completo de este prompt se detalla en el \autoref{section:A-1-prompt-transcripcion}." (label ya existía en `1-Prompting.tex:48`) |
| 17 | L p.49 (re-aplic. #10) | `1-Prompting.tex:7` + `4-Arquitectura.tex:100` | re-agregado `\label{section:A-1-prompt-asistente}` a la sección "Prompt del asistente educativo" y `(\autoref{section:A-1-prompt-asistente})` en "Construcción del prompt" |

## Verificación pendiente en Overleaf

- Compilar y confirmar que los `\autoref{section:A-1-prompt-transcripcion}` y
  `\autoref{section:A-1-prompt-asistente}` resuelven (no `??`).
- Confirmar que borrar la frase de `3-RequisitosDelSistema.tex:6` no dejó un salto raro.

| 18 | L p.1 | `main.tex:235`, `Estructura.tex:27,64` | "Tansinni" → "Tansini" (una n, como marcó Luis en su primer comentario). `main.tex:57` ya estaba bien (sesión 1). Ahora unificado. La nota del checklist que decía "el correcto es Tansinni" era un error mío, ya corregida. |

## Sigue pendiente (no mecánico / necesita decisión)

Ver `cambios-aplicados-sesion1.md` sección "Pendiente" y `checklist-correcciones-tutores.md`.
Lo grande: error conceptual p.86 (Re-Ranking), inconsistencia 24 vs 16 preguntas, anexo de
planificación, ampliar el Resumen, refactor Anexo IdeM, citas faltantes de Libertad (p.15/16/34).
