# Checklist: Protección de Datos

**OWASP Top 10:** A04 — Insecure Design, A09 — Logging Failures
**ASVS:** V7, V8
**WSTG:** WSTG-DATA-01 al WSTG-DATA-03

## PII / Datos personales

- [ ] ¿Se recolecta solo la data mínima necesaria?
- [ ] ¿Los usuarios pueden ver/exportar sus datos?
- [ ] ¿Los usuarios pueden eliminar su cuenta/datos?
- [ ] ¿Hay consentimiento explícito para recolección?
- [ ] ¿Política de privacidad accesible?

## Datos en reposo

- [ ] ¿Datos sensibles cifrados en DB?
- [ ] ¿Backups cifrados?
- [ ] ¿Los datos temporales se eliminan?
- [ ] ¿Las tablas con PII están identificadas?

## Logging

- [ ] ¿No se loguean datos sensibles (passwords, tokens)?
- [ ] ¿Los logs tienen información de auditoría (quién, qué, cuándo)?
- [ ] ¿Los logs están protegidos contra modificación?
- [ ] ¿Hay retención de logs definida?

## Eliminación de datos

- [ ] ¿Hay proceso para eliminar datos de usuarios?
- [ ] ¿Se eliminan datos de tablas temporales?
- [ ] ¿Cache se invalida al eliminar datos?

## Referencias

| Test | Descripción | Herramienta |
|------|-------------|-------------|
| WSTG-DATA-01 | Información sensible en respuestas | ZAP + Semgrep |
| WSTG-DATA-02 | Información sensible en logs | Semgrep |
| WSTG-DATA-03 | Datos en URLs | ZAP |
