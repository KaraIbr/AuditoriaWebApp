# Checklist: Dependencias

**OWASP Top 10:** A06 — Vulnerable Components
**ASVS:** V14

## SCA (Software Composition Analysis)

- [ ] ¿Se escanean dependencias regularmente? — Semgrep + Trivy ejecutados manualmente esta auditoría
- [ ] ¿Hay alertas automáticas de vulns críticas? — No integrado
- [ ] ¿Las dependencias están actualizadas? — Ver reporte de npm audit y Trivy
- [ ] ¿Se revisan los changelogs de actualizaciones? — No verificado

## Supply chain

- [x] ¿Los paquetes vienen de fuentes oficiales? — npm registry + PyPI
- [ ] ¿Se verifican checksums/firmas de paquetes? — No implementado
- [x] ¿Hay lockfile (package-lock, yarn.lock, go.sum)? — `package-lock.json` presente
- [ ] ¿Se auditan dependencias transitivas? — npm audit cubre transitivas

## Gestión

- [ ] ¿Dependencias innecesarias se eliminan? — No auditado
- [ ] ¿Hay política de versionado? — No identificada
- [ ] ¿Las vulns conocidas tienen plan de remediación? — No identificado
- [ ] ¿Se usa Dependabot/Renovate para actualizaciones? — No configurado

## Herramientas

- [x] `npm audit` o equivalente ejecutado — Frontend: 0 vulnerabilidades
- [x] Trivy/Grype escaneando imágenes — No disponible (sin Docker)
- [ ] SCA integrado en CI/CD — No implementado

## Resultados

### Frontend (npm audit)
- **Resultado:** 0 vulnerabilidades encontradas
- **Dependencias directas:** 12 (React 19, React Router, React Query, Axios, Zod, Recharts, etc.)
- **Lockfile:** `package-lock.json` presente

### Backend (pip + uv)
- **Python 3.14 + uv.lock** presente
- **Dependencias principales:** FastAPI, SQLModel, python-jose, passlib, python-multipart, langchain, langgraph, etc.
- Semgrep SAST: 0 findings en IAM y CRM

## Observaciones

- npm audit: 0 vulnerabilidades ✅
- Trivy no disponible para SCA completo del sistema
- Sin Dependabot/Renovate para actualizaciones automáticas
- `uv.lock` y `package-lock.json` presentes

## Referencias

| Test | Descripción | Herramienta | Estado |
|------|-------------|-------------|--------|
| A06 | Vulnerable Components | Trivy + npm audit | ✅ npm audit: 0 vulns |
