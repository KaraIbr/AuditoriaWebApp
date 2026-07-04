# Flujo de trabajo con branches

## Idea principal

Cada auditoría o revisión vive en su propia branch. Esto te da:

- **Historial completo** — Sabes qué se auditó, cuándo y por quién
- **Evidencia inmutable** — Los hallazgos quedan registrados en el tiempo
- **Trazabilidad** — Para compliance ISO 27001, SOC2, PCI DSS
- **Re-auditorías** — Compara el estado antes y después de los fixes

---

## Convención de nombres

```
audit/YYYY-MM-NOMBRE-DEL-PROYECTO
revision/YYYY-MM-NOMBRE-DEL-PROYECTO
```

Ejemplos:
```
audit/2026-07-ecommerce-app
audit/2026-08-internal-crm
revision/2026-09-ecommerce-app
```

---

## Flujo completo

### 1. Inicio de una auditoría

```bash
git checkout main
git checkout -b audit/2026-07-ecommerce-app
python scripts/init-audit.py --name "E-commerce App" --desc "React + Node.js + PostgreSQL"
```

Esto crea:
```
scope/scope.json
scope/01-identificacion.md
scope/03-plan-auditoria.md
findings/
reports/
evidence/
```

### 2. Durante la auditoría

```bash
git add findings/WA-2026-0001.md
git commit -m "finding: SQLi en endpoint de productos - Critical"
```

### 3. Al entregar

```bash
git add reports/reporte-final.md
git commit -m "report: entrega final E-commerce App"
git push origin audit/2026-07-ecommerce-app
```

### 4. Re-auditoría

```bash
git checkout main
git checkout -b revision/2026-09-ecommerce-app
```

---

## Estructura de cada branch

```
audit/2026-07-ecommerce-app/
├── scope/
│   ├── scope.json
│   ├── 01-identificacion.md
│   └── 03-plan-auditoria.md
├── checklists/
│   ├── 01-auth.md
│   ├── 03-input.md
│   └── ...
├── findings/
│   ├── WA-2026-0001.md
│   ├── WA-2026-0001.json
│   └── ...
├── reports/
│   ├── reporte-final.md
│   └── reporte-final.json
├── evidence/
│   ├── screenshots/
│   ├── tool-output/
│   └── requests/
└── README.md
```

---

## Comandos útiles

```bash
# Ver todas las auditorías
git branch --list 'audit/*' 'revision/*'

# Comparar dos auditorías
git diff audit/2026-07-ecommerce-app/main.py revision/2026-09-ecommerce-app/main.py

# Historial de una auditoría
git log audit/2026-07-ecommerce-app --oneline

# Tag de cierre
git tag -a "v1.0-audit-ecommerce" -m "Auditoría E-commerce App v1.0"
```

---

## Tips

- **Commits frecuentes** — Cada hallazgo = un commit
- **Tags al entregar** — Marca el cierre con tag
- **No borres branches** — Son evidencia
- **README en cada branch** — Explica qué cubre esa auditoría
