# Requisito nuevo — Declaración de Uso de Herramientas de IA

Fuente: mensaje de Luis (WhatsApp). Requisito nuevo de los proyectos de grado, no estaba
cuando arrancamos.

Documento oficial: **"Guía para Uso ético y crítico de Herramientas de Inteligencia
Artificial en los Proyectos de Grado"** (v2026 V2), 6 páginas. Copia local en
`mine/comments/Uso-etico-y-critico-de-la-IA-en-el-PG-2026.pdf`.
URL EVA: `https://eva.fing.edu.uy/pluginfile.php/116451/mod_resource/content/2/Uso%20%C3%A9tico%20de%20la%20IA%20en%20el%20PG%20-%202026.pdf`

La guía se apoya en tres documentos institucionales: el programa de la UC, la GUIAFI (Guía
para el uso ético y crítico de IA en las unidades curriculares de FIng) y los PRIA
(Principios Rectores para el uso de IA en la UdelaR, 11 principios).

## Nivel de uso definido para el PG (§2.1)

> "Se permite el uso crítico moderado/extensivo de IA generativa con la declaración de uso
> adecuada", respetando las directivas del documento.

O sea: se puede usar bastante, pero hay que declararlo bien y hacerse cargo de la autoría.

## Lo que hay que agregar al informe (§2.2.4 "Confección del Informe Final") — texto verbatim

> **Transparencia e Integridad Académica.** Los estudiantes deberán incluir un apartado
> obligatorio titulado "Declaración de Uso de Herramientas de IA". Allí deberán detallar en
> qué tareas específicas se utilizó soporte automatizado (por ejemplo: revisión bibliográfica,
> corrección de estilo, traducción, optimización de algoritmos o generación de código
> secundario), qué herramientas se emplearon (ChatGPT, Gemini, GitHub Copilot, Claude Code,
> etc.), una breve descripción de los criterios utilizados y el impacto en el trabajo
> realizado (por ejemplo, se pueden brindar métricas de porcentaje de código generado con IA,
> algo análogo para otros entregables).

> **Evitar delegar secciones reflexivas.** Las secciones críticas del proyecto e informe que
> buscan demostrar la madurez e idoneidad del futuro ingeniero —tales como Conclusiones,
> Discusión de Resultados, Análisis de Impacto Económico/Social y Trabajo Futuro— deben ser de
> autoría del estudiante. El equipo docente o el tribunal considerará una falta grave si estas
> secciones muestran indicios de haber sido redactadas de forma automatizada, sin un proceso
> de asimilación e interpretación por parte del estudiante.

### Contenido mínimo del apartado (derivado del texto)

1. Tareas específicas en que se usó IA (no genérico: qué tarea concreta).
2. Herramientas empleadas, nombradas.
3. Criterios de uso (cómo se decidió usarla, para qué sí y para qué no).
4. Impacto en el trabajo.
5. Opcional: métrica de % de código / texto generado con IA.

## Dónde va

Luis: "yo la pondría en el capítulo de introducción, antes de 'Organización del documento'".

Nueva `\section{Declaración de Uso de Herramientas de IA}` en
`Nuestro/Capitulos/1-Introduccion.tex`, entre `\section{Aportes del Proyecto}` y
`\section{Organización del Documento}` (línea 48 actual). No es capítulo, no hace falta tocar
la sección de Organización.

## Otras directivas relevantes de la guía (para tener presente al redactar)

- **§2.2.1 Oportunidad y monitoreo**: idealmente se acuerda con el tutor un plan de uso al
  inicio y se revisa durante el proyecto. Minimizar "deuda cognitiva": entender siempre las
  decisiones, propias o de la herramienta.
- **§2.2.2 Responsabilidad sobre la autoría**: el estudiante rinde cuentas del uso de IA en la
  defensa. La IA no sustituye el juicio humano; hay que verificar salidas (errores,
  alucinaciones, sesgos). Plagio por ideas de terceros sin atribución = falta grave.
- **§2.2.3 Desarrollo técnico**: el uso de asistentes debe limitarse a soporte (código base,
  tests, refactorización). La lógica del núcleo (elección de metodologías, decisiones de
  ingeniería) no se puede delegar. Todo fallo/alucinación/vulnerabilidad introducida por IA y
  no revisada críticamente es falta del estudiante. Considerar datos sensibles, propiedad
  intelectual (código/datos/textos cargados en herramientas de terceros no deben vulnerar
  derechos de UdelaR ni de empresas asociadas), y preferir software abierto / desarrollos
  propios de UdelaR cuando sea posible.
- **§2.3.1 Evaluación oral**: el tribunal evaluará si informe y defensa son transparentes
  respecto al uso de IA, y si hay incapacidad de explicar partes importantes (texto,
  resultados). Puede pedir reentrega, penalizar nota o reprobar la UC.

## Qué tenemos que decidir / juntar antes de redactar

- [ ] Lista real de herramientas de IA usadas por cada integrante (Diego y Guido), tarea por
  tarea: código del sistema (`../tesis`), redacción del informe, revisión bibliográfica,
  pipeline de transcripción/experimentos, diagramas.
- [ ] Para cada una: en qué tarea concreta, con qué criterio, qué se revisó/validó a mano,
  qué impacto tuvo.
- [ ] Decidir si incluimos la métrica opcional de % de código generado con IA y cómo se estima.
- [ ] Confirmar que no se acordó un "plan de uso" formal con los tutores al inicio (§2.2.1);
  si Luis/Libertad lo mencionan, referenciarlo.
- [ ] La sección la redacta el estudiante (es la sección de integridad); Claude puede ayudar
  con estructura/estilo, no con el contenido ni los criterios.
- [ ] Pasada final a Conclusiones, Trabajo a Futuro y discusión de resultados (Cap. 6/7/8) con
  el criterio "secciones reflexivas de autoría del estudiante" en mente.

## Estado

- [x] Sección redactada e insertada en `1-Introduccion.tex` (entre "Aportes del Proyecto" y
  "Organización del Documento"), label `section:1-Declaración de Uso de IA` — 2026-08-30.
  Decisiones tomadas: no se incluye porcentaje de código IA (se apela al historial del repo);
  los criterios se presentan como conversados en las reuniones de seguimiento, sin plan
  formal previo.
- [ ] Diego: agregar párrafo sobre Gemini si corresponde (hay un `% TODO (Diego)` en el .tex
  en el lugar exacto).
- [ ] Revisada con Luis y Libertad antes de la entrega final.
- [ ] Compilar en Overleaf y verificar que el `\autoref` / label resuelvan.
