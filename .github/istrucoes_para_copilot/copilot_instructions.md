# GitHub Copilot Instructions Template

This file provides standardized instructions for GitHub Copilot to follow when working on this project.

---
## 🤖 Instruções: Visão Geral do Projeto
---

Este projeto utiliza [descrição breve da arquitetura/framework principal] para criar [objetivos principais do sistema]. O sistema processa [tipo de entrada] e produz [tipo de saída], utilizando [tecnologias principais].

### 📁 Estrutura do Projeto

O projeto está organizado da seguinte forma:

*   **`app.py`**: [Descrição do ponto de entrada da aplicação]
*   **`[arquivo_principal].py`**: [Descrição do componente principal]
*   **`[outros_componentes].py`**: [Descrição de outros componentes importantes]
*   **`.env`**: Variáveis de ambiente (chaves de API, configurações, etc.)
*   **`pyproject.toml`**: Metadados do projeto e dependências Python.

### 🧠 Componentes Principais

O projeto utiliza os seguintes componentes:

1.  **[Componente 1]**
    *   **Propósito**: [Descrição sucinta]
    *   **Características**: [Atributos importantes]

2.  **[Componente 2]**
    *   **Propósito**: [Descrição sucinta]
    *   **Características**: [Atributos importantes]

### 📝 Fluxo de Execução

1.  **[Passo 1]**: [Descrição]
2.  **[Passo 2]**: [Descrição]
3.  **[Passo 3]**: [Descrição]

### 🧩 Dependências

Principais dependências: `[lista de dependências]`

### ⚙️ Configuração

*   **Variáveis de Ambiente**: [Lista de variáveis importantes]
*   **Arquivos de Configuração**: [Descrição dos arquivos]

---
## 🧰 Padrões de Código
---

### Convenções de Nomenclatura

*   **Classes**: PascalCase (Ex: `NomeDeClasse`)
*   **Métodos/Funções**: snake_case (Ex: `nome_de_funcao`)
*   **Variáveis**: snake_case (Ex: `nome_de_variavel`)
*   **Constantes**: UPPER_SNAKE_CASE (Ex: `NOME_DE_CONSTANTE`)

### Documentação

*   Usar docstrings para todas as classes, métodos e funções.
*   Seguir o formato [formato escolhido - Google, NumPy, etc.]

### Testes

*   Frameworks: [pytest/unittest/etc.]
*   Cobertura mínima: [percentual]%

---
## 📋 Padrões para Commits
---

### 🔄 Instruções: Commits Automáticos após Aceitação de Sugestões do GitHub Copilot

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
     - `[Copilot] Adiciona funcionalidade de processamento de dados`
     - `[Copilot] Corrige bug na consulta ao banco de dados`
     - `[Copilot] Refatora método de autenticação`

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
     [Copilot] Refatora lógica de autenticação
     
     - Simplifica o método authenticate no AuthService
     - Melhora a legibilidade do código e remove redundâncias
     - Arquivo modificado: auth_service.py
     ```

3. **Boas Práticas:**
   - Certifique-se de que a mensagem reflete claramente a intenção da modificação.
   - Use linguagem objetiva e evite mensagens genéricas como "update" ou "fix".

4. **Exemplo de Commit Completo:**
   ```
   [Copilot] Implementa nova funcionalidade de upload
   
   - Adiciona suporte para upload de arquivos múltiplos
   - Integra validação de formato e tamanho
   - Arquivo afetado: upload_service.py
   ```

### 🚀 Processo de Commit

1. **Detecção de Sugestões Aceitas:**
   - Sempre que uma sugestão do Copilot for confirmada e aplicada no código, o sistema deve identificar automaticamente as alterações.

2. **Geração de Commit:**
   - Após identificar que a alteração foi aplicada, crie um commit automático com a mensagem no formato definido acima.

3. **Commit Agrupado (Opcional):**
   - Para múltiplas sugestões aceitas em uma mesma sessão, agrupe as alterações em um único commit, detalhando cada uma no corpo da mensagem.

4. **Referências ao Código:**
   - Inclua informações sobre os arquivos ou métodos modificados, para facilitar o rastreamento.

---
## 📕 Guia de Estilo de Código
---

### Python

* Seguir PEP 8
* Comprimento máximo de linha: 88 caracteres
* Usar tipagem estática quando possível
* Usar formatadores automáticos (black, isort)

### JavaScript/TypeScript (se aplicável)

* Seguir ESLint com configuração padrão
* Preferir async/await a Promises encadeadas
* Usar tipagem estrita no TypeScript

---
## 🔄 Fluxo de Trabalho
---

### Desenvolvimento de Features

1. Criar branch a partir da main: `feature/nome-da-feature`
2. Desenvolver com commits pequenos e frequentes
3. Solicitar code review ao finalizar
4. Merge para main após aprovação

### Correção de Bugs

1. Criar branch a partir da main: `fix/descricao-do-bug`
2. Adicionar testes que reproduzem o bug
3. Corrigir o bug
4. Solicitar code review

---
## 🛠️ Ferramentas Recomendadas
---

* **Gerenciador de Pacotes**: Poetry ou uv
* **Formatter**: Black, isort
* **Linter**: Flake8, pylint
* **Testes**: pytest
* **CI/CD**: GitHub Actions

---
## 📚 Recursos e Documentação
---

* [Link para documentação interna]
* [Link para recursos externos]
* [Link para tutoriais relevantes]

---
## 🔄 Instruções para Atualização da Documentação

Este arquivo deve ser mantido atualizado com as versões mais recentes e as melhores práticas das bibliotecas e frameworks utilizados no projeto.

### Processo de Atualização

1. **Verificar as tecnologias**: Revisar periodicamente as versões das tecnologias e frameworks utilizados.
2. **Consultar documentações oficiais**: Buscar por atualizações nas documentações oficiais.
3. **Atualizar instruções**: Modificar este arquivo para refletir as informações mais recentes.
4. **Documentar atualizações**: Manter um registro das alterações realizadas com data e versão das tecnologias.

### Recomendação

Executar este processo de atualização ao menos uma vez a cada três meses ou quando houver atualizações significativas nas tecnologias utilizadas.

---
## 📝 Histórico de Atualizações

* **[DATA]**: Criação inicial do documento
* **[DATA]**: Atualização de [tecnologia] para versão [X.Y.Z]