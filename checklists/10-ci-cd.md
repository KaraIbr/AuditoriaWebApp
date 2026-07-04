# Checklist: CI/CD

**OWASP Top 10:** A08 — Data Integrity Failures

## Pipeline

- [ ] ¿SAST se ejecuta en cada PR?
- [ ] ¿SCA se ejecuta en cada PR?
- [ ] ¿Secret scanning en cada push?
- [ ] ¿Los tests de seguridad bloquean el merge?
- [ ] ¿Hay code review obligatorio?

## Secrets

- [ ] ¿No hay secrets hardcodeados en CI config?
- [ ] ¿Los secrets se inyectan como variables de entorno?
- [ ] ¿Los artifacts no contienen secrets?
- [ ] ¿Los logs del CI no exponen secrets?

## Artefactos

- [ ] ¿Las imágenes se escanean antes de deploy?
- [ ] ¿Los artifacts se firman?
- [ ] ¿Hay trazabilidad de builds (qué código, qué commit)?

## Deploy

- [ ] ¿El deploy requiere aprobación?
- [ ] ¿Hay rollback automatizado?
- [ ] ¿Los cambios se deployan gradualmente?
- [ ] ¿Hay validación post-deploy?

## Referencias

| Práctica | Descripción | Herramienta |
|----------|-------------|-------------|
| SAST gates | Bloquear PRs con vulns críticas | Semgrep + CI |
| Secret scanning | Detectar secrets en commits | Gitleaks |
| Image scanning | Escanear imágenes vulnerables | Trivy |
