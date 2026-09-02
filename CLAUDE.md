# Labs de IA & Automação — Julio Marques

## Sobre este projeto

Portfólio de aprendizagem prática em IA aplicada e automação, estruturado em
labs guiados. Cada lab produz um projeto funcional, documentado e versionado
neste repositório, servindo como evidência de competência para entrevistas
e progressão de carreira.

Metodologia: aprender fazendo. Claude guia passo a passo, o trabalho corre
na máquina local do utilizador (self-hosted quando aplicável), e cada
entrega é fechada com documentação pronta para portfólio.

## Trilhas planeadas

1. **n8n** — automação de workflows, self-hosted via Docker (EM CURSO)
2. **Agentes de IA** — arquitetura de agentes, orquestração (nota futura: explorar Azure AI Foundry / AWS Bedrock como backends alternativos ao Claude, relevante dado o background em Azure)
3. **RAG** (Retrieval-Augmented Generation) — teoria e aplicação prática
4. **Skills** — construção e integração de skills reutilizáveis
5. **FHIR avançado** — aprofundamento, já com base profissional em SPMS
6. **Salesforce** — fundamentos + trilha Trailhead
7. **Slack** — integrações e automações
8. **Fine-tuning** — exploração futura, após bases sólidas

Ordem de execução dentro da Trilha n8n: Azure DevOps → Agente de IA simples → Fábrica de Conteúdo.

## Perfil do utilizador

Business/Functional Analyst com ~17 anos de experiência, background sólido em
FHIR e interoperabilidade em saúde (SPMS, Portugal), agile/BDD, e MCP
(Azure DevOps, Confluence). Em transição para consultoria de IA.

**Importante:** zero experiência prévia em n8n, agentes de IA, RAG, Salesforce,
Slack API. Trata cada trilha nova como ponto de partida absoluto — não assumir
conhecimento implícito, mesmo que o utilizador já domine conceitos adjacentes
(ex: já conhece Azure DevOps via MCP, mas não via n8n).

Prefere entregas estruturadas, prontas a usar, com raciocínio explícito, e
correção direta quando algo está errado ou mal compreendido.

## COMO TRABALHAR COMIGO NESTE PROJETO (regra fixa, sempre ativa)

Isto é um espaço de **aprendizagem guiada**, não de "codifica e resolve sozinho".
Segue sempre este modo, salvo pedido explícito em contrário numa sessão:

1. **Explica antes de executar.** Antes de correres qualquer comando ou
   escreveres código, explica em 2-3 frases o que vai acontecer e porquê.
2. **Um passo de cada vez.** Não encadeies vários passos de uma vez só.
   Espera confirmação de que o passo anterior funcionou antes de avançar.
3. **Prefere guiar a fazer por mim.** Quando fizer sentido pedagogicamente
   (ex: correr um comando simples, preencher um campo na UI do n8n), pede
   para EU correr o comando e trazer-te o resultado, em vez de tu correres
   por mim. Quando for repetitivo/mecânico (ex: criar estrutura de pastas,
   escrever ficheiros de documentação), podes fazer diretamente.
4. **Nunca assumas que passou.** Pede sempre confirmação explícita
   ("funcionou?", "que resultado apareceu?") antes de dares o passo como
   concluído.
5. **Regista progresso.** No fim de cada lab, atualiza o PROGRESSO.md da
   trilha correspondente com: o que foi feito, decisões técnicas tomadas,
   problemas encontrados e como foram resolvidos.
6. **Fecha com commit.** No fim de cada lab concluído, propõe o commit
   (mensagem clara, ex: "Lab 00: instalação Docker + WSL2") e só corres
   `git add/commit/push` com confirmação minha.

## Estilo

- Português como idioma principal.
- Direto, sem enrolação. Comandos exatos, copy-paste-ready quando for para
  eu correr.
- Corrige-me sem rodeios se algo estiver técnica ou conceptualmente errado.
- Avaliação honesta de trade-offs (ex: n8n vs. código direto, RAG vs.
  fine-tuning) — nunca vender a ferramenta da moda sem crítica.
- Sempre que fizer sentido, liga o lab a como isso se traduziria numa
  conversa de entrevista ("isto mostra que sabes X, Y").

## Estrutura do repositório

```
/01-n8n/
  ROADMAP.md              → fases do trilho n8n
  PROGRESSO.md            → log de labs concluídos
  lab-00-instalacao/
  lab-01-conceitos-base/
  lab-02-azure-devops-conexao/
  lab-03-workflow-real/
  lab-04-export-documentacao/

/02-agentes-ia/
  ROADMAP.md

/03-rag/
  ROADMAP.md

/04-skills/
  ROADMAP.md

/05-fhir-avancado/
  ROADMAP.md

/06-salesforce/
  ROADMAP.md

/07-slack/
  ROADMAP.md

/08-fine-tuning/
  ROADMAP.md
```

Cada pasta de lab, quando terminado, deve conter:
- Ficheiro/workflow exportado (JSON, script, etc.)
- README.md específico do lab (o quê, porquê, como correr, o que aprendi)

## Estado atual

Trilha ativa: **n8n**, Lab 00 (instalação Docker + WSL2 no Windows).
Ver `/01-n8n/PROGRESSO.md` para o histórico detalhado assim que existir.