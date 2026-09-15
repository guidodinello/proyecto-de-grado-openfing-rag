# Presentación defensa — 17/9/2026

Working doc para el contenido de las diapositivas. **Google Slides es la fuente de
verdad para layout y figuras**; acá trabajamos el texto y el guion, y después se
copia a Slides a mano.

- Deck: `pdfs/Presentacion 17_9 Tesis.pdf` (23 diapos, 16:9)
- Informe completo compilado: `pdfs/Proyecto_de_Grado_INCO_InCo_FIng_UdelaR.pdf`
- Outline de la charla (estructura + timing): `presentacion-defensa.md`
- Q&A simulado: `qa-simulacion-tribunal.md`
- Workflow de preparación de cada diapo: `WORKFLOW.md`

Convención por diapo:
- **Actual** = lo que hay hoy en el deck (verbatim, con sus typos).
- **Propuesta** = redacción sugerida para pegar en Slides.
- **Notas** = guion del orador.
- **TODO** = lo que falta (imagen, dato, decisión).

Estilo: sin em dashes, sin dos puntos como conector (igual que el informe).

---

## 1 — Portada

**Actual:** "Guido Dinello y Diego Amorena"

**TODO:** título del proyecto, tutores (Luis Chiruzzo, Libertad Tansini), FING/UdelaR, fecha.

**Notas:**

---

## 2 — Problema Abordado

**Actual:**
- La falta de una herramienta adaptada y contextualizada a la FING.
- La adopción de los estudiantes de herramientas de LLMs que no son educativos ni están entrenadas con contexto local.
- Lidera a los estudiantes a estudiar a partir de fuentes genéricas que pueden estar equivocadas, sesgadas o con un enfoque diferente a sus cursos.

**TODO:** corregir redacción ("Lidera a" -> "Lleva a"). Acortar a 3 bullets limpios.

**Notas:**

---

## 3 — OpenFING

**Actual:**
- Plataforma de videos educativos abierta con las clases grabadas. Proyecto de Grado de 2011.
- 239 cursos y 4.339 clases.
- Cantidad dinámica: los profesores pueden mostrar u ocultar su contenido.
- También es posible editar los videos una vez subidos.
- Videos hosteados por la URI o por YouTube.

**TODO:** confirmar números contra `../corpus-numeros.md` / informe. El deck dice 239/4339; el informe puede tener otra cifra.

**Notas:**

---

## 4 — UEFI / URI

**Actual:**
- Refinamiento de requisitos técnicos.
- Familiarización con los procesos internos de la URI.
- Estado actual de OpenFING y futuros proyectos.
- Reuniones con la Uefi de ayuda.
- Recabado de cursos clave y requisitos. Experimentación del momento.

**Aclaración (2026-09-13, confirmado por Guido):** no es un error de sigla, son dos entidades distintas y la diapo habla de ambas.
- **UEFI** = Unidad de Enseñanza de la FING.
- **URI** = Unidad de Recursos Informáticos.

**TODO:** el título de la diapo dice solo "UEFI", pero el contenido mezcla interacciones con las dos unidades — conviene que el título o la bajada deje explícito que son dos entidades (ej. "UEFI y URI" o aclarar en el cuerpo qué bullet corresponde a cuál). Redacción telegráfica igual, pasar a prosa de bullet ("Recabado de cursos clave y requisitos. Experimentación del momento." sigue siendo poco claro).

**Notas:**

---

## 5 — Objetivos (funcionales)

**Actual:**
- Desarrollar y validar una herramienta RAG basada en el corpus de OpenFING.
- Chatbot RAG interactivo: responde consultas según el contenido de las clases.
- Trazabilidad de fuentes: curso, lección y minuto exacto del video.
- Transparencia contextual: avisa cuando la respuesta no se basa en el repositorio.
- Pipeline automatizado: scraping, descarga de audio, ASR, vectorización e indexación incremental.
- Panel de administración: estado, progreso y errores del pipeline en tiempo real.

**TODO:** alinear textualmente con los 5 objetivos específicos del Cap. 1 del informe.

**Notas:**

---

## 6 — Objetivos (no funcionales)

**Actual:**
- Código abierto: repositorio público con documentación para despliegue y mantenimiento.
- Extensibilidad: arquitectura modular adaptable a nuevas fuentes (ej. OpenUDELAR).
- Privacidad y autonomía: opción de self-hosting para proteger datos y controlar costos de inferencia.

**Notas:**

---

## 7 — Procesos Seguidos

**Actual:**
- Desarrollo, empezando por una herramienta de scraping de todo OpenFING.
- Evaluación y prueba de distintas herramientas: scraping, descargas, ASR, vectorización, estructura de BD, generación de respuestas.
- Análisis de arquitectura, costos e infraestructura.

**Notas:**

---

## 8 — Variaciones de RAG

**Actual:** Naive RAG (decisión del grupo) / Advanced / Modular RAG.

**TODO:** diagrama de las 3 variantes. Justificar por qué Naive. Ver nota de taxonomía RAG en `../presentacion-defensa.md`.

**Notas:**

---

## 9 — Ingesta: Scraping

**Actual:**
- Scraping con BeautifulSoup.
- Problema: las clases subidas a OpenFING cambian según la altura del semestre.
- Se usa código de curso + código de clase + número de clase.

**TODO:** `[Añadir imagen ejemplo]` del problema de identificadores.

**Notas:**

---

## 10 — Ingesta: Descargas

**Actual:**
- yt-dlp `[arreglar nombre de biblioteca en el deck]`
- Ancho de banda limitado, cuidado de no sobre-exigir a OpenFING, proceso lento, videos hosteados en distintos lugares.

**TODO:** completar bullets vacíos. Dato concreto de volumen/tiempo total de descarga.

**Notas:**

---

## 11 — Ingesta: Transcripción

**Actual:**
- Mayor limitante de tiempo. Mucha investigación sobre cómo acelerar el proceso.
- Bugs en versión GPU; CPU muy lento.
- Validación de estadísticas manual.

**TODO:** esta diapo está duplicada con la 13. Fusionar. Nombrar el modelo (Whisper), tamaño, WER medido, hardware, uso del cluster de facultad y luego dataset provisto por la URI (ver memoria de sesión 2026-09-06).

**Notas:**

---

## 12 — Ingesta: Vectorización

**Actual:** "Calidad vs Velocidad" / "Opciones Multilenguaje vs ..."

**TODO:** completar. Modelo elegido, dimensión, criterio. Ver Cap. 6 del informe.

**Notas:**

---

## 13 — Ingesta: Transcripción (DUPLICADA de 11)

**TODO:** eliminar o fusionar con la 11.

---

## 14 — Base de Datos

**Actual:** pgvector.

**TODO:** por qué pgvector y no FAISS. Argumento: en las pruebas pgvector anda rápido; FAISS = costo mayor en producción porque el índice vive en RAM y hay que reconstruirlo en cada arranque (memoria sesión 2026-09-06). Diagrama del esquema.

**Notas:**

---

## 15 — Modelo (LLM)

**Actual:** Qwen — Hugging Face.

**TODO:** versión y tamaño exacto de Qwen, por qué, requisitos de VRAM. Ver `../detalles-tecnicos-codigo.md`.

**Notas:**

---

## 16 — Experimentación: Modelos de Transcripción

**Actual:** placeholder ("Modelo de Transcripcion.").

**TODO:** escribir de cero. Motivación, modelos comparados, métrica (WER), resultado, decisión. Fuente: Cap. 6 informe.

**Notas:**

---

## 17 — Experimentación: Modelos de Vectorización

**Actual:** placeholder.

**TODO:** escribir de cero. Modelos comparados, métrica, resultado. Fuente: Cap. 6.

**Notas:**

---

## 18 — Experimentación: Modelos de Lenguaje

**Actual:** placeholder.

**TODO:** escribir de cero. Modelos comparados, evaluación (categorías de preguntas / RAGAS o lo que se haya usado), resultado. Fuente: Cap. 6.

**Notas:**

---

## 19 — Análisis de Infraestructura

**Actual:** placeholder.

**Propuesta** (detalle y guion en `analisis-de-infraestructura/propuesta-final.md`):

Título: **Análisis de Infraestructura** · bajada "Viabilidad operativa en costos, latencia y modelo de inferencia".

Bullets:
- El costo de operar el modelo adoptado es de aproximadamente 0,047 USD por cada mil consultas, hasta diez veces menor que el de otros modelos abiertos de mayor tamaño y muy por debajo de los modelos propietarios de frontera. Un semestre de uso intensivo de un curso se sostiene con centavos de dólar.
- La generación de respuestas se delega a un servicio de inferencia gestionada porque el servidor de despliegue no disponía de GPU y el modelo requiere del orden de 16 GB de memoria de video. En CPU la inferencia local llevaba varios minutos por consulta.
- El self-hosting sigue siendo la vía para satisfacer plenamente el requisito de privacidad y autonomía. El modelo adoptado es de pesos abiertos, así que ese cambio no exige rediseñar la arquitectura y queda planteado como trabajo a futuro con hardware dedicado.
- La latencia se midió sobre 272 consultas reales en el servidor de producción, con una mediana de 5,4 segundos de extremo a extremo.
- La dependencia de un proveedor externo se asume como un costo conocido. Cualquier alternativa basada en modelos de pesos abiertos mantiene el gasto en el mismo orden de magnitud.

Visual: gráfico de barras horizontales en escala logarítmica, costo de tokens de entrada por 1.000 consultas para Llama 3.1 8B (0,047), Qwen2.5 72B (0,45), GPT-4.1 (2,36), GPT-5 Pro (17,7). Barra de Llama resaltada, número ancla ≈ 0,047 USD / 1.000 consultas, nota al pie con fecha de tarifas.

Backup slide: tabla de contraste inferencia como servicio vs. self-hosting (hardware, latencia, privacidad, mantenimiento, costo). Se muestra solo si preguntan por el RNF5.

**Notas:** guion de 2-3 min en `analisis-de-infraestructura/propuesta-final.md`.

**Pendiente:** decidir gráfico vs. tabla, armar la figura, pasar a Slides.

---

## 20 — Despliegue y Validación

**Actual:** placeholder.

**TODO:** escribir. Dónde corre, validación con usuarios (si hubo), estado del deploy en la URI.

**Notas:**

---

## 21 — Conclusiones

**Actual:** placeholder.

**TODO:** escribir. Cerrar contra los 6 objetivos de la diapo 5-6. Fuente: Cap. 7 informe.

**Notas:**

---

## 22 — Trabajo a Futuro

**Actual:**
- Transición de conocimiento. Deploy en la URI.
- Integración con más contenido no exclusivo de OpenFING, segmentando por origen.
- Técnicas avanzadas de RAG u otros tipos de RAG, o fine-tuning de modelos.

**Notas:**

---

## 23 — Trabajo a Futuro (cont.)

**Actual:** un bullet vacío.

**TODO:** eliminar o completar.

---

## Pendientes globales

- Slides 16-21 son placeholders, hay que escribirlas de cero desde el Cap. 6/7.
- Diapo 11 y 13 duplicadas.
- Diapo 23 vacía.
- Varias imágenes marcadas como TODO (8, 9, 14).
- Falta demo (checklist en `../presentacion-defensa.md`).
- Pasada de estilo y typos a todo el deck.
- Timing: 23 diapos para ~20-30 min de charla, chequear contra el outline.
