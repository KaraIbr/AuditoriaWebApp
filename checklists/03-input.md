# Checklist: Validación de Entrada

**OWASP Top 10:** A03 — Injection
**ASVS:** V5
**WSTG:** WSTG-INPV-01 al WSTG-INPV-18

## XSS

- [ ] ¿Los inputs de usuario están sanitizados?
- [ ] ¿Se usa escaping contextual (HTML, JS, CSS)?
- [ ] ¿Content-Security-Policy configurado?
- [ ] ¿XSS reflejado en parámetros de URL?
- [ ] ¿XSS almacenado en comentarios/perfiles?
- [ ] ¿DOM-based XSS en JS?

## SQL Injection

- [ ] ¿Se usan consultas parametrizadas (prepared statements)?
- [ ] ¿ORM configurado sin raw SQL?
- [ ] ¿Stored procedures sin concatenación?
- [ ] ¿SQLi en parámetros GET/POST/headers?
- [ ] ¿SQLi en ORDER BY / LIMIT dinámicos?

## SSTI (Server-Side Template Injection)

- [ ] ¿Los templates no permiten código arbitrario?
- [ ] ¿Los inputs de usuario no se pasan a templates?
- [ ] ¿Sandbox de templates configurado?

## Command Injection

- [ ] ¿No se ejecutan comandos del sistema con input directo?
- [ ] ¿Si se necesitan, se sanitiza el input?
- [ ] ¿Se usa allowlist de comandos permitidos?

## SSRF

- [ ] ¿Las URLs ingresadas por usuario se validan?
- [ ] ¿Hay allowlist de dominios permitidos?
- [ ] ¿Se bloquean IPs privadas (127.0.0.1, 10.x, 172.x, 192.168.x)?
- [ ] ¿Las peticiones salientes tienen timeout?

## File Upload

- [ ] ¿Se valida el tipo MIME real (no solo extensión)?
- [ ] ¿Se valida el tamaño máximo?
- [ ] ¿Los archivos se almacenan fuera del webroot?
- [ ] ¿Los nombres de archivo se sanitizan?
- [ ] ¿Se escanea el contenido (virus/malware)?

## Path Traversal

- [ ] ¿Los paths ingresados se normalizan?
- [ ] ¿Se bloquea `../` y paths absolutos?
- [ ] ¿Se usa allowlist de archivos permitidos?

## Referencias

| Test | Descripción | Herramienta |
|------|-------------|-------------|
| WSTG-INPV-01 | Reflected XSS | ZAP + Semgrep |
| WSTG-INPV-02 | Stored XSS | ZAP + Semgrep |
| WSTG-INPV-03 | DOM XSS | Semgrep |
| WSTG-INPV-05 | SQLi | Semgrep + ZAP |
| WSTG-INPV-11 | SSTI | Semgrep |
| WSTG-INPV-12 | Command Injection | Semgrep |
| WSTG-INPV-13 | File Inclusion | Semgrep |
| WSTG-INPV-18 | SSRF | Manual + ZAP |
