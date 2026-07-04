# 05. Mapeo OWASP ↔ WebAudit

## OWASP Top 10 (2021) ↔ ASVS ↔ WSTG ↔ Checklists

| # | OWASP Top 10 | ASVS L1 | WSTG | Checklist WebAudit |
|---|-------------|---------|------|--------------------|
| A01 | Broken Access Control | V1, V4 | WSTG-AUTHZ-xx | `04-authorization.md` |
| A02 | Cryptographic Failures | V2, V6 | WSTG-CRYP-xx | `06-crypto.md` |
| A03 | Injection | V5 | WSTG-INPV-xx | `03-input.md` |
| A04 | Insecure Design | V1, V4, V11 | — | `12-business-logic.md` |
| A05 | Security Misconfiguration | V2, V12, V14 | WSTG-CONF-xx | `07-infra.md` |
| A06 | Vulnerable Components | V14 | — | `09-deps.md` |
| A07 | ID and Auth Failures | V2, V3 | WSTG-AUTH-xx | `01-auth.md` |
| A08 | Data Integrity Failures | V5, V13 | WSTG-SESS-xx | `10-ci-cd.md`, `02-session.md` |
| A09 | Logging Failures | V7 | WSTG-ERRH-xx | `08-data.md` |
| A10 | SSRF | V11 | WSTG-INPV-xx | `03-input.md`, `05-api.md` |

---

## OWASP ASVS v4.0 — Niveles de verificación

| Nivel | Para quién | Cobertura WebAudit |
|-------|-----------|-------------------|
| **L1** | Todas las apps (mínimo indispensable) | Checklists 01-09 |
| **L2** | Apps que manejan datos sensibles | Checklists 01-12 |
| **L3** | Apps críticas (financieras, salud, infra) | L2 + herramientas + pentest |

---

## WSTG por checklist

| Checklist | WSTG IDs principales |
|-----------|---------------------|
| Auth | WSTG-AUTH-01 al WSTG-AUTH-10 |
| Session | WSTG-SESS-01 al WSTG-SESS-09 |
| Input | WSTG-INPV-01 al WSTG-INPV-18 |
| Authorization | WSTG-AUTHZ-01 al WSTG-AUTHZ-04 |
| API | WSTG-APIT-01 al WSTG-APIT-02 |
| Crypto | WSTG-CRYP-01 al WSTG-CRYP-04 |
| Infra | WSTG-CONF-01 al WSTG-CONF-10 |
| Data | WSTG-DATA-01 al WSTG-DATA-03 |

---

## Cómo usar este mapeo

1. **En scoping** — Identificar qué OWASP categorías aplican según el tipo de app
2. **En checklists** — Cada ítem referencia OWASP + ASVS + WSTG
3. **En hallazgos** — Cada finding incluye: `OWASP-A03` + `WSTG-INPV-01` + `ASVS 5.1.1`
4. **En reporte** — Tabla de cobertura OWASP Top 10 + ASVS nivel alcanzado
