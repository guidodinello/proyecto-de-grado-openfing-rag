# Auditoría de Citas — Cap. 5 Implementación
Fecha: 2026-04-26

Total auditadas: 28
✅ VALID:     26
⚠️  DUBIOUS:   1  (React_JS_Coderhouse)
🔶 BAJA:       1  (vite — autor incorrecto en bib)
❌ NOT_FOUND:  0

| Clave                    | Afirmación (extracto)                                | Veredicto    |
|--------------------------|------------------------------------------------------|--------------|
| `React_JS_Coderhouse`    | "74,5% de apreciación según..."                      | ⚠️ DUBIOUS   |
| `react`                  | "Destaca en rendimiento y agiliza..."                | ✅ VALID      |
| `typescript`             | "Superconjunto de JavaScript que añade tipado..."    | ✅ VALID      |
| `vite`                   | "Tiempos de inicio y reconstrucción rápidos..."      | ✅ VALID 🔶   |
| `pnpm`                   | "Reduce el espacio en disco y acelera..."            | ✅ VALID      |
| `tailwind`               | "Permite personalizar la interfaz..."                | ✅ VALID      |
| `radix-ui`               | "Primitivas como diálogos, menús..."                 | ✅ VALID      |
| `zustand`                | "API minimalista basada en hooks..."                 | ✅ VALID      |
| `tanstack-query`         | "Gestiona el estado asíncrono del servidor..."       | ✅ VALID      |
| `axios`                  | "Cliente HTTP para peticiones a la API"              | ✅ VALID      |
| `jwt`                    | "Estándar para autenticación en apps web..."         | ✅ VALID      |
| `sentry`                 | "Plataforma de monitoreo de errores..."              | ✅ VALID      |
| `docker`                 | "Plataforma de contenedorización..."                 | ✅ VALID      |
| `uv`                     | "Gestor de paquetes y entornos virtuales..."         | ✅ VALID      |
| `uvicorn`                | "Servidor ASGI para Python..."                       | ✅ VALID      |
| `python`                 | "Lenguaje de programación interpretado..."           | ✅ VALID      |
| `fastapi`                | "Framework web moderno para Python..."               | ✅ VALID      |
| `sqlalchemy`             | "ORM utilizado para interactuar con la BD..."        | ✅ VALID      |
| `alembic`                | "Gestiona las migraciones de esquema..."             | ✅ VALID      |
| `prefect`                | "Plataforma de orquestación de workflows..."         | ✅ VALID      |
| `langchain`              | "Framework para aplicaciones con LLMs (LCEL)..."    | ✅ VALID      |
| `postgresql`             | "Sistema de gestión de bases de datos..."            | ✅ VALID      |
| `pgvector`               | "Extensión de PostgreSQL para vectores..."           | ✅ VALID      |
| `faster_whisper`         | "Reimplementación de Whisper con CTranslate2..."     | ✅ VALID      |
| `radford2022robust`      | "Modelo Whisper de OpenAI..."                        | ✅ VALID      |
| `hf_llama31_8b_instruct` | "Meta-Llama-3.1-8B-Instruct, desarrollado por..."   | ✅ VALID      |
| `hf_qwen25_72b_instruct` | "Qwen2.5-72B-Instruct como alternativa..."           | ✅ VALID      |
| `hf_mistral_7b_instruct_v03` | "Mistral-7B-Instruct-v0.3 como prototipo..."    | ✅ VALID      |

---

## Problemas encontrados

### ⚠️ DUBIOUS — `React_JS_Coderhouse`
La afirmación "74,5% de apreciación" corresponde realmente a los datos de la **Stack Overflow Developer Survey 2019** (categoría "Loved"). El artículo de Coderhouse probablemente cita ese dato, pero el contenido de la página no pudo cargarse para confirmarlo. Problemas:
1. La fuente primaria es Stack Overflow, no Coderhouse.
2. El dato es de 2019 — está desactualizado (React tiene métricas más recientes).
3. Coderhouse es un blog comercial, no una fuente académica.

**Recomendación**: Citar directamente la Stack Overflow Developer Survey correspondiente, o bien usar datos más recientes del mismo survey.

### 🔶 BAJA — `vite` (autor incorrecto en bib)
El campo `author` en la entrada bib dice `"Evan You and Vite Contributors"`, pero el copyright oficial en vite.dev dice `"VoidZero Inc. and Vite contributors"`. Evan You es el fundador de VoidZero y creador de Vite, pero la entidad legal es VoidZero Inc.

**Recomendación**: Cambiar a `author = "{VoidZero Inc. and Vite contributors}"` para mayor precisión. Es un problema menor.

---

Artefactos detallados en: `mine/citation-audits/2026-04-26-cap5/`
