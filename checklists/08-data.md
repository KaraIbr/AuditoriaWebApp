# Checklist: Protección de Datos

**OWASP Top 10:** A04 — Insecure Design, A09 — Logging Failures
**ASVS:** V7, V8
**WSTG:** WSTG-DATA-01 al WSTG-DATA-03

## PII / Datos personales

- [x] ¿Se recolecta solo la data mínima necesaria? — Users: email, name, password | Contacts: name, phone, email
- [ ] ¿Los usuarios pueden ver/exportar sus datos? — IAM `GET /users/me` disponible
- [ ] ¿Los usuarios pueden eliminar su cuenta/datos? — `delete_user` requiere `iam.users.deactivate`
- [ ] ¿Hay consentimiento explícito para recolección? — No implementado
- [ ] ¿Política de privacidad accesible? — No implementado

## Datos en reposo

- [ ] ¿Datos sensibles cifrados en DB? — Passwords hasheadas con bcrypt, resto en texto plano
- [ ] ¿Backups cifrados? — Sin backup config
- [ ] ¿Los datos temporales se eliminan? — Sin política visible
- [x] ¿Las tablas con PII están identificadas? — `iam_user`, `contact`, `lead`, `proposal`

## Logging

- [x] ¿No se loguean datos sensibles (passwords, tokens)? — CRM usa `structlog` (JSON structured)
- [x] ¿Los logs tienen información de auditoría (quién, qué, cuándo)? — Pipeline stage transitions audit trail
- [ ] ¿Los logs están protegidos contra modificación? — No implementado
- [ ] ¿Hay retención de logs definida? — No implementado

## Eliminación de datos

- [ ] ¿Hay proceso para eliminar datos de usuarios? — Hard delete disponible via API
- [ ] ¿Se eliminan datos de tablas temporales? — No identificado
- [ ] ¿Cache se invalida al eliminar datos? — Sin cache layer

## Observaciones

- **PII presente** en IAM (users), CRM (contacts, leads, proposals)
- **Passwords hasheadas** con bcrypt — ✅
- **Audit trail** en pipeline stage transitions — ✅
- **Sin cifrado en reposo** para datos de contactos/leads/propuestas
- **structlog** en CRM para logging estructurado — buena práctica
- **Hard delete** disponible — riesgo de pérdida de datos vs GDPR right to erasure

## Referencias

| Test | Descripción | Herramienta | Estado |
|------|-------------|-------------|--------|
| WSTG-DATA-01 | Información sensible en respuestas | ZAP + Semgrep | ✅ |
| WSTG-DATA-02 | Información sensible en logs | Semgrep | ✅ |
| WSTG-DATA-03 | Datos en URLs | ZAP | ✅ |
