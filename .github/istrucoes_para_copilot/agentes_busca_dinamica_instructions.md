# 🤖 Documentação: Projeto `agentes_busca_dinamica`

Este projeto utiliza o framework CrewAI para criar um sistema que processa mensagens de texto ou áudio recebidas (provavelmente via WhatsApp através da Evolution API). Ele classifica a intenção da mensagem e direciona para diferentes equipes (Crews) de agentes de IA para gerar uma resposta apropriada, que é então convertida em áudio e enviada de volta ao remetente.

## 📁 Estrutura do Projeto

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

---

## 🧠 Agentes (Agents)

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

---

## 📝 Tarefas (Tasks)

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

---

## 🧰 Ferramentas (Tools)

*   **`QueryCSV` (`custom_tool_vendas.py`)**:
    *   **`name`**: Ferramenta de execução de código de consulta a um CSV
    *   **`description`**: Executa e retorna dados de uma consulta a partir de um CSV.
    *   **Funcionamento**: Recebe uma string contendo código Python (`codigo_python`). Executa este código usando `exec()` e retorna o valor da variável `resultado` definida dentro do contexto de execução desse código. É projetada para executar consultas pandas no arquivo CSV de vendas.

---

## ⚙️ Crew / Fluxo (Flow)

O projeto utiliza um `Flow` do CrewAI (`FluxoAudio` em `fluxo_audio.py`) para orquestrar a execução:

1.  **`@start()`**: O fluxo começa recebendo o texto da mensagem (`self.state.text`). Ele instancia e executa a `FacadeCrew` para classificar o texto. O resultado ('vendas' ou 'trivialidades') é armazenado em `self.state.tipo_msg`.
2.  **`@router(start)`**: Após a etapa inicial, este roteador direciona o fluxo com base no valor de `self.state.tipo_msg` (convertido para string minúscula).
3.  **`@listen("vendas")`**: Se o roteador direcionar para 'vendas', este método é executado. Ele instancia e executa a `SalesReportCrew` com o texto original da mensagem como query. O resultado (o parágrafo do relatório) é retornado como final do fluxo.
4.  **`@listen("trivialidades")`**: Se o roteador direcionar para 'trivialidades', este método é executado. Ele instancia e executa a `TalkingCrew` com o texto original. O resultado (a resposta do agente) é retornado como final do fluxo.

O processo é essencialmente sequencial dentro de cada rota possível após a classificação inicial.

---

## 🚀 Fluxo de Execução (`app.py`)

1.  **Recebimento:** A rota `/messages-upsert` do Flask recebe uma requisição POST (webhook da Evolution API).
2.  **Parsing:** O JSON da requisição é parseado pela classe `MessageSandeco` para extrair informações relevantes (remetente, tipo de mensagem, conteúdo).
3.  **Validação:** Verifica se a mensagem é do número de telefone autorizado ("351912331561").
4.  **Extração/Transcrição:**
    *   Se for texto (`conversation`), o texto é extraído diretamente.
    *   Se for áudio (`audioMessage`), a classe `Transcript` é usada para:
        *   Decodificar o áudio base64.
        *   Salvar temporariamente como arquivo `.wav`.
        *   Transcrever o áudio para texto usando Whisper.
        *   Remover o arquivo temporário.
5.  **Processamento CrewAI:** O `FluxoAudio` é instanciado e iniciado (`kickoff`) com o texto obtido. O fluxo interno (classificação e roteamento para a crew apropriada) é executado, retornando a resposta final em texto (`resposta`).
6.  **Síntese de Fala:** A classe `TextToSpeech` é usada para converter o texto da `resposta` em um arquivo de áudio (`output.mp3`) usando a API ElevenLabs.
7.  **Envio da Resposta:** A classe `SendSandeco` é usada para enviar o arquivo `output.mp3` de volta para o número de telefone do remetente original via Evolution API.
8.  **Tratamento de Erro:** Um bloco `try...except` captura exceções durante o processo e envia uma mensagem de erro em texto para o remetente.

---

## 🧩 Dependências (`pyproject.toml`)

As principais dependências incluem:

*   `crewai` e `crewai-tools`: Framework principal de agentes.
*   `flask`: Para criar o servidor web (webhook).
*   `python-dotenv`: Para carregar variáveis de ambiente.
*   `elevenlabs`: API para conversão de texto em fala.
*   `whisper-openai`: Modelo para transcrição de áudio.
*   `evolutionapi`: Biblioteca cliente para interagir com a Evolution API (WhatsApp).
*   `pandas` (implícito): Usado no código gerado pela `SalesReportCrew` para consultar o CSV.

---

## ⚙️ Configuração (`.env`)

O arquivo `.env` deve conter as seguintes variáveis:

*   Chaves de API para LLMs (OpenAI, DeepSeek - embora Gemini pareça ser o usado nos crews).
*   Configurações da Evolution API (`EVO_API_TOKEN`, `EVO_INSTANCE_TOKEN`, `EVO_INSTANCE_NAME`, `EVO_BASE_URL`).
*   Chave da API ElevenLabs (`ELEVENLABS_API_KEY`) e ID da voz (`SANDECO_VOICE_ID`).
