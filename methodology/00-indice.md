# WebAudit Framework — Índice General

**Versión:** 1.0.0
**Estándar Base:** OWASP Top 10 + OWASP ASVS + OWASP WSTG
**Última Actualización:** 2026-07-03

---

## Methodology

| # | Archivo | Descripción |
|---|---------|-------------|
| 01 | `01-introduccion.md` | Introducción, propósito, guía de uso del framework |
| 02 | `02-principios.md` | Principios fundamentales de auditoría de aplicaciones web |
| 03 | `03-fases.md` | Descripción del ciclo de auditoría en 5 fases |
| 04 | `04-clasificacion-riesgos.md` | Matriz de severidad, impacto y probabilidad |
| 05 | `05-mapping-owasp.md` | Mapeo OWASP Top 10 + WSTG + ASVS |
| 06 | `06-compliance.md` | Referencias a ISO 27001, PCI DSS, GDPR |

## Scoping

| # | Archivo | Descripción |
|---|---------|-------------|
| 01 | `01-identificacion.md` | Template de identificación y perfilado de la aplicación |
| 02 | `02-cobertura.md` | Determinación de cobertura por tipo de aplicación |
| 03 | `03-plan-auditoria.md` | Plan de auditoría según alcance determinado |
| 04 | `04-seleccion-herramientas.md` | Guía de selección de herramientas SAST/DAST/SCA |

## Checklists

| # | Archivo | Dominio |
|---|---------|---------|
| 01 | `01-auth.md` | Autenticación |
| 02 | `02-session.md` | Manejo de sesiones |
| 03 | `03-input.md` | Validación de entrada |
| 04 | `04-authorization.md` | Autorización |
| 05 | `05-api.md` | APIs |
| 06 | `06-crypto.md` | Criptografía |
| 07 | `07-infra.md` | Infraestructura |
| 08 | `08-data.md` | Protección de datos |
| 09 | `09-deps.md` | Dependencias |
| 10 | `10-ci-cd.md` | CI/CD |
| 11 | `11-ecommerce.md` | E-commerce |
| 12 | `12-business-logic.md` | Lógica de negocio |

## Findings

| # | Archivo | Descripción |
|---|---------|-------------|
| 01 | `finding-schema.json` | JSON Schema para findings estructurados |
| 02 | `finding-categorias.json` | Catálogo de categorías de hallazgos |
| 03 | `severidad.md` | Clasificación detallada de severidad |

## Scripts

| # | Archivo | Descripción |
|---|---------|-------------|
| 01 | `scope-analyzer.py` | Analiza descripción y stack tecnológico |
| 02 | `finding-generator.py` | Genera hallazgos en .md y .json |
| 03 | `report-builder.py` | Construye reporte final |
| 04 | `tools/semgrep-runner.py` | SAST con Semgrep |
| 05 | `tools/zap-runner.py` | DAST con OWASP ZAP |
| 06 | `tools/trivy-runner.py` | SCA con Trivy |
| 07 | `tools/nuclei-runner.py` | Escaneo de infra con Nuclei |

## Docs

| # | Archivo | Descripción |
|---|---------|-------------|
| 01 | `docs/GIT-WORKFLOW.md` | Flujo de trabajo con branches para auditorías |
