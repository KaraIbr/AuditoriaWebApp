# Checklist: Autorización

**OWASP Top 10:** A01 — Broken Access Control
**ASVS:** V4
**WSTG:** WSTG-AUTHZ-01 al WSTG-AUTHZ-04

## IDOR (Insecure Direct Object References)

- [x] ¿Los IDs en URLs son difíciles de adivinar? — IDs numéricos/secuenciales
- [x] ¿Se verifica que el usuario es propietario del recurso? — CRM: `user_can_access_lead`, `user_can_access_proposal`
- [x] ¿Las APIs verifican propiedad antes de devolver datos? — Cada endpoint CRM llama a `require_permission` + scope check
- [ ] ¿Está protegido contra enumeración de IDs? — IDs secuenciales sin rate limiting por recurso

## RBAC / Roles

- [x] ¿Los roles están bien definidos? — IAM: 8 permisos | CRM: 4 roles (ADMIN, MANAGER, SALES, TECH) + 84 permisos
- [x] ¿Se verifica el rol en cada endpoint protegido? — Cada endpoint en `leads/router.py` y `proposals/router.py` usa `require_permission`
- [x] ¿No hay privilege escalation vertical (user → admin)? — `can_manage_user` en CRM impide que MANAGER modifique ADMIN
- [x] ¿No hay privilege escalation horizontal (user A → user B)? — Resource-scoped access checks (`user_can_access_lead`, etc.)
- [x] ¿El middleware de autorización cubre todos los endpoints? — `CurrentUser` dependency verifica autenticación + cada endpoint verifica permiso

## Admin functions

- [x] ¿Las rutas admin requieren autenticación + rol admin? — IAM: `require_permission` verifica permisos específicos
- [x] ¿No hay admin functions expuestas en URLs públicas? — No se identificaron
- [x] ¿Las APIs admin verifican rol en cada endpoint? — Sí, basado en permisos, no en roles directos
- [ ] ¿Los paneles admin no están en subdominios guesseables? — Frontend SPA sin subdominios

## API authorization

- [x] ¿Cada endpoint verifica autenticación? — `CurrentUser` dependency en IAM y CRM
- [x] ¿Cada endpoint verifica autorización? — `require_permission` en cada operación
- [ ] ¿GraphQL queries están restringidas por rol? — No usa GraphQL
- [ ] ¿WebSocket connections verifican auth? — No usa WebSockets

## Business logic

- [x] ¿Un usuario puede acceder a datos de otro sin permiso? — `user_can_access_*` previene acceso horizontal
- [x] ¿Un usuario puede ejecutar acciones de otro? — `require_permission` + resource scope checks
- [x] ¿Las operaciones masivas están protegidas? — Endpoints individuales, no bulk operations identificadas
- [x] ¿Los workflows tienen validación de permisos en cada paso? — Pipeline `transition()` verifica visibilidad + estado

## Observaciones

- **IAM**: RBAC con 8 permisos atómicos, bootstrap grants full permissions
- **CRM**: 84 permisos atómicos en 4 roles, con resource-scoped access checks
- **Resource scoping**: `user_can_access_lead`, `user_can_access_proposal`, `user_can_access_contact`, `user_can_access_technical_visit`
- **Bootstrap seguro**: primer usuario admin, luego requiere `iam.users.create`
- **Auto-protección**: usuarios no pueden modificar sus propios permisos ni desactivarse
- **No privilege escalation**: managers no pueden modificar admins; solo admins asignan admin

## Referencias

| Test | Descripción | Herramienta | Estado |
|------|-------------|-------------|--------|
| WSTG-AUTHZ-01 | Path traversal en rutas | Manual | ✅ |
| WSTG-AUTHZ-02 | IDOR horizontal | Manual | ✅ |
| WSTG-AUTHZ-03 | IDOR vertical | Manual | ✅ |
| WSTG-AUTHZ-04 | Privilege escalation | Manual + Semgrep | ✅ |
