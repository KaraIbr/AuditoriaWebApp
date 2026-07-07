# Identificación de la Aplicación

## Datos Generales

| Campo | Valor |
|-------|-------|
| **Nombre del proyecto** | VERP WebApp |
| **Versión** | 0.1.0 |
| **URL / entorno** | Frontend: http://localhost:3000 | IAM: http://localhost:8100 | CRM: http://localhost:8000 |
| **Fecha de auditoría** | 2026-07-07 |
| **Auditor(es)** | Security Team |
| **Cliente / Equipo** | Ventura Energy |

## Tipo de Aplicación

- [x] Web app (SPA)
- [ ] Web app (SSR)
- [x] REST API
- [ ] GraphQL API
- [ ] Mobile backend
- [x] Microservicio
- [ ] CMS
- [ ] E-commerce
- [ ] SaaS
- [ ] Internal tool
- [ ] Otro: ERP (Enterprise Resource Planning)

## Stack Tecnológico

| Capa | Tecnología |
|------|-----------|
| **Frontend** | React 19 + TypeScript + Vite + Tailwind CSS + React Query + React Router |
| **Backend** | Python 3.14 + FastAPI + SQLModel + LangGraph + AzureOpenAI |
| **Base de datos** | SQLite (dev) / PostgreSQL (prod) + Alembic migrations |
| **Autenticación** | JWT (HS256) + bcrypt + OAuth2 password flow + Refresh tokens (7d) |
| **Infraestructura** | Local development (uv + uvicorn) |
| **CI/CD** | GitHub Actions + pre-commit (ruff + mypy) |

## Datos Sensibles

- [x] Datos personales (PII) — emails, nombres, teléfonos en Users, Contacts, Leads
- [ ] Datos financieros
- [x] Credenciales de acceso — passwords con bcrypt, JWT tokens
- [x] Tokens / API keys — AzureOpenAI API key, JWT signing secret
- [ ] Datos de salud
- [ ] Ninguno
