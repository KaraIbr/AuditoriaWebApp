"""
zap-runner.py — Ejecuta OWASP ZAP DAST contra una URL.

Uso:
    python scripts/tools/zap-runner.py --url https://example.com --output zap-results.json
"""

import argparse
import json
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description="Ejecuta OWASP ZAP DAST")
    parser.add_argument("--url", required=True, help="URL de la app a escanear")
    parser.add_argument("--output", default="zap-results.json", help="Archivo de salida")
    parser.add_argument("--docker", action="store_true", help="Usar Docker para ZAP")
    args = parser.parse_args()

    if args.docker:
        cmd = [
            "docker", "run", "--rm",
            "-v", f"{args.output}:/zap/results/output.json",
            "ghcr.io/zaproxy/zaproxy:stable",
            "zap-full-scan.py",
            "-t", args.url,
            "-r", "output.json",
        ]
    else:
        cmd = ["zap-cli", "quick-scan", args.url]

    print(f"Ejecutando ZAP contra: {args.url}")
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
        print(f"ZAP completado.")
        if result.stderr:
            print(f"Stderr: {result.stderr[:500]}")
    except FileNotFoundError:
        print("Error: ZAP no está instalado.")
        print("  Docker: docker pull ghcr.io/zaproxy/zaproxy")
        print("  Local:  https://www.zaproxy.org/download/")
        sys.exit(1)
    except subprocess.TimeoutExpired:
        print("Error: ZAP excedió el tiempo límite (10 min)")


if __name__ == "__main__":
    main()
