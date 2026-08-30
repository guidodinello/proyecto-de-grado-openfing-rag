# Cambios aplicados — sesión 1 (2026-08-27)

Correcciones mecánicas de los comentarios de tutores. **Falta compilar en Overleaf para verificar.**
Referencias cruzadas: `checklist-correcciones-tutores.md`, `analisis-esfuerzo-correcciones.md`.

L = Luis · T = Libertad · `p.N` = página del PDF de comentarios.

## Aplicados (19)

| # | Coment. | Archivo:línea | Antes → Después |
|---|---|---|---|
| 1 | L p.38 | `Nuestro/Capitulos/3-RequisitosDelSistema.tex:114` | "estadísticas objetivas que **señalizan** cuán **cercano es** una transcripción" → "que **indican** cuán **cercana es** una transcripción" |
| 2 | L p.38 | `Nuestro/Capitulos/3-RequisitosDelSistema.tex:138` | `\cite{Morris2004}` movido: estaba suelto tras la fórmula de MER, ahora va al final de la frase de definición ("…eliminaciones e inserciones `\cite{Morris2004}`.") |
| 3 | L p.40 | `Nuestro/Capitulos/3-RequisitosDelSistema.tex:187` | "reuniones con la **UEFI( Unidad**" → "**UEFI (Unidad**" |
| 4 | L p.40 | `Nuestro/Capitulos/3-RequisitosDelSistema.tex:193` | "Por lo tanto**,se** debe" → "Por lo tanto**, se** debe" |
| 5 | L p.20 | `referencias.bib:163` (entrada `RussellNorvig2020`) | `author = "{Stuart J. Russell and Peter Norvig}"` → `author = "Russell, Stuart J. and Norvig, Peter"`. Con natbib+apalike la cita pasa a imprimir **(Russell and Norvig, 2020)** en vez del nombre completo. **Verificar el render en Overleaf.** |
| 6 | L p.22 | `Nuestro/Capitulos/2-MarcoTeorico.tex:56` | "fue introducida **por Vaswani et al.** `\cite{vaswani2017attention}`" → "fue introducida **en** `\cite{vaswani2017attention}`" |
| 7 | T p.22 | `Nuestro/Capitulos/2-MarcoTeorico.tex:50` | "ajuste iterativo de **pesos matemáticos**" → "**pesos en funciones matemáticas**" |
| 8 | L p.48 | `Nuestro/Capitulos/4-Arquitectura.tex:86` | comillas rectas → LaTeX: `` ``ruido'' ``, `` ``¿Por qué?'' ``, `` ``¿Algún ejemplo?'' `` |
| 9 | L p.46 | `Nuestro/Capitulos/4-Arquitectura.tex:52` | agregada frase: "El texto completo de este prompt se detalla en el `\autoref{section:A-1-prompt-transcripcion}`." (el label ya existía en `1-Prompting.tex:48`) |
| 10 | L p.49 | `Nuestro/Anexos/1-Prompting.tex:7` + `Nuestro/Capitulos/4-Arquitectura.tex:100` | agregado `\label{section:A-1-prompt-asistente}` a la sección "Prompt del asistente educativo" y referencia en la subsección "Construcción del prompt": "…primero el *system prompt* del asistente educativo (`\autoref{section:A-1-prompt-asistente}`), luego…" |
| 11 | L p.68 | `Nuestro/Capitulos/6-Experimentacion.tex:36` | "las primeras clases del curso de Computación 1 **posee**" → "**poseen**" |
| 12 | L p.74 | `Nuestro/Capitulos/6-Experimentacion.tex:178` | "más detalles que en la **tabla,(respuesta, contexto, etc)**." → "en la **tabla (respuesta, contexto, etc.)**." |
| 13 | L p.78 | `Nuestro/Capitulos/6-Experimentacion.tex:310` | "el precio a la fecha de **consulta(30** de mayo de 2026)" → "fecha de **consulta (30** de mayo de 2026)" |
| 14 | L p.82 | `Nuestro/Capitulos/6-Experimentacion.tex:359` | "un **poster** presentado por el grupo **Ingenieria** de Muestra." → "un **póster** presentado por el grupo **en Ingeniería** de Muestra." |
| 15 | L p.83 | `Nuestro/Capitulos/7-Conclusiones.tex:4` | "…el tiempo que demanda el preprocesamiento de las clases **no es un impedimento**." → "**no son un impedimento**." (sujeto compuesto: volumen + cómputo + tiempo) |
| 16 | L p.85 | `Nuestro/Capitulos/7-Conclusiones.tex:26` | "…de manera online**. Desarrollando** herramientas similares a OpenFing." → "…de manera online**, desarrollando** herramientas similares a OpenFing." (+ doble espacio quitado, "UDELAR" → "UdelaR") |
| 17 | L p.84 | `Nuestro/Capitulos/7-Conclusiones.tex:18` | "El proyecto **valida** que las barreras… **abriendo posibilidades**" → "El proyecto **muestra** que las barreras… **lo que abre posibilidades**" |
| 18 | T p.84 | `Nuestro/Capitulos/7-Conclusiones.tex:18` | "herramientas educativas basadas en IA" → "herramientas educativas **de tipo `\acrshort{rag}`** basadas en IA" |
| 19 | L p.1 | `main.tex:57`, `main.tex:235`, `Nuestro/Otros_Documentos/Estructura.tex:27,64` | "**Tansinni**" → "**Tansini**" (según indicación de Luis, apellido sin doble n) |

## Notas de verificación en Overleaf

- **#5** es el más importante de revisar: confirmar que la cita a Russell & Norvig ahora sale como "(Russell and Norvig, 2020)" y que no aparezca invertida ni rota en la bibliografía.
- **#9 y #10**: confirmar que los `\autoref` resuelven bien (nº de sección y no `??`).
- Compilación local en esta máquina no fue posible: falta el paquete `apacite.sty`.

## Pendiente para la próxima sesión

### Necesitan mirar el PDF de Luis al lado (anchors de una sola palabra, no ubicables por grep)
- L p.82 — "hubo", "prototipo", ", el", "." (varias marcas de puntuación/redacción en la zona de conclusiones, `7-Conclusiones.tex:4-14`).

### Necesitan decisión o redacción
- L p.48 — "esta no va": recortar parte de la frase del "ruido visual" en `4-Arquitectura.tex:86`.
- L p.51 — "cinco": verificar contra el dato real a qué número apunta (`7-Conclusiones.tex:6` "menos de cinco errores" o un conteo de componentes).
- L p.68 — notas al pie dentro de tablas que no renderizan (`6-Experimentacion.tex:23-33`): usar `tablefootnote` / `\footnotemark`+`\footnotetext`.
- L p.68 — expandir "PLN": ya está definido en `2-MarcoTeorico:41` y reexpandido en `6-Exp:113`; el único roce son las etiquetas `PLN-1/PLN-2` de la tabla (`6-Exp:85,93`). Decidir si se toca.
- L p.73/74 — inconsistencia **24 vs 16 preguntas**: aclarar "preguntas únicas" vs "consultas evaluadas" y uniformar todo el Cap. 6.
- L p.79 — Tabla 6.4 + 6.5 son dos `\caption` de una sola tabla (`6-Exp:265` y `6-Exp:303`): unificar en un solo caption.
- L p.80 — cross-refs "sección 6.6": revisar que los `\autoref` a la experiencia de IdeM apunten a `\section{Experiencia en Ingeniería de Muestra}` (`6-Exp:346`) y no solo al anexo (`6-Exp:333` y cercanos).
- L p.85 — "garantizaría" (`7-Conclusiones.tex:28`): reescribir la oración "Por lo que permitir segmentar… se garantiza que…", está mal construida.
- L p.86 — ⚠️ **error conceptual** sobre similitud semántica de embeddings (`7-Conclusiones.tex:30`, párrafo de Re-Ranking). Ver detalle en `checklist-correcciones-tutores.md`.
- L p.86 — sugerencia de fine-tuning con corpus de preguntas (párrafo nuevo en Trabajo a Futuro).
- L p.93 — renombrar Anexo IdeM a "Póster utilizado en Ingeniería de Muestra" y ajustar `\autoref` que lo citan.
- L p.99 — Anexo de Estimaciones no está referenciado desde el cuerpo compilado (solo desde `8-Conclusiones.tex`, que no compila). Agregar `\autoref{Estimaciones de lo que significaría para OpenFing}` en `7-Conclusiones.tex` y/o Cap. 3.

### Bloque "ref" de Libertad (juntar todas las fuentes de una)
- T p.15 — 4 "ref" + "ref, pie de página" (`1-Introduccion.tex:4,6`): alucinaciones, riesgo educativo, OpenFing.
- T p.16 — "ref" ASR (`1-Introduccion.tex:22`) + "(ASR por sus siglas en inglés)".
- T p.15 — "(RAG por sus siglas en inglés)" en la primera expansión.
- T p.34 — "ref" en FAISS, pgvector, Elasticsearch, "API REST" (`3-RequisitosDelSistema.tex` lista de tecnologías, líneas ~24-33).

### Contenido nuevo
- T p.9 — reordenar Resumen antes del índice + ampliarlo (datos del corpus + IdeM 2025). `main.tex:231` / `0-Resumen.tex`.
- T p.6 — crear anexo de planificación (Gantt inicial/final, % dedicación, horas, demoras).
- T p.43 — agrandar Figura 4.1 (`4-Arquitectura.tex:9`).
- T p.79 — achicar letra de la tabla de modelos.
- T p.19/27/37/40 — dudas de redacción ("¿específicamente?", "¿deseable?", "¿ya que?", "¿refinamiento?").
- T p.33 — "para mi no va esta frase" (`3-RequisitosDelSistema.tex:6`, oración con "capitulos" x2 y "y" duplicado).
- T p.83 — añadir referencia a la evidencia cualitativa de IdeM en `7-Conclusiones.tex:8`.

### Limpieza estructural
- Borrar / marcar obsoletos `Nuestro/Capitulos/8-Conclusiones.tex` y `Nuestro/Capitulos/7-TrabajoAFuturo.tex` (no compilan, duplican contenido; el error conceptual de p.86 está triplicado).
- `7-Conclusiones.tex:2` usa `\label{chapter:8-Conclusiones}` y `7-Conclusiones.tex:21` usa `\label{chapter:7-Trabajo a futuro}` (labels con numeración cruzada).
- Unificar sigla UEFI / URI y su expansión (hoy: "Unidad de Enseñanza…", "Unidad de Repositorios Institucionales", "Unidad de Recursos Informáticos").
