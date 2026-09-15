# Todo lo que dice el Cap. 7 (cuerpo de Conclusiones, sin filtrar)

Fuente: `Nuestro/Capitulos/7-Conclusiones.tex`, párrafos 1-9 (antes de
"Trabajo a futuro"). Un punto por párrafo del informe, en orden.

1. **Logro general.** Se logró desarrollar satisfactoriamente el chatbot
   educativo. La PoC muestra que el alto volumen de datos, el cómputo
   requerido y el tiempo de preprocesamiento no son un impedimento. La
   solución es viable y funciona como se esperaba.

2. **Resultados concretos que respaldan el logro.**
   - Whisper *medium* con especificación explícita de idioma español, WER
     promedio inferior a 0.05 en todos los conjuntos de prueba (menos de 5
     errores cada 100 palabras).
   - Pipeline de transcripción aplicado al corpus completo, 239 cursos, 4.339
     clases.
   - *faster-whisper* con CTranslate2, 2 a 4 veces más rápido que Whisper
     original.
   - Generación de respuestas con *Llama 3.1 8B Instruct*, vía API de
     inferencia de HuggingFace, adecuado para el dominio académico en
     español sin requerir GPU propia.

3. **Valor para el estudiante.** Respuestas mayoritariamente correctas, en
   tiempo y forma razonable. Útil para estudiar, facilita el aprendizaje,
   agiliza la asimilación de conceptos, apoya el estudio autónomo, respuestas
   inmediatas sobre consultas específicas, complementa los recursos
   actuales. Esto se reforzó con la retroalimentación de Ingeniería de
   Muestra, donde estudiantes del interior y de otras facultades destacaron
   el valor del asistente como herramienta de equidad educativa.

4. **Valor para la facultad.** Oportunidad de escalar el acceso al
   conocimiento. Consolida material disperso en muchos videos en una interfaz
   conversacional única. Los recursos computacionales ya están disponibles en
   la infraestructura de la facultad, la operación continua no debería
   representar una carga significativa.

5. **Cumplimiento de los 5 objetivos específicos (Cap. 1), con distinta
   profundidad:**
   - **1. Pipeline automatizado** (extracción, descarga, transcripción,
     indexación). Cumplido, sistema modular de 5 componentes orquestados con
     Prefect.
   - **2. Evaluar ASR para español académico rioplatense.** Satisfecho,
     evaluación cuantitativa y cualitativa de Whisper *base*, *small* y
     *medium*, se eligió *medium* con especificación de idioma.
   - **3. Chatbot RAG con referencia al instante exacto del video.**
     Cumplido, el sistema recupera fragmentos e incluye metadatos de
     temporización en cada respuesta.
   - **4. Evaluar calidad del pipeline RAG con experimentos de
     pregunta-respuesta.** Abordado **parcialmente**. La evaluación de
     transcripción quedó completa y documentada. La evaluación del
     componente conversacional sobre el corpus completo es la principal
     área pendiente.
   - **5. Software de código abierto, arquitectura extensible.** Logrado,
     arquitectura de microservicios que permite incorporar nuevas bases de
     conocimiento sin rediseño estructural.

6. **Áreas de mejora, aunque cumple su función demostrativa.**
   Refinamiento de la precisión de respuestas, métricas de uso, integración
   con sistemas académicos existentes, expansión del corpus a otras
   asignaturas.

7. **Autocrítica.** El alcance del procesamiento resultó más amplio de lo
   estimado inicialmente. El preprocesamiento del corpus completo demandó un
   tiempo de cómputo significativo que condicionó los ciclos de
   experimentación. Una estimación más precisa de los costos computacionales
   en la planificación habría permitido distribuir mejor el tiempo. La
   evaluación de pregunta-respuesta no alcanzó la profundidad prevista
   porque el tiempo priorizó la construcción y estabilización del pipeline
   completo sobre la fase experimental. Se remite al Anexo A (Planificación)
   para el detalle de cronograma planeado vs. real y las demoras.

8. **Cierre.** Las barreras para implementar herramientas educativas RAG
   basadas en IA son principalmente metodológicas, no económicas, lo que
   abre posibilidades para democratizar el acceso a asistentes pedagógicos
   inteligentes en contextos académicos.
