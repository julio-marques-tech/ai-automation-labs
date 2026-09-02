# Progresso — Trilha n8n

Log de labs concluídos, decisões técnicas e problemas resolvidos ao longo da trilha.

## Lab 00 — Instalação (Docker + WSL2)

**Estado:** concluído (2026-09-02)

**Feito:**
- WSL2 reparado e funcional (era necessário — instalação corrompida)
- Docker Desktop instalado (via `winget`), engine WSL2-based confirmado
- Extensão oficial "Claude Code for VS Code" instalada e autenticada
- n8n a correr como container Docker, com volume persistente (`n8n_data`),
  acessível em `localhost:5678`

**Decisões técnicas:**
- n8n local-only por agora (sem exposição de rede) — suficiente para
  aprendizagem, revisita-se se for preciso aceder de outro dispositivo
- Login no Claude Code via Claude.ai Subscription (não via Anthropic
  Console/API billing) — mais simples para uso interativo

**Problemas e resolução:** ver detalhe em
[lab-00-instalacao/README.md](lab-00-instalacao/README.md#problemas-encontrados-e-como-foram-resolvidos)

**Nota para trilhas futuras:** explorar AWS Bedrock / Azure AI Foundry como
backends alternativos ao Claude (relevante dado o background em Azure) —
registado em `CLAUDE.md`, trilha de Agentes de IA.
