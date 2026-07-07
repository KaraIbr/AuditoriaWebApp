# Checklist: APIs

**OWASP Top 10:** A01, A05, A06
**ASVS:** V5, V11
**WSTG:** WSTG-APIT-01, WSTG-APIT-02

## REST API

- [x] ¿Todas las rutas requieren autenticación (excepto públicas)? — IAM login es pública, resto requiere `CurrentUser`
- [x] ¿Se valida el Content-Type y Accept headers? — FastAPI lo maneja automáticamente
- [ ] ¿Hay rate limiting por usuario/IP? — No implementado en IAM ni CRM
- [ ] ¿Hay límite de tamaño en request body? — No configurado explícitamente
- [x] ¿Se validan todos los parámetros de entrada? — Pydantic/SQLModel validación en schemas
- [x] ¿Los errores no exponen stack traces? — FastAPI en producción oculta detalles
- [ ] ¿CORS configurado restrictivamente? — `IAM/config.py:42`: `cors_origins` depende de configuración

## GraphQL

- [ ] ¿Introspection deshabilitado en producción? — N/A
- [ ] ¿Hay query depth limiting? — N/A
- [ ] ¿Hay query complexity/aliasing limiting? — N/A
- [ ] ¿Autenticación requerida en mutations? — N/A
- [ ] ¿Rate limiting por query? — N/A
- [ ] ¿Batching attacks mitigados? — N/A

## Headers de seguridad

- [ ] `Content-Security-Policy` configurado — No configurado
- [ ] `X-Content-Type-Options: nosniff` — No configurado explícitamente
- [ ] `X-Frame-Options: DENY` o `SAMEORIGIN` — No configurado explícitamente
- [ ] `Strict-Transport-Security` (HSTS) — No configurado
- [ ] `Cache-Control` en respuestas con datos sensibles — No configurado explícitamente

## Rate Limiting

- [ ] ¿Hay rate limiting en login? — No implementado
- [ ] ¿Hay rate limiting en APIs? — No implementado
- [ ] ¿Hay rate limiting en endpoints sensibles? — No implementado
- [ ] ¿Las respuestas 429 son informativas? — N/A
- [ ] ¿El rate limiting es por usuario + IP? — N/A

## Observaciones

- **Sin rate limiting** en ningún endpoint — riesgo de abuso, brute force, DoS parcial
- **CORS** depende de configuración en `.env` — asegurar que no sea `*` en producción
- **Sin security headers** configurados — CSP, HSTS, X-Frame-Options ausentes
- **Validación de input** con Pydantic/SQLModel cubre todos los endpoints
- **Autenticación** requerida en todos los endpoints excepto IAM `/auth/login` y `/docs`
- **IAM endpoints**: `/api/v1/auth/`, `/api/v1/users/`, `/api/v1/permissions/`, `/api/v1/services/`
- **CRM endpoints**: `/api/v1/leads/`, `/api/v1/proposals/`, `/api/v1/contacts/`, `/api/v1/agent/`, `/api/v1/pipeline/`, etc.

## Referencias

| Test | Descripción | Herramienta | Estado |
|------|-------------|-------------|--------|
| WSTG-APIT-01 | API endpoints testing | ZAP | ✅ |
| WSTG-APIT-02 | GraphQL testing | ZAP + Manual | N/A |
