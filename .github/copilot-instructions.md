# GitHub Copilot Instructions

This file consolidates instructions for GitHub Copilot regarding various aspects of the BellaDerme project.

---
## 🤖 Instruções: Projeto `agentes_belladerme`
---

Este projeto utiliza o framework CrewAI para criar um sistema que processa mensagens de texto ou áudio recebidas (provavelmente via WhatsApp através da Evolution API). Ele classifica a intenção da mensagem e direciona para diferentes equipes (Crews) de agentes de IA para gerar uma resposta apropriada, que é então convertida em áudio e enviada de volta ao remetente.

### 📁 Estrutura do Projeto

O projeto está organizado da seguinte forma:

*   **`app.py`**: Aplicação Flask que serve como ponto de entrada (webhook) para receber mensagens. Orquestra a recepção, transcrição (se áudio), classificação, processamento pela CrewAI e envio da resposta.
*   **`fluxo_audio.py`**: Define o `FluxoAudio`, uma classe `Flow` do CrewAI que gerencia a lógica de roteamento entre diferentes crews com base na classificação da mensagem.
*   **`crew_facade.py`**: Define a `FacadeCrew`, responsável pela classificação inicial do texto da mensagem.
*   **`crew_sales_report.py`**: Define a `SalesReportCrew`, especializada em gerar relatórios consultando dados de vendas em um arquivo CSV.
*   **`crew_talking.py`**: Define a `TalkingCrew`, responsável por gerar respostas para mensagens classificadas como "trivialidades".
*   **`custom_tool_vendas.py`**: Define a ferramenta `QueryCSV` utilizada pela `SalesReportCrew` para executar código Python (pandas) e consultar o CSV de vendas.
*   **`generate.py`**: Contém a classe `TextToSpeech` para converter texto em áudio usando a API ElevenLabs.
*   **`transcript.py`**: Contém a classe `Transcript` para transcrever arquivos de áudio (recebidos em base64) para texto usando o modelo Whisper.
*   **`message_sandeco.py`**: Classe auxiliar para parsear e extrair informações das mensagens recebidas (estrutura da Evolution API).
*   **`send_sandeco.py`**: Classe auxiliar para enviar mensagens (texto, áudio, etc.) de volta usando a Evolution API.
*   **`vendas_ficticias_brasil.csv`**: Arquivo CSV com dados de vendas utilizado pela `SalesReportCrew`.
*   **`.env`**: Arquivo para armazenar variáveis de ambiente (chaves de API, configurações da Evolution API, etc.).
*   **`pyproject.toml`**: Define metadados do projeto e dependências Python.

### 🧠 Agentes (Agents)

O projeto utiliza os seguintes agentes CrewAI:

1.  **Classificador de Texto (`crew_facade.py`)**
    *   **`role`**: Classificador de Texto
    *   **`goal`**: Classificar um texto em duas categorias: 'Vendas' ou 'trivialidades'.
    *   **`backstory`**: Especialista em análise de linguagem, capaz de interpretar textos e classificá-los de acordo com o contexto: vendas ou trivialidades. A palavra deve estar em minúsculas.

2.  **Analista de Dados (`crew_sales_report.py`)**
    *   **`role`**: Analista de Dados
    *   **`goal`**: Criar códigos em Python que executam uma consulta em um determinado CSV.
    *   **`backstory`**: Analista de dados experiente, capaz de escrever códigos em Python capazes de extrair informações solicitadas de conjuntos de dados estruturados como arquivos CSV.

3.  **Redator (`crew_sales_report.py`)**
    *   **`role`**: Redator
    *   **`goal`**: Escrever um parágrafo baseado no contexto fornecido pelo Analista de Dados e pela solicitação `{query}`.
    *   **`backstory`**: Escritor habilidoso, capaz de transformar dados técnicos e análises em textos claros e cativantes, sempre mantendo um tom formal e direcionado ao chefe.

4.  **Processador de transcrições (`crew_talking.py`)**
    *   **`role`**: Processador de transcrições
    *   **`goal`**: Receber uma transcrição de áudio como texto e produzir uma resposta relevante e coerente.
    *   **`backstory`**: Especialista em compreender contextos e responder com clareza.

### 📝 Tarefas (Tasks)

As tarefas definidas para os agentes são:

1.  **Tarefa de Classificação (`crew_facade.py`)**
    *   **`description`**: Determina se o texto fala sobre 'vendas' ou 'trivialidades'.
    *   **`expected_output`**: Retorna somente uma das categorias: 'vendas' ou 'trivialidades' (em minúsculas).
    *   **`agent`**: Classificador de Texto

2.  **Tarefa de Consulta CSV (`crew_sales_report.py`)**
    *   **`description`**: Dada uma solicitação `{query}`, cria um código Python (usando pandas) para ler `vendas_ficticias_brasil.csv`, executar a consulta e atribuir o resultado formatado a uma variável `resultado`. Utiliza a ferramenta `QueryCSV` para executar o código.
    *   **`expected_output`**: Um texto em um parágrafo sobre: `{query}` (este output esperado parece ser do agente Redator, a tarefa do Analista na verdade gera o código e o executa, retornando o conteúdo da variável `resultado`).
    *   **`agent`**: Analista de Dados
    *   **`tools`**: `QueryCSV`

3.  **Tarefa de Redação de Relatório (`crew_sales_report.py`)**
    *   **`description`**: Usa o contexto fornecido pela tarefa anterior (resultado da consulta CSV) para escrever um parágrafo respondendo à solicitação `{query}`, começando com 'Oi Chefe' e explicando a resposta de forma clara, escrevendo valores numéricos por extenso.
    *   **`expected_output`**: Um parágrafo começando com 'Oi Chefe', explicando a resposta à solicitação `{query}`.
    *   **`agent`**: Redator
    *   **`context`**: Tarefa de Consulta CSV

4.  **Tarefa de Resposta Trivial (`crew_talking.py`)**
    *   **`description`**: Analisa o texto da transcrição `{transcription_text}` e fornece uma resposta clara e objetiva, começando sempre com 'Oi chefe', 'Fala professor', 'Oi professor' ou 'Aqui está chefe'.
    *   **`expected_output`**: Um texto com uma resposta coerente e relevante.
    *   **`agent`**: Processador de transcrições

### 🧰 Ferramentas (Tools)

*   **`QueryCSV` (`custom_tool_vendas.py`)**:
    *   **`name`**: Ferramenta de execução de código de consulta a um CSV
    *   **`description`**: Executa e retorna dados de uma consulta a partir de um CSV.
    *   **Funcionamento**: Recebe uma string contendo código Python (`codigo_python`). Executa este código usando `exec()` e retorna o valor da variável `resultado` definida dentro do contexto de execução desse código. É projetada para executar consultas pandas no arquivo CSV de vendas.

### ⚙️ Crew / Fluxo (Flow)

O projeto utiliza um `Flow` do CrewAI (`FluxoAudio` em `fluxo_audio.py`) para orquestrar a execução:

1.  **`@start()`**: O fluxo começa recebendo o texto da mensagem (`self.state.text`). Ele instancia e executa a `FacadeCrew` para classificar o texto. O resultado ('vendas' ou 'trivialidades') é armazenado em `self.state.tipo_msg`.
2.  **`@router(start)`**: Após a etapa inicial, este roteador direciona o fluxo com base no valor de `self.state.tipo_msg` (convertido para string minúscula).
3.  **`@listen("vendas")`**: Se o roteador direcionar para 'vendas', este método é executado. Ele instancia e executa a `SalesReportCrew` com o texto original da mensagem como query. O resultado (o parágrafo do relatório) é retornado como final do fluxo.
4.  **`@listen("trivialidades")`**: Se o roteador direcionar para 'trivialidades', este método é executado. Ele instancia e executa a `TalkingCrew` com o texto original. O resultado (a resposta do agente) é retornado como final do fluxo.

### 🚀 Fluxo de Execução (`app.py`)

1.  **Recebimento:** A rota `/messages-upsert` do Flask recebe uma requisição POST (webhook da Evolution API).
2.  **Parsing:** O JSON da requisição é parseado pela classe `MessageSandeco` para extrair informações relevantes (remetente, tipo de mensagem, conteúdo).
3.  **Validação:** Verifica se a mensagem é do número de telefone autorizado ("351912331561").
4.  **Extração/Transcrição:**
    *   Se for texto (`conversation`), o texto é extraído diretamente.
    *   Se for áudio (`audioMessage`), a classe `Transcript` é usada para transcrever o áudio para texto usando Whisper.
5.  **Processamento CrewAI:** O `FluxoAudio` é instanciado e iniciado (`kickoff`) com o texto obtido. O fluxo interno é executado, retornando a resposta final em texto (`resposta`).
6.  **Síntese de Fala:** A classe `TextToSpeech` é usada para converter o texto da `resposta` em áudio (`output.mp3`) usando a API ElevenLabs.
7.  **Envio da Resposta:** A classe `SendSandeco` é usada para enviar o áudio de volta via Evolution API.
8.  **Tratamento de Erro:** Captura exceções e envia mensagem de erro.

### 🧩 Dependências (`pyproject.toml`)

Principais dependências: `crewai`, `crewai-tools`, `flask`, `python-dotenv`, `elevenlabs`, `whisper-openai`, `evolutionapi`, `pandas`.

### ⚙️ Configuração (`.env`)

Requer chaves de API (LLMs, ElevenLabs) e configurações da Evolution API.

---
## 📸 Instruções: API do Instagram
---

Este documento resume como usar a API do Instagram para começar, publicar conteúdo e gerenciar menções, utilizando tanto o Login do Instagram quanto o Login do Facebook.

### Visão Geral

A Plataforma Instagram permite que aplicativos interajam com contas Profissionais do Instagram (Negócios e Criadores). APIs principais:

1.  **API com Login do Instagram:** Usuário do app é o dono da conta. Requer token de acesso do usuário do Instagram.
2.  **API com Login do Facebook:** Usuário do app gerencia Página do Facebook conectada. Requer token de acesso do usuário do Facebook com permissões.

### Primeiros Passos

**Pré-requisitos Comuns:** Conta Profissional Instagram, Conta Desenvolvedor Facebook, App Registrado no Facebook (tipo Negócios).

**Usando Login do Facebook:**
1.  Configurar Login do Facebook para Negócios no App.
2.  Implementar Login (pedir `instagram_basic`, `pages_show_list`).
3.  Obter Token de Acesso do Usuário Facebook.
4.  Obter Páginas (`GET /me/accounts`).
5.  Obter Conta Instagram Business (`GET /{page-id}?fields=instagram_business_account`) -> `ig-user-id`.
6.  Obter Mídia (Opcional: `GET /{ig-user-id}/media`).

**Usando Login do Instagram:**
1.  App Meta deve ser tipo Negócios.
2.  Obter Token de Acesso (Fluxo de Login ou Painel de Apps). Estender validade se necessário.
3.  Obter ID e Nome de Usuário (`GET /me?fields=user_id,username`) -> `<IG_ID>`.
4.  Obter Mídia (Opcional: `GET /<IG_ID>/media`).

### Publicação de Conteúdo

Publica fotos, vídeos, carrosséis, reels, stories.

**Requisitos:** Permissão `instagram_content_publish`, Token de Acesso, Servidor Público para mídia, Limite de 50 posts/24h.

**Endpoints:** `POST /{ig-user-id}/media` (criar contêiner), `POST /{ig-user-id}/media_publish` (publicar), `GET /{ig-container-id}?fields=status_code` (verificar status).

**Fluxo (Mídia Única):**
1.  `POST /{ig-user-id}/media` com `image_url` ou `video_url` (e `caption`, `media_type=STORIES/REELS`, etc.). -> `<IG_CONTAINER_ID>`.
2.  `POST /{ig-user-id}/media_publish` com `creation_id=<IG_CONTAINER_ID>`. -> `<IG_MEDIA_ID>`.

**Fluxo (Carrossel):**
1.  `POST /{ig-user-id}/media` para *cada item* com `is_carousel_item=true`. Guardar IDs.
2.  `POST /{ig-user-id}/media` com `media_type=CAROUSEL` e `children=[lista de IDs]`. -> ID contêiner carrossel.
3.  `POST /{ig-user-id}/media_publish` com `creation_id` do contêiner carrossel. -> ID mídia carrossel.

**Marcação de Produtos:** Possível, ver guia específico.

**Solução de Problemas:** Verificar status com `GET /{ig-container-id}?fields=status_code`.

### Menções e Tags

Identificar e responder a @menções, obter mídias marcadas.

**Requisitos:** Permissões `instagram_manage_comments`, `instagram_basic`, Token de Acesso.

**Endpoints:** `GET /{ig-user-id}/tags` (mídias marcadas), `POST /{ig-user-id}/mentions` (responder menção com `comment_id` e `message`).

**Limitações:** Não suporta menções em Stories, não permite comentar em fotos marcadas (usar API de Comentários). Webhooks podem falhar para contas privadas.

**Fluxo Comum:**
1.  Ouvir Webhooks para `mentions`.
2.  Obter Detalhes (opcional).
3.  Responder com `POST /{ig-user-id}/mentions`.

**Links de Referência:** Consultar documentação oficial linkada no arquivo original `api_instagram_instructions.md`.

---
## 🤖 Instruções para GitHub Copilot: Especialista em CrewAI
---

Estas instruções guiam o Copilot a colaborar de forma **especializada no framework CrewAI**.

### 📚 Sobre o CrewAI

CrewAI orquestra **agentes autônomos de IA** que colaboram em tarefas. Cada agente tem `role`, `goal`, `backstory` e é designado a `tasks`.

### 📁 Estrutura Padrão do Projeto CrewAI

```bash
src/nome_do_projeto/
├── config/
│   ├── agents.yaml      # Definição dos agentes
│   └── tasks.yaml       # Definição das tarefas
├── crew.py              # Monta a equipe e organiza a execução
├── main.py              # Executa a crew com inputs
└── tools/
    └── custom_tool.py   # Ferramentas personalizadas com @tool
```
*(Nota: O projeto `agentes_busca_dinamica` pode ter uma estrutura ligeiramente diferente, mas os conceitos são os mesmos).*

### 🧠 Agentes (`agents.yaml` ou definido em Python)

Definir com `role`, `goal`, `backstory`.
*   **Copilot deve:** Sugerir papéis especializados, metas claras, histórias consistentes.

### 📝 Tarefas (`tasks.yaml` ou definido em Python)

Definir com `description`, `expected_output`, `agent`.
*   **Copilot deve:** Sugerir tarefas com escopo claro, linguagem objetiva, resultados bem definidos.

### 🧰 Ferramentas (`tools/custom_tool.py` ou similar)

Funções Python com decorador `@tool` para ações externas.
*   **Copilot deve:** Sugerir ferramentas úteis para interações externas.

### ⚙️ Crew (`crew.py` ou similar)

Define a orquestração (`agents`, `tasks`, `process=Process.sequential/parallel`).
*   **Copilot deve:** Sugerir a ordem correta baseada nas dependências.

### 🚀 Início (`main.py` ou `app.py`)

Executa a crew com `kickoff(inputs={...})`.
*   **Copilot deve:** Sugerir entradas e testes.

### 🚨 Troubleshooting para Copilot

*   **Sugestões genéricas:** Adicionar mais contexto/exemplos.
*   **Erro YAML:** Validar indentação.
*   **Ferramenta ausente:** Verificar importação e decorador `@tool`.

### 💡 Dica final para o Copilot

Sempre proponha:
*   Papéis especializados.
*   Tarefas objetivas.
*   Ferramentas quando necessário.
*   Respeitar o fluxo de orquestração.

---
## 🤖 Manual de Instruções Gerais: CrewAI
---

Este manual guia no uso do framework CrewAI para criar equipes de agentes de IA colaborativos.

### 🧠 O que é o CrewAI?

Cria agentes com `role`, `goal`, `backstory`, `tools`, `memory` que colaboram em tarefas.

### 📁 Estrutura Padrão do Projeto

(Ver seção anterior "Instruções para GitHub Copilot: Especialista em CrewAI")

### ⚙️ Configurando Agentes (`agents.yaml` ou Python)

Definir `role`, `goal`, `backstory`.

### 📌 Configurando Tarefas (`tasks.yaml` ou Python)

Definir `description`, `expected_output`, `agent`.

### 🛠️ Criando Ferramentas Customizadas

Funções Python com `@tool` para ações específicas (APIs, DBs, etc.).

### 🚀 Executando o Projeto

1.  Instalar dependências (`pip install -e .` ou `uv pip sync`).
2.  Configurar variáveis de ambiente (API Keys).
3.  Executar (`python src/nome_do_projeto/main.py` ou via Flask app).

### 💡 Dicas para Colaboração

*   Comentar intenções no código.
*   Usar YAML/Python descritivo para agentes/tarefas.
*   Usar `TODO`s para guiar desenvolvimento.

### ✨ Melhorias no Fluxo de Trabalho CrewAI

*   **Gerenciamento de Memória:** Configurar `memory_retention`, `memory_window` no Agente.
*   **Execução Paralela:** Usar `async_execution=True` nas Tarefas.
*   **Hierarquia:** Usar `process=Process.hierarchical` na Crew para fluxos complexos.

### 🚨 Troubleshooting Comum

*   **Loop infinito:** `allow_delegation=False` ou revisar lógica.
*   **Output inconsistente:** Aumentar memória (`memory_retention`).
*   **Erro de delegação:** Definir `process=Process.hierarchical`.
*   **Perda de contexto:** Ajustar `memory_window`.

---
## ⚡ Instruções: Gerenciador de Pacotes `uv`
---

`uv` é um gerenciador de pacotes e projetos Python rápido, escrito em Rust, substituindo `pip`, `pip-tools`, `pipx`, etc.

### Destaques

*   Substitui múltiplas ferramentas.
*   10-100x mais rápido que `pip`.
*   Suporte a lockfiles, workspaces.
*   Gerencia versões Python e ambientes virtuais.

### Instalação

**Standalone (macOS/Linux):**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
**Standalone (Windows):**
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
**Via PyPI:**
```bash
pip install uv
# ou
pipx install uv
```
**Atualizar:**
```bash
uv self update
```

### Funcionalidades Principais

*   **Gerenciamento de Projetos:**
    ```bash
    uv init [nome_projeto]
    cd [nome_projeto]
    uv add [pacote]  # Adiciona ao pyproject.toml e instala
    uv run [comando] # Executa comando no ambiente virtual
    uv lock          # Gera uv.lock a partir de pyproject.toml
    uv sync          # Instala dependências do uv.lock (ou pyproject.toml)
    ```
*   **Ambientes Virtuais:**
    ```bash
    uv venv          # Cria .venv se não existir
    uv python install [versao] # Instala versão Python
    uv python pin [versao]    # Fixa versão para o diretório
    ```
*   **Interface `pip`:**
    ```bash
    uv pip install [pacote]
    uv pip uninstall [pacote]
    uv pip freeze > requirements.txt
    uv pip compile requirements.in -o requirements.txt
    uv pip sync requirements.txt
    ```
*   **Ferramentas CLI:**
    ```bash
    uv tool install [ferramenta] # Instala globalmente (isolado)
    uv tool uninstall [ferramenta]
    uvx [comando] [args...]     # Executa comando em ambiente temporário
    ```
*   **Scripts com Dependências Inline:**
    ```bash
    # script.py
    # /// script
    # dependencies = ["requests"]
    # ///
    import requests
    print(requests.get("https://example.com"))

    uv run script.py
    ```

### Suporte e Contribuição

Ver documentação oficial e guia de contribuição no repositório `astral-sh/uv`.

---
# 🤖 Instruções para Atualização da Documentação Interna do Copilot

Este arquivo define o processo para o GitHub Copilot manter atualizado o arquivo de instruções (`.github/copilot-instructions.md`). O objetivo é garantir que as instruções reflitam as versões mais recentes e as melhores práticas das bibliotecas e frameworks utilizados no projeto BellaDerme.

## 🎯 Objetivo

Manter este arquivo de instruções para o Copilot sincronizado com a documentação oficial e as versões mais recentes das tecnologias relevantes (ex: CrewAI, Flask, Evolution API, ElevenLabs, Whisper, UV, Instagram API, etc.).

## 📂 Escopo da Atualização

Este arquivo de instruções (`.github/copilot-instructions.md`) deve ser verificado e atualizado periodicamente para garantir que todas as seções estejam atualizadas:

*   `agentes_busca_dinamica_instructions.md`
*   `api_instagram_instructions.md`
*   `copilot_instructions.md`
*   `crewai_instructions.md`
*   `uv_instructions.md`
*   *(Qualquer outro arquivo `.md` adicionado posteriormente a esta pasta)*

## ⚠️ Prioridade

**Este processo de atualização deve ser a primeira tarefa realizada pelo Copilot ao iniciar o trabalho neste workspace.** Antes de prosseguir com outras solicitações, verifique e atualize este arquivo de instruções conforme descrito neste documento.

## 🔄 Processo de Atualização (Workflow para Copilot)

1.  **Ler Instruções Existentes:** Use a ferramenta `read_file` para carregar o conteúdo do arquivo `.github/copilot-instructions.md`.
2.  **Identificar Tecnologias:** Analise o conteúdo lido (texto e exemplos de código) para identificar todas as bibliotecas, frameworks, APIs ou ferramentas específicas mencionadas em cada seção (ex: `crewai`, `flask`, `evolutionapi`, `elevenlabs`, `whisper`, `uv`, Instagram API, etc.).
3.  **Pesquisar Documentação Atual:** Para cada tecnologia identificada no passo 2, use a ferramenta `vscode-websearchforcopilot_webSearch` para encontrar sua documentação oficial mais recente. Use consultas como:
    *   `"documentação oficial [nome da biblioteca] python"`
    *   `"latest release notes [nome da biblioteca]"`
    *   `"changelog [nome da biblioteca]"`
    *   `"API reference [nome da biblioteca] python"`
4.  **Comparar e Identificar Mudanças:** Compare as informações encontradas na documentação oficial recente com as instruções presentes no arquivo. Preste atenção especial a:
    *   **Mudanças na API:** Nomes de funções, classes, métodos, parâmetros, tipos de retorno, decoradores.
    *   **Funcionalidades Obsoletas (Deprecated):** Identifique se alguma funcionalidade mencionada nas instruções foi marcada como obsoleta.
    *   **Novas Funcionalidades:** Verifique se há novos recursos ou abordagens recomendadas que deveriam ser incluídos nas instruções.
    *   **Exemplos de Código:** Certifique-se de que os exemplos de código nas instruções ainda são válidos e seguem as práticas atuais.
    *   **Instalação e Configuração:** Verifique se os comandos de instalação ou etapas de configuração mudaram.
5.  **Aplicar Atualizações:** Se forem encontradas discrepâncias significativas ou informações desatualizadas:
    *   Use a ferramenta `insert_edit_into_file` para modificar seções específicas do arquivo.
    *   Atualize o texto explicativo e os exemplos de código para refletir as informações mais recentes.
    *   Seja claro sobre as mudanças (ex: "Atualizado para usar `nova_funcao()` em vez de `funcao_antiga()` conforme a versão X.Y").
    *   Mantenha a estrutura e o propósito original de cada seção do arquivo.
6.  **Documentar Atualizações:** Mantenha um registro das alterações realizadas com data e versão das tecnologias atualizadas no final do arquivo.

## 🛠️ Ferramentas a Utilizar

*   `read_file`: Para ler o conteúdo dos arquivos `.md`.
*   `vscode-websearchforcopilot_webSearch`: Para pesquisar a documentação mais recente.
*   `insert_edit_into_file`: Para aplicar as atualizações nos arquivos `.md`.

## 💡 Considerações Importantes

*   **Foco na Precisão:** As atualizações devem ser tecnicamente precisas e baseadas na documentação oficial.
*   **Clareza:** As instruções atualizadas devem permanecer claras e fáceis de entender.
*   **Contexto:** Mantenha o contexto original do arquivo de instrução ao fazer atualizações. Não adicione informações irrelevantes.
*   **Frequência:** Este processo deve ser executado periodicamente ou quando houver suspeita de uma atualização relevante em uma das tecnologias documentadas.
---
GeorgeMyller: 
@github  crie  orientaçoes para o copilot  sobre:

## 🔄 Instruções: Commits Automáticos após Uso do Módulo Agent
---

O GitHub Copilot deve automaticamente sugerir um commit sempre que o módulo `agent` for utilizado no projeto BellaDerme. Esta prática visa manter um histórico detalhado das alterações e interações com os agentes de IA.

### 📝 Formato do Commit

Ao sugerir commits após o uso do módulo `agent`, siga este formato:



GitHub: ### 🔄 Instruções: Commits Automáticos após Uso do Módulo Agent

---

O GitHub Copilot deve automaticamente sugerir um commit sempre que o módulo `agent` for utilizado no projeto BellaDerme. Esta prática visa manter um histórico detalhado das alterações e interações com os agentes de IA.

### 📝 Formato do Commit

Ao sugerir commits após o uso do módulo `agent`, siga este formato:

1. **Mensagem do Commit:**
   - A mensagem do commit deve ser clara, objetiva e seguir o padrão:
     ```
     [Agent] <Descrição da ação realizada>
     ```
   - Exemplos:
     - `[Agent] Atualiza lógica de classificação para mensagens de vendas`
     - `[Agent] Adiciona suporte ao processamento de áudio no fluxo`
     - `[Agent] Corrige erro na consulta ao CSV de vendas`

2. **Estrutura da Mensagem:**
   - Caso necessário, utilize um corpo descritivo para detalhar as alterações realizadas:
     ```
     [Agent] <Descrição resumida>
     
     - <Detalhamento das alterações realizadas>
     - <Impacto ou melhorias no fluxo>
     - <Notas adicionais, se houver>
     ```
   - Exemplo:
     ```
     [Agent] Implementa nova funcionalidade de transcrição de áudio
     
     - Adiciona suporte ao uso do Whisper para transcrição de áudio
     - Integra o resultado ao fluxo principal do CrewAI
     - Melhora o desempenho do fluxo de mensagens de áudio
     ```

3. **Referência ao Código ou Arquivo:**
   - Inclua referências aos arquivos ou classes principais modificados, quando aplicável. Exemplo:
     ```
     [Agent] Ajusta classificação de mensagens no FluxoAudio
     
     - Modificado arquivo: crew_facade.py
     - Atualizado método: classify_message
     ```

4. **Boas Práticas:**
   - Certifique-se de que a mensagem reflete claramente a intenção e o escopo da alteração.
   - Use linguagem descritiva e evite mensagens genéricas como "fix" ou "update".

5. **Exemplo de Commit Completo:**
   ```
   [Agent] Atualiza lógica de roteamento no FluxoAudio
   
   - Corrige erro ao classificar mensagens de áudio como trivialidades
   - Ajusta o método @router no fluxo principal para maior precisão
   - Arquivo afetado: fluxo_audio.py
   ```

### 🔎 Considerações Adicionais

- **Frequência de Commits:**
  - Sempre que o módulo `agent` for alterado, adicione um commit específico para essas mudanças.
  - Caso várias alterações sejam realizadas em uma única execução, agrupe mudanças relacionadas em um único commit.

- **Compatibilidade com Tarefas:**
  - Verifique se as alterações realizadas no módulo `agent` mantêm a compatibilidade com as tarefas definidas no fluxo do CrewAI.

- **Validação:** 
  - Antes de realizar o commit, garanta que os testes automatizados relacionados

GeorgeMyller: @github quero criar uma instruçao para cada vez que aceitar as modificaçoes do github copilot seja feito um commit automaticamente identificando as alteraçoes.

GitHub: ### 🔄 Instruções: Commits Automáticos após Aceitação de Sugestões do GitHub Copilot

---

O GitHub Copilot deve automaticamente sugerir um commit sempre que uma sugestão for **aceita e aplicada** no código. Esta prática visa manter um histórico claro e detalhado das alterações realizadas com o auxílio do Copilot.

### 📝 Formato do Commit

Ao sugerir commits após a aceitação de sugestões do Copilot, siga este formato:

1. **Mensagem do Commit:**
   - A mensagem deve descrever brevemente o contexto da modificação e indicar que foi gerada com o auxílio do Copilot.
   - Formato:
     ```
     [Copilot] <Descrição da alteração>
     ```
   - Exemplos:
     - `[Copilot] Adiciona lógica de transcrição no fluxo de áudio`
     - `[Copilot] Corrige bug na consulta ao CSV de vendas`
     - `[Copilot] Refatora método de roteamento no Flask app`

2. **Estrutura da Mensagem:**
   - Caso necessário, inclua um corpo descritivo para detalhar alterações ou contexto adicional:
     ```
     [Copilot] <Descrição resumida>
     
     - <Detalhamento das alterações realizadas>
     - <Impacto ou melhorias no código>
     - <Notas adicionais, se houver>
     ```
   - Exemplo:
     ```
     [Copilot] Refatora lógica de classificação de mensagens
     
     - Simplifica o método classify_message na FacadeCrew
     - Melhora a legibilidade do código e remove redundâncias
     - Arquivo modificado: crew_facade.py
     ```

3. **Boas Práticas:**
   - Certifique-se de que a mensagem reflete claramente a intenção da modificação.
   - Use linguagem objetiva e evite mensagens genéricas como "update" ou "fix".

4. **Exemplo de Commit Completo:**
   ```
   [Copilot] Implementa nova funcionalidade de geração de áudio
   
   - Adiciona suporte à API ElevenLabs para conversão de texto em áudio
   - Integra a funcionalidade ao fluxo principal do CrewAI
   - Arquivo afetado: generate.py
   ```

### 🚀 Processo Automático de Commit

1. **Detecção de Sugestões Aceitas:**
   - Sempre que uma sugestão do Copilot for confirmada e aplicada no código, o sistema deve identificar automaticamente as alterações.

2. **Geração de Commit:**
   - Após identificar que a alteração foi aplicada, crie um commit automático com a mensagem no formato definido acima.

3. **Commit Agrupado (Opcional):**
   - Para múltiplas sugestões aceitas em uma mesma sessão, agrupe as alterações em um único commit, detalhando cada uma no corpo da mensagem:
     ```
     [Copilot] Aceitação de múltiplas sugestões no fluxo de áudio
     
     - Adiciona suporte à transcrição de áudio no método transcribe_audio
     - Corrige erro de roteamento na classe FluxoAudio
     - Arquivos modificados: fluxo_audio.py, transcript.py
     ```

4. **Referências ao Código:**
   - Inclua informações sobre os arquivos ou métodos modificados, para facilitar o rastreamento.

### 🔎 Considerações Adicionais

- **Frequência:** O commit deve ser gerado imediatamente após a aceitação da sugestão, salvo o caso de commits agrupados.
- **Revisão Opcional:** Dependendo da política do projeto, os commits gerados podem passar por uma revisão antes de serem enviados ao repositório principal.