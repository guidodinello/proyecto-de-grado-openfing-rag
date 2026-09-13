# Auditoría de Citas — Cap. 2 (cambios del diff 2026-04-28)
Fecha: 2026-04-28

Auditoría de las citas agregadas o modificadas en el diff de `Nuestro/Capitulos/2-MarcoTeorico.tex`.

**Total auditadas**: 9 claves (13 ocurrencias contando usos múltiples)
- ✅ VALID:    7
- ⚠️  DUBIOUS: 2
- ❌ NOT_FOUND: 0

| Clave                      | Afirmación (extracto)                                 | Veredicto      |
|----------------------------|-------------------------------------------------------|----------------|
| `OpenFing`                 | "plataforma de videos educativos de la FING"          | ✅ VALID        |
| `Goodfellow-et-al-2016` ①  | "IA generativa orientada a producir texto/imágenes..."| ⚠️  DUBIOUS    |
| `Goodfellow-et-al-2016` ②  | "deep learning transformó el campo del PLN"           | ✅ VALID        |
| `Goodfellow-et-al-2016` ③  | "referencia exhaustiva sobre redes neuronales"        | ✅ VALID        |
| `SpeechandLanguageProcessing` | PLN, tokenización, LMs, embeddings, chunking       | ✅ VALID        |
| `Zhao2023LLMSurvey`        | "LLMs se distinguen por mayor complejidad y escala"   | ✅ VALID        |
| `Brown2020GPT3`            | "mejores prompts incluyen petición+rol+contexto+ej."  | ⚠️  DUBIOUS    |
| `reimers2019sbert`         | "SBERT produce representaciones aptas comparación"    | ✅ VALID        |
| `karpukhin2020dense`       | "DPR supera métodos dispersos en búsqueda abierta"    | ✅ VALID        |
| `vaswani2017attention`     | "arquitectura transformer para embeddings y Whisper"  | ✅ VALID        |
| `faster_whisper`           | "reimplementación Whisper con CTranslate2, VAD..."    | ✅ VALID        |

---

## Acciones recomendadas

### ⚠️ Goodfellow-et-al-2016 (ocurrencia 1 — IA generativa)
El libro de 2016 cubre modelos generativos técnicos (GANs, VAEs) pero no el concepto moderno de "IA generativa orientada a producir texto/imágenes/código/audio/video a partir de indicaciones en lenguaje natural". La formulación del texto es post-2020.

**Recomendación**: Reemplazar esta cita por una referencia a un survey reciente de IA generativa, por ejemplo:
```bibtex
@article{cao2023survey,
  author  = {Yihan Cao and Siyu Li and Yixin Liu and Zhiling Yan and Yutong Dai and Philip S. Yu and Lichao Sun},
  title   = {A Comprehensive Survey of AI-Generated Content (AIGC): A History of Generative AI from GAN to ChatGPT},
  journal = {arXiv preprint arXiv:2303.04226},
  year    = {2023},
  url     = {https://arxiv.org/abs/2303.04226}
}
```

### ⚠️ Brown2020GPT3 — afirmación sobre estructura de prompts
El paper de Brown et al. (GPT-3) introduce el concepto de few-shot prompting pero **no** establece que "los mejores prompts incluyen petición + instrucciones + contexto + rol + ejemplos". Esta taxonomía proviene de la literatura de prompt engineering, no del paper de GPT-3.

**Opción A**: Mantener la cita pero acotar la afirmación solo a lo que el paper dice: "proveer ejemplos en el prompt (few-shot) mejora significativamente el rendimiento del modelo."

**Opción B**: Agregar una cita adicional de prompt engineering, como:
```bibtex
@article{white2023promptpatterns,
  author  = {Jules White and Quchen Fu and Sam Hays and Michael Sandborn and Carlos Olea and Henry Gilbert and Ashraf Elnashar and Jesse Spencer-Smith and Douglas C. Schmidt},
  title   = {A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT},
  journal = {arXiv preprint arXiv:2302.11382},
  year    = {2023},
  url     = {https://arxiv.org/abs/2302.11382}
}
```

Artefactos en: `mine/citation-audits/2026-04-28-cap2-diff/`
