# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

LaTeX thesis document for a grade project (Proyecto de Grado) at FING/UdelaR. The project implements a Generative AI assistant over OpenFing educational content using a RAG architecture. Authors: Diego Amorena and Guido Dinello. Supervisors: Luis Chiruzzo and Libertad Tansinni.

The source code for the system itself lives in a sibling directory (`../tesis`), not here.

## Document Structure

```
main.tex                  # Root document, includes all chapters
prgrado.cls               # Custom FING thesis class
referencias.bib           # Global bibliography
Nuestro/
  Capitulos/              # Main chapters (numbered 0–8)
    0-Resumen.tex
    1-Introduccion.tex
    2-MarcoTeorico.tex
    3-RequisitosDelSistema.tex
    4-Arquitectura.tex
    5-Implementacion.tex
    6-Experimentacion.tex
    7-TrabajoAFuturo.tex
    8-Conclusiones.tex
  Anexos/                 # Appendices (numbered 0–4)
    0-IDM.tex
    1-Prompting.tex
    2-EstimacionesParaOpenFing.tex
    3-Manual_De_Usuario.tex
    4-Recursos.tex
  Imagenes/               # Figures used in chapters
  Tablas/                 # Table definitions
figs/                     # Additional figures
build/                    # Compiled output (gitignored)
```

## Writing Guidelines

Consult these files in `mine/` at the start of every writing session:

- `mine/lineamientos-informe.md` — digest of the official INCO report guide (`GuiaInfProyGrado.pdf`): required structure, chapter contents, extension (40–80 pages), and citation rules (author, title, place, year; URLs must include last-access date).
- `mine/overview.md` — summary of what each chapter covers; use it to understand context before editing any section.
- `mine/progreso.md` — current completion state per chapter; check it to know what is done and what still needs work.
- `mine/todos.md` — concrete pending tasks per chapter; the starting point for any writing session.
- `mine/detalles-tecnicos-codigo.md` — concrete technical details extracted from the `../tesis` codebase (models, parameters, dataset stats, stack); use as source of truth when writing Caps. 2, 4, 5, and 6.

## Writing Style

- **No em dashes** (—): usar comas o puntos en su lugar.
- **Evitar los dos puntos** (:) como conector de oraciones: preferir comas o punto y seguido.
- Estilo general: prosa académica continua, sin listas innecesarias dentro del cuerpo del texto.
- **Conectores consecutivos**: cuando una oración expresa una consecuencia de la anterior, hacer la relación explícita con "así", "de este modo", "por tanto", etc. en lugar de dejarla implícita en un gerundio suelto. Ejemplo: preferir "…entrenados para optimizar X, produciendo así vectores aptos para Y" sobre "…produciendo vectores aptos para Y".
- **Marco Teórico vs. Implementación**: el Marco Teórico explica *qué es* y *por qué* se usa una tecnología; los parámetros concretos y decisiones de configuración van en Cap. 5 (Implementación) o Cap. 6 (Experimentación). No repetir detalles de implementación en el Marco Teórico.
- **Nivel de detalle técnico**: evitar términos de arquitectura interna (ej. "redes siamesas", "funciones de pérdida contrastiva") cuando no son necesarios para que el lector entienda el concepto. Preferir descripciones funcionales sobre descripciones de implementación.

## Conventions

- Figures go in `Nuestro/Imagenes/`, referenced with `\includegraphics`
- Citations use `\cite{}` referencing keys in `referencias.bib`
- The class file `prgrado.cls` defines the document format — avoid overriding its styles directly; add customizations in `main.tex` preamble if needed
- Spanish is the document language

## Overleaf sync

This repo is edited in parallel with an Overleaf project. The authors edit mostly in Overleaf;
the local repo receives snapshots via `./scripts/sync-overleaf.sh <zip>` (an `rsync` from a
downloaded zip, **no `--delete`**), so the local git history has **only sync snapshots, not the
intermediate edits made in Overleaf**. `git log`/`git log -S` on this repo is therefore an
incomplete record of what actually happened to a paragraph.

Before running the sync, everything uncommitted must be committed (the rsync overwrites
`.tex`/`.bib`). Before assuming Overleaf is ahead or behind, extract the zip to a temp dir and
`diff` it against `HEAD` — do not run the sync blindly.

### Verify before assuming — do not undo/redo edits without understanding why they were made

When something looks wrong, missing, or "lost" (a paragraph gone, a section shorter than
expected, a change that seems like a regression), **investigate the real history before
touching it.** A paragraph that is absent may have been removed *deliberately* — e.g. in
response to tutor feedback — and re-adding it silently would reintroduce something the authors
explicitly cut. This nearly happened once with a "trabajo a futuro" paragraph on automated
testing that Diego had removed on purpose.

The authoritative source for Overleaf history is the **diff API**, not the local git log:

```
GET https://www.overleaf.com/project/<PROJECT_ID>/diff?from=<v>&to=<v>&pathname=<url-encoded path>
```

- `PROJECT_ID`: `67b9ca8f36dc38d47bc61e3b`
- Headers needed (ask the user to copy these from their browser devtools while logged in):
  `Cookie: overleaf_session2=...; GCLB=...` and `X-Csrf-Token: ...`
- Response: JSON `{"diff":[{"u":"unchanged"},{"i":"inserted"},{"d":"deleted"}, ...]}`.
  Reconstruct a file's content at version `to` by concatenating all `u` + `i` segments.
- Version numbers come from a saved copy of the history panel HTML:
  the dropdown button ids are `history-version-dropdown-toggle-<lo>_<hi>`, and each version
  block lists its date, author, and changed files. Ask the user to paste the panel HTML into
  `mine/comments/html-overleaf-history/` when a deep history check is needed.

Workflow: bisect across versions to find exactly when a line appeared or disappeared, read the
`i`/`d` segments of that one version to see *what else* changed alongside it (a targeted edit
vs. a bulk restructure tells you whether it was intentional), identify the author and date, and
**bring that to the user before making any change** — especially before `git revert`,
re-adding removed content, or "fixing" something that may not be broken.
