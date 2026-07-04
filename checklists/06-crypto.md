# Checklist: Criptografía

**OWASP Top 10:** A02 — Cryptographic Failures
**ASVS:** V2, V6
**WSTG:** WSTG-CRYP-01 al WSTG-CRYP-04

## TLS / Transporte

- [ ] ¿Todas las comunicaciones usan TLS 1.2+?
- [ ] ¿Está deshabilitado TLS 1.0 y 1.1?
- [ ] ¿El certificado es válido (no expirado)?
- [ ] ¿Las redirecciones HTTP→HTTPS son seguras?
- [ ] ¿HSTS configurado con `includeSubDomains`?

## Hashing de contraseñas

- [ ] ¿Las contraseñas se hashean con bcrypt/argon2/scrypt?
- [ ] ¿No se usa SHA-1/MD5 para contraseñas?
- [ ] ¿Se usa salt único por usuario?
- [ ] ¿El factor de trabajo es adecuado (bcrypt ≥ 10)?

## Secrets management

- [ ] ¿No hay API keys / secrets en el código?
- [ ] ¿No hay secrets en archivos .env en el repo?
- [ ] ¿Se usa vault/secrets manager en producción?
- [ ] ¿Las claves se rotan periódicamente?

## Cifrado de datos

- [ ] ¿Datos sensibles en reposo están cifrados?
- [ ] ¿Se usa AES-256 o equivalente?
- [ ] ¿Las claves de cifrado están protegidas?
- [ ] ¿Los tokens de acceso no contienen datos en texto plano?

## Referencias

| Test | Descripción | Herramienta |
|------|-------------|-------------|
| WSTG-CRYP-01 | TLS débil | ZAP + testssl |
| WSTG-CRYP-02 | Padding oracle | Manual |
| WSTG-CRYP-03 | Sensitive data exposure | Semgrep |
| WSTG-CRYP-04 | Weak cryptography | Semgrep |
