# Reporte de Auditoría — VERP WebApp

**Cliente:** Ventura Energy
**Fecha:** 2026-07-07
**Auditor(es):** Security Team
**Tipo de app:** Web app (SPA + REST API + Microservicios)
**Profundidad:** L2 — Estándar

---

## Resumen Ejecutivo

Se realizó una auditoría de seguridad sobre la aplicación VERP WebApp, cubriendo los tres componentes principales: Frontend (React 19), IAM (FastAPI), y CRM (FastAPI + LangGraph AI Agent). La auditoría incluyó análisis estático de código (SAST) con Semgrep, revisión de dependencias con npm audit, y revisión manual de seguridad siguiendo 11 checklists basadas en OWASP WSTG/ASVS.

El código base muestra buenas prácticas de seguridad generales: uso consistente de ORM parametrizado (SQLModel), hashing de contraseñas con bcrypt, arquitectura de autorización RBAC bien definida con scope de recursos, y 0 hallazgos en SAST automatizado. Sin embargo, se identificaron áreas de mejora en autenticación, manejo de sesiones y configuración de seguridad.

| Severidad | Cantidad |
|-----------|----------|
| Critical | 0 |
| High | 0 |
| Medium | 2 |
| Low | 4 |
| Info | 0 |
| **Total** | **6** |

## OWASP Top 10 cubiertos

- [x] A01 — Broken Access Control
- [x] A02 — Cryptographic Failures
- [x] A03 — Injection
- [x] A04 — Insecure Design
- [x] A05 — Security Misconfiguration
- [x] A06 — Vulnerable Components
- [x] A07 — ID and Auth Failures
- [x] A08 — Data Integrity Failures
- [x] A09 — Logging Failures
- [x] A10 — SSRF

---

## Hallazgos por Severidad

### Medium

| ID | Título | Componente | OWASP |
|----|--------|-----------|-------|
| WA-2026-0001 | JWT tokens almacenados en localStorage | Frontend | A03, A05 |
| WA-2026-0002 | Falta de rate limiting en login | IAM | A07 |

### Low

| ID | Título | Componente | OWASP |
|----|--------|-----------|-------|
| WA-2026-0003 | Logout no invalida tokens server-side | IAM | A07 |
| WA-2026-0004 | Security headers ausentes | IAM + CRM | A05 |
| WA-2026-0005 | Dev mode bypass de autenticación | IAM | A05 |
| WA-2026-0006 | Default JWT secret key inseguro | IAM | A02 |

---

## Hallazgos Detallados

### WA-2026-0001 — JWT tokens almacenados en localStorage

- **Severidad:** Medium
- **OWASP:** A03 — Injection, A05 — Security Misconfiguration
- **Archivo:** `frontend/src/services/api-client.ts:5-6`
- **Descripción:** Los JWT de acceso y refresco se almacenan en localStorage del navegador, accesibles desde JavaScript mediante `localStorage.getItem('verp_access_token')`. Un XSS en la aplicación permitiría robar ambos tokens y suplantar al usuario.
- **Impacto:** Suplantación total de usuario, acceso a todas las APIs de IAM y CRM.
- **Recomendación:** Migrar a httpOnly cookies con Secure + SameSite=Strict. Implementar CSP restrictivo. Considerar patrón BFF.
- **Estado:** Open

### WA-2026-0002 — Falta de rate limiting en login

- **Severidad:** Medium
- **OWASP:** A07 — Identification and Authentication Failures
- **Archivo:** `IAM/src/iam/domains/auth/router.py:15-26`
- **Descripción:** El endpoint `/api/v1/auth/login` no implementa rate limiting, bloqueo de cuenta, ni captcha. Un atacante puede realizar ataques de fuerza bruta ilimitados.
- **Impacto:** Compromiso de cuentas por brute force.
- **Recomendación:** Implementar rate limiting con slowapi, bloqueo de cuenta tras 5 intentos fallidos, y logging de intentos fallidos.
- **Estado:** Open

### WA-2026-0003 — Logout no invalida tokens server-side

- **Severidad:** Low
- **OWASP:** A07 — Identification and Authentication Failures
- **Archivo:** `IAM/src/iam/domains/auth/router.py:39-43`
- **Descripción:** El endpoint `/api/v1/auth/logout` es un no-op. Los tokens JWT no se invalidan al cerrar sesión, manteniendo su validez hasta la expiración natural.
- **Impacto:** Un token robado sigue siendo válido post-logout.
- **Recomendación:** Implementar blacklist de tokens (Redis o DB) con el jti del JWT.
- **Estado:** Open

### WA-2026-0004 — Security headers ausentes

- **Severidad:** Low
- **OWASP:** A05 — Security Misconfiguration
- **Descripción:** No se configuran security headers HTTP (CSP, HSTS, X-Frame-Options, X-Content-Type-Options, Referrer-Policy) en IAM ni CRM.
- **Impacto:** Mayor exposición a XSS, clickjacking, downgrade attacks y MIME sniffing.
- **Recomendación:** Agregar middleware de seguridad para inyectar headers en todas las respuestas HTTP.
- **Estado:** Open

### WA-2026-0005 — Dev mode bypass de autenticación

- **Severidad:** Low
- **OWASP:** A05 — Security Misconfiguration
- **Archivo:** `IAM/src/iam/api/dependencies.py:42-45`
- **Descripción:** En modo development, si no se provee token JWT, la aplicación retorna automáticamente el usuario admin (ID 1) sin autenticación.
- **Impacto:** Si un servidor development está expuesto externamente, cualquier request obtiene acceso admin.
- **Recomendación:** Asegurar que servidores development no sean accesibles externamente. Documentar el riesgo.
- **Estado:** Open

### WA-2026-0006 — Default JWT secret key inseguro

- **Severidad:** Low
- **OWASP:** A02 — Cryptographic Failures
- **Archivo:** `IAM/src/iam/core/config.py:32`
- **Descripción:** El valor por defecto de `IAM_JWT_SECRET_KEY` es `"change-me-in-local-development"`.
- **Impacto:** Si no se cambia en producción, cualquiera puede forjar JWTs válidos.
- **Recomendación:** Cambiar el secret JWT antes del deploy. Usar secret manager o variable de entorno.
- **Estado:** Open

---

## Checklists Completadas

- [x] 01-auth.md — Autenticación (bcrypt ✅, rate limiting ❌, MFA ❌)
- [x] 02-session.md — Sesiones (JWT validado ✅, localStorage ⚠️, logout no-op ❌)
- [x] 03-input.md — Validación de entrada (ORM ✅, CSP ❌, AI agent ⚠️)
- [x] 04-authorization.md — Autorización (RBAC ✅, resource scoping ✅, IDOR protegido ✅)
- [x] 05-api.md — APIs (auth requerida ✅, rate limiting ❌, security headers ❌)
- [x] 06-crypto.md — Criptografía (bcrypt ✅, JWT ⚠️, TLS ❌)
- [x] 07-infra.md — Infraestructura (CORS ⚠️, security headers ❌, Docker N/A)
- [x] 08-data.md — Protección de datos (PII identificada ✅, cifrado en reposo ❌)
- [x] 09-deps.md — Dependencias (npm audit 0 vulns ✅, SCA no integrado ❌)
- [x] 10-ci-cd.md — CI/CD (pre-commit ✅, SAST gates ❌, secret scanning ❌)
- [ ] 11-ecommerce.md — No aplica
- [x] 12-business-logic.md — Lógica de negocio (pipeline validado ✅, race conditions ⚠️)

---

## Herramientas Ejecutadas

| Herramienta | Resultado |
|-------------|-----------|
| Semgrep (SAST) — IAM | ✅ 0 findings (36 files, 151 rules) |
| Semgrep (SAST) — CRM | ✅ 0 findings (107 files, 151 rules) |
| Semgrep (SAST) — Frontend | ✅ 0 findings (242 files, 74 rules) |
| npm audit | ✅ 0 vulnerabilities |
| ZAP (DAST) | ❌ No disponible (herramienta no instalada) |
| Trivy (SCA) | ❌ No disponible (herramienta no instalada) |
| Nuclei (Infra) | ❌ No disponible (herramienta no instalada) |

---

## Fortalezas Identificadas

1. **Arquitectura de autorización sólida** — RBAC con 4 roles en CRM y 8 permisos atómicos en IAM, con resource-scoped access checks en cada operación
2. **ORM parametrizado** — SQLModel/SQLAlchemy usado consistentemente, sin raw SQL identificado
3. **Bcrypt password hashing** — Contraseñas hasheadas con bcrypt via passlib
4. **SAST 0 findings** — Semgrep con reglas OWASP Top Ten no encontró vulnerabilidades
5. **npm audit 0 vulnerabilidades** — Dependencias frontend actualizadas sin CVEs conocidos
6. **Pipeline validation** — Stage transitions validadas con mapas explícitos y audit trail
7. **Bootstrapping seguro** — Primer usuario creado sin auth, luego requiere `iam.users.create`
8. **Auto-protección** — Usuarios no pueden modificar sus propios permisos ni desactivarse

---

## Plan de Acción

| Prioridad | Hallazgo | Componente | Acción Recomendada |
|-----------|----------|-----------|-------------------|
| Alta | WA-2026-0001 — Tokens en localStorage | Frontend | Migrar a httpOnly cookies + CSP |
| Alta | WA-2026-0002 — Sin rate limiting en login | IAM | Implementar rate limiting + bloqueo de cuenta |
| Media | WA-2026-0003 — Logout no-op | IAM | Implementar blacklist de tokens |
| Media | WA-2026-0004 — Security headers | IAM + CRM | Agregar middleware de security headers |
| Baja | WA-2026-0005 — Dev mode bypass | IAM | Documentar y asegurar acceso |
| Baja | WA-2026-0006 — JWT default secret | IAM | Cambiar secret antes de producción |

---

## Disclaimer

Esta auditoría se realizó sobre la versión del código y entorno indicados. Los hallazgos representan el estado de la aplicación al momento de la auditoría. Cambios posteriores pueden introducir nuevas vulnerabilidades. Las herramientas automatizadas (Semgrep, npm audit) se ejecutaron con reglas gratuitas; reglas adicionales podrían revelar más hallazgos.

---

## Firmas

| Rol | Nombre | Firma |
|-----|--------|-------|
| Auditor líder | Security Team | — |
| Cliente | Ventura Energy | — |
