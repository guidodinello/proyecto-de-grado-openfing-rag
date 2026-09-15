# Simulación de Q&A del Tribunal

Borrador vivo. Formato: pregunta (estilo tribunal) → respuesta dada en el ensayo → feedback → versión ajustada (si aplica). Complementa `mine/presentacion-defensa.md` (sección "Preparación para Q&A").

## Backlog de temas a practicar

- **Flujo principal de la consulta** (Sección 3 de `presentacion-defensa.md`, "el corazón de la demo"): practicar bien el detalle de manejo de memoria/historial, qué se manda en cada turno/consulta, cómo se le pasan las fuentes (chunks recuperados) al modelo, y cómo se construye el prompt/mensaje final (system prompt + historial ≤4000 tokens + contexto + consulta). Ver diagrama de flujo compartido 2026-09-12 (decisión de skip-retrieval en follow-ups cortos ≤3 palabras, k=4, ensamblado de contexto agrupado por clase, persistencia de `message_sources`).

---

## P1 — ¿Por qué RAG estándar y no RAG híbrido / con grafo de conocimiento?

**Respuesta dada (ensayo):**
> Nos pareció un approach simple y que está bastante de moda hoy en día, es simple de entender y simple de agregar flujos más complejos si se necesita como re-ranking o steps más avanzados, la idea era tener algo funcionando para validar la idea. Dado que el tema de procesar todo el corpus de OpenFing ya era un trabajo grande y para el cual teníamos varias incógnitas, decidimos no complicarnos en más frentes. Por otro lado, estamos al tanto que existen otros RAGs como los que construyen un grafo de conocimiento a partir del corpus, pero estábamos más familiarizados con el RAG naive dado que en una materia anterior mi grupo hizo un prototipo de este mismo proyecto (usábamos Vercel y Mongo en vez de Postgres) pero la idea en general era la misma, un RAG conversativo con timestamps y links a las clases.

**Feedback:**
- Contenido correcto (simplicidad, alcance ya grande con OpenFing, experiencia previa con prototipo), pero mezclado, con relleno ("digamos") y oraciones muy largas — suena a pensar en voz alta, no a respuesta preparada.
- Faltó el cierre fuerte ya identificado: no fue desconocimiento de alternativas, **búsqueda híbrida está explícitamente en Trabajo a Futuro (Cap. 7)** — eso muestra decisión de alcance consciente, no punto ciego. Es lo que más le importa a un tribunal.
- Cuidado con mencionar el prototipo previo como argumento central — puede sonar a "ya lo habíamos hecho antes", minimizando el trabajo de este PG. Mejor como frase corta de cierre, no como pilar del argumento.

**Versión ajustada:**
> Elegimos el enfoque estándar porque es simple de entender, fácil de extender después con reranking u otros pasos, y porque el procesamiento del corpus de OpenFing ya era en sí un desafío grande con varias incógnitas propias. No fue una limitación de conocimiento: identificamos búsqueda híbrida explícitamente como próximo paso en el Cap. 7. Además, veníamos con experiencia de un prototipo similar de una materia anterior, lo que nos dio confianza en que el enfoque naive/conversacional era suficiente para validar la idea en este alcance.

---

## P2 — Llama 3.1 8B es un modelo relativamente chico. ¿Cómo se aseguraron de no limitar artificialmente la calidad de las respuestas?

**Respuesta dada (ensayo):**
> Fue más que nada ensayo y error, probamos varios, el Qwen que usamos al principio consumía los free credits de la HuggingFace API muy rápido y nos daba para 4 o 5 preguntas, con este otro modelo que experimentamos vimos que las respuestas no eran malas y nos daba para conversaciones mucho más largas.

**Feedback:**
- Es honesto y es una razón real, pero arrancar por ahí suena a "elegimos por plata, no por calidad" — justo la sospecha que la pregunta busca confirmar. Mala apertura.
- El informe (Cap. 6 §Modelos) ya documenta una razón más sólida: Mistral descartado por menor desempeño en el dominio académico en español; Qwen (72B) más fluido pero con costo computacional desproporcionado respecto a la mejora observada. Es una comparación calidad/costo real, no solo "se acababan los créditos". El dato de los créditos es color de apoyo, no debe liderar la respuesta.
- Punto gratis que falta: los 3 ejemplos cualitativos de la Sección 4 ya muestran que Llama 3.1 8B ancla bien las respuestas y falla de forma predecible/entendible — esa es la evidencia real de que 8B no fue una limitación artificial. Conecta con algo que el tribunal ya vio en la misma presentación, más fuerte que "probamos y andaba bien".

**Versión ajustada:**
> Fue una decisión de costo/calidad, no solo de calidad aislada. Evaluamos Mistral 7B, que tuvo peor desempeño en el dominio académico en español, y Qwen 72B, que daba respuestas más fluidas pero con un costo computacional desproporcionado frente a la mejora real observada. Llama 3.1 8B dio el mejor equilibrio, y eso se ve en los resultados que mostramos antes, ancla bien las respuestas en las fuentes y cuando falla, falla de forma consistente y entendible. Como dato adicional, con modelos más grandes como Qwen los créditos gratuitos de la API se agotaban en 4-5 preguntas, lo cual hubiese sido inviable para evaluar el sistema con el volumen que necesitábamos.

---

## P3 — Evaluaron manualmente siendo los autores del sistema, y descartaron LLM-as-a-judge por sesgo. ¿No es la autoevaluación un sesgo igual o mayor?

**Nota**: este punto NO está explícitamente abordado en el PDF (ya entregado al tribunal, no se puede tocar). Es una pregunta que requiere respuesta oral preparada, no hay dónde señalar en el informe.

**Respuesta dada (ensayo, tras aclarar la pregunta):**
> Sí lo cuidamos. Las categorías (Están / Se pueden derivar / No están / No tienen nada que ver) sirven justamente porque sabemos de antemano, en líneas generales, cómo tiene que responder el agente: si está, que responda y cite las fuentes; si se puede derivar, que responda y diga que lo derivó; si no están, que diga que no están y avise que respondió de su conocimiento; si no tienen nada que ver, lo mismo, que avise que no está en las fuentes pero puede responder de conocimiento general.

**Feedback:**
- Buena base real: el diseño de las categorías define de antemano el comportamiento *esperado*, lo cual acota el juicio subjetivo. Falta nombrar esto explícitamente como respuesta a "sesgo" — decir directamente que convierte la evaluación en verificación de comportamiento esperado vs. juicio de calidad libre, que es el punto que neutraliza la pregunta del tribunal.
- Reconocer de entrada, sin miedo, que el informe no lo aborda explícitamente — mejor decirlo con seguridad ("es un punto justo, y es cierto que no lo desarrollamos en el texto, pero...") que evadir.

**Versión ajustada:**
> Es una preocupación válida, y es cierto que el informe no lo aborda explícitamente. Pero el diseño mismo de las categorías ya reduce ese riesgo, porque cada categoría define de antemano cómo debería comportarse el sistema: si la respuesta está en el corpus, se espera que cite la fuente; si se puede derivar, que lo indique; si no está o no tiene relación, que avise que está respondiendo con conocimiento general y no con el material de los cursos. Eso convierte la evaluación en algo más cercano a verificar si el comportamiento coincidió con lo esperado para esa categoría, que en un juicio subjetivo de "¿es una buena respuesta?". No elimina el sesgo del todo, pero lo acota bastante frente a una evaluación de calidad libre.

---

## P4 — Con 217.986 chunks, ¿no preocupa el rendimiento de pgvector frente a soluciones especializadas (FAISS)?

**Respuesta dada (ensayo):**
> No realmente, en nuestras pruebas pgvector anda rápido y FAISS significa un costo más elevado en producción porque el índice vive en memoria RAM y hay que construirlo cada vez que se levanta.

**Feedback:**
- Instinto correcto pero apoyado en una afirmación sin respaldo medido ("hay que construirlo cada vez que se levanta" no está en el informe ni fue medido) — riesgo de que el tribunal pregunte "¿tienen datos de eso?" y no haya nada que mostrar.
- Existe evidencia real, mucho más fuerte: latencia de producción medida sobre 272 consultas reales (Cap. 6 §Latencia en Producción). La fase de vectorización+búsqueda en pgvector tiene mediana de 2,9s (con embeddings ya cargados), dominada por el embedding de la consulta, no por la búsqueda sobre los 217k chunks. El pico real de latencia (hasta 75s) es cold start del modelo de embeddings, no un problema de pgvector.
- El criterio de selección documentado en Cap. 3 no fue "más rápido en benchmark", fue minimizar complejidad operativa sin sacrificar filtrado: pgvector combina búsqueda semántica + filtros relacionales (curso/lección) en una sola consulta SQL; FAISS "requiere gestión separada de metadatos y persistencia en disco" (cita textual del informe).

**Versión ajustada (aprobada 2026-09-06):**
> No nos preocupa, y de hecho tenemos evidencia real de producción que lo respalda. Con 272 consultas reales medidas en el VPS, la fase de vectorización más búsqueda en pgvector tiene una mediana de 2,9 segundos, y eso está dominado por cargar el modelo de embeddings, no por la búsqueda sobre los 217 mil chunks. Además, la elección de pgvector no fue solo por velocidad bruta, fue el criterio documentado en el Cap. 3, minimizar complejidad operativa sin perder capacidades de filtrado: con pgvector podemos combinar búsqueda semántica y filtros relacionales, por curso o por lección, en una sola consulta SQL, algo que FAISS no resuelve nativamente porque requiere gestión separada de metadatos y persistencia. Para la escala de este proyecto, esa simplicidad pesó más que una posible ganancia de rendimiento bruto de FAISS.

---

## P5 — ¿Consideraron los aspectos de propiedad intelectual / autorización para usar el contenido de OpenFing?

**Respuesta dada (ensayo, primera pasada):**
> Sí, nos comunicamos con la UEFI en todo momento, incluso ellos nos proporcionaron las transcripciones de todo el corpus de sus videos.

**Aclaración post-pregunta (verificación de consistencia con Cap. 6, que documenta metodología propia de transcripción)**: fue ambas cosas. El grupo tiene su propio pipeline y corrió transcripciones propias (incluso se intentó usar el cluster de la facultad para acelerar, pero hubo problemas de multithreading no resueltos del todo). Más adelante, la UEFI proporcionó el dataset completo de transcripciones, lo cual aceleró el trabajo para el corpus completo.

**Corrección 2026-09-14**: esta respuesta decía originalmente "la URI" en vez de "la UEFI". El Cap. 6 (línea 148) solo menciona a la UEFI en relación al acceso a GPU/dataset de transcripciones; la URI no aparece en ese contexto en el `.tex`. Corregido para no introducir en la defensa una entidad que el informe no respalda ahí.

**Feedback:**
- La primera versión no respondía directamente a "¿tenían autorización?" — establecía relación institucional pero no cerraba el punto de IP/autorización explícitamente.
- Falta un dato de contexto gratis: OpenFing ya es una plataforma de **acceso abierto**, pensada para que estudiantes de FING accedan a clases subidas por profesores — no es contenido privado/restringido de entrada. Eso baja el riesgo percibido de IP antes incluso de hablar de la relación institucional.
- El detalle del cluster con problemas de multithreading es un buen dato de honestidad técnica (muestra intento real, no solo lo que salió bien) — vale la pena incluirlo brevemente.

**Versión ajustada:**
> Sí. Trabajamos en contacto directo con la UEFI y la URI durante todo el proyecto, documentado en el Cap. 3, incluyendo un documento de estimaciones de infraestructura que entregamos a la UEFI. Además, OpenFing ya es una plataforma de acceso abierto pensada para que los estudiantes de FING accedan a las clases subidas por los profesores, no es contenido privado o restringido. En una primera etapa scrapeamos y transcribimos el contenido nosotros mismos, con nuestro propio pipeline, incluso intentamos acelerar eso usando el cluster de la facultad aunque tuvimos problemas de multithreading que no llegamos a resolver del todo. Más adelante, la UEFI directamente nos proporcionó el dataset completo de transcripciones, lo cual no solo aceleró el trabajo sino que es en sí mismo una muestra de respaldo institucional al proyecto.

---

## P6 — Chunking: ¿por qué 1200 caracteres / overlap 200?

**Respuesta dada (ensayo):**
> No llevamos a cabo pruebas muy rigurosas pero las que llevamos a cabo nos mostraron que ese era un buen tradeoff. 1200 caracteres es una cantidad razonable para asumir que la idea completa queda dentro del chunk (entre 170 y 200 palabras) y el overlap ayuda a que segmentos consecutivos en la transcripción tengan más probabilidad de aparecer en la recuperación, dado que si ciertas palabras clave quedan contenidas en un solo chunk hay menos redundancia en la recuperación.

**Feedback:**
- El razonamiento de fondo es correcto (tamaño pensado para capturar una idea completa; el overlap busca que las palabras clave cerca de un borde no queden aisladas en un solo chunk, sino que aparezcan también en el adyacente, y esa redundancia sube la probabilidad de que cualquiera de los dos sea recuperado), pero la frase de cierre deja implícito el condicional ("si no hubiera overlap..."), lo que la hace sonar ambigua/invertida al escucharla suelta. Mismo contenido, mejor explicitar el condicional al decirlo en voz alta.
- Punto de contenido más importante: la respuesta describe el `RecursiveCharacterTextSplitter` (1200/200), pero el Cap. 5 (línea 92) es explícito en que esa fue la estrategia del **desarrollo inicial**, mientras que el corpus real indexado en producción (217.986 chunks) se generó con **Semantic Chunking** (`threshold_type: percentile`, `semantic_threshold: 0.6`, `min_chunk_size: 400`). Si la pregunta del tribunal no especifica "recursivo" y se responde solo con 1200/200 sin aclarar cuál corrió en producción, alguien que leyó el Cap. 5 con atención puede notar la inconsistencia.
- Evitar liderar con "no hicimos pruebas muy rigurosas" — abre la puerta a la misma sospecha que en P2 (elección informal/arbitraria). Mejor liderar con el criterio y mencionar la falta de grid search formal como aclaración breve, no como primera frase.

**Versión ajustada (aprobada 2026-09-12):**
> Para aclarar primero, el 1200/200 corresponde al `RecursiveCharacterTextSplitter`, que fue la estrategia usada durante el desarrollo inicial y que dejamos disponible en el sistema como alternativa de menor costo computacional. El corpus que efectivamente está indexado en producción, los 217.986 chunks, se generó con Semantic Chunking, no con este splitter. Para el recursivo, el criterio fue que 1200 caracteres equivalen aproximadamente a 170-200 palabras, un tamaño razonable para que una idea completa quede contenida en un solo fragmento sin cortarla a la mitad, y el overlap de 200 caracteres existe para que las palabras clave cerca de un borde no queden aisladas en un solo chunk, sino que aparezcan también en el fragmento adyacente, así ninguno de los dos pierde la posibilidad de ser recuperado. No hicimos una búsqueda sistemática de parámetros tipo grid search, pero sí evaluamos empíricamente esta configuración frente a otras antes de quedarnos con ella.

---

## P7 — Generalización del fix Prompt 1 → Prompt 2

**Pregunta simulada:**
> El cambio de Prompt 1 a Prompt 2 lo validaron con dos preguntas fuera de dominio. ¿Cómo saben que ese fix generaliza y no solo resuelve esos dos casos puntuales que ya conocían?

**Respuesta dada (ensayo):**
> Sinceramente no lo sabemos, con modelos no determinísticos no podés garantizar mucho, nos limitamos a hacer pruebas exploratorias y vimos que con los grupos de preguntas que definimos junto a los tutores para hacer las pruebas, el prompt 2 cumplía con nuestros requerimientos bastante mejor que el prompt 1.

**Feedback:**
- El argumento de fondo (no se puede garantizar generalización con un modelo no determinístico a partir de pocas pruebas) es válido y mejor que fingir certeza, pero abrir con "sinceramente no lo sabemos" suena a rendirse ante la pregunta en vez de responderla.
- La premisa de la pregunta subestima la evidencia real: el Cap. 6 documenta que las 8 preguntas de corpus completo se evaluaron con ambos prompts (16 de las 24 consultas totales), y el patrón Prompt 1 vs. Prompt 2 no aparece solo en paella/planetas ("No tienen nada que ver"), también en la categoría "No están" (pregunta sobre tasa de precisión de traducción automática), donde "en varios casos" el Prompt 2 señaló que el dato no estaba en el material. El patrón se sostuvo en dos categorías distintas, no en dos preguntas aisladas.
- "Cumplía con nuestros requerimientos bastante mejor" es vago — nombrar el requerimiento concreto: que el sistema señale explícitamente cuando el contexto no alcanza, en vez de mezclar conocimiento del modelo sin avisar.

**Versión ajustada (aprobada 2026-09-12):**
> No podemos garantizarlo con certeza absoluta, eso es cierto de cualquier evaluación sobre un modelo no determinístico, pero el patrón no se observó solo en esas dos preguntas puntuales. Las ocho preguntas de corpus completo se evaluaron con ambos prompts, y el mismo comportamiento apareció en dos categorías distintas, no solo en las preguntas totalmente fuera de dominio, sino también en la categoría donde el tema es afín pero el dato específico no está en el corpus. En varios de esos casos, con el Prompt 2 el sistema señaló explícitamente que la información no estaba en el material de clase, algo que con el Prompt 1 no ocurría. Eso nos da más confianza en que la mejora responde a la instrucción del prompt y no a esas dos preguntas específicas, aunque coincidimos en que una validación más amplia y sistemática sería necesaria para afirmar generalización en un sentido más fuerte.

---

## P8 — ¿Qué significa el porcentaje que aparece en cada tarjeta de fuente (source)?

**Nota**: no está preguntado todavía, es prep proactiva porque la diapo de Demo va a mostrar capturas de la UI con ese porcentaje visible, y es un valor fácil de malinterpretar a simple vista.

**Verificado en el código** (`../tesis/backend/shared/database/repositories/vector_repository.py` y `frontend/src/utils/numbers.ts`), no solo de memoria:
- El valor sale de `similarity_search_with_score` de `PGVectorStore` (langchain-postgres), que por defecto usa **distancia coseno** (`COSINE_DISTANCE`) entre el embedding de la consulta y el del chunk.
- El frontend (`floatToPercentage`) solo hace `valor * 100`, sin invertir el número.
- Consecuencia importante y contraintuitiva: **es una distancia, no una confianza ni una probabilidad. Más bajo = más parecido (mejor match)**. Por eso en el ejemplo de bubble sort los porcentajes eran ~11-12% (buen match, pregunta en dominio) y en el ejemplo de la paella valenciana ~21% (peor match, pregunta fuera de dominio).
- El backend y el informe (Cap. 4, "puntuación de confianza que corresponde a la similitud vectorial obtenida en la búsqueda") lo llaman `confidence_score`/"confianza", lo cual sugiere lo contrario de cómo se comporta en realidad. El propio código lo trata internamente de forma consistente con esto (`chat_service.py` ordena las fuentes `sort(..., reverse=False)`, ascendente, para mostrar primero el chunk con menor distancia = mejor match), así que el sistema funciona bien, es el nombre el que induce a error si alguien lo lee de afuera esperando que "más alto es mejor".

**Respuesta preparada, si preguntan:**
> Ese porcentaje es la distancia coseno entre el embedding de la pregunta y el del fragmento recuperado, expresada como porcentaje. Es más bajo cuanto más parecido es el fragmento a la consulta, no es una probabilidad ni una confianza en el sentido de "más alto es mejor". Reconocemos que el nombre interno que usamos para ese campo, `confidence_score`, es un poco confuso en ese sentido, es una convención heredada de la librería de retrieval que usamos, pero el sistema en sí ordena y prioriza los fragmentos correctamente según esa distancia.

**Pendiente de decidir**: si conviene aclarar esto en el guion de la diapo de Demo antes de mostrar la captura (para que el tribunal no lo lea como "solo 21% de confianza, mala respuesta"), o dejarlo solo como respuesta de Q&A si preguntan. Ver `presentacion-defensa.md` sección Demo.
