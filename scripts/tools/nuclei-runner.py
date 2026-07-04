"""
nuclei-runner.py — Escanea infraestructura con Nuclei.

Uso:
    python scripts/tools/nuclei-runner.py --url https://example.com --output nuclei-results.json
"""

import argparse
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description="Ejecuta Nuclei para escaneo de infra")
    parser.add_argument("--url", required=True, help="URL a escanear")
    parser.add_argument("--output", default="nuclei-results.json", help="Archivo de salida")
    parser.add_argument("--severity", default="critical,high,medium", help="Filtrar por severidad")
    args = parser.parse_args()

    cmd = [
        "nuclei",
        "-u", args.url,
        "-json", args.output,
        "-severity", args.severity,
    ]

    print(f"Ejecutando Nuclei en: {args.url}")
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(f"Nuclei completado. Salida en: {args.output}")
        if result.stderr:
            print(f"Stderr: {result.stderr[:500]}")
    except FileNotFoundError:
        print("Error: Nuclei no está instalado.")
        print("  winget install projectdiscovery.nuclei")
        print("  O: https://docs.projectdiscovery.io/tools/nuclei/install")
        sys.exit(1)


if __name__ == "__main__":
    main()
