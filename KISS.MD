# WebAudit — KISS

**Keep It Simple.** Auditoría de aplicaciones web en 5 pasos.

---

## ¿Qué es esto?

Un toolkit para auditar aplicaciones web, APIs, e-commerce y software interno. Basado en OWASP Top 10 + OWASP WSTG + OWASP ASVS.

Lo clonas, creas una branch por cada auditoría, y tienes todo el historial.

---

## Auditoría en 5 pasos

```
1. Crea tu branch
2. Define el alcance
3. Corre las checklists
4. Documenta hallazgos
5. Genera el reporte
```

### 1. Crea tu branch

```bash
git checkout -b audit/2026-07-mi-app
```

Cada auditoría vive en su propia branch. Historial completo y evidencia.

### 2. Define el alcance

```bash
python scripts/scope-analyzer.py \
  --desc "Describe tu app aquí" \
  --tech "react,nodejs,postgres" \
  --output scope/scope.json
```

Esto detecta el tipo de app, tecnologías y recomienda checklists.

### 3. Corre las checklists

| Checklist | Evalúa |
|-----------|--------|
| Auth | Autenticación, MFA, OAuth, credenciales |
| Session | Cookies, JWT, CSRF, sesiones |
| Input | XSS, SQLi, SSTI, SSRF, File upload |
| Authorization | IDOR, roles, privilege escalation |
| API | REST/GraphQL, rate limiting, CORS |
| Crypto | TLS, hashing, secrets management |
| Infra | Security headers, CSP, server config |
| Data | PII, GDPR, datos en reposo |
| Deps | Dependencias, SCA, supply chain |
| CI/CD | SAST en pipeline, secret scanning |
| E-commerce | Pagos, carrito, cupones, órdenes |
| Business Logic | Flujos críticos, privilegios |

Cada ítem tiene criterios ✅/❌.

### 4. Documenta hallazgos

Cada vulnerabilidad → un `.md` + `.json`:

```yaml
Severidad: Critical | High | Medium | Low | Info
OWASP: A01 — Broken Access Control
Estado: Open | Confirmed | Fixed | Accepted
```

### 5. Genera el reporte

```bash
python scripts/report-builder.py \
  --findings-dir ./findings \
  --output reports/reporte-final.md
```

---

## Severidad rápida

| ¿Qué pasó? | Severidad |
|------------|-----------|
| Acceso completo a DB o admin sin autenticación | **Critical** |
| El atacante obtiene datos de otros usuarios | **High** |
| Exposición de información sensible sin explotación directa | **Medium** |
| Falta de buena práctica, sin impacto demostrable | **Low** |
| Sugerencia / observación | **Info** |

---

## ¿Cómo aportar?

| Acción | Cómo |
|--------|------|
| Reportar bug | Abre un issue |
| Sugerir mejora | Abre un issue |
| Enviar código | Pull Request |
| Compartir auditoría | Crea tu branch |

---

**License MIT — Hecho para la comunidad de seguridad de aplicaciones**
