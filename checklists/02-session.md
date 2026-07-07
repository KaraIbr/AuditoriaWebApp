# Checklist: Manejo de Sesiones

**OWASP Top 10:** A02 — Cryptographic Failures, A08 — Data Integrity Failures
**ASVS:** V3
**WSTG:** WSTG-SESS-01 al WSTG-SESS-09

## Cookies

- [ ] ¿Las cookies de sesión tienen Secure flag? — No usa cookies, usa Bearer tokens
- [ ] ¿Tienen HttpOnly flag? — N/A
- [ ] ¿Tienen SameSite=Lax o Strict? — N/A
- [ ] ¿Las cookies de sesión expiran al cerrar? — N/A
- [ ] ¿No se usa cookie persistent para sesión? — Usa localStorage (persistente)

## JWT

- [x] ¿Se valida la firma del JWT? — `security.py:112` via `jose.jwt.decode`
- [ ] ¿Está protegido contra alg=none? — Depende de `python-jose`; no hay validación explícita
- [x] ¿El JWT tiene exp (expiración)? — `security.py:57` — access: 30min, refresh: 7d
- [ ] ¿El JWT tiene nbf (not before)? — No incluido
- [ ] ¿El secret/private key es suficientemente fuerte? — Default: "change-me-in-local-development" en `config.py:32`
- [ ] ¿No se almacenan datos sensibles en el payload? — Solo `sub` (user_id) y `email`
- [ ] ¿Se rota el signing key periódicamente? — No implementado

## CSRF

- [ ] ¿Hay tokens CSRF en formularios? — No usa cookies para sesión
- [ ] ¿Los tokens CSRF son únicos por sesión? — N/A
- [ ] ¿Se validan los tokens en el servidor? — N/A
- [x] ¿SameSite=cookie configurado? — No aplica (Bearer tokens)
- [ ] ¿Las APIs con cookies usan CSRF protection? — N/A

## Manejo de sesión

- [x] ¿El ID de sesión es generado de forma segura? — JWT generado con `jose.jwt.encode`
- [ ] ¿Se regenera el ID tras login? — Nuevo token en cada login
- [x] ¿La sesión expira por inactividad? — Access token: 30min
- [ ] ¿Al hacer logout se destruye la sesión? — No, logout es no-op
- [ ] ¿Hay límite de sesiones concurrentes? — No implementado
- [ ] ¿Está protegido contra session fixation? — No aplica (JWT)

## Observaciones

- **Tokens almacenados en localStorage** (`api-client.ts:5-6`) — vulnerables a XSS
- **Refresh token rotation** implementado en `auth/service.py:68`
- **Auto-refresh interceptor** en `api-client.ts:56-76` — refresca automáticamente en 401
- **Sin httpOnly cookies** — los tokens son accesibles desde JavaScript
- **Refresh token en body** — visible en logs de request

## Referencias

| Test | Descripción | Herramienta | Estado |
|------|-------------|-------------|--------|
| WSTG-SESS-01 | Session management scheme | Manual | ✅ |
| WSTG-SESS-02 | Cookie attributes | ZAP | N/A (Bearer) |
| WSTG-SESS-03 | Session ID predictability | Manual | ✅ |
| WSTG-SESS-04 | Session ID in URL | ZAP | ✅ |
| WSTG-SESS-05 | CSRF | ZAP + Semgrep | N/A |
| WSTG-SESS-06 | Logout functionality | Manual | ❌ No-op |
| WSTG-SESS-07 | Session timeout | Manual | ✅ |
| WSTG-SESS-08 | Session puzzling | Manual | ✅ |
| WSTG-SESS-09 | JWT | Semgrep | ⚠️ Ver observaciones |
