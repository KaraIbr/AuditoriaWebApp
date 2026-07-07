# Checklist: Infraestructura

**OWASP Top 10:** A05 — Security Misconfiguration
**ASVS:** V12
**WSTG:** WSTG-CONF-01 al WSTG-CONF-10

## Security Headers

- [ ] `Content-Security-Policy` presente — No configurado
- [ ] `X-Frame-Options: DENY | SAMEORIGIN` — No configurado
- [ ] `X-Content-Type-Options: nosniff` — No configurado
- [ ] `Referrer-Policy: strict-origin-when-cross-origin` — No configurado
- [ ] `Permissions-Policy` configurado — No configurado
- [ ] `Strict-Transport-Security` con `max-age ≥ 31536000` — No configurado

## CORS

- [ ] `Access-Control-Allow-Origin` no es `*` — Depende de config `cors_origins` en IAM
- [ ] `Access-Control-Allow-Credentials` no está con `*` — Depende de config
- [ ] CORS solo en orígenes confiables — Configurable via `.env`
- [ ] Preflight requests validan origen — FastAPI CORSMiddleware

## Server Config

- [ ] Server version no expuesta en headers — FastAPI no expone por defecto
- [x] Directory listing deshabilitado — FastAPI no sirve archivos estáticos
- [x] Métodos HTTP restringidos (solo GET, POST, etc.) — Solo métodos definidos en routers
- [ ] Archivos sensibles protegidos (.env, .git, config) — Depende del deploy
- [x] Debug/development mode deshabilitado — `debug: bool = False` en IAM config

## Contenedores / Docker

- [ ] Imagen base actualizada — Sin Dockerfile en el repo
- [ ] No se ejecuta como root — N/A
- [ ] Puertos expuestos mínimos — N/A
- [ ] No hay secrets en la imagen — N/A
- [ ] No hay capas innecesarias — N/A

## Kubernetes

- [ ] RBAC configurado — N/A
- [ ] Network policies restrictivas — N/A
- [ ] Secrets en etcd cifrados — N/A
- [ ] Pod security policies aplicadas — N/A
- [ ] Contenedores con límites de recursos — N/A

## Observaciones

- **Sin security headers** — CSP, HSTS, X-Frame-Options, X-Content-Type-Options ausentes
- **CORS configurable** via `IAM/.env` — asegurar que no sea `*` en producción
- **Vite dev proxy** expone IAM y CRM en un solo puerto (3000) en desarrollo
- **Sin Docker/K8s config** — despliegue actual es local con `uvicorn`
- **Pre-commit hooks** configurados (`ruff`, `mypy`) en `.pre-commit-config.yaml`

## Referencias

| Test | Descripción | Herramienta | Estado |
|------|-------------|-------------|--------|
| WSTG-CONF-01 | Server version | ZAP + Nuclei | ✅ |
| WSTG-CONF-02 | Directory listing | ZAP | ✅ |
| WSTG-CONF-03 | Methods HTTP | ZAP | ✅ |
| WSTG-CONF-04 | Security headers | ZAP | ❌ Faltan headers |
| WSTG-CONF-05 | CORS | ZAP | ⚠️ Configurable |
