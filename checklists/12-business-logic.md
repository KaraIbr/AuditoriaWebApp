# Checklist: Lógica de Negocio

**OWASP Top 10:** A04 — Insecure Design
**ASVS:** V4, V11

## Flujos críticos

- [x] ¿Los flujos importantes requieren confirmación? — Pipeline stage transitions registradas en `stage_transition`
- [x] ¿Hay validación de estado en cada paso? — `ensure_transition_allowed` valida transiciones
- [x] ¿Los workflows no pueden ser saltados? — Transiciones definidas en `LEAD_STAGE_TRANSITIONS` y `PROPOSAL_STAGE_TRANSITIONS`
- [x] ¿Las transiciones de estado son válidas? — Mapa de transiciones explícito (service.py:15-53)

## Privilegios

- [x] ¿Un usuario normal no puede ejecutar acciones admin? — `require_permission` verifica permisos
- [x] ¿Las acciones masivas están protegidas? — Sin bulk endpoints
- [x] ¿Los límites (rate, cantidad) se aplican por usuario? — Sin rate limiting

## Manipulación

- [x] ¿No se puede manipular el estado de objetos? — Pipeline transitions validadas
- [x] ¿No se pueden crear objetos sin permisos? — `require_permission` en cada creación
- [x] ¿No se pueden modificar objetos de otros usuarios? — Resource scoped access checks
- [x] ¿Las operaciones de borrado son seguras? — Hard delete con verificación de ownership

## Race conditions

- [ ] ¿Las operaciones concurrentes están protegidas? — SQLite no maneja concurrencia alta
- [ ] ¿Los locks/bloqueos se usan donde es necesario? — No implementado
- [x] ¿Las transacciones tienen aislamiento adecuado? — SQLModel/SQLAlchemy maneja transacciones
- [ ] ¿Los límites de uso (cupones, votos) previenen race conditions? — Sin límites de uso

## Business rules

- [x] ¿Las reglas de negocio se validan en backend? — Validadas en service layer
- [x] ¿No se confía en validación del frontend? — Backend valida independientemente
- [x] ¿Los workflows complejos tienen logging? — Pipeline transitions audit trail

## Observaciones

### CRM Pipeline
- **Lead stage machine**: NEW → QUALIFYING → PROPOSAL_PHASE → CLOSED_WON|CLOSED_LOST
- **Proposal stage machine**: DRAFT → SENT → NEGOTIATION → WON|LOST|SUPERSEDED
- **Transiciones validadas** en `pipeline/service.py` con mapas explícitos
- **Audit trail**: cada transición registrada en `stage_transition` (append-only)
- **Inmutabilidad**: transiciones pasadas no se modifican

### AI Agent (LangGraph)
- **Graph**: `build_agent_graph` en `agent/graph.py` — tools + model + skill selection
- **Tools**: contacts, leads, proposals, pipeline CRUD via domain services
- **Prompt injection surface**: el agente acepta lenguaje natural del usuario
- **Skill selection**: `select_skills` filtra habilidades por texto de input

### Riesgos identificados
- **Race conditions** potenciales en pipeline transitions concurrentes
- **AI Agent prompt injection** — usuario puede manipular al agente via texto
- **AI Agent tool abuse** — agente podría ejecutar operaciones no autorizadas si la autorización no cubre todos los paths

## Referencias

| Test | Descripción | Herramienta | Estado |
|------|-------------|-------------|--------|
| Workflow bypass | Saltar pasos en un flujo | Manual | ✅ Transiciones validadas |
| Race conditions | Condiciones de carrera en transacciones | Manual | ⚠️ No protegido |
| Business limit bypass | Evadir límites de negocio | Manual | ✅ |
| State manipulation | Manipular estado de objetos | Manual | ✅ |
