"""
report-builder.py — Construye reporte final consolidado desde hallazgos.

Uso:
    python scripts/report-builder.py --findings-dir ./findings --output reporte-final.md
"""

import argparse
import json
import os
from datetime import date
from collections import Counter


def build_report(findings_dir: str, output: str):
    findings = []
    if os.path.isdir(findings_dir):
        for f in os.listdir(findings_dir):
            if f.endswith(".json"):
                with open(os.path.join(findings_dir, f), encoding="utf-8") as fh:
                    findings.append(json.load(fh))

    findings.sort(key=lambda x: {"Critical": 0, "High": 1, "Medium": 2, "Low": 3, "Info": 4}.get(x.get("severity", "Info"), 5))

    severity_count = Counter(f.get("severity", "Info") for f in findings)
    total = len(findings)

    owasp_refs = set()
    for f in findings:
        if f.get("owasp_top10"):
            owasp_refs.add(f["owasp_top10"])

    report = f"""# Reporte de Auditoría

**Fecha:** {date.today()}
**Total de hallazgos:** {total}

---

## Resumen Ejecutivo

| Severidad | Cantidad |
|-----------|----------|
| Critical | {severity_count.get("Critical", 0)} |
| High | {severity_count.get("High", 0)} |
| Medium | {severity_count.get("Medium", 0)} |
| Low | {severity_count.get("Low", 0)} |
| Info | {severity_count.get("Info", 0)} |

**OWASP Top 10 referenciados:** {", ".join(sorted(owasp_refs)) if owasp_refs else "N/A"}

---

## Hallazgos por Severidad

"""

    for severity in ["Critical", "High", "Medium", "Low", "Info"]:
        sev_findings = [f for f in findings if f.get("severity") == severity]
        if not sev_findings:
            continue
        report += f"### {severity}\n\n"
        for f in sev_findings:
            report += f"- **{f.get('id')}**: {f.get('title')} — {f.get('owasp_top10', '')}\n"
        report += "\n"

    report += "---\n\n## Hallazgos Detallados\n\n"
    for f in findings:
        report += f"""### {f.get('id')}: {f.get('title')}

| Campo | Valor |
|-------|-------|
| **Severidad** | {f.get('severity', 'Info')} |
| **OWASP Top 10** | {f.get('owasp_top10', 'N/A')} |
| **Estado** | {f.get('status', 'Open')} |
| **Auditor** | {f.get('auditor', 'N/A')} |
| **Fecha** | {f.get('date', 'N/A')} |

**Descripción:** {f.get('description', '')}

**Impacto:** {f.get('impact', '')}

**Recomendación:** {f.get('recommendation', '')}

---
"""
    with open(output, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"Reporte generado: {output} ({total} hallazgos)")


def main():
    parser = argparse.ArgumentParser(description="Construye reporte final de auditoría")
    parser.add_argument("--findings-dir", required=True, help="Directorio con hallazgos .json")
    parser.add_argument("--output", default="reporte-final.md", help="Archivo de salida")
    args = parser.parse_args()
    build_report(args.findings_dir, args.output)


if __name__ == "__main__":
    main()
