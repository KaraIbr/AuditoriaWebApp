# 06. Compliance

## Mapeo a estándares de cumplimiento

### ISO 27001:2022

| Control ISO | Área | Cómo se cubre en WebAudit |
|-------------|------|---------------------------|
| A.8 | Gestión de activos | Inventario de apps, dependencias |
| A.9 | Control de acceso | Checklists auth + authorization |
| A.10 | Criptografía | Checklist crypto |
| A.12 | Seguridad operacional | CI/CD, infra, monitoreo |
| A.14 | Desarrollo seguro | SAST en pipeline, code review |
| A.16 | Gestión de incidentes | Plan de remediación, reportes |

### PCI DSS (para e-commerce)

| Requisito PCI | Cómo se cubre |
|--------------|---------------|
| 3 — Proteger datos almacenados | Checklist data |
| 4 — Encriptar transmisión | Checklist crypto (TLS) |
| 6 — Desarrollar apps seguras | SAST + checklists input/auth |
| 7 — Restringir acceso | Checklist authorization |
| 11 — Probar seguridad | DAST + SCA + pentest periódico |

### GDPR

| Requisito | Cómo se cubre |
|-----------|---------------|
| Data minimization | Checklist data |
| Consentimiento | Revisión de formularios y cookies |
| Derecho al olvido | Revisión de eliminación de datos |
| Notificación de brechas | Plan de respuesta a incidentes |
| Logs de acceso | Checklist data (logging) |

### SOC2

| Criterio | Cómo se cubre |
|----------|---------------|
| Security | Framework completo |
| Availability | Checklist infra |
| Confidentiality | Checklist crypto + data |
| Privacy | Checklist data + compliance GDPR |
