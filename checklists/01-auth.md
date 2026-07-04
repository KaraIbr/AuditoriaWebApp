# Checklist: Autenticación

**OWASP Top 10:** A07 — Identification and Authentication Failures
**ASVS:** V2, V3
**WSTG:** WSTG-AUTH-01 al WSTG-AUTH-10

## Credenciales

- [ ] ¿Se usan contraseñas con requisitos mínimos de complejidad?
- [ ] ¿Se almacenan contraseñas con hash (bcrypt/argon2/scrypt)?
- [ ] ¿Hay rate limiting en login?
- [ ] ¿Está protegido contra fuerza bruta?
- [ ] ¿Se bloquea la cuenta tras N intentos fallidos?
- [ ] ¿Hay opción de cambio de contraseña seguro?

## MFA

- [ ] ¿Ofrece MFA para usuarios?
- [ ] ¿Es obligatorio para roles administrativos?
- [ ] ¿Los códigos MFA tienen expiración?
- [ ] ¿Está protegido contra MFA fatigue?

## OAuth / OIDC

- [ ] ¿Se valida el redirect URI?
- [ ] ¿Se usa state parameter anti-CSRF?
- [ ] ¿Se valida el token de id_token?
- [ ] ¿Los scopes son mínimos necesarios?
- [ ] ¿Está protegido contra account takeover por OAuth?

## Registro / Recuperación

- [ ] ¿El registro requiere verificación de email?
- [ ] ¿La recuperación de contraseña usa token temporal?
- [ ] ¿Los tokens de recuperación expiran?
- [ ] ¿Hay rate limiting en recuperación?

## Sesión

- [ ] ¿Las sesiones expiran por inactividad?
- [ ] ¿Al cerrar sesión se invalida el token?
- [ ] ¿Hay límite de sesiones concurrentes?

## Referencias

| Test | Descripción | Herramienta |
|------|-------------|-------------|
| WSTG-AUTH-01 | Credenciales transportadas por canal seguro | ZAP |
| WSTG-AUTH-02 | Enumeración de usuarios | Manual |
| WSTG-AUTH-03 | Bloqueo de cuenta | Manual |
| WSTG-AUTH-04 | Bypass de autenticación | Semgrep |
| WSTG-AUTH-05 | Credenciales débiles | Manual |
| WSTG-AUTH-07 | Preguntas de recuperación | Manual |
| WSTG-AUTH-08 | Autenticación débil | Manual |
| WSTG-AUTH-09 | Cambio de contraseña | Manual |
| WSTG-AUTH-10 | Autenticación insegura en APIs | ZAP |
