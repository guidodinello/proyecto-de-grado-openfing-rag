# Auditoría de Citas — Nuevas entradas en referencias.bib (git diff HEAD~1)
Fecha: 2026-04-26

Contexto: Cap. 5 (Implementación) — bibliotecas y herramientas del stack técnico.

Total auditadas: 19
✅ VALID:     18
⚠️  DUBIOUS:  1
❌ NOT_FOUND: 0

| Clave                     | Afirmación (extracto)                              | Veredicto    |
|---------------------------|----------------------------------------------------|--------------|
| huggingface_inference_api | "...acceder al modelo a través de una API REST..." | ⚠️ DUBIOUS  |
| ollama                    | "...ejecuta modelos cuantizados en la máquina..."  | ✅ VALID     |
| pgvector                  | "...almacenar y consultar vectores de embeddings"  | ✅ VALID     |
| zustand                   | "...API minimalista basada en hooks..."            | ✅ VALID     |
| tanstack-query            | "...estado asíncrono del servidor, el caché..."    | ✅ VALID     |
| axios                     | "...peticiones a la API del backend"               | ✅ VALID     |
| vite                      | "...módulos ES nativos y procesamiento bajo demanda" | ✅ VALID   |
| pnpm                      | "...almacén centralizado con enlaces simbólicos"   | ✅ VALID     |
| shadcn-ui                 | "...componentes se generan en el código fuente..." | ✅ VALID     |
| radix-ui                  | "...primitivas accesibles y sin estilos..."        | ✅ VALID     |
| llm-ui                    | "...streaming de tokens, Markdown progresivo..."   | ✅ VALID     |
| sentry                    | "...captura excepciones y trazas de pila..."       | ✅ VALID     |
| sqlalchemy                | "...ORM con soporte nativo para async (v2.0)..."   | ✅ VALID     |
| alembic                   | "...migraciones de esquema incremental y versionada" | ✅ VALID  |
| prefect                   | "...reintentos automáticos, monitoreo de ejecuciones" | ✅ VALID |
| yt-dlp                    | "...extraer audio en el mejor formato disponible"  | ✅ VALID     |
| beautifulsoup4            | "...estructura jerárquica de cursos en OpenFing"   | ✅ VALID     |
| aiohttp                   | "...múltiples peticiones de forma concurrente..."  | ✅ VALID     |
| faster_whisper            | "...reduce memoria y acelera vs. implementación original" | ✅ VALID |

## Detalle del caso DUBIOUS

### huggingface_inference_api
- **Problema**: El producto fue renombrado. La página https://huggingface.co/docs/api-inference/ ahora se llama **"Inference Providers"**, no "Inference API". El título en el bib (`Hugging Face Inference API`) ya no corresponde al nombre oficial.
- **La afirmación es correcta**: la funcionalidad descrita (acceso a modelos vía REST sin gestionar GPU) sigue siendo precisa.
- **Corrección sugerida**:

```bibtex
@misc{huggingface_inference_api,
  author       = {{Hugging Face}},
  title        = {Hugging Face Inference Providers},
  howpublished = {\url{https://huggingface.co/docs/api-inference/}},
  year         = {2026},
  note         = {Último acceso: 26 de abril de 2026}
}
```

## Notas generales
- Todas las 19 URLs resuelven correctamente.
- Los autores y años son precisos en todos los casos.
- zustand, tanstack-query y axios ya habían sido auditados en contexto de Cap. 4 (carpeta `2026-04-26-frontend-libs`); los veredictos son consistentes.
- llm-ui: el autor real es Richard Gill; el bib usa "{llm-ui contributors}" que es genérico pero aceptable.
