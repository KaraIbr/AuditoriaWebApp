# Selección de Herramientas

## Árbol de decisión

```
¿Qué necesitas auditar?
├── Código fuente → SAST (Semgrep)
├── App en ejecución → DAST (ZAP)
├── Dependencias → SCA (Trivy)
├── Infraestructura → Nuclei
└── Todo → Todos los anteriores

¿Qué tecnología usa?
├── JavaScript/TypeScript → Semgrep + ESLint security
├── Python → Semgrep + Bandit
├── Java → Semgrep + FindSecBugs
├── Go → Semgrep + gosec
├── Contenedores → Trivy + Docker Bench
└── Kubernetes → Trivy + Kube Bench + Nuclei

¿Qué profundidad?
├── L1 → Solo Semgrep
├── L2 → Semgrep + Trivy
├── L3 → Semgrep + Trivy + ZAP
└── L4 → Semgrep + Trivy + ZAP + Nuclei + manual
```

## Matriz de herramientas

| Herramienta | Tipo | Cuándo usarla | Instalación |
|-------------|------|---------------|-------------|
| **Semgrep** | SAST | Siempre (código disponible) | `pip install semgrep` |
| **OWASP ZAP** | DAST | App en ejecución (dev/staging) | `docker pull ghcr.io/zaproxy/zaproxy` |
| **Trivy** | SCA | Siempre (repo o imagen) | `winget install aquasecurity.Trivy` |
| **Nuclei** | Infra | URLs de la app disponibles | `winget install projectdiscovery.nuclei` |
| **ESLint** | SAST | Proyectos JS/TS | `npm init @eslint/config` |
| **Bandit** | SAST | Proyectos Python | `pip install bandit` |
| **Gitleaks** | Secrets | Siempre (repo) | `winget install gitleaks` |

## Combinaciones recomendadas

| Combinación | Para qué sirve |
|-------------|----------------|
| Semgrep + Trivy | Audit rápida de código + dependencias |
| Semgrep + Trivy + ZAP | Audit estándar de app web |
| Semgrep + Trivy + ZAP + Nuclei | Audit completa app + infra |
| Semgrep + Gitleaks + Trivy | Audit de repo (código + secrets + deps) |
