# Checklist: Autenticación

**OWASP Top 10:** A07 — Identification and Authentication Failures
**ASVS:** V2, V3
**WSTG:** WSTG-AUTH-01 al WSTG-AUTH-10

## Credenciales

- [x] ¿Se usan contraseñas con requisitos mínimos de complejidad? — IAM: validación en `UserCreate`
- [x] ¿Se almacenan contraseñas con hash (bcrypt/argon2/scrypt)? — `security.py:13`: `CryptContext(schemes=["bcrypt"])`
- [ ] ¿Hay rate limiting en login? — No implementado en `auth/router.py`
- [ ] ¿Está protegido contra fuerza bruta? — Sin rate limiting ni bloqueo
- [ ] ¿Se bloquea la cuenta tras N intentos fallidos? — No implementado
- [x] ¿Hay opción de cambio de contraseña seguro? — `update_user` en `users/service.py`

## MFA

- [ ] ¿Ofrece MFA para usuarios? — No implementado
- [ ] ¿Es obligatorio para roles administrativos? — No implementado
- [ ] ¿Los códigos MFA tienen expiración? — N/A
- [ ] ¿Está protegido contra MFA fatigue? — N/A

## OAuth / OIDC

- [ ] ¿Se valida el redirect URI? — No usa OAuth externo
- [ ] ¿Se usa state parameter anti-CSRF? — No usa OAuth externo
- [ ] ¿Se valida el token de id_token? — N/A
- [ ] ¿Los scopes son mínimos necesarios? — N/A
- [ ] ¿Está protegido contra account takeover por OAuth? — N/A

## Registro / Recuperación

- [x] ¿El registro requiere verificación de email? — `normalize_email` usado, cuenta se crea activa
- [ ] ¿La recuperación de contraseña usa token temporal? — No implementado (sin forgot-password flow)
- [ ] ¿Los tokens de recuperación expiran? — N/A
- [ ] ¿Hay rate limiting en recuperación? — N/A

## Sesión

- [x] ¿Las sesiones expiran por inactividad? — JWT access token: 30min (`config.py:36`)
- [ ] ¿Al cerrar sesión se invalida el token? — `logout` en auth/router.py:40 es un no-op
- [ ] ¿Hay límite de sesiones concurrentes? — No implementado

## Observaciones

- Las contraseñas usan bcrypt con salt (passlib CryptContext)
- JWT usa HS256 con firma validada en `decode_token`
- No hay rate limiting en login — riesgo de fuerza bruta
- No hay bloqueo de cuenta tras intentos fallidos
- No hay MFA
- El logout no invalida tokens server-side
- La creación del primer usuario (bootstrap) bypass autenticación por diseño

## Referencias

| Test | Descripción | Herramienta | Estado |
|------|-------------|-------------|--------|
| WSTG-AUTH-01 | Credenciales transportadas por canal seguro | ZAP | ✅ |
| WSTG-AUTH-02 | Enumeración de usuarios | Manual | ⚠️ No protegido |
| WSTG-AUTH-03 | Bloqueo de cuenta | Manual | ❌ No implementado |
| WSTG-AUTH-04 | Bypass de autenticación | Semgrep | ✅ Bootstrap controlado |
| WSTG-AUTH-05 | Credenciales débiles | Manual | ⚠️ Sin validación de complejidad |
| WSTG-AUTH-07 | Preguntas de recuperación | Manual | N/A |
| WSTG-AUTH-08 | Autenticación débil | Manual | ✅ |
| WSTG-AUTH-09 | Cambio de contraseña | Manual | ✅ |
| WSTG-AUTH-10 | Autenticación insegura en APIs | ZAP | ✅ |
