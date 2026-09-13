# **Cronograma Proyecto de Grado**

## **Módulo Generativo basado en OpenFing**

**Estudiantes:** Diego Amorena, Guido Dinello  
 **Supervisor:** Luis Chiruzzo  
 **Co-supervisor:** Libertad Tansinni  
 **Duración:** 8 meses (Marzo 2025 \- Octubre 2025\)  
 **Dedicación estimada:** 15 horas semanales por estudiante

---

## **Mes 1: Marzo 2025**

### **Estado del Arte y Fundamentos Teóricos**

**Objetivos del mes:**

* Establecer base teórica sólida  
* Definir arquitectura general del sistema  
* Configurar entorno de desarrollo

**Actividades principales:**

* **Semana 1-2:** Investigación exhaustiva de sistemas RAG existentes

  * Revisión de papers sobre arquitecturas RAG  
  * Análisis de soluciones educativas similares (nacional e internacional)  
  * Estudio de herramientas de transcripción automática  
* **Semana 3-4:** Investigación de componentes técnicos

  * Comparación de modelos de embedding (SBERT, OpenAI, multilingual)  
  * Análisis de bases de datos vectoriales (PGVector, Chroma, Pinecone)  
  * Estudio de modelos LLM (GPT-4, Claude, Llama-2, Mistral)

**Entregables:**

* Documento de estado del arte (15-20 páginas)  
* Arquitectura técnica preliminar  
* Configuración del entorno de desarrollo (Docker, uv, PostgreSQL)

---

## **Mes 2: Abril 2025**

### **Diseño del Sistema y Prototipado Inicial**

**Objetivos del mes:**

* Definir arquitectura final  
* Implementar módulos base  
* Establecer pipeline de datos básico

**Actividades principales:**

* **Semana 1-2:** Diseño detallado del sistema

  * Definición de esquemas de base de datos  
  * Diseño de API REST con FastAPI  
  * Especificación de interfaces entre módulos  
* **Semana 3-4:** Desarrollo del backend base

  * Implementación de modelos SQLAlchemy  
  * Sistema de repositorios y dependencias  
  * API básica para gestión de cursos y lecciones

**Entregables:**

* Documentación de arquitectura definitiva  
* Backend base funcional  
* Esquemas de base de datos implementados

---

## **Mes 3: Mayo 2025**

### **Módulo de Transcripción y Web Scraping**

**Objetivos del mes:**

* Implementar sistema de transcripción  
* Desarrollar scraper de OpenFing  
* Establecer pipeline de procesamiento de audio

**Actividades principales:**

* **Semana 1-2:** Sistema de transcripción

  * Integración con Whisper (múltiples modelos: tiny, base, medium, large)  
  * Implementación de transcriber con timestamps  
  * Sistema de almacenamiento de transcripciones  
* **Semana 3-4:** Web scraping y descarga

  * Scraper para OpenFing (cursos y lecciones)  
  * Sistema de descarga de videos con yt-dlp  
  * CLI para operaciones de transcripción batch

**Entregables:**

* Módulo de transcripción funcional  
* Scraper de OpenFing operativo  
* CLI para gestión de transcripciones

---

## **Mes 4: Junio 2025**

### **Sistema de Vectorización y RAG**

**Objetivos del mes:**

* Implementar sistema de embeddings  
* Desarrollar pipeline RAG  
* Primera evaluación de avance

**Actividades principales:**

* **Semana 1-2:** Vectorización y almacenamiento

  * Implementación de sistema de embeddings  
  * Integración con PGVector  
  * Chunking inteligente de transcripciones  
* **Semana 3-4:** Pipeline RAG básico

  * Sistema de búsqueda semántica  
  * Integración con LLM (inicialmente OpenAI GPT-4)  
  * Implementación de citación de fuentes

**Entregables:**

* **EVALUACIÓN DEL 4TO MES** ⚠️  
* Sistema RAG funcional básico  
* Base de datos vectorial operativa  
* Informe de avance para supervisores

---

## **Mes 5: Julio 2025**

### **Frontend y API Completa**

**Objetivos del mes:**

* Desarrollar interfaz de usuario  
* Completar API REST  
* Integrar todos los módulos

**Actividades principales:**

* **Semana 1-2:** Desarrollo del frontend

  * Interfaz React para chat interactivo  
  * Componentes para visualización de fuentes  
  * Sistema de autenticación básico  
* **Semana 3-4:** API REST completa

  * Endpoints para todas las funcionalidades  
  * Sistema de gestión de usuarios  
  * Documentación OpenAPI/Swagger

**Entregables:**

* Frontend React funcional  
* API REST completa documentada  
* Sistema integrado end-to-end

---

## **Mes 6: Agosto 2025**

### **Experimentación y Optimización**

**Objetivos del mes:**

* Evaluar diferentes configuraciones  
* Optimizar rendimiento  
* Implementar mejoras avanzadas

**Actividades principales:**

* **Semana 1-2:** Experimentación con modelos

  * Comparación de modelos de transcripción (Whisper tiny vs medium vs large)  
  * Evaluación de diferentes embeddings  
  * Testing de modelos LLM alternativos  
* **Semana 3-4:** Optimización y features avanzadas

  * Implementación de reranking  
  * Sistema de caché para embeddings  
  * Mejoras de performance y escalabilidad

**Entregables:**

* Análisis comparativo de modelos  
* Sistema optimizado con reranking  
* Métricas de performance documentadas

---

## **Mes 7: Septiembre 2025**

### **Evaluación Integral y Documentación**

**Objetivos del mes:**

* Evaluación exhaustiva del sistema  
* Documentación técnica completa  
* Preparación para entrega final

**Actividades principales:**

* **Semana 1-2:** Evaluación del sistema

  * Métricas de calidad de transcripción (WER, MER)  
  * Evaluación de respuestas del chatbot  
  * Testing con usuarios reales (estudiantes/docentes)  
* **Semana 3-4:** Documentación

  * Manual de usuario  
  * Documentación técnica completa  
  * Guías de instalación y deployment

**Entregables:**

* Informe de evaluación integral  
* Documentación técnica completa  
* Manual de usuario

---

## **Mes 8: Octubre 2025**

### **Informe Final y Presentación**

**Objetivos del mes:**

* Redactar informe final  
* Preparar presentación pública  
* Evaluación final

**Actividades principales:**

* **Semana 1-2:** Redacción del informe final

  * Introducción y marco teórico  
  * Descripción técnica detallada  
  * Análisis de resultados y experimentación  
* **Semana 3-4:** Preparación de la defensa

  * Presentación oral (40 minutos)  
  * Demo del sistema funcionando  
  * Preparación para preguntas del tribunal

**Entregables:**

* **Informe Final completo**  
* **Presentación pública**  
* **Evaluación final del proyecto**

---

## **Hitos Críticos y Puntos de Control**

### **Evaluación del 4to Mes (Junio 2025\)**

* **Objetivo:** Verificar viabilidad técnica y avance del proyecto  
* **Entregables obligatorios:**  
  * Sistema RAG básico funcionando  
  * Pipeline completo audio → transcripción → vectorización  
  * Demo funcional del chatbot  
  * Informe de avance técnico

### **Revisión del 7mo Mes (Septiembre 2025\)**

* **Objetivo:** Confirmar preparación para entrega final  
* **Entregables:**  
  * Sistema completo y optimizado  
  * Evaluación integral realizada  
  * Documentación técnica completa

### **Entrega Final (Octubre 2025\)**

* **Objetivo:** Defensa pública del proyecto  
* **Entregables:**  
  * Informe final  
  * Código fuente completo  
  * Presentación oral y demo

---

## **Recursos y Consideraciones Técnicas**

### **Hardware Requerido**

* **Transcripción:** GPU para Whisper (8-16GB VRAM recomendado)  
* **LLM:** Acceso a API externa o GPU potente para modelos locales  
* **Base de datos:** Servidor PostgreSQL con extensión PGVector

### **Riesgos Identificados**

1. **Complejidad de integración** entre múltiples tecnologías  
2. **Performance del LLM** para múltiples usuarios concurrentes  
3. **Calidad de transcripciones** en audio de clases reales  
4. **Escalabilidad** del sistema con grandes volúmenes de datos

