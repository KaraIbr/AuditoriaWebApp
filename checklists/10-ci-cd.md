# Checklist: CI/CD

**OWASP Top 10:** A08 — Data Integrity Failures

## Pipeline

- [ ] ¿SAST se ejecuta en cada PR? — `.github/` no verificado
- [ ] ¿SCA se ejecuta en cada PR? — No identificado
- [ ] ¿Secret scanning en cada push? — No identificado
- [ ] ¿Los tests de seguridad bloquean el merge? — No identificado
- [x] ¿Hay code review obligatorio? — Pre-commit hooks configurados

## Secrets

- [ ] ¿No hay secrets hardcodeados en CI config? — No verificado
- [ ] ¿Los secrets se inyectan como variables de entorno? — No verificado
- [ ] ¿Los artifacts no contienen secrets? — N/A
- [ ] ¿Los logs del CI no exponen secrets? — N/A

## Artefactos

- [ ] ¿Las imágenes se escanean antes de deploy? — Sin Docker
- [ ] ¿Los artifacts se firman? — N/A
- [ ] ¿Hay trazabilidad de builds (qué código, qué commit)? — Git branches

## Deploy

- [ ] ¿El deploy requiere aprobación? — Sin pipeline CI/CD
- [ ] ¿Hay rollback automatizado? — No implementado
- [ ] ¿Los cambios se deployan gradualmente? — No implementado
- [ ] ¿Hay validación post-deploy? — No implementado

## Observaciones

- **Pre-commit hooks** configurados en `.pre-commit-config.yaml` con `ruff` y `mypy`
- **Sin CI/CD pipeline** visible (GitHub Actions no configurados)
- **Sin secret scanning** automatizado
- **Sin SAST/SCA gates** en CI
- **Calidad de código**: `ruff` lint + `mypy` type checking en pre-commit
- **Testing**: `pytest` configurado en ambos servicios

## Referencias

| Práctica | Descripción | Herramienta | Estado |
|----------|-------------|-------------|--------|
| SAST gates | Bloquear PRs con vulns críticas | Semgrep + CI | ❌ No implementado |
| Secret scanning | Detectar secrets en commits | Gitleaks | ❌ No implementado |
| Image scanning | Escanear imágenes vulnerables | Trivy | ❌ Sin Docker |
