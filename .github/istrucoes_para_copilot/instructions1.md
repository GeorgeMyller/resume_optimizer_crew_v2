# GitHub Copilot Instructions (Genéricas)

Este arquivo oferece um modelo genérico de instruções para o GitHub Copilot, baseado na técnica de Custom Instructions descrita em https://code.visualstudio.com/blogs/2025/03/26/custom-instructions. Ele deve ser personalizado para cada projeto.

---
## 🤖 Instruções: `{{project_name}}` (Placeholder)
---

**Resumo:** Neste projeto, utilizamos o framework CrewAI para orquestrar agentes que realizam tarefas específicas (leitura, análise e edição) de forma colaborativa.

### 📁 Estrutura do Projeto (Genérica)

```
src/
  crew.py           # Configura e instancia o Crew
  main.py           # Ponto de entrada: carrega configs e executa o Crew
  config/
    agents.yaml     # Definições dos agentes
    tasks.yaml      # Definições das tarefas
  tools/
    pdf_reader.py   # Ferramenta para ler PDFs como material de apoio
    latex_reader.py # (Exemplo) Ferramenta para ler arquivos .tex
    web_scraper.py  # (Exemplo) Ferramenta para extrair conteúdo de URLs
input/
  resume.tex        # Exemplo de entrada (pode ser .tex, PDF, JSON etc.)
  pdfs/             # Pasta com PDFs de referência (materiais de apoio)
output/
  result.tex        # Saída gerada pelo Crew
.env                # Variáveis de ambiente (chaves de API, etc.)
pyproject.toml      # Metadados e dependências (gerenciadas com UV)
```  

### 🧠 Agentes (`config/agents.yaml`)

Use placeholders para cada agente:

1. **{{agent_id_1}}**
   - **role**: {{role_1}}
   - **goal**: {{goal_1}}
   - **backstory**: {{backstory_1}}
   - **tool**: {{tool_name_1}}

2. **{{agent_id_2}}**
   - **role**: {{role_2}}
   - **goal**: {{goal_2}}
   - **backstory**: {{backstory_2}}
   - **tool**: {{tool_name_2}}

> ⚙️ *Dica:* Para habilitar memória de curto prazo em um agente, defina `memory: true`.

### 📝 Tarefas (`config/tasks.yaml`)

Cada tarefa define uma ação orientada e seu agente responsável:

1. **{{task_id_1}}**
   - description: Leia e processe {{input_type_1}}.
   - expected_output: {{output_format_1}}
   - agent: {{agent_id_1}}

2. **{{task_id_2}}**
   - description: Analise o conteúdo para extrair {{tipo_de_info}}.
   - expected_output: {{output_format_2}}
   - agent: {{agent_id_2}}

> 📌 *Exemplo:* Para tarefas paralelas, use `async_execution: true` e em `crew.py` defina `process=Process.parallel`.

### 🧰 Ferramentas (`src/tools/`)

Adicione ferramentas para interagir com arquivos, APIs e PDFs:

* **PDFReaderTool** (`pdf_reader.py`)
  ```python
  @tool("PDFReaderTool")
  def read_pdf_folder(folder_path: str) -> List[str]:
      """Lê todos os PDFs em uma pasta de materiais auxiliares e retorna texto extraído"""
      # ... implementação usando libraries como PyPDF2 ou pdfminer
  ```
* **LatexReaderTool** (`latex_reader.py`) — exemplo de leitura de `.tex`
* **WebScraperTool** (`web_scraper.py`) — exemplo de scraping de URLs

> 📚 *Técnica de Auxílio com PDFs:* Coloque PDFs em `input/pdfs/`. O agente Reader pode usar `PDFReaderTool` para incorporar conteúdo extra de artigos, tutoriais ou specs como contexto para tarefas de análise.

### ⚙️ Fluxo do Crew (`src/crew.py`)

```python
# ...existing code...
crew = Crew(
    agents=load_agents('config/agents.yaml'),
    tasks=load_tasks('config/tasks.yaml'),
    process=Process.sequential,  # ou parallel, hierarchical
)
# ...existing code...
```  

### 🚀 Execução (`src/main.py`)

1. Carregue variáveis de ambiente (`.env`).
2. Configure cliente LLM (ex: OpenAI/Gemini).
3. Defina inputs:
   ```python
   inputs = {
       'resume_path': 'input/resume.tex',
       'pdf_folder': 'input/pdfs/',      # materiais de apoio
       'job_url': 'https://...'
   }
   ```
4. Execute:
   ```python
   result = crew.kickoff(inputs=inputs)
   save_output('output/result.tex', result)
   ```

### ✨ Boas Práticas

* Use `uv` para gerenciar dependências e ambientes:
  ```bash
  uv venv
  uv sync
  uv add crewai crewai-tools python-dotenv pylatexenc
  ```
* Mantenha `pyproject.toml` atualizado e gere `uv.lock`.
* Padronize nomes de arquivos e convenções YAML.

---
> Este modelo baseia‑se na técnica de Custom Instructions apresentada no artigo "Custom Instructions for Copilot" em https://code.visualstudio.com/blogs/2025/03/26/custom-instructions.
