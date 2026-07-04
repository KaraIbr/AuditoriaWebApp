# Checklist: Infraestructura

**OWASP Top 10:** A05 — Security Misconfiguration
**ASVS:** V12
**WSTG:** WSTG-CONF-01 al WSTG-CONF-10

## Security Headers

- [ ] `Content-Security-Policy` presente
- [ ] `X-Frame-Options: DENY | SAMEORIGIN`
- [ ] `X-Content-Type-Options: nosniff`
- [ ] `Referrer-Policy: strict-origin-when-cross-origin`
- [ ] `Permissions-Policy` configurado
- [ ] `Strict-Transport-Security` con `max-age ≥ 31536000`

## CORS

- [ ] `Access-Control-Allow-Origin` no es `*`
- [ ] `Access-Control-Allow-Credentials` no está con `*`
- [ ] CORS solo en orígenes confiables
- [ ] Preflight requests validan origen

## Server Config

- [ ] Server version no expuesta en headers
- [ ] Directory listing deshabilitado
- [ ] Métodos HTTP restringidos (solo GET, POST, etc.)
- [ ] Archivos sensibles protegidos (.env, .git, config)
- [ ] Debug/development mode deshabilitado

## Contenedores / Docker

- [ ] Imagen base actualizada
- [ ] No se ejecuta como root
- [ ] Puertos expuestos mínimos
- [ ] No hay secrets en la imagen
- [ ] No hay capas innecesarias

## Kubernetes

- [ ] RBAC configurado
- [ ] Network policies restrictivas
- [ ] Secrets en etcd cifrados
- [ ] Pod security policies aplicadas
- [ ] Contenedores con límites de recursos

## Referencias

| Test | Descripción | Herramienta |
|------|-------------|-------------|
| WSTG-CONF-01 | Server version | ZAP + Nuclei |
| WSTG-CONF-02 | Directory listing | ZAP |
| WSTG-CONF-03 | Methods HTTP | ZAP |
| WSTG-CONF-04 | Security headers | ZAP |
| WSTG-CONF-05 | CORS | ZAP |
