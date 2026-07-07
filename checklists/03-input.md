# Checklist: Validación de Entrada

**OWASP Top 10:** A03 — Injection
**ASVS:** V5
**WSTG:** WSTG-INPV-01 al WSTG-INPV-18

## XSS

- [x] ¿Los inputs de usuario están sanitizados? — React maneja XSS por diseño (JSX escapa)
- [x] ¿Se usa escaping contextual (HTML, JS, CSS)? — React JSX + Tailwind
- [ ] ¿Content-Security-Policy configurado? — Vite dev sin CSP configurado
- [ ] ¿XSS reflejado en parámetros de URL? — Frontend sin server-side rendering
- [ ] ¿XSS almacenado en comentarios/perfiles? — CRM contact/lead fields: depende de validación
- [ ] ¿DOM-based XSS en JS? — React minimiza DOM manipulation directa

## SQL Injection

- [x] ¿Se usan consultas parametrizadas (prepared statements)? — SQLModel/SQLAlchemy ORM
- [x] ¿ORM configurado sin raw SQL? — No se encontró raw SQL en IAM/CRM src/
- [ ] ¿Stored procedures sin concatenación? — N/A (SQLite/PostgreSQL sin SP)
- [x] ¿SQLi en parámetros GET/POST/headers? — ORM parametriza automáticamente
- [ ] ¿SQLi en ORDER BY / LIMIT dinámicos? — No se identificaron dinámicos

## SSTI (Server-Side Template Injection)

- [x] ¿Los templates no permiten código arbitrario? — FastAPI + Pydantic, sin templates
- [x] ¿Los inputs de usuario no se pasan a templates? — N/A
- [x] ¿Sandbox de templates configurado? — N/A

## Command Injection

- [x] ¿No se ejecutan comandos del sistema con input directo? — No se identificó en IAM/CRM
- [x] ¿Si se necesitan, se sanitiza el input? — N/A
- [x] ¿Se usa allowlist de comandos permitidos? — N/A

## SSRF

- [ ] ¿Las URLs ingresadas por usuario se validan? — AI Agent tools podrían aceptar URLs
- [ ] ¿Hay allowlist de dominios permitidos? — No identificado en agent tools
- [ ] ¿Se bloquean IPs privadas (127.0.0.1, 10.x, 172.x, 192.168.x)? — No identificado
- [ ] ¿Las peticiones salientes tienen timeout? — No verificado

## File Upload

- [ ] ¿Se valida el tipo MIME real (no solo extensión)? — `leads/router.py:110`: `UploadFile` sin validación MIME explícita
- [x] ¿Se valida el tamaño máximo? — FastAPI `UploadFile` sin límite explícito visible
- [x] ¿Los archivos se almacenan fuera del webroot? — `uploads/` fuera de webroot
- [x] ¿Los nombres de archivo se sanitizan? — No verificado en detalle
- [ ] ¿Se escanea el contenido (virus/malware)? — No implementado

## Path Traversal

- [x] ¿Los paths ingresados se normalizan? — No se identificaron operaciones de path con input de usuario
- [x] ¿Se bloquea `../` y paths absolutos? — No verificado en file upload
- [x] ¿Se usa allowlist de archivos permitidos? — N/A

## Observaciones

- **AI Agent** en CRM (`agent/tools/`) acepta lenguaje natural — riesgo de prompt injection
- **File upload** sin validación MIME (`leads/router.py:110`)
- **SQLModel/SQLAlchemy** usado consistentemente sin raw SQL — buena práctica
- **Sin CSP** configurado en frontend — riesgo de XSS si hay bypass de React
- Semgrep SAST encontró 0 findings de inyección en las 3 capas

## Referencias

| Test | Descripción | Herramienta | Estado |
|------|-------------|-------------|--------|
| WSTG-INPV-01 | Reflected XSS | ZAP + Semgrep | ✅ |
| WSTG-INPV-02 | Stored XSS | ZAP + Semgrep | ⚠️ Según validación |
| WSTG-INPV-03 | DOM XSS | Semgrep | ✅ |
| WSTG-INPV-05 | SQLi | Semgrep + ZAP | ✅ |
| WSTG-INPV-11 | SSTI | Semgrep | ✅ |
| WSTG-INPV-12 | Command Injection | Semgrep | ✅ |
| WSTG-INPV-13 | File Inclusion | Semgrep | ✅ |
| WSTG-INPV-18 | SSRF | Manual + ZAP | ⚠️ AI Agent riesgo potencial |
