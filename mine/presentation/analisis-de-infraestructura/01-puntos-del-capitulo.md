# ¿Cuáles son los puntos del capítulo?

Fuente: `6-Experimentacion.tex` §6.7 y §6.8. La sección plantea la viabilidad
operativa del sistema en tres dimensiones, costos, latencia y modelo de
inferencia.

---

## 1. Costos de inferencia (§6.7.1)

**Metodología.**
- Se parte de la muestra de preguntas analizada en §6.6 (QA).
- Consulta promedio: **1.179,25 tokens de entrada** y **405,125 de salida**.
- Peor caso de la muestra: **1.268 de entrada** y **702 de salida**.
- Los tokens de entrada en una arquitectura RAG incluyen la consulta del usuario,
  las instrucciones del sistema y todos los fragmentos recuperados de la base
  vectorial. Los de salida incluyen la respuesta visible y los tokens de
  razonamiento interno de los modelos que lo usan.
- Proyección a un volumen de **1.000 consultas**.

**Tabla comparativa** (Tabla 6.x, tarifas al 30/05/2026, USD por millón de tokens).
Costo proyectado para 1.000 consultas. La tabla del informe da columnas separadas
**P Prom** (costo de tokens de entrada, volumen promedio) y **R Prom** (costo de
tokens de salida, volumen promedio), y **no las suma en una columna de total**. La
columna "Suma P+R" de acá abajo es una derivación propia para tener el panorama,
el informe no la muestra.

| Modelo | Proveedor | Entrada $/1M | Salida $/1M | P Prom | R Prom | Suma P+R (deriv.) |
|---|---|---|---|---|---|---|
| Meta-Llama-3-8B-Instruct | HuggingFace | 0,04 | 0,04 | **0,047** | 0,016 | ~0,063 |
| Qwen2.5-72B-Instruct | HuggingFace | 0,38 | 0,40 | 0,448 | 0,162 | ~0,61 |
| GPT-5.4 Nano | OpenAI | 0,20 | 1,25 | 0,236 | 0,506 | ~0,74 |
| Gemini 2.5 Pro | Google | 1,25 | 10,00 | 1,474 | 4,051 | ~5,5 |
| Gemini 3.5 Flash | Google | 1,50 | 9,00 | 1,769 | 3,646 | ~5,4 |
| GPT-4.1 | OpenAI | 2,00 | 8,00 | 2,358 | 3,241 | ~5,6 |
| Claude Sonnet 4.6 | Anthropic | 3,00 | 15,00 | 3,538 | 6,077 | ~9,6 |
| Claude Opus 4.1 | Anthropic | 15,00 | 75,00 | 17,689 | 30,384 | ~48 |
| GPT-5 Pro | OpenAI | 15,00 | 120,00 | 17,689 | 48,615 | ~66 |

**Cifra que cita el informe como costo operativo (§6.8.2):** aproximadamente
**0,047 USD por cada 1.000 consultas** con Llama 3.1 8B vía Novita. Ese valor es
la columna P Prom, es decir el costo de los tokens de entrada. El informe no
aclara que sea solo entrada, lo usa como "costo promedio". Los tokens de entrada
dominan el costo en RAG, así que es una aproximación válida. Se usa 0,047 tal cual
en la presentación.

**Lecturas de la tabla.**
- Enorme varianza de precios entre modelos comerciales.
- Los modelos servidos por HuggingFace son sustancialmente más baratos.
- El modelo elegido (Llama-3-8B) es hasta **10 veces más barato que Qwen2.5-72B**,
  el otro modelo que se evaluó.
- El costo no depende solo del volumen de tokens, algunos modelos aplican
  optimizaciones internas que podrían bajar los valores de la tabla.
- Para Gemini 2.5 Pro, que tiene precio dinámico, se usó la tarifa de contextos
  menores a 200.000 tokens.

**Riesgo operativo.** Los proveedores de inferencia gestionada pueden retirar,
discontinuar o modificar el acceso a un modelo de forma unilateral. Si el modelo
elegido deja de mantenerse bajo las condiciones actuales, el sistema debe migrar.
Esa transición altera las proyecciones económicas y puede traer problemas
técnicos, reconfiguración de arquitectura, recalibración de prompts y variaciones
de rendimiento.

---

## 2. Latencia en producción (§6.8.1)

**Medición.**
- Registrada por el middleware de logging, que marca tiempo al inicio y al fin de
  cada solicitud HTTP procesada por FastAPI.
- No incluye latencia de red navegador-servidor ni renderizado en el cliente.
  Como servidor y usuarios estaban en Uruguay, ese componente es de decenas de
  milisegundos y se considera despreciable.
- Se emite un registro intermedio al terminar la recuperación de fragmentos, lo
  que permite separar la latencia en dos fases.

**Muestra.** 272 consultas exitosas del VPS de Mi Nube ANTEL, entre el 26/08 y el
22/10/2025. 166 de las 272 se concentran en la jornada de Ingeniería de Muestra.

**Resultados.**
- Latencia total: **mediana 5,4 s**, **promedio 8,8 s**, rango **1,6 s a 76 s**.
- Fase 1, vectorización de la consulta con el modelo de embeddings más búsqueda en
  pgvector. Distribución bimodal.
  - Modelo de embeddings ya cargado en memoria: **mediana 2,9 s**.
  - Tras inactividad prolongada, la carga inicial del modelo lleva la fase hasta
    **75 s**, fenómeno de arranque en frío (cold start) del modelo en CPU.
- Fase 2, llamada a HuggingFace Inference API y generación: **mediana 2,4 s**,
  con casos aislados de hasta 25 s por la cola de solicitudes del proveedor.

**Decisión derivada.** Nginx se configuró con timeout de **300 s** hacia el
backend, margen que cubre el peor caso y evita cortes prematuros en alta carga o
cold start.

---

## 3. Self-hosting vs. inferencia como servicio (§6.8.2 y RNF5 en §3.3.4)

**Encuadre (RNF5).** El sistema necesita un LLM para generar respuestas, lo que
plantea una decisión de infraestructura, alojar el modelo localmente
(self-hosting) o delegar la inferencia a un servicio externo (inference as a
service). Impacta costo operativo, latencia, privacidad de datos, viabilidad de
producción y calidad de las respuestas.

**Ventajas de self-hosting según el informe.**
- Privacidad y seguridad, las consultas de los estudiantes quedan en servidores
  de la facultad, bajo ley uruguaya.
- Latencia, sin dependencia de llamadas externas sujetas a congestión de red.
- Costos operativos, sin pagos recurrentes a terceros.

**Desventaja principal.** Requerimientos de hardware, una o varias GPU de alta
gama con costo de adquisición y de energía elevado.

**Tensión teórica citada.**
- Kaplan et al. 2020, el tamaño del modelo es el factor dominante del rendimiento.
- Mistral 7B, el problema es tridimensional, capacidad, costo de entrenamiento y
  costo de inferencia, y se puede comprimir más conocimiento en modelos chicos de
  lo que se creía.

**Restricción concreta del despliegue.**
- Llama 3.1 8B pide, en inferencia estándar a 16 bits, una GPU con al menos
  **16 GB de VRAM**, o **~8 GB en cuantización de 4 bits**.
- El VPS de Mi Nube ANTEL **no tenía GPU**.
- Self-hosting vía Ollama hubiera sido inferencia solo en CPU, con latencias
  estimadas de **varios minutos por consulta**, incompatible con una experiencia
  conversacional interactiva.
- No es un problema exclusivo de este proyecto, modelos del orden de Llama 3.1 8B
  y Mistral 7B imponen requisitos de GPU que no suelen estar en entornos de
  prototipado de bajo costo.

**Decisión tomada.** HuggingFace Inference API para la generación.
- Ventajas, sin mantenimiento de GPU propia, disponibilidad a cargo del proveedor,
  escalado sin intervención del equipo, costo proporcional al uso.
- Dato de costo, **~0,047 USD por cada mil consultas** con Llama 3.1 8B vía el
  proveedor Novita, adecuado para un entorno académico con base de usuarios
  moderada.
- Contrapartida, dependencia externa, el proveedor puede cambiar tarifas, degradar
  el servicio o discontinuar el soporte sin aviso.
- Para un despliegue institucional de mayor escala o con disponibilidad
  garantizada, el self-hosting con hardware dedicado sería viable y más predecible
  a largo plazo, con esfuerzo operativo mucho mayor.

---

## 4. Anexo E, estimaciones de ingesta para todo OpenFing (contexto de apoyo)

No es parte de §6.7 pero respalda la dimensión de infraestructura del pipeline.

- OpenFing, estimado **1 TB de video**, **2.835 videos públicos**, tamaño medido
  999,29 GB.
- Conversión mp4 a m4a, entre **184 y 200 GB** de audio, a razón de **~130 horas
  de video procesadas por cada hora de cómputo**.
- Transcripción, hardware de referencia RTX 4050 (6 GB VRAM), faster-whisper 1.1.0,
  modelo Medium, español. **180 transcripciones en 8:49:18**, lo que proyecta
  **~132,7 horas** para todo OpenFing.
- Calidad ASR, WER de **0,046 (medium)** y **0,15 (small)** contra transcripción
  manual de referencia. Tiny y base descartados por error frecuente.
