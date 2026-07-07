# Auditoría: VERP WebApp

**Branch:** `audit/2026-07-verp-webapp`
**Fecha:** 2026-07-07
**Estado:** En progreso
**Stack:** React 19 + TypeScript + Vite (Frontend) | FastAPI + Python 3.14 + SQLModel (IAM + CRM) | LangGraph + AzureOpenAI (AI Agent) | JWT + bcrypt (Auth) | SQLite/PostgreSQL (DB)

## Descripción

Auditoría de seguridad completa para VERP — ERP de energías renovables. Cubre:

- **Frontend:** React SPA con 17 módulos funcionales, JWT en localStorage, proxy API
- **IAM (Identity & Access Management):** FastAPI, autenticación JWT, bcrypt, RBAC, gestión de usuarios/permisos/servicios
- **CRM (Backend):** FastAPI, pipeline de leads/propuestas, visitas técnicas, agente AI con LangGraph

## Contenido

- `scope/` — Documentos de alcance
- `checklists/` — Checklists completadas
- `findings/` — Hallazgos (.md + .json)
- `reports/` — Reportes generados
- `evidence/` — Evidencia (screenshots, requests, tool output)
