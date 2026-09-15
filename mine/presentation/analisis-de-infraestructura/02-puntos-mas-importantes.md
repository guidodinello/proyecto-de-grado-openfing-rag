# ¿Cuáles son los más importantes?

Lo que tiene que quedar en la lámina y en la cabeza del tribunal. Cuatro ideas,
en orden de prioridad.

---

## 1. El sistema es económicamente viable, y hay un número que lo prueba

**~0,047 USD por cada 1.000 consultas** con Llama 3.1 8B vía inferencia gestionada.

Es la cifra que da el §6.8.2 del informe. Corresponde a la columna P Prom de la
tabla, o sea el costo de los tokens de entrada. Sumando la salida el total es del
orden de 0,063 USD. Se usa 0,047 en la presentación por consistencia con el
informe, que está aceptado. Ver punto H del archivo 03 para el Q&A.

Es el dato que cierra la pregunta implícita de todo el proyecto, ¿esto se puede
sostener en producción sin presupuesto? La respuesta es sí, y con margen enorme.
Un curso con miles de consultas al semestre cuesta centavos de dólar.

Por qué importa, un proyecto de grado que propone una herramienta institucional
tiene que demostrar que no es un prototipo insostenible. Este número lo hace.

---

## 2. La restricción de hardware determinó la arquitectura, no fue una preferencia

El VPS no tenía GPU. Llama 3.1 8B necesita **~16 GB de VRAM** (u ~8 GB en 4 bits).
Self-hosting en CPU daba **varios minutos por consulta**, inviable para un chat.

Por eso se eligió **inference as a service** (HuggingFace Inference API). No fue
una decisión de diseño tomada en abstracto, fue la única opción compatible con el
entorno real de despliegue.

Por qué importa, conecta directo con el RNF5 (§3.3.4) y hay que contar la historia
completa, se evaluaron las dos alternativas, self-hosting era deseable por
privacidad y costo a largo plazo, el hardware disponible lo impidió.

---

## 3. La latencia se midió con tráfico real, no en laboratorio

**Mediana 5,4 s** sobre **272 consultas reales** del VPS de ANTEL. Descompuesta en
recuperación (mediana 2,9 s) y generación (mediana 2,4 s).

Por qué importa, distingue este análisis de una simulación. El sistema estuvo
público, lo usaron estudiantes y docentes, y esos son los tiempos que
experimentaron.

Matiz que hay que decir, no esconder el **cold start de hasta 75 s** del modelo
de embeddings en CPU. Se explica solo, el modelo se carga en el primer request
tras inactividad y después queda caliente. Con uso sostenido no se percibe.

---

## 4. La dependencia del proveedor es una deuda técnica asumida a conciencia

Inference as a service trae una dependencia externa. El proveedor puede
re-tarifar, degradar o discontinuar el modelo sin aviso. Eso obliga a migrar,
recalibrar prompts y revalidar.

Por qué importa, muestra madurez de análisis. No se vende la decisión como
perfecta, se nombra el costo y se explica por qué es aceptable, migrar a otro
modelo open cuesta trabajo pero no rompe la viabilidad económica, los órdenes de
magnitud de precio se mantienen.

---

## Lo que NO es central para esta lámina

- El detalle del hardening del VPS (SSH, Fail2Ban, UFW). Va en la diapo 20
  (Despliegue), no en esta.
- Las estimaciones de ingesta del Anexo E (1 TB, 132 h de transcripción). Son
  contexto del pipeline, se pueden mencionar de pasada pero no son el foco de
  "análisis de infraestructura" tal como lo define §6.7.
- La tabla completa de 9 modelos. En la lámina van 3 o 4 filas como mucho, el
  resto satura.
