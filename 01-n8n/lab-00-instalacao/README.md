# Lab 00 — Instalação (Docker + WSL2 + n8n)

## O quê

Preparar o ambiente local no Windows para correr o n8n self-hosted via Docker,
e ligar o Claude Code ao VSCode como ambiente de trabalho para a trilha.

## Porquê

O n8n corre melhor como container Docker — isola dependências, é fácil de
atualizar/remover, e reflete como se corre em produção (self-hosted num
servidor). No Windows, o Docker Desktop precisa do WSL2 como motor de
virtualização por baixo.

## O que foi instalado

- **WSL2** (Windows Subsystem for Linux) — motor de virtualização exigido
  pelo Docker Desktop no Windows
- **Docker Desktop** — via `winget install -e --id Docker.DockerDesktop`
- **Extensão "Claude Code for VS Code"** (publisher Anthropic) — integração
  do Claude Code diretamente no editor, autenticada via Claude.ai Subscription
- **n8n** — a correr como container Docker, com volume persistente

## Problemas encontrados e como foram resolvidos

### WSL2 corrompido (`REGDB_E_CLASSNOTREG`)

Ao correr `wsl --version` pela primeira vez, o Windows devolveu:
```
wsl: WSL installation appears to be corrupted (Error code: Wsl/CallMsi/Install/REGDB_E_CLASSNOTREG)
```

**Causa:** componente COM do WSL mal registado — comum quando a feature do
Windows nunca foi corretamente ativada.

**Resolução:**
1. Ativar as duas features do Windows necessárias (PowerShell como
   Administrador):
   ```powershell
   dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
   dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
   ```
2. Reiniciar o PC (as features só ficam ativas após reboot)
3. Correr `wsl --update` e, quando aparecer o prompt "Press any key to
   repair WSL", deixar o auto-reparo correr (em vez de cancelar)

Depois disto, `wsl --version` passou a devolver a versão sem erro.

### Docker: comando não reconhecido logo após instalar

Depois de instalar o Docker Desktop via `winget`, o comando `docker` não era
reconhecido no PowerShell. **Causa:** a janela do terminal já estava aberta
antes da instalação terminar, e o Windows só atualiza o `PATH` em janelas
novas. **Resolução:** abrir um novo terminal.

## Como correr

```powershell
# Subir o n8n com dados persistentes
docker volume create n8n_data
docker run -d --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n

# Confirmar que está a correr
docker ps
```

Depois, aceder a [http://localhost:5678](http://localhost:5678).

Para parar/retomar sem perder dados:
```powershell
docker stop n8n
docker start n8n
```

## O que aprendi

- Diferença entre WSL1/WSL2 e porque o Docker Desktop no Windows depende do
  WSL2 como motor de virtualização
- Diagnosticar e reparar uma instalação de WSL corrompida via DISM
  (ativação de features do Windows) em vez de reinstalar tudo do zero
- Diferença entre imagem, container e volume Docker — e porque um volume é
  necessário para não perder dados do n8n entre reinícios
- Instalar e autenticar a extensão oficial "Claude Code for VS Code",
  distinguindo-a de extensões não-oficiais com nomes semelhantes no
  Marketplace
- Existem backends alternativos para correr Claude em contexto empresarial
  (AWS Bedrock, Azure AI Foundry, Google Vertex) — a explorar mais à frente
  na trilha de Agentes de IA
