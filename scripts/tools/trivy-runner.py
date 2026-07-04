"""
trivy-runner.py — Escanea dependencias con Trivy.

Uso:
    python scripts/tools/trivy-runner.py --path ./repo --output trivy-results.json
    python scripts/tools/trivy-runner.py --image node:18 --output trivy-image.json
"""

import argparse
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description="Ejecuta Trivy SCA")
    parser.add_argument("--path", help="Ruta al repositorio/código")
    parser.add_argument("--image", help="Imagen Docker a escanear")
    parser.add_argument("--output", default="trivy-results.json", help="Archivo de salida")
    args = parser.parse_args()

    if not args.path and not args.image:
        print("Error: debe especificar --path o --image")
        sys.exit(1)

    if args.path:
        cmd = ["trivy", "fs", "--format", "json", "--output", args.output, args.path]
        target = args.path
    else:
        cmd = ["trivy", "image", "--format", "json", "--output", args.output, args.image]
        target = args.image

    print(f"Ejecutando Trivy en: {target}")
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(f"Trivy completado. Salida en: {args.output}")
        if result.stderr:
            print(f"Stderr: {result.stderr[:500]}")
    except FileNotFoundError:
        print("Error: Trivy no está instalado.")
        print("  winget install aquasecurity.Trivy")
        print("  O: https://trivy.dev/latest/getting-started/installation/")
        sys.exit(1)


if __name__ == "__main__":
    main()
