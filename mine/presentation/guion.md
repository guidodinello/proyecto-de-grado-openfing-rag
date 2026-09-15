# Guion de la defensa — diapos de Guido

Texto que digo en cada diapo (guion oral) y bullets de respaldo. Numeración por
título de diapo, no por número de posición (ver `WORKFLOW.md`, el número se
corre en Slides). Orden de referencia actual, tras mover Arquitectura antes de
las etapas de ingesta:

Naive RAG (Diego) → **Arquitectura** → Ingesta-Scraping → Ingesta-Descargas →
Ingesta-Transcripción → Ingesta-Vectorización → Indexación (nueva) →
Generación → Flujo → ...

---

## Arquitectura

**Bullets (lámina):**
- El sistema se organiza en dos fases: una de ingesta offline, que indexa el
  contenido de OpenFing por adelantado, y otra de consulta en tiempo real, que
  corre ante cada pregunta del estudiante.
- Los módulos de ingesta funcionan de forma asincrónica y desacoplada entre
  sí, coordinados mediante cron jobs y comunicándose únicamente a través de la
  base de datos, no de llamadas directas entre módulos.
- Backend organizado en 5 módulos: Scraper, Descargas, Transcriptor, Generador
  y un módulo transversal Shared (incluye vectorización, configuración y
  modelos de base de datos compartidos).

**Guion (oral):**
Ya vimos en teoría qué es un sistema RAG. En nuestro caso, esto se
traduce en la arquitectura de la figura. Se divide en dos fases, una de
ingesta, que corre offline, de forma asíncrona, para mantener la base
de conocimiento al día, y otra de consulta, que simplemente lee de esa
base de datos ante cada pregunta.

En nuestro sistema, nosotros definimos y diferenciamos 5 módulos o
servicios, el módulo de scrapeo, el de descargas, el de transcripciones,
el de vectorización y el de generación.

Vamos a ir recorriendo cada una de estas etapas en las próximas
diapositivas.

Algo interesante de esta arquitectura es notar lo desacopladas que están
estas fases de ingesta de la de generación, esto permite que el mismo
proyecto pueda ser utilizado, como vamos a ver más adelante con
diferentes bases de conocimiento, como podrían llegar a ser diferentes
facultades.

**Nota 2026-09-15 (decisión explícita del usuario, no un descuido):** el
párrafo del medio nombra los 5 módulos como "scrapeo, descargas,
transcripciones, vectorización y generación", lo cual **no coincide**
con el bullet de esta misma lámina ni con el Cap. 4 (que dice Scraper,
Descargas, Transcriptor, Generador y **Shared**, con vectorización como
subcomponente de Shared, no un módulo propio). Se le señaló la
inconsistencia y decidió dejarlo así de todas formas.

---

## Ingesta de Datos - Scraping

**Bullets (lámina):**
- Scraping con BeautifulSoup, primer paso del pipeline de ingesta: mantiene
  la base de conocimiento al día a medida que se publican nuevas clases en
  OpenFing.
- Las consultas a cada curso se paralelizan con un pool de threads, y la
  sincronización contra la base de datos es idempotente (actualiza cursos y
  clases existentes y agrega los nuevos, sin borrar y recrear todo en cada
  corrida).

**Guion (oral):**
El primer paso del pipeline de ingesta es el scraping. Recorremos OpenFing
con BeautifulSoup para mantener la base de conocimiento al día, a medida
que se van publicando nuevas clases. A nivel técnico, paralelizamos las
consultas a cada curso con un pool de threads, y la sincronización contra
la base de datos es idempotente, cada corrida actualiza lo que ya existe y
agrega lo nuevo, sin borrar y recrear todo desde cero.

**Notas para Q&A (no van en la lámina, no están en el informe):**
- El detalle real de por qué el catálogo cambia (profesores ocultan/muestran
  contenido según el semestre) no está en el `.tex`, solo la idea general de
  "nuevas clases publicadas". Si preguntan por qué el scraping necesita
  reintentos/manejo de errores, ahí se explica el matiz real.

---

## Ingesta de Datos - Descargas

**Bullets (lámina):**
- Descarga el audio con yt-dlp, entrada del módulo de transcripción; evita
  redescargar lo ya existente.
- Plugin propio (OpenFingIE): reutiliza el extractor de YouTube de la
  librería para tratar igual video directo y embed. De yt-dlp:
  postprocesamiento, concurrencia, reintentos y reanudación.

**Guion (oral):**
Una vez que el Scraper identificó las clases, este módulo descarga el
audio con yt-dlp. Si ya está descargado, se salta.

OpenFing hostea sus videos tanto en su propio sitio como en YouTube, y por
eso definimos un plugin, con una clase OpenFingIE que hereda de la clase
abstracta InfoExtractor de yt-dlp. Así le indicamos a la librería cómo
encontrar el link de descarga, y con una interfaz común bajamos la clase
sin importar si el video está servido directamente o embebido desde
YouTube.

Esta librería también nos da gratis otras features, como hooks de
postprocesamiento para descartar la imagen y quedarnos con el audio usando
ffmpeg, descarga de los videos en fragmentos concurrentes, reintentos
automáticos, y reanudación de descargas interrumpidas si se cortan a mitad
de camino.

**Notas para Q&A (no van en la lámina):**
- El chequeo de "¿ya descargué esta lección?" lo hace el propio
  `DownloaderService` (glob de archivos existentes en `_download_lesson`)
  antes de invocar a yt-dlp, no es una feature nativa de la librería. Hay
  una función `make_filter` en el código pensada para usar el
  `match_filter` nativo de yt-dlp con el mismo propósito, pero quedó sin
  usar (dead code). Respuesta honesta si preguntan por qué hay dos
  mecanismos.
- Parámetros concretos: `fragment_retries: 3`, `retries: 3`,
  `continuedl: True`, `concurrent_fragment_downloads` = cantidad de
  workers configurada.

---

## Ingesta de Datos - Transcripción ASR

**Bullets (lámina):**
- La transcripción fue la etapa que más tiempo llevó: empezamos con
  Whisper simple (muy lento), probamos acelerarlo con el cluster de la
  facultad (problemas de multithreading no resueltos del todo), y
  terminamos con faster-whisper, más simple de usar y más rápida que la
  versión original.
- Para transcribir el corpus se eligió el tamaño medium: con GPU propia,
  una clase pasó de más de 12 horas en CPU (con small) a unos 5 minutos.
  La colaboración con la UEFI también aportó acceso a GPU para procesar
  el corpus.

**Guion (oral):**
Whisper es una biblioteca de código abierto de OpenAI para reconocimiento
de habla, muy estándar en el ámbito. Fue la etapa que más tiempo nos llevó
del pipeline. Empezamos con Whisper simple, que era muy lento, 12 horas
para transcribir una sola clase con el modelo small en CPU. Buscamos
alternativas, probamos acelerarlo con el cluster de la facultad pero
tuvimos problemas de multithreading que no llegamos a resolver del todo.
Finalmente encontramos faster-whisper, que además de ser más simple de
usar terminó siendo más rápida que la versión original de Whisper. Con
GPU propia, esa misma clase que tardaba 12 horas pasó a procesarse en
unos 5 minutos, usando el modelo medium. La colaboración con la UEFI
también nos dio acceso a GPU para procesar el corpus.

**Notas para Q&A (no van en la lámina):**
- El dataset de transcripciones que aportó la UEFI (no la URI, ver
  corrección 2026-09-14 en `qa-simulacion-tribunal.md`) complementó el
  trabajo propio, no lo reemplazó.
- El WER medido por tamaño de modelo (tiny/base/small/medium) es Cap. 6,
  cubierto en la diapo de Experimentación de Diego (Modelo de ASR), no
  se repite acá para no duplicar contenido entre las dos diapos.

---

## Ingesta de Datos - Vectorización

**Layout real de la lámina (tarjetas + texto, no párrafos largos):**
- Tarjeta **Velocidad** — "Tiempo de procesamiento y respuesta"
- Tarjeta **Calidad** — "Dimensión del vector y precisión semántica"
- Tarjeta **Opciones Multilenguaje** — "Costo de inferencia y recursos"
- Texto: "Un embedding representa el texto como un vector: la cercanía
  geométrica entre vectores refleja similitud semántica."
- Texto: "Distancia Coseno."
- Texto: "Base de Datos: PostgreSQL - PG Vector. Permite combinar
  búsqueda semántica con filtros."

**Guion (oral):**
Un embedding es una forma de representar texto como un vector numérico,
de manera que la cercanía geométrica entre esos vectores refleja qué tan
parecido es el significado. El ejemplo clásico es este, rey menos hombre
más mujer da aproximadamente reina, porque el modelo captura relaciones
como género y realeza como direcciones dentro del espacio vectorial.

Para nuestro corpus evaluamos dos modelos. Uno más liviano, en inglés,
que usamos en etapas tempranas del desarrollo cuando el corpus era más
chico. Y multilingual-e5-base, que elegimos para producción porque
OpenFing es mayormente en español pero con bastante terminología técnica
en inglés, y el modelo en inglés no daba resultados satisfactorios para
ese dominio. Para buscar los fragmentos más relevantes usamos similitud
coseno sobre esos vectores, indexados en pgvector.

**Notas para Q&A (no van en la lámina):**
- Dimensión de cada modelo: all-MiniLM-L6-v2 = 384, multilingual-e5-base
  = 768. La mayor dimensionalidad del segundo permite representar con más
  detalle las relaciones entre conceptos del dominio académico.

---

## Indexación (chunking + base de datos)

Diapo nueva, separada de Vectorización para no apretar todo junto
(decisión 2026-09-15). Cubre cómo se fragmenta el texto y cómo se
almacena/busca, después de haber cubierto en la diapo anterior cómo se
genera el vector.

**Bullets (lámina, versión final — el diagrama ya nombra las clases de
LangChain, no hace falta repetirlo en texto):**
- Base de Datos: PostgreSQL - PG Vector. Permite combinar búsqueda
  semántica con filtros.

**Decisión 2026-09-15: "Distancia Coseno" se sacó de esta diapo.**
Corresponde a la fase de *retrieval* (búsqueda en tiempo de consulta,
Cap. 4: "el sistema ejecuta una búsqueda por similitud coseno... y
recupera los cuatro fragmentos"), no a la fase de indexación/offline que
cubre esta diapo. Va mencionada en **Flujo** en cambio, junto con k=4.
No olvidar agregarla ahí.

**Diagrama:** comparación longitud fija vs. chunking semántico, con
ejemplo de texto (árbol AVL, ya usado como ejemplo en el Cap. 4). Longitud
fija corta a mitad de palabra ("balan|ceado"); semántico corta en los
límites de oración. Parámetros reales al pie (`percentile`, `0.6`, `400`
caracteres). Fuente:
`ingesta-vectorizacion/chunking-longitud-fija-vs-semantico.html`.

**Guion (oral):**
Para indexar el corpus primero hay que partirlo en fragmentos. LangChain
nos da dos estrategias, RecursiveCharacterTextSplitter, que corta por
longitud fija de caracteres, y SemanticChunker, que corta según dónde
cambia el tema entre oraciones. Elegimos la segunda para producción,
porque un corte por longitud fija puede partir una idea a la mitad,
mientras que el semántico tiende a mantener cada fragmento como una idea
completa.

Para almacenar y consultar esos vectores usamos PostgreSQL con la
extensión pgvector, que nos permite combinar la búsqueda semántica con
filtros relacionales, por ejemplo restringir a un curso o lección
puntual, en una sola consulta SQL. Cómo se busca exactamente sobre esos
vectores lo vemos en la diapo de Flujo.

**Notas para Q&A (no van en la lámina):**
- Por qué no FAISS: la razón documentada en el Cap. 4 es simplicidad
  operativa. FAISS mantiene el índice en RAM y requiere serialización y
  carga manual para persistirlo en disco, mientras que pgvector persiste
  los vectores con las mismas garantías transaccionales que el resto de
  los datos, sin infraestructura adicional.
- El problema no trivial detrás de la trazabilidad con timestamp exacto:
  la transcripción viene con `segments` (texto + tiempos en segundos),
  pero el chunker corta el texto plano por caracteres o semántica, sin
  relación directa con esos segmentos. `BaseChunker` reconstruye la
  posición de cada segmento dentro del texto concatenado
  (`_create_timestamp_mapping`, con fallback fuzzy si el texto no
  matchea exacto), y para cada chunk calcula su `start_time`/`end_time`
  buscando qué segmentos se solapan, interpolando linealmente si ninguno
  cae justo ahí (`_interpolate_timestamp`). Este es justo el mecanismo
  que tenía un bug que se corrigió (guardaba `start_pos`/`end_pos` en vez
  de `start_time`/`end_time` en `_format_sources`) — buen ejemplo de qué
  puede salir mal cuando conviven dos sistemas de coordenadas (caracteres
  vs. tiempo) en la misma metadata.
- `normalize_embeddings: True` en el `Embedder` — relevante porque
  pgvector/similitud coseno asume vectores normalizados.
- Cache de modelos de embeddings a nivel de clase (`_models_cache` +
  `threading.RLock`) para no recargar el modelo en memoria/GPU cada vez
  que se instancia un `Embedder`.
- Mensaje de comparación con los módulos anteriores si preguntan por el
  diseño general: downloader y scraper son integraciones/wrappers sobre
  herramientas externas (yt-dlp, requests+BeautifulSoup); vectorización es
  donde vive la lógica de dominio propia de la tesis, el mapeo
  carácter↔tiempo y las heurísticas de chunking no existen en ninguna
  librería, son diseño propio sobre primitivas de LangChain.

---

## Generación - Modelo de Inferencia

**Layout real de la lámina (tarjetas + diagrama, sin texto extra — un
párrafo largo rompía el autoajuste de fuente, mismo problema que en
Descargas):**
- Tarjeta **Latencia** — "Tiempo de procesamiento y respuesta"
- Tarjeta **Calidad de respuesta** — "Precisión y adopción del
  entrenamiento"
- Tarjeta **Precio** — "Costo de inferencia y recursos"
- Diagrama: `LLMFactory` (plugin propio, instancia según config) →
  `ChatOllama` (local, dev/privacidad) o `ChatHuggingFace` (HuggingFace
  Inference API, remoto), ambos detrás de la interfaz común `Runnable`
  de LangChain que usa el resto del pipeline (`LLMService`, chains) sin
  importarle el proveedor. Fuente:
  `generacion-modelo-inferencia/llmfactory.html`.

**Guion (oral):**
Para la generación evaluamos tres modelos. Mistral 7B lo descartamos por
menor desempeño en el dominio académico en español. Qwen2.5-72B daba
respuestas más fluidas, pero el costo de inferencia no se justificaba
frente a esa mejora, el detalle de costos lo vemos en la próxima sección.
Nos quedamos con Llama 3.1 8B, que ofrecía el mejor equilibrio entre
calidad y costo.

A nivel de implementación, el módulo Generador no está atado a un
proveedor específico. Definimos una fábrica, LLMFactory, que instancia
el modelo según configuración, puede ser Ollama corriendo en local o
HuggingFace Inference API en remoto. Los dos quedan detrás de la misma
interfaz común de LangChain, así que el resto del pipeline no necesita
saber cuál de los dos está corriendo por detrás.

**Notas para Q&A (no van en la lámina):**
- Retrieval: `VectorRepository.similarity_search` usa `PGVectorStore`
  (de `langchain_postgres`, sobre pgvector) con
  `similarity_search_with_score`, filtrando por curso/lección vía
  metadata JSON (`$in` filters).
- Optimización de costo/latencia: `_is_follow_up_question` es una
  heurística simple (¿hay historial y la consulta tiene ≤3 palabras?)
  para saltear el retrieval en preguntas de seguimiento cortas. No es NLP
  sofisticado, y está detrás de un feature flag
  (`NEVER_SKIP_RETRIEVAL`) por si da falsos positivos.
- Prompt engineering con LCEL: `self.chain = self.prompt | self.llm`,
  patrón pipe de `Runnable`s de LangChain, un `ChatPromptTemplate` propio
  encadenado directo al LLM.
- Trimming de historial: `trim_messages(strategy="last", max_tokens=4000)`
  de LangChain, para no exceder el context window en vez de mandar todo
  el historial siempre.
- Dos rutas de conversación: usuarios autenticados persisten en Postgres
  (`ConversationRepository`/`MessageRepository`, con rollback
  transaccional si el LLM falla); usuarios anónimos usan
  `EphemeralConversationHandler`, un cache en memoria
  (`cachetools.TTLCache`) con lock de asyncio, TTL de 1 hora y tope de
  historial, sin tocar la base de datos. Mismo `ChatService` maneja
  ambos casos con la misma interfaz de `LLMService`.
- Detalle de diseño (ya mencionado en Q&A de Indexación): los chunks
  usan UUIDs determinísticos (`generate_chunk_uuid(transcription_id,
  chunk_index)`) en vez de aleatorios, para que re-vectorizar la misma
  transcripción haga upsert en vez de duplicar filas.

---

## Flujo

Diagrama original de Slides, sin rediseño (se probó una versión con
routing en ángulo recto para las dos ramas de la decisión, y otra que
seguía siempre hacia la derecha sin volver atrás, pero se decidió
mantener el diagrama original — 2026-09-15). Completo: Estudiante →
Frontend → Backend → heurística de follow-up → búsqueda por similitud
coseno (k=4) en pgvector → ensamblar contexto agrupado por clase →
prompt → Llama 3.1 8B vía HuggingFace Inference API → persistencia →
respuesta con fuentes. Coincide con el flujo descripto en Cap. 4 §4.2.
Pendiente: cambiar la caja "similitud vectorial" a "similitud
**coseno**" (acá va el término que sacamos de Indexación).

**Guion (oral):**
Este es el recorrido completo de una consulta. El estudiante pregunta en
lenguaje natural desde el frontend, la solicitud llega al backend con el
JWT si está autenticado, y ahí se aplica una heurística simple, si ya
hay historial de conversación y la consulta tiene tres palabras o menos,
se asume que es una pregunta de seguimiento y se omite la recuperación,
se responde directo con el historial existente.

Si no se omite, se hace una búsqueda por similitud coseno en pgvector,
trayendo los cuatro fragmentos más relevantes, k=4. Esos fragmentos se
agrupan por clase para armar el contexto, evitando repetir encabezados
cuando varios fragmentos vienen de la misma lección. Con eso se construye
el prompt, se lo pasamos a Llama 3.1 8B a través de HuggingFace Inference
API, y la respuesta en español vuelve con las fuentes, los chunk_ids
usados. Esa respuesta se persiste junto con sus fuentes, y el frontend la
muestra con las referencias, curso, lección y el timestamp exacto en el
video.

**Notas para Q&A (no van en la lámina):**
- La heurística de follow-up (`_is_follow_up_question`, ¿hay historial +
  consulta ≤3 palabras?) es simple a propósito, no NLP sofisticado, y
  está detrás de un feature flag (`NEVER_SKIP_RETRIEVAL`) por si da
  falsos positivos y hay que desactivarla.
- El límite de 4000 tokens de historial se aplica con
  `trim_messages(strategy="last")` de LangChain.
- Por qué no reranking ni umbral de similitud: el sistema retiene los 4
  fragmentos de mayor puntuación sin importar su distancia absoluta
  (Cap. 4); reranking queda como trabajo a futuro (Cap. 7).

---

## Despliegue y validación

Carpeta ya cerrada (`despliegue-y-validacion/propuesta-final.md`). Nota
2026-09-15: la propuesta original preveía una sola diapo con dos
tarjetas (Arquitectura + Validación en Ingeniería de Muestra), pero en
el deck real quedaron como **dos diapos separadas** — esta es solo
arquitectura; "Ingeniería de Muestra" es otra diapo aparte, con su
propio guion cuando lleguemos a ella.

**Bullets (lámina):**
- Desplegado en un VPS de Mi Nube ANTEL, containerizado con Docker
  Compose.

**Diagrama:** `despliegue-y-validacion/arquitectura-despliegue.png` —
Usuario/Navegador → Nginx (único punto de entrada) → Frontend (React) /
Backend (FastAPI) → PostgreSQL (red interna, nunca expuesto), todo
dentro de un rectángulo punteado "Docker Compose". Iconos reales de
Docker/Nginx (simple-icons), el resto con íconos simples a color en vez
de logos oficiales.

**Guion (oral, ~1 min, arranca conectando con Análisis de
Infraestructura sin repetir el dato de latencia):**
El mismo despliegue del que salieron los datos de latencia que vimos
antes también nos sirvió para probar la arquitectura en producción real.
Todo corre containerizado con Docker Compose, sobre un servidor que nos
cedió Antel sin costo, como apoyo institucional. Utilizamos un dominio
gratuito gracias al servicio de DuckDNS, un servicio gratuito de DNS
dinámico que nos permite asociarle un nombre de dominio a la IP del
servidor sin tener que pagar por uno, y configuramos la certificación
SSL gracias a dos herramientas open source, Let's Encrypt y certbot.

Utilizamos Nginx como servidor y único punto de entrada. Y como se puede
apreciar en la imagen, la base de datos queda aislada del acceso
exterior y solo el backend puede conectar con ella utilizando una red
interna separada.

**Notas para Q&A (no van en la lámina — fuente:
`mine/data/deployment-minube-antel.md`, ninguno de estos datos está en
el `.tex`, aclarar eso si se mencionan):**
- ¿El sistema sigue funcionando hoy? No, el VPS era temporal (el período
  gratuito de Mi Nube ANTEL terminó, sin renovarse); el código está
  versionado en GitLab, no se perdió nada. Lo único que quedó en el
  servidor eran métricas de uso (conteo de consultas/conversaciones).
- Hardening de seguridad, capa por capa (defensa en profundidad):
  firewall de la plataforma Mi Nube → UFW (firewall de host, deniega
  todo por defecto, solo abre 80/443 al mundo) → Fail2Ban (bloquea IP
  tras 3 intentos fallidos de SSH en 10 min, ban de 24h) → SSH endurecido
  (puerto 2222 en vez de 22, sin login de root, solo clave ED25519, un
  único usuario permitido) → aislamiento de red de Docker.
- SSH además restringido por IP: solo alcanzable desde rangos de Antel
  Uruguay (no desde cualquier lugar del mundo).
- Dato concreto si preguntan por volumen de ataques: se registraron más
  de **533.000 intentos de conexión SSH** de atacantes de todo el mundo
  antes/durante el hardening (usuarios más probados: `root`, `admin`,
  `test`). Con Fail2Ban activo, se bloquearon 10 IPs y se detectaron 62
  intentos fallidos en los primeros 5 minutos. No se detectó ninguna
  brecha exitosa en todo el período.
- Anécdota técnica honesta: durante la configuración se encontró que UFW
  tenía una regla de IPv6 demasiado permisiva (SSH abierto a cualquier
  IPv6 del mundo), que pasó por alto las restricciones cuidadosas puestas
  en IPv4. Se corrigió al detectarlo — buen ejemplo de que un sistema
  dual-stack necesita atención explícita a ambas familias de protocolo.
- Otros detalles de infraestructura no mencionados en el informe: rate
  limiting en Nginx (10 req/s en `/api`, 1 req/s en endpoints pesados),
  compresión gzip, endpoint `/health` para healthchecks, usuario no-root
  dentro de los contenedores, builds multi-stage de Docker, `uv` para
  dependencias de Python y `pnpm` para el frontend (más rápidos que
  pip/yarn).
- Por qué Docker Compose y no Kubernetes: complejidad apropiada para un
  proyecto de un solo servidor, mismos beneficios de aislamiento con
  operación mucho más simple.

---

## Ingeniería de Muestra

Segunda mitad de la propuesta original de `despliegue-y-validacion/`,
ahora como diapo propia separada.

**Bullets (lámina):**
- **Alcance institucional** — Extender la herramienta más allá de
  OpenFing.
- **Equidad educativa** — Estudiantes del interior, que no siempre
  pueden asistir de forma presencial.
- Texto: "Durante IdeM, el grupo mostró el prototipo y recogió
  devolución cualitativa de estudiantes y docentes. Hay entusiasmo de
  que una herramienta por el estilo esté en producción."

**Guion (oral):**
En octubre de 2025 participamos de Ingeniería de Muestra, la instancia
donde la facultad comparte los proyectos de grado con toda la comunidad
académica. Mostramos el prototipo funcionando en vivo y recogimos
devolución cualitativa de estudiantes, docentes y actores académicos.

Dos perspectivas se repitieron. Estudiantes que viven en el interior del
país nos contaron que no poder asistir de forma regular genera una
desconexión real con el curso, y que las vías tradicionales para
resolver dudas no siempre alcanzan. A partir de esa conversación
identificamos que un chatbot entrenado con el material de su curso puede
ser un recurso que sostenga su rendimiento a la par de sus compañeros
que cursan en Montevideo.

La segunda perspectiva vino de estudiantes de otras facultades de la
Universidad de la República, que plantearon que la herramienta podría
extenderse más allá de OpenFing con un filtrado por facultad.

**Notas para Q&A (no van en la lámina):**
- ¿Es un estudio de usuario formal? No, es devolución cualitativa, no
  encuestas ni métricas formales, no busca representatividad
  estadística.
- ¿La extensión a otras facultades está diseñada o es una idea suelta?
  Es una idea planteada por estudiantes, tiempo condicional ("podría
  extenderse"), no una funcionalidad entregada ni diseñada en detalle.

---

## Conclusiones

Carpeta ya cerrada (`conclusiones/propuesta-final.md`). Nota 2026-09-15:
el gerundio suelto ("Sirviendo como...") que la propuesta documentaba
como corregido volvió a aparecer en la versión final de Slides —
decisión explícita del usuario, dejarlo así, no es un descuido.

**Layout real de la lámina:**
- Fila de 5 íconos con estado (orden real en Slides, distinto al de la
  propuesta escrita pero mismo contenido): Pipeline completo
  automatizado (✓) · Extensible a otras bases de conocimiento (✓) ·
  Evaluación de herramientas de ASR (✓) · Chatbot RAG conversacional (✓)
  · Evaluación extensiva de respuestas (◐, parcial, al final).
- Tarjeta izquierda (acento teal), "Qué se logró": "Quedó implementado
  un sistema que logra consolidar el conocimiento impartido por el
  cuerpo docente y exponerlo a los estudiantes mediante una interfaz
  simple y moderna. Sirviendo como herramienta de autoestudio para los
  tiempos actuales."
- Tarjeta derecha (acento naranja), "Más evaluación": "Más evaluación es
  el principal camino a seguir, para continuar mejorando la herramienta
  y lograr el mayor provecho de la misma."
- Cierre, ancho completo, cursiva: "Una prueba de concepto totalmente
  viable y de potencial para la comunidad educativo-universitaria."

**Guion (oral, ~2 minutos):**
Volviendo a los cinco objetivos específicos que planteamos al inicio,
cuatro se cumplieron en su totalidad. El pipeline automatizado de
extracción, transcripción e indexación, la evaluación de modelos de ASR
para español académico rioplatense, el chatbot RAG con trazabilidad al
instante exacto del video, y la arquitectura de código abierto
extensible.

El cuarto objetivo, evaluar la calidad del pipeline mediante
experimentos de pregunta-respuesta, lo abordamos parcialmente. La
evaluación de la transcripción quedó completa y documentada con
métricas concretas. Lo que no llegamos a profundizar fue la evaluación
del componente conversacional sobre el corpus completo, priorizamos el
tiempo en estabilizar el pipeline de punta a punta antes que en esa fase
experimental adicional.

Con ese balance, lo que queda implementado es un sistema que consolida
el conocimiento impartido en los cursos de OpenFing y lo expone a los
estudiantes en una interfaz simple y moderna, una herramienta de
autoestudio pensada para los tiempos actuales. La solución es viable y
funciona como esperábamos, algo que también se reflejó en la devolución
que recibimos en Ingeniería de Muestra.

Dicho esto, más evaluación es el principal camino para seguir mejorando
la herramienta y aprovechar todo su potencial, ese es justamente el
punto de partida de lo que viene en Trabajo a Futuro.

En términos generales, el proyecto muestra que las barreras para este
tipo de herramientas educativas basadas en IA son principalmente
metodológicas, no económicas. La generación de respuestas, en
particular, no requirió infraestructura de GPU propia, se resolvió con
inferencia como servicio.

**Notas para Q&A (no van en la lámina):**
- ¿El objetivo 4 incompleto preocupa? El checklist y el guion encuadran
  explícitamente "profundidad distinta entre componentes", no objetivo
  incumplido, y el símbolo ◐ evita que se lea como fallo.
- ¿"Viable" es "ya en producción"? No, ni la tarjeta ni el guion
  mencionan despliegue o continuidad operativa, eso quedó cubierto en
  Despliegue y Validación (y ahí mismo se aclara que el VPS ya no está
  activo).
- **Riesgo a vigilar en Trabajo a Futuro:** la tarjeta derecha de esta
  diapo ("más evaluación") se superpone en espíritu con la diapo de
  Trabajo a Futuro. Si esa diapo desarrolla el mismo mensaje con detalle
  técnico (re-ranking, ajuste fino, feedback explícito), evitar repetir
  la idea genérica dos veces seguidas.

---

## Trabajo a futuro

Última diapo de contenido antes del cierre ("Muchas gracias"). Se
enriqueció respecto a la versión original del deck (muy comprimida/vaga:
"otros tipos de RAG", typos "FineTunning"/"OpenFING"), con el detalle
real del Cap. 7 §Trabajo a futuro, sin alargarla ni duplicar el mensaje
de "más evaluación" de Conclusiones.

**Bullets (lámina):**
- Transición de conocimiento: integrar el proyecto en un entorno
  institucional (URI / OpenFing) y automatizar la incorporación de
  nuevas clases, más allá del despliegue provisional actual en Mi Nube
  ANTEL.
- Extender la integración a otras facultades de la UdelaR, con filtrado
  por facultad para mantener la relevancia y coherencia disciplinar de
  las respuestas.
- Técnicas más avanzadas de recuperación y generación: re-ranking,
  búsqueda híbrida, fine-tuning del modelo de embeddings y del LLM,
  habilitados por un mecanismo de feedback explícito del usuario.
  (Decisión 2026-09-15: se sacó la aclaración "(densa + BM25)" de la
  lámina, el usuario no se sentía cómodo explicándola en vivo si
  preguntan sobre ella en detalle sin ensayarlo antes. Queda en Q&A.)

**Guion (oral):**
Para que los estudiantes realmente adopten esta herramienta en sus
cursos, el paso siguiente es la transición de conocimiento hacia un
entorno institucional, con la URI y OpenFing, y automatizar la
incorporación de clases nuevas, hoy el sistema está desplegado de forma
provisional en Mi Nube de Antel.

También queremos extender la integración a otras facultades de la
UdelaR, que ya están empezando a subir sus clases online. Para eso hace
falta un filtrado por facultad, así el chatbot mantiene coherencia con
el enfoque y la profundidad de cada disciplina.

Y a nivel técnico, hay varias líneas para mejorar la calidad de las
respuestas: re-ranking de los fragmentos recuperados, búsqueda híbrida
combinando similitud vectorial con BM25, y ajuste fino tanto del modelo
de embeddings como del LLM. Todo esto se habilita mucho mejor si
agregamos un mecanismo de feedback explícito del usuario, que nos dé los
datos reales para hacer ese ajuste fino.

**Notas para Q&A (no van en la lámina):**
- Qué significa "búsqueda híbrida" si preguntan (Cap. 7, línea 34):
  hoy la recuperación es 100% **densa** (embeddings + similitud coseno,
  entiende significado aunque no coincidan las palabras exactas, pero
  puede "difuminar" siglas/nombres de cursos poco frecuentes). Híbrida
  = sumarle **BM25**, un algoritmo clásico de búsqueda por palabras
  clave/frecuencia de términos (sin embeddings), para no perder
  precisión en términos técnicos exactos. Se fusionan los resultados de
  ambos antes de generar la respuesta.
- Fine-tuning del LLM: técnicas eficientes como LoRA y QLoRA permiten
  adaptar un modelo del tamaño de Llama 3.1 8B con recursos de cómputo
  moderados, sin reentrenar todos los parámetros.
- Por qué no se hizo ya: todas estas líneas requieren datos reales de
  interacción etiquetados (qué respuestas fueron útiles o no), que recién
  se podrían acumular con el sistema en uso continuo, no durante el
  desarrollo del PG.
- Riesgo a vigilar (ver nota en Conclusiones): si el tribunal ya escuchó
  "más evaluación" en Conclusiones, acá el ángulo es distinto y más
  concreto, técnicas específicas y alcance institucional, no repetir la
  idea genérica.

---
