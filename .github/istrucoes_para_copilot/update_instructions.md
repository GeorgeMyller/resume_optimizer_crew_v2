# 🤖 Instruções para Atualização da Documentação Interna do Copilot

Este arquivo define o processo para o GitHub Copilot manter atualizados os arquivos de instrução (`.md`) localizados nesta pasta (`Instruçoes para copilot/`). O objetivo é garantir que as instruções reflitam as versões mais recentes e as melhores práticas das bibliotecas e frameworks mencionados.

## 🎯 Objetivo

Manter os arquivos `.md` de instruções para o Copilot sincronizados com a documentação oficial e as versões mais recentes das tecnologias relevantes (ex: CrewAI, Flask, Evolution API, ElevenLabs, Whisper, UV, Instagram API, etc.).

## 📂 Arquivos Alvo

Os seguintes arquivos nesta pasta devem ser verificados e atualizados:

*   `agentes_busca_dinamica_instructions.md`
*   `api_instagram_instructions.md`
*   `copilot_instructions.md`
*   `crewai_instructions.md`
*   `uv_instructions.md`
*   *(Qualquer outro arquivo `.md` adicionado posteriormente a esta pasta)*

## ⚠️ Prioridade

**Este processo de atualização deve ser a primeira tarefa realizada pelo Copilot ao iniciar o trabalho neste workspace.** Antes de prosseguir com outras solicitações, verifique e atualize os arquivos listados acima conforme descrito neste documento.

## 🔄 Processo de Atualização (Workflow para Copilot)

1.  **Ler Instruções Existentes:** Para cada arquivo `.md` na pasta `Instruçoes para copilot/`, use a ferramenta `read_file` para carregar seu conteúdo.
2.  **Identificar Tecnologias:** Analise o conteúdo lido (texto e exemplos de código) para identificar todas as bibliotecas, frameworks, APIs ou ferramentas específicas mencionadas (ex: `crewai`, `flask`, `evolutionapi`, `elevenlabs`, `whisper`, `uv`, etc.).
3.  **Pesquisar Documentação Atual:** Para cada tecnologia identificada no passo 2, use a ferramenta `vscode-websearchforcopilot_webSearch` para encontrar sua documentação oficial mais recente. Use consultas como:
    *   `"documentação oficial [nome da biblioteca] python"`
    *   `"latest release notes [nome da biblioteca]"`
    *   `"changelog [nome da biblioteca]"`
    *   `"API reference [nome da biblioteca] python"`
4.  **Comparar e Identificar Mudanças:** Compare as informações encontradas na documentação oficial recente com as instruções presentes no arquivo `.md` correspondente. Preste atenção especial a:
    *   **Mudanças na API:** Nomes de funções, classes, métodos, parâmetros, tipos de retorno, decoradores.
    *   **Funcionalidades Obsoletas (Deprecated):** Identifique se alguma funcionalidade mencionada nas instruções foi marcada como obsoleta.
    *   **Novas Funcionalidades:** Verifique se há novos recursos ou abordagens recomendadas que deveriam ser incluídos nas instruções.
    *   **Exemplos de Código:** Certifique-se de que os exemplos de código nas instruções ainda são válidos e seguem as práticas atuais.
    *   **Instalação e Configuração:** Verifique se os comandos de instalação ou etapas de configuração mudaram.
5.  **Aplicar Atualizações:** Se forem encontradas discrepâncias significativas ou informações desatualizadas:
    *   Use a ferramenta `insert_edit_into_file` para modificar o arquivo `.md` correspondente.
    *   Atualize o texto explicativo e os exemplos de código para refletir as informações mais recentes.
    *   Seja claro sobre as mudanças (ex: "Atualizado para usar `nova_funcao()` em vez de `funcao_antiga()` conforme a versão X.Y").
    *   Mantenha a estrutura e o propósito original do arquivo de instrução.
6.  **Repetir:** Execute os passos 1 a 5 para todos los arquivos `.md` alvo.

## 🛠️ Ferramentas a Utilizar

*   `read_file`: Para ler o conteúdo dos arquivos `.md`.
*   `vscode-websearchforcopilot_webSearch`: Para pesquisar a documentação mais recente.
*   `insert_edit_into_file`: Para aplicar as atualizações nos arquivos `.md`.

## 💡 Considerações Importantes

*   **Foco na Precisão:** As atualizações devem ser tecnicamente precisas e baseadas na documentação oficial.
*   **Clareza:** As instruções atualizadas devem permanecer claras e fáceis de entender.
*   **Contexto:** Mantenha o contexto original do arquivo de instrução ao fazer atualizações. Não adicione informações irrelevantes.
*   **Frequência:** Este processo deve ser executado periodicamente ou quando houver suspeita de uma atualização relevante em uma das tecnologias documentadas.
