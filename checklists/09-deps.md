# Checklist: Dependencias

**OWASP Top 10:** A06 — Vulnerable Components
**ASVS:** V14

## SCA (Software Composition Analysis)

- [ ] ¿Se escanean dependencias regularmente?
- [ ] ¿Hay alertas automáticas de vulns críticas?
- [ ] ¿Las dependencias están actualizadas?
- [ ] ¿Se revisan los changelogs de actualizaciones?

## Supply chain

- [ ] ¿Los paquetes vienen de fuentes oficiales?
- [ ] ¿Se verifican checksums/firmas de paquetes?
- [ ] ¿Hay lockfile (package-lock, yarn.lock, go.sum)?
- [ ] ¿Se auditan dependencias transitivas?

## Gestión

- [ ] ¿Dependencias innecesarias se eliminan?
- [ ] ¿Hay política de versionado?
- [ ] ¿Las vulns conocidas tienen plan de remediación?
- [ ] ¿Se usa Dependabot/Renovate para actualizaciones?

## Herramientas

- [ ] `npm audit` o equivalente ejecutado
- [ ] Trivy/Grype escaneando imágenes
- [ ] SCA integrado en CI/CD

## Referencias

| Test | Descripción | Herramienta |
|------|-------------|-------------|
| A06 | Vulnerable Components | Trivy + npm audit |
