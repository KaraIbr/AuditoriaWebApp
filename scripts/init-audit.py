"""
init-audit.py — Inicializa una nueva auditoría en su propia branch.

Uso:
    python scripts/init-audit.py --name "E-commerce App" --desc "React + Node.js + PostgreSQL"

Crea:
    - Branch: audit/YYYY-MM-NOMBRE
    - Directorios: scope/, checklists/, findings/, reports/, evidence/
    - Templates iniciales
"""

import argparse
import json
import os
import subprocess
import sys
from datetime import date


def slugify(name: str) -> str:
    return name.lower().replace(" ", "-").replace("/", "-")


def run_git(cmd: list[str]) -> subprocess.CompletedProcess:
    try:
        return subprocess.run(["git"] + cmd, capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error en git {' '.join(cmd)}: {e.stderr.strip()}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Inicializa una nueva auditoría en su branch")
    parser.add_argument("--name", required=True, help="Nombre del proyecto a auditar")
    parser.add_argument("--desc", default="", help="Descripción breve del proyecto")
    parser.add_argument("--tech", default="", help="Stack tecnológico (ej: react,nodejs,postgres)")
    args = parser.parse_args()

    today = date.today().strftime("%Y-%m")
    branch_name = f"audit/{today}-{slugify(args.name)}"

    # 1. Crear branch desde main
    print(f"Creando branch: {branch_name}")
    run_git(["checkout", "-b", branch_name])

    # 2. Crear directorios
    dirs = [
        "scope", "checklists", "findings", "reports",
        "evidence/screenshots", "evidence/tool-output", "evidence/requests"
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)
        print(f"  Directorio: {d}/")

    # 3. Copiar templates de checklists
    template_dir = "checklists"
    if os.path.isdir(template_dir):
        for f in sorted(os.listdir(template_dir)):
            if f.endswith(".md"):
                src = os.path.join(template_dir, f)
                dst = os.path.join("checklists", f)
                if not os.path.exists(dst) and os.path.exists(src):
                    with open(src) as fsrc:
                        content = fsrc.read()
                    with open(dst, "w") as fdst:
                        fdst.write(content)
                    print(f"  Checklist: {dst}")

    # 4. Generar scope inicial
    scope = {
        "project": args.name,
        "description": args.desc,
        "tech_stack": args.tech.split(",") if args.tech else [],
        "branch": branch_name,
        "date": str(date.today()),
        "status": "in-progress",
        "auditor": "",
        "scope": {
            "app_type": "",
            "checklists": [],
            "depth": "standard",
            "estimated_days": 0
        }
    }
    with open("scope/scope.json", "w") as f:
        json.dump(scope, f, indent=2)
    print(f"  Scope: scope/scope.json")

    # 5. README de la auditoría
    readme = f"""# Auditoría: {args.name}

**Branch:** {branch_name}
**Fecha:** {date.today()}
**Estado:** En progreso
**Stack:** {args.tech or "Pendiente"}

## Descripción
{args.desc or "Pendiente"}

## Contenido
- `scope/` — Documentos de alcance
- `checklists/` — Checklists completadas
- `findings/` — Hallazgos (.md + .json)
- `reports/` — Reportes generados
- `evidence/` — Evidencia (screenshots, requests, tool output)
"""
    with open("README.md", "w") as f:
        f.write(readme)
    print(f"  README: README.md")

    # 6. Commit inicial
    run_git(["add", "."])
    run_git(["commit", "-m", f"feat: iniciar auditoría {args.name}"])
    print(f"\nAuditoría inicializada en branch: {branch_name}")
    print(f"Comandos útiles:")
    print(f"  git push -u origin {branch_name}")
    print(f"  python scripts/scope-analyzer.py --desc \"{args.desc}\" --output scope/scope.json")


if __name__ == "__main__":
    main()
