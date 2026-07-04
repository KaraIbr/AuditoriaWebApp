# Checklist: Lógica de Negocio

**OWASP Top 10:** A04 — Insecure Design
**ASVS:** V4, V11

## Flujos críticos

- [ ] ¿Los flujos importantes requieren confirmación?
- [ ] ¿Hay validación de estado en cada paso?
- [ ] ¿Los workflows no pueden ser saltados?
- [ ] ¿Las transiciones de estado son válidas?

## Privilegios

- [ ] ¿Un usuario normal no puede ejecutar acciones admin?
- [ ] ¿Las acciones masivas están protegidas?
- [ ] ¿Los límites (rate, cantidad) se aplican por usuario?

## Manipulación

- [ ] ¿No se puede manipular el estado de objetos?
- [ ] ¿No se pueden crear objetos sin permisos?
- [ ] ¿No se pueden modificar objetos de otros usuarios?
- [ ] ¿Las operaciones de borrado son seguras?

## Race conditions

- [ ] ¿Las operaciones concurrentes están protegidas?
- [ ] ¿Los locks/bloqueos se usan donde es necesario?
- [ ] ¿Las transacciones tienen aislamiento adecuado?
- [ ] ¿Los límites de uso (cupones, votos) previenen race conditions?

## Business rules

- [ ] ¿Las reglas de negocio se validan en backend?
- [ ] ¿No se confía en validación del frontend?
- [ ] ¿Los workflows complejos tienen logging?

## Referencias

| Test | Descripción | Herramienta |
|------|-------------|-------------|
| Workflow bypass | Saltar pasos en un flujo | Manual |
| Race conditions | Condiciones de carrera en transacciones | Manual |
| Business limit bypass | Evadir límites de negocio | Manual |
| State manipulation | Manipular estado de objetos | Manual |
