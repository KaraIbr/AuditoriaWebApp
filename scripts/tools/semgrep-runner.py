"""
semgrep-runner.py — Ejecuta Semgrep con reglas OWASP Top 10.

Uso:
    python scripts/tools/semgrep-runner.py --path ./src --output semgrep-results.json
"""

import argparse
import json
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description="Ejecuta Semgrep SAST")
    parser.add_argument("--path", required=True, help="Ruta al código a analizar")
    parser.add_argument("--output", default="semgrep-results.json", help="Archivo de salida")
    parser.add_argument("--rules", default="p/owasp-top-ten", help="Reglas Semgrep (default: OWASP Top Ten)")
    args = parser.parse_args()

    cmd = [
        "semgrep", "--config", args.rules,
        "--json",
        "--output", args.output,
        args.path,
    ]

    print(f"Ejecutando: {' '.join(cmd)}")
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(f"Semgrep completado. Salida en: {args.output}")
        if result.stderr:
            print(f"Stderr: {result.stderr[:500]}")
    except FileNotFoundError:
        print("Error: Semgrep no está instalado. Instala con: pip install semgrep")
        sys.exit(1)


if __name__ == "__main__":
    main()
