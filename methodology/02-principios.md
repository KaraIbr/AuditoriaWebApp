# 02. Principios de Auditoría

## Principios fundamentales

### 1. Basado en riesgos

No todos los hallazgos son iguales. Priorizar por impacto real en el negocio.

### 2. Repetible

Misma metodología → mismos resultados. Dos auditores distintos deben llegar a conclusiones similares.

### 3. Evidencia documentada

Cada hallazgo debe incluir:
- Cómo reproducirlo (PoC)
- Evidencia (request, screenshot, log)
- Referencia al estándar (OWASP WSTG-xxx)

### 4. Trazabilidad

Cada auditoría en su branch. Cada hallazgo es un commit. El historial de git es la evidencia.

### 5. Enfoque en remediación

No basta con encontrar bugs. Cada hallazgo debe incluir una recomendación clara y accionable.

### 6. Jerarquía de verificación

1. **Automático** — SAST, DAST, SCA (rápido, amplio)
2. **Semi-automático** — Semgrep rules personalizadas, ZAP scripts
3. **Manual** — Revisión de lógica de negocio, auth, sesiones
4. **Validación** — Confirmación manual de hallazgos automáticos

### 7. Niveles de profundidad

| Nivel | Cobertura | Tiempo estimado |
|-------|-----------|-----------------|
| L1 (Superficial) | OWASP Top 10 + ASVS L1 | 2-3 días |
| L2 (Estándar) | L1 + checklists por dominio + SAST | 5-7 días |
| L3 (Profunda) | L2 + DAST + revisión manual + SCA | 10-14 días |
| L4 (Completa) | L3 + Pentest + compliance (PCI/GDPR) | 3-4 semanas |
