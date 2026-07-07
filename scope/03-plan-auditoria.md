# Plan de Auditoría

## Datos de la auditoría

| Campo | Valor |
|-------|-------|
| **Proyecto** | VERP WebApp |
| **Branch** | audit/2026-07-verp-webapp |
| **Fecha inicio** | 2026-07-07 |
| **Fecha estimada fin** | 2026-07-20 |
| **Auditor líder** | Security Team |
| **Equipo** | Ventura Energy Dev Team |

## Checklists a completar

- [ ] 01-auth.md — IAM: JWT, bcrypt, rate limiting, brute force, MFA
- [ ] 02-session.md — Token storage (localStorage), refresh rotation, CSRF, logout
- [ ] 03-input.md — XSS (React), SQLi (SQLModel), SSRF (AI agent), file upload
- [ ] 04-authorization.md — RBAC (IAM+CRM), IDOR leads/proposals, privilege escalation
- [ ] 05-api.md — REST endpoints, CORS, rate limiting, error handling, input validation
- [ ] 06-crypto.md — JWT HS256 strength, bcrypt config, TLS, secrets management
- [ ] 07-infra.md — Security headers (CSP, HSTS), server config, CORS origins
- [ ] 08-data.md — PII (users, contacts), GDPR, audit logging, data at rest
- [ ] 09-deps.md — npm audit (frontend), pip audit (backend), Trivy SCA
- [ ] 10-ci-cd.md — GitHub Actions, pre-commit, SAST gates, secret scanning
- [ ] 12-business-logic.md — CRM pipeline, stage transitions, AI agent tool abuse, race conditions

## Herramientas a ejecutar

- [ ] Semgrep (SAST) — IAM src/ + CRM src/ + Frontend src/
- [ ] ZAP (DAST) — IAM http://localhost:8100 + CRM http://localhost:8000
- [ ] Trivy (SCA) — Full repo deps (npm + pip)
- [ ] Nuclei (Infra) — IAM + CRM endpoints
- [ ] npm audit — Frontend deps

## Cronograma

| Día | Actividad | Responsable |
|-----|-----------|-------------|
| 1 | Init branch + scope + automated scans (Semgrep, Trivy, ZAP, Nuclei) | Security Team |
| 2 | Auth + Session checklists (IAM JWT, Frontend token storage) | Security Team |
| 3 | Input + API checklists (XSS, SQLi, SSRF, CORS, rate limiting) | Security Team |
| 4 | Authorization checklist (RBAC, IDOR, privilege escalation) | Security Team |
| 5 | Business Logic checklist (CRM pipeline, AI agent abuse, race conditions) | Security Team |
| 6 | Crypto + Infra + Data + Deps + CI/CD checklists | Security Team |
| 7-8 | Finding generation + evidence + PoC documentation | Security Team |
| 9 | Report building + executive summary | Security Team |
| 10 | Review + finalize + present | Security Team |

## Profundidad

- [ ] L1 — Superficial
- [ ] L2 — Estándar
- [ ] L3 — Profunda
- [ ] L4 — Completa
