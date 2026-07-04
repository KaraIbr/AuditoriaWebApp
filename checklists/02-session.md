# Checklist: Manejo de Sesiones

**OWASP Top 10:** A02 — Cryptographic Failures, A08 — Data Integrity Failures
**ASVS:** V3
**WSTG:** WSTG-SESS-01 al WSTG-SESS-09

## Cookies

- [ ] ¿Las cookies de sesión tienen Secure flag?
- [ ] ¿Tienen HttpOnly flag?
- [ ] ¿Tienen SameSite=Lax o Strict?
- [ ] ¿Las cookies de sesión expiran al cerrar?
- [ ] ¿No se usa cookie persistent para sesión?

## JWT

- [ ] ¿Se valida la firma del JWT?
- [ ] ¿Está protegido contra alg=none?
- [ ] ¿El JWT tiene exp (expiración)?
- [ ] ¿El JWT tiene nbf (not before)?
- [ ] ¿El secret/private key es suficientemente fuerte?
- [ ] ¿No se almacenan datos sensibles en el payload?
- [ ] ¿Se rota el signing key periódicamente?

## CSRF

- [ ] ¿Hay tokens CSRF en formularios?
- [ ] ¿Los tokens CSRF son únicos por sesión?
- [ ] ¿Se validan los tokens en el servidor?
- [ ] ¿SameSite=cookie configurado?
- [ ] ¿Las APIs con cookies usan CSRF protection?

## Manejo de sesión

- [ ] ¿El ID de sesión es generado de forma segura?
- [ ] ¿Se regenera el ID tras login?
- [ ] ¿La sesión expira por inactividad?
- [ ] ¿Al hacer logout se destruye la sesión?
- [ ] ¿Hay límite de sesiones concurrentes?
- [ ] ¿Está protegido contra session fixation?

## Referencias

| Test | Descripción | Herramienta |
|------|-------------|-------------|
| WSTG-SESS-01 | Session management scheme | Manual |
| WSTG-SESS-02 | Cookie attributes | ZAP |
| WSTG-SESS-03 | Session ID predictability | Manual |
| WSTG-SESS-04 | Session ID in URL | ZAP |
| WSTG-SESS-05 | CSRF | ZAP + Semgrep |
| WSTG-SESS-06 | Logout functionality | Manual |
| WSTG-SESS-07 | Session timeout | Manual |
| WSTG-SESS-08 | Session puzzling | Manual |
| WSTG-SESS-09 | JWT | Semgrep |
