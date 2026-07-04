# Determinación de Cobertura

## Reglas por tipo de aplicación

| Tipo de App | Checklists obligatorias | Checklists opcionales |
|-------------|------------------------|----------------------|
| **SPA / Frontend** | 01-auth, 02-session, 03-input, 06-crypto, 07-infra | 04-authz, 05-api, 08-data |
| **REST API** | 01-auth, 02-session, 03-input, 04-authz, 05-api, 06-crypto | 07-infra, 08-data, 09-deps |
| **GraphQL API** | 01-auth, 04-authz, 05-api, 03-input | 02-session, 06-crypto |
| **E-commerce** | 01-auth, 03-input, 04-authz, 11-ecommerce, 12-bizlogic | 02-session, 05-api, 06-crypto, 07-infra, 08-data |
| **CMS** | 01-auth, 03-input, 04-authz, 07-infra | 02-session, 09-deps, 10-ci-cd |
| **Microservicios** | 01-auth, 05-api, 06-crypto, 07-infra, 09-deps, 10-ci-cd | 02-session, 03-input, 04-authz |
| **Internal tool** | 01-auth, 04-authz, 08-data, 12-bizlogic | 02-session, 03-input, 07-infra |

## Reglas de activación por tecnología

| Tecnología | Checklists adicionales |
|------------|------------------------|
| JWT | 02-session (JWT validation, alg=none, expiry) |
| OAuth / OIDC | 01-auth (OAuth flows, redirect URIs, state param) |
| GraphQL | 05-api (introspection, depth limiting, batching) |
| File upload | 03-input (malicious files, path traversal, MIME) |
| Payments | 11-ecommerce (PCI DSS, amount tampering, refunds) |
| Docker / K8s | 07-infra (container escape, secrets, network policies) |

## Profundidad de Auditoría

| Nivel | Descripción | Cuándo aplica |
|-------|-------------|--------------|
| **L1 (Superficial)** | OWASP Top 10 básico + ASVS L1 | App interna sin datos sensibles |
| **L2 (Estándar)** | L1 + checklists por dominio + SAST | App con usuarios reales |
| **L3 (Profunda)** | L2 + DAST + revisión manual + SCA | App con datos financieros o PII |
| **L4 (Completa)** | L3 + pentest + compliance (PCI/GDPR) | E-commerce, fintech, health |
