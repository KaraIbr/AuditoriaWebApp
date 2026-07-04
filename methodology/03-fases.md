# 03. Fases del Ciclo de Auditoría

```
Fase 0: Scoping
    │
    ▼
Fase 1: Evaluación General (OWASP Top 10)
    │
    ▼
Fase 2: Evaluación Específica (checklists por dominio)
    │
    ▼
Fase 3: Generación de Hallazgos
    │
    ▼
Fase 4: Reporte y Cierre
```

---

## Fase 0: Scoping

**Objetivo:** Determinar qué auditar y con qué profundidad.

**Actividades:**
| Actividad | Entregable |
|-----------|------------|
| Perfilado de la aplicación | `scoping/01-identificacion.md` |
| Determinación de cobertura | `scoping/02-cobertura.md` |
| Selección de herramientas | `scoping/04-seleccion-herramientas.md` |
| Plan de auditoría | `scoping/03-plan-auditoria.md` |

**Output:** Scope document con tipo de app, tecnologías, dominios a auditar.

---

## Fase 1: Evaluación General

**Objetivo:** Evaluar OWASP Top 10 + ASVS L1 que aplican a toda web app.

| OWASP Top 10 | ASVS Nivel | Verificaciones Clave |
|-------------|------------|----------------------|
| A01 — Broken Access Control | L1 | IDOR, roles, admin funcs |
| A02 — Cryptographic Failures | L1 | TLS, hashing, secrets |
| A03 — Injection | L1 | XSS, SQLi, SSTI, Command |
| A04 — Insecure Design | L1 | Lógica, rate limiting |
| A05 — Security Misconfiguration | L1 | Headers, CORS, CSP |
| A06 — Vulnerable Components | L1 | SCA, dependencias |
| A07 — ID and Auth Failures | L1 | Auth, MFA, passwords |
| A08 — Data Integrity Failures | L1 | CSRF, CI/CD |
| A09 — Logging Failures | L1 | Logs, monitoreo |
| A10 — SSRF | L1 | Server-side request forgery |

**Output:** Evaluación general completada con observaciones iniciales.

---

## Fase 2: Evaluación Específica

**Objetivo:** Deep dive en los dominios identificados en scoping.

| Checklist | Dominio | Herramientas |
|-----------|---------|-------------|
| Auth | Autenticación | Semgrep, revisión manual |
| Session | Sesiones | Revisión manual, ZAP |
| Input | Validación de entrada | Semgrep, ZAP |
| Authorization | Autorización | Semgrep, manual |
| API | APIs | ZAP, Semgrep |
| Crypto | Criptografía | Semgrep |
| Infra | Infraestructura | Nuclei, ZAP |
| Data | Datos | Revisión manual |
| Deps | Dependencias | Trivy |
| CI/CD | Pipeline | Revisión manual |
| E-commerce | Pagos/carrito | ZAP, manual |
| Business Logic | Lógica de negocio | Manual |

**Output:** Checklists completados con hallazgos preliminares.

---

## Fase 3: Generación de Hallazgos

**Objetivo:** Documentar cada hallazgo de forma estructurada.

```yaml
ID: WA-2026-0001
Título: ""
Severidad: Critical | High | Medium | Low | Info
OWASP Top 10: A01 — Broken Access Control
OWASP WSTG: WSTG-INPV-01
ASVS: 1.2.3
Impacto: ""
Probabilidad: Alta | Media | Baja
Condición: ""
Evidencia: ""
Recomendación: ""
Estado: Open | Confirmed | Fixed | Accepted
```

**Output:** Archivos individuales en `findings/` (`.md` + `.json`).

---

## Fase 4: Reporte y Cierre

**Objetivo:** Consolidar todos los hallazgos en un reporte.

| Entregable | Formato | Audiencia |
|------------|---------|-----------|
| Reporte ejecutivo | `.md` | Stakeholders no técnicos |
| Reporte técnico | `.md` | Equipo de desarrollo |
| Findings JSON | `.json` | Procesamiento programático |

**Actividades de cierre:**
- Presentación de hallazgos
- Discusión de severidades
- Plan de remediación
- Firma de cierre
