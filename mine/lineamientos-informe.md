# Lineamientos para el Informe Final de Proyecto de Grado

Resumen de la guía oficial del INCO/FING: `GuiaInfProyGrado.pdf`.

## Estructura requerida

### Elementos preliminares

- **Carátula**: título del proyecto, nombres de los estudiantes, nombres de los supervisores, cometido (ej. "Informe de Proyecto de Grado presentado al Tribunal Evaluador como requisito de graduación de la carrera Ingeniería en Computación"), lugar y año.
- **Resumen** (200–500 palabras), en página separada, seguido de palabras clave:
  - Debe dar una idea completa del proyecto: formalismos, técnicas, herramientas y lenguajes utilizados.
  - Debe describir la **solución** y su evaluación, no solo el problema.
  - **No** incluir referencias bibliográficas ni referencias a otras partes del informe.
  - **No** usar acrónimos sin explicar su significado.
- **Tabla de contenido**, en página separada.

### Extensión y organización

**40–80 páginas** aproximadamente, organizado en capítulos y/o secciones.

### Capítulos obligatorios

1. **Introducción**
   - Motivación del trabajo
   - Planteamiento y definición del problema
   - Objetivos: general del proyecto y específicos
   - Resultados esperados
   - Conclusiones resumidas
   - Organización general del documento

2. **Revisión de antecedentes**
   - Productos, procesos y publicaciones relacionadas (nivel académico y comercial)
   - Puede incluir introducción a los conceptos necesarios para entender el trabajo

3. **Parte central** (aporte propio)
   - Requerimientos, análisis y diseño de la solución
   - Decisiones de implementación (los detalles de código van a los anexos)

4. **Experimentación**
   - Casos de prueba y resultados obtenidos
   - Análisis de resultados, puede incluir comparaciones

5. **Conclusiones y trabajo futuro**
   - Evaluación de resultados alcanzados y dificultades encontradas
   - Contraste entre lo planteado y lo realizado
   - Aportes del proyecto
   - Posibles extensiones
   - Autocrítica (tiempo, recursos, prioridades)
   - Información sobre gestión del proyecto (si aplica)

6. **Referencias bibliográficas** (ver sección de citas abajo)

7. **Anexos**
   - Material complementario no fundamental para entender el trabajo
   - Para proyectos de software: **incluir manual de usuario** (obligatorio)

---

## Citas y referencias bibliográficas

La guía establece:

> "El material utilizado debe ser todo citado y referenciado, con **autores, título, lugar de publicación y año**. En caso de material en formato web, se establece la **dirección de la página web junto a la fecha del último acceso**."

### Aplicación práctica en este proyecto (LaTeX/BibTeX)

- Citar con `\cite{clave}` en el texto.
- Todas las entradas en `referencias.bib` deben incluir: autor(es), título, lugar/editorial y año.
- Referencias web (`@misc` u `@online`): incluir `url` y `urldate` (o equivalente en el campo `note`) con la **fecha de último acceso**.
- No se especifica un estilo concreto (APA, IEEE, etc.) en la guía, pero mantener consistencia en todo el documento.
