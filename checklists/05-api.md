# Checklist: APIs

**OWASP Top 10:** A01, A05, A06
**ASVS:** V5, V11
**WSTG:** WSTG-APIT-01, WSTG-APIT-02

## REST API

- [ ] ¿Todas las rutas requieren autenticación (excepto públicas)?
- [ ] ¿Se valida el Content-Type y Accept headers?
- [ ] ¿Hay rate limiting por usuario/IP?
- [ ] ¿Hay límite de tamaño en request body?
- [ ] ¿Se validan todos los parámetros de entrada?
- [ ] ¿Los errores no exponen stack traces?
- [ ] ¿CORS configurado restrictivamente?

## GraphQL

- [ ] ¿Introspection deshabilitado en producción?
- [ ] ¿Hay query depth limiting?
- [ ] ¿Hay query complexity/aliasing limiting?
- [ ] ¿Autenticación requerida en mutations?
- [ ] ¿Rate limiting por query?
- [ ] ¿Batching attacks mitigados?

## Headers de seguridad

- [ ] `Content-Security-Policy` configurado
- [ ] `X-Content-Type-Options: nosniff`
- [ ] `X-Frame-Options: DENY` o `SAMEORIGIN`
- [ ] `Strict-Transport-Security` (HSTS)
- [ ] `Cache-Control` en respuestas con datos sensibles

## Rate Limiting

- [ ] ¿Hay rate limiting en login?
- [ ] ¿Hay rate limiting en APIs?
- [ ] ¿Hay rate limiting en endpoints sensibles?
- [ ] ¿Las respuestas 429 son informativas?
- [ ] ¿El rate limiting es por usuario + IP?

## Referencias

| Test | Descripción | Herramienta |
|------|-------------|-------------|
| WSTG-APIT-01 | API endpoints testing | ZAP |
| WSTG-APIT-02 | GraphQL testing | ZAP + Manual |
