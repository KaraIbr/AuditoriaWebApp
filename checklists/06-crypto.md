# Checklist: Criptografía

**OWASP Top 10:** A02 — Cryptographic Failures
**ASVS:** V2, V6
**WSTG:** WSTG-CRYP-01 al WSTG-CRYP-04

## TLS / Transporte

- [ ] ¿Todas las comunicaciones usan TLS 1.2+? — Dev: HTTP local; Prod: depende de infraestructura
- [ ] ¿Está deshabilitado TLS 1.0 y 1.1? — N/A en dev
- [ ] ¿El certificado es válido (no expirado)? — N/A en dev
- [ ] ¿Las redirecciones HTTP→HTTPS son seguras? — No configuradas
- [ ] ¿HSTS configurado con `includeSubDomains`? — No configurado

## Hashing de contraseñas

- [x] ¿Las contraseñas se hashean con bcrypt/argon2/scrypt? — `security.py:13`: bcrypt via passlib
- [x] ¿No se usa SHA-1/MD5 para contraseñas? — Usa bcrypt
- [x] ¿Se usa salt único por usuario? — passlib CryptContext genera salt automático
- [ ] ¿El factor de trabajo es adecuado (bcrypt ≥ 10)? — No configurado explícitamente, usa default de passlib (12)

## Secrets management

- [ ] ¿No hay API keys / secrets en el código? — `.env` files presentes en IAM/ y CRM/
- [ ] ¿No hay secrets en archivos .env en el repo? — `.env` en `.gitignore` (verificar)
- [ ] ¿Se usa vault/secrets manager en producción? — No implementado
- [ ] ¿Las claves se rotan periódicamente? — No implementado

## Cifrado de datos

- [ ] ¿Datos sensibles en reposo están cifrados? — SQLite sin cifrado en dev
- [ ] ¿Se usa AES-256 o equivalente? — No implementado
- [ ] ¿Las claves de cifrado están protegidas? — N/A
- [x] ¿Los tokens de acceso no contienen datos en texto plano? — Solo `sub` (user_id) y `email`

## Observaciones

- **bcrypt** para hashing de passwords — buena práctica ✅
- **JWT HS256** con `python-jose` — firma validada en cada request
- **JWT secret key** default inseguro: `"change-me-in-local-development"` en `IAM/config.py:32`
- **Sin cifrado en reposo** para datos sensibles en DB
- **Secrets en `.env` files** — asegurar que están en `.gitignore`
- **Sin HSTS/TLS** configurado en la aplicación (depende del deploy)

## Referencias

| Test | Descripción | Herramienta | Estado |
|------|-------------|-------------|--------|
| WSTG-CRYP-01 | TLS débil | ZAP + testssl | ⚠️ Solo dev |
| WSTG-CRYP-02 | Padding oracle | Manual | N/A |
| WSTG-CRYP-03 | Sensitive data exposure | Semgrep | ✅ |
| WSTG-CRYP-04 | Weak cryptography | Semgrep | ✅ |
