# 04. Clasificación de Riesgos

## Matriz de Severidad

Severidad = **Impacto × Probabilidad**:

| Impacto \ Probabilidad | Alta | Media | Baja |
|------------------------|------|-------|------|
| **Crítico** | Critical | Critical | High |
| **Alto** | Critical | High | Medium |
| **Medio** | High | Medium | Low |
| **Bajo** | Medium | Low | Info |

---

## Definición de Impacto

| Nivel | Descripción | Ejemplo Web |
|-------|-------------|-------------|
| **Crítico** | Acceso no autorizado a datos sensibles, ejecución remota de código, compromiso total del sistema | RCE, SQLi que expone toda la DB, autenticación bypass total |
| **Alto** | Exposición de datos de usuarios, acceso a funcionalidades administrativas, manipulación de datos crítica | IDOR que expone datos de otros usuarios, XSS almacenado que afecta a todos |
| **Medio** | Exposición limitada de información, degradación de seguridad, manipulación condicional | XSS reflejado, falta de headers de seguridad, información de versión expuesta |
| **Bajo** | Sin impacto directo en seguridad, pero debilita la postura | Falta de logging, cookies sin Secure flag, información de depuración |

---

## Definición de Probabilidad

| Nivel | Criterio |
|-------|----------|
| **Alta** | El ataque es trivial, no requiere autenticación, no tiene restricciones |
| **Media** | El ataque requiere autenticación, condiciones específicas, o conocimiento técnico |
| **Baja** | El ataque requiere múltiples condiciones, acceso privilegiado, o encadenamiento complejo |

---

## Severidades

### Critical
Vulnerabilidad que permite comprometer completamente la aplicación o acceder a todos los datos.

**Ejemplos:**
- SQLi sin autenticación que expone toda la base de datos
- RCE en endpoint público
- Autenticación bypass completo
- SSRF que permite acceso a servicios internos críticos

### High
Vulnerabilidad que permite acceder a datos de otros usuarios o funcionalidades restringidas.

**Ejemplos:**
- IDOR en endpoints de usuarios
- XSS almacenado que afecta a todos los usuarios
- Broken access control en admin functions
- JWT sin validación de firma

### Medium
Vulnerabilidad que permite explotación en condiciones específicas.

**Ejemplos:**
- XSS reflejado (requiere interacción del usuario)
- CORS mal configurado
- Rate limiting ausente
- Security headers faltantes

### Low
Vulnerabilidad sin impacto directo pero debe corregirse.

**Ejemplos:**
- Server version disclosure
- Cookies sin Secure/HttpOnly flags
- Falta de Content-Security-Policy
- Logs sin sanitización

### Info
Observación informativa, mejora recomendada.

**Ejemplos:**
- Dependencias desactualizadas sin vuln conocida
- Mejoras de logging
- Sugerencias de hardening
