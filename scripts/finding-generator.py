"""
finding-generator.py — Genera hallazgos en .md y .json desde datos estructurados.

Uso:
    python scripts/finding-generator.py --data finding-data.json --output-dir ./findings
    python scripts/finding-generator.py --batch hallazgos.json --output-dir ./findings
"""

import argparse
import json
import os
import sys
from datetime import date


FINDING_TEMPLATE = """# {title}

**ID:** {id}
**Severidad:** {severity}
**OWASP Top 10:** {owasp}
**Estado:** {status}
**Fecha:** {date}
**Auditor:** {auditor}

---

## Descripción

{description}

## Impacto

{impact}

## Probabilidad

{likelihood}

## Condición

{condition}

## Reproducción

{reproduction}

## Evidencia

{evidence}

## Recomendación

{recommendation}
"""


def generate_finding(data: dict, output_dir: str):
    finding_id = data.get("id", f"WA-{date.today().year}-0001")
    title = data.get("title", "Hallazgo sin título")

    md_content = FINDING_TEMPLATE.format(
        id=finding_id,
        title=title,
        severity=data.get("severity", "Info"),
        owasp=data.get("owasp_top10", ""),
        status=data.get("status", "Open"),
        date=data.get("date", str(date.today())),
        auditor=data.get("auditor", ""),
        description=data.get("description", ""),
        impact=data.get("impact", ""),
        likelihood=data.get("likelihood", ""),
        condition=data.get("condition", ""),
        reproduction=data.get("reproduction", ""),
        evidence=data.get("evidence", ""),
        recommendation=data.get("recommendation", ""),
    )

    os.makedirs(output_dir, exist_ok=True)

    md_path = os.path.join(output_dir, f"{finding_id}.md")
    json_path = os.path.join(output_dir, f"{finding_id}.json")

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Generado: {md_path}")
    print(f"Generado: {json_path}")


def main():
    parser = argparse.ArgumentParser(description="Genera hallazgos en .md y .json")
    parser.add_argument("--data", help="Archivo JSON con un hallazgo")
    parser.add_argument("--batch", help="Archivo JSON con array de hallazgos")
    parser.add_argument("--output-dir", default="./findings", help="Directorio de salida")
    args = parser.parse_args()

    if args.batch:
        with open(args.batch, encoding="utf-8") as f:
            findings = json.load(f)
        for finding in findings:
            generate_finding(finding, args.output_dir)
        print(f"Generados {len(findings)} hallazgos en {args.output_dir}")

    elif args.data:
        with open(args.data, encoding="utf-8") as f:
            finding = json.load(f)
        generate_finding(finding, args.output_dir)

    else:
        print("Error: debe especificar --data o --batch")
        sys.exit(1)


if __name__ == "__main__":
    main()
