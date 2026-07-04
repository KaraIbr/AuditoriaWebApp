"""
scope-analyzer.py — Analiza la descripción de una app y determina alcance.

Uso:
    python scripts/scope-analyzer.py --desc "E-commerce con React y Node.js" --output scope.json
"""

import argparse
import json
import re


CHECKLIST_MAP = {
    "auth": "01-auth",
    "session": "02-session",
    "input": "03-input",
    "authorization": "04-authorization",
    "api": "05-api",
    "crypto": "06-crypto",
    "infra": "07-infra",
    "data": "08-data",
    "deps": "09-deps",
    "ci-cd": "10-ci-cd",
    "ecommerce": "11-ecommerce",
    "business-logic": "12-business-logic",
}


def detect_checklists(desc: str) -> list[str]:
    desc_lower = desc.lower()
    checklists = []

    rules = [
        ("auth", ["login", "oauth", "auth", "register", "signup", "mfa", "password"]),
        ("session", ["session", "jwt", "token", "cookie"]),
        ("input", ["form", "input", "upload", "search", "comment"]),
        ("authorization", ["admin", "role", "permission", "rbac", "acl"]),
        ("api", ["api", "rest", "graphql", "endpoint"]),
        ("crypto", ["tls", "ssl", "encrypt", "hash", "secret"]),
        ("infra", ["docker", "k8s", "kubernetes", "nginx", "cloud"]),
        ("data", ["pii", "gdpr", "personal", "privacy", "data"]),
        ("deps", ["npm", "pip", "maven", "dependency", "package"]),
        ("ci-cd", ["ci", "cd", "pipeline", "deploy", "github action"]),
        ("ecommerce", ["ecommerce", "payment", "cart", "checkout", "order", "price", "store"]),
        ("business-logic", ["workflow", "business", "flow", "process"]),
    ]

    for checklist_id, keywords in rules:
        if any(kw in desc_lower for kw in keywords):
            checklists.append(checklist_id)

    if not checklists:
        checklists = ["auth", "input", "api"]

    return checklists


def detect_app_type(desc: str) -> str:
    desc_lower = desc.lower()
    if any(w in desc_lower for w in ["ecommerce", "shop", "store", "payment"]):
        return "ecommerce"
    if any(w in desc_lower for w in ["api", "microservice"]):
        return "api"
    if any(w in desc_lower for w in ["cms", "blog", "content"]):
        return "cms"
    if any(w in desc_lower for w in ["saas", "dashboard", "internal"]):
        return "saas"
    return "webapp"


def main():
    parser = argparse.ArgumentParser(description="Analiza una app y determina alcance")
    parser.add_argument("--desc", required=True, help="Descripción de la aplicación")
    parser.add_argument("--output", default="scope.json", help="Archivo de salida")
    args = parser.parse_args()

    checklists = detect_checklists(args.desc)
    app_type = detect_app_type(args.desc)

    result = {
        "app_type": app_type,
        "description": args.desc,
        "checklists": [CHECKLIST_MAP[c] for c in checklists],
        "checklist_ids": checklists,
        "estimated_days": max(len(checklists), 3),
    }

    with open(args.output, "w") as f:
        json.dump(result, f, indent=2)

    print(f"Tipo de app: {app_type}")
    print(f"Checklists recomendadas: {len(checklists)}")
    for c in checklists:
        print(f"  - {CHECKLIST_MAP[c]}.md ({c})")
    print(f"Días estimados: {result['estimated_days']}")
    print(f"Guardado en: {args.output}")


if __name__ == "__main__":
    main()
