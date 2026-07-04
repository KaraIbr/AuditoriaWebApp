# WebAudit — Web Application Audit Framework

**Framework abierto de auditoría para aplicaciones web, e-commerce y software interno**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

WebAudit es un framework de código abierto para auditar aplicaciones web tradicionales. Combina los estándares **OWASP WSTG**, **OWASP ASVS** y **OWASP Top 10** con herramientas automatizadas (SAST, DAST, SCA) y checklists específicas por dominio de seguridad.

Creado para que cualquier equipo de seguridad o desarrollador pueda auditar sus aplicaciones de forma estructurada, repetible y documentada.

---

## Índice

- [¿Cómo funciona?](#cómo-funciona)
- [Workflow con branches](#workflow-con-branches)
- [Arquitectura](#arquitectura)
- [Quick Start](#quick-start)
- [Checklists disponibles](#checklists-disponibles)
- [Estándares incluidos](#estándares-incluidos)
- [Sugerencias y hoja de ruta](#sugerencias-y-hoja-de-ruta)
- [Contribuye](#contribuye)
- [Licencia](#licencia)

---

## ¿Cómo funciona?

### 1. Metodología OWASP aplicada a web apps

Cada hallazgo se asocia a estándares OWASP:

| Estándar | Propósito |
|----------|-----------|
| **OWASP Top 10 (2021)** | Priorización de vulnerabilidades más críticas |
| **OWASP ASVS v4.0** | Niveles de verificación L1/L2/L3 |
| **OWASP WSTG** | Tests técnicos detallados (WSTG-xxx) |

### 2. Pipeline de auditoría

```
App Description → Scoping → General Assessment → Deep Dives → Findings → Report
```

| Fase | Qué se hace | Salida |
|------|------------|--------|
| **Scoping** | Identificar tipo de app, tecnologías, dominios a auditar | `scope.json` |
| **General Assessment** | Evaluar contra OWASP Top 10 y ASVS L1 | Checklist general |
| **Deep Dives** | Auditoría específica por dominio (auth, input, api, infra, etc.) | Checklists por dominio |
| **Findings** | Documentar cada hallazgo con PoC, severidad, OWASP ref | `.md` + `.json` |
| **Report** | Generar reporte ejecutivo y técnico | `reporte-final.md` |

### 3. Clasificación de riesgos

Severidad = **Impacto × Probabilidad**:

| Impacto \ Probabilidad | Alta | Media | Baja |
|------------------------|------|-------|------|
| **Crítico** | Critical | Critical | High |
| **Alto** | Critical | High | Medium |
| **Medio** | High | Medium | Low |
| **Bajo** | Medium | Low | Info |

### 4. Automatización

| Script | Función |
|--------|---------|
| `scripts/scope-analyzer.py` | Analiza descripción y stack tecnológico |
| `scripts/tools/semgrep-runner.py` | SAST con reglas OWASP |
| `scripts/tools/zap-runner.py` | DAST automatizado |
| `scripts/tools/trivy-runner.py` | SCA de dependencias |
| `scripts/tools/nuclei-runner.py` | Escaneo de infraestructura |
| `scripts/finding-generator.py` | Genera hallazgos estructurados |
| `scripts/report-builder.py` | Construye reporte final |

---

## Workflow con branches

Cada auditoría o revisión vive en su propia branch.

```
main                              # Framework base
├── audit/2026-07-ecommerce-app   # Auditoría completa
├── revision/2026-09-ecommerce-app  # Re-auditoría post-fixes
└── ...
```

Cada branch contiene:
```
scope/          → Alcance y plan
checklists/     → Checklists completadas
findings/       → Hallazgos (.md + .json)
reports/        → Reporte final
evidence/       → Screenshots, tool output
```

Iniciar una auditoría:
```bash
python scripts/init-audit.py --name "Mi app" --desc "E-commerce en React + Node.js"
```

Guía completa en [`docs/GIT-WORKFLOW.md`](docs/GIT-WORKFLOW.md).

---

## Arquitectura

```
├── methodology/        # Metodología OWASP + ASVS + compliance
├── scoping/            # Determinación de alcance y selección de herramientas
├── checklists/         # 12 dominios de seguridad (auth, input, api, etc.)
├── findings/           # Esquemas de hallazgos (JSON Schema)
├── scripts/            # Automatización: SAST, DAST, SCA, init-audit
├── templates/          # Templates de hallazgos y reportes
├── logs/               # Ejemplos de auditorías ejecutadas
├── docs/               # Documentación complementaria
└── branches/           # Benchmarks vs otras metodologías
```

---

## Quick Start

```bash
# 1. Clona
git clone ... && cd AuditoriaWebApp

# 2. Inicia una auditoría
python scripts/init-audit.py --name "E-commerce App" --desc "React + Node.js + PostgreSQL"

# 3. Analiza alcance
python scripts/scope-analyzer.py --desc "E-commerce con pagos, carrito, auth" --output scope.json

# 4. Corre SAST
python scripts/tools/semgrep-runner.py --path ./src --output analysis.json

# 5. Genera hallazgos
python scripts/finding-generator.py --data finding-data.json --output-dir ./findings

# 6. Reporte
python scripts/report-builder.py --findings-dir ./findings --output reports/reporte-final.md
```

---

## Checklists disponibles

| # | Checklist | Dominio | OWASP Ref |
|---|-----------|---------|-----------|
| 01 | Auth | Autenticación, MFA, OAuth, credenciales | A02, A04, A07 |
| 02 | Session | Cookies, JWT, CSRF, sesiones | A02, A05 |
| 03 | Input | XSS, SQLi, SSTI, SSRF, File upload | A01, A03 |
| 04 | Authorization | IDOR, RBAC, privilege escalation | A01, A04 |
| 05 | API | REST/GraphQL, rate limiting, CORS | A01, A05, A06 |
| 06 | Crypto | TLS, hashing, secrets, encryption | A02, A04 |
| 07 | Infra | Security headers, CSP, server config | A05, A06 |
| 08 | Data | PII, GDPR, data at rest, logs | A04, A05 |
| 09 | Deps | SCA, supply chain, known vulns | A06 |
| 10 | CI/CD | Pipeline, secret scanning, SAST gates | — |
| 11 | E-commerce | Pagos, carrito, cupones, órdenes | A01, A03, A04 |
| 12 | Business Logic | Flujos críticos, privilegios por contexto | A01, A04 |

---

## Estándares incluidos

| Estándar | Cobertura |
|----------|-----------|
| OWASP Top 10 (2021) | Mapeo completo a checklists |
| OWASP ASVS v4.0 | Niveles L1, L2, L3 referenciados |
| OWASP WSTG | Tests WSTG-xxx por dominio |
| NIST SP 800-115 | Guía complementaria de testing |
| PCI DSS | Referencias para e-commerce con pagos |
| ISO 27001:2022 | Mapeo de controles aplicables (A.9, A.10, A.12, A.14) |

---

## Sugerencias y hoja de ruta

### Prioridad alta

- **Integración CI/CD** — GitHub Action que corra el pipeline al abrir un PR
- **Dashboard visual** — UI web para progreso de auditoría
- **Playwright/Puppeteer tests** — Automatización de pruebas funcionales de seguridad
- **Más runners** — Dependency-check, Grype, Snyk CLI

### Prioridad media

- **Reporting en PDF** — Exportación a PDF con html2pdf
- **Multilenguaje** — Traducción de checklists a inglés/portugués
- **Template de reporte ejecutivo** — Para stakeholders no técnicos
- **Base de datos de hallazgos** — Catálogo comunitario de vulnerabilidades web

### Prioridad baja

- **VSCode extension** — Snippets y validación de hallazgos
- **Integración con Jira** — Exportar hallazgos a issues
- **Benchmarks** — Comparativa con metodologías empresariales (NIST, CIS)

---

## Contribuye

Cualquier persona puede contribuir:

- Reporta bugs → issue
- Sugiere checklists → issue
- Envía PRs → pull request
- Comparte auditorías → branch de ejemplo
- Traduce checklists → PR

---

## Licencia

MIT. Puedes usarlo, modificarlo y redistribuirlo libremente.

---

**Hecho para la comunidad de seguridad de aplicaciones**
