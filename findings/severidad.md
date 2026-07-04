# Clasificación de Severidad

## Determinación

Severidad = **Impacto × Probabilidad**

| Impacto \ Probabilidad | Alta | Media | Baja |
|------------------------|------|-------|------|
| **Crítico** | Critical | Critical | High |
| **Alto** | Critical | High | Medium |
| **Medio** | High | Medium | Low |
| **Bajo** | Medium | Low | Info |

## Ejemplos por Severidad

### Critical
- RCE en endpoint público
- SQLi sin autenticación
- Autenticación bypass total
- SSRF a servicios internos críticos

### High
- IDOR que expone datos de otros usuarios
- XSS almacenado
- JWT sin validación de firma
- Admin functions sin auth

### Medium
- XSS reflejado
- CORS mal configurado
- Rate limiting ausente
- Security headers faltantes

### Low
- Server version disclosure
- Cookies sin Secure flag
- Falta de CSP
- Logs sin sanitización

### Info
- Dependencias desactualizadas sin vuln conocida
- Mejoras de logging
- Sugerencias de hardening

## Scoring

| Severidad | Peso | Plazo |
|-----------|------|-------|
| Critical | 10 | < 48h |
| High | 7 | 1 semana |
| Medium | 4 | 2 semanas |
| Low | 1 | 1 mes |
| Info | 0 | Próximo release |
