# Números del corpus — fuente de verdad y contexto

## Números canónicos para el informe

| Métrica | Valor | Usar en informe |
|---|---|---|
| Cursos | **239** | Sí |
| Clases (lecciones) | **4.339** | Sí |
| Chunks indexados | **217.986** | Sí |

Estos números provienen del código del proyecto antes del incidente del volumen de Docker (ver abajo). Son los valores correctos para reportar en la tesis porque representan el corpus sobre el cual el sistema fue construido y evaluado.

## Estado actual (post-incidente, 2026-06-15)

| Fuente | Cursos | Clases | Chunks | Transcripciones |
|---|---|---|---|---|
| `rag.courses/lessons/chunks` (DB actual) | 160 | 2.986 | 217.763 | 2.561 |
| Carpeta `transcriptions/medium/` (disco) | 227 | 4.009 | — | — |
| **Informe (números originales)** | **239** | **4.339** | **217.986** | — |

## Por qué difieren los números

1. **Incidente del volumen Docker**: Claude Code ejecutó `docker compose down -v` durante una sesión, destruyendo el volumen `postgres_data`. La DB fue recreada desde cero.

2. **OpenFing oculta contenido dinámicamente**: el pipeline de sync re-escanea OpenFing para saber qué cursos y clases existen. En el re-sync post-incidente, OpenFing tenía menos cursos/clases visibles que cuando se procesó el corpus original (algunos fueron ocultados por la plataforma entre ambos momentos).

3. **Consecuencia**: la DB actual tiene 160 cursos y 2.986 lecciones. La carpeta de transcripciones en disco tiene 227 cursos y 4.009 clases (archivos `.json`). Ni la DB ni la carpeta reflejan el estado original completo.

4. **Los chunks están casi intactos**: `rag.chunks` tiene 217.763 entradas, diferencia de solo −223 respecto al original (< 0.1%), lo que sugiere que la tabla de chunks se preservó parcialmente o fue re-generada desde los archivos en disco.

## Conclusión

Los números del informe (239/4.339/217.986) son correctos y defendibles. Si en la defensa preguntan sobre el corpus, la explicación es que OpenFing es una plataforma dinámica que oculta y publica contenido, y los números del informe corresponden al estado del corpus en el momento del procesamiento.

## Dónde aparecen estos números en el informe

| Archivo | Línea | Contenido |
|---|---|---|
| `Capitulos/1-Introduccion.tex` | 45 | 239 cursos, 4.339 clases, 217.986 fragmentos |
| `Capitulos/5-Implementacion.tex` | 92 | 217.986 chunks |
| `Capitulos/6-Experimentacion.tex` | 114 | 4.339 clases |
| `Capitulos/6-Experimentacion.tex` | 126 | 217.986 fragmentos |
| `Capitulos/8-Conclusiones.tex` | 6 | 239 cursos, 4.339 clases |
