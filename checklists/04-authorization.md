# Checklist: Autorización

**OWASP Top 10:** A01 — Broken Access Control
**ASVS:** V4
**WSTG:** WSTG-AUTHZ-01 al WSTG-AUTHZ-04

## IDOR (Insecure Direct Object References)

- [ ] ¿Los IDs en URLs son difíciles de adivinar?
- [ ] ¿Se verifica que el usuario es propietario del recurso?
- [ ] ¿Las APIs verifican propiedad antes de devolver datos?
- [ ] ¿Está protegido contra enumeración de IDs?

## RBAC / Roles

- [ ] ¿Los roles están bien definidos?
- [ ] ¿Se verifica el rol en cada endpoint protegido?
- [ ] ¿No hay privilege escalation vertical (user → admin)?
- [ ] ¿No hay privilege escalation horizontal (user A → user B)?
- [ ] ¿El middleware de autorización cubre todos los endpoints?

## Admin functions

- [ ] ¿Las rutas admin requieren autenticación + rol admin?
- [ ] ¿No hay admin functions expuestas en URLs públicas?
- [ ] ¿Las APIs admin verifican rol en cada endpoint?
- [ ] ¿Los paneles admin no están en subdominios guesseables?

## API authorization

- [ ] ¿Cada endpoint verifica autenticación?
- [ ] ¿Cada endpoint verifica autorización?
- [ ] ¿GraphQL queries están restringidas por rol?
- [ ] ¿WebSocket connections verifican auth?

## Business logic

- [ ] ¿Un usuario puede acceder a datos de otro sin permiso?
- [ ] ¿Un usuario puede ejecutar acciones de otro?
- [ ] ¿Las operaciones masivas están protegidas?
- [ ] ¿Los workflows tienen validación de permisos en cada paso?

## Referencias

| Test | Descripción | Herramienta |
|------|-------------|-------------|
| WSTG-AUTHZ-01 | Path traversal en rutas | Manual |
| WSTG-AUTHZ-02 | IDOR horizontal | Manual |
| WSTG-AUTHZ-03 | IDOR vertical | Manual |
| WSTG-AUTHZ-04 | Privilege escalation | Manual + Semgrep |
