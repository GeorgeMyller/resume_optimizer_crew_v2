# GitHub Copilot Instructions (Template)

This file provides a generic template for instructing GitHub Copilot on how to assist with a CrewAI-based project. Replace placeholders (e.g., `<project_name>`, `<tool_name>`, `<agent_name>`, etc.) with your project-specific details.

---
## 🤖 Instructions: `<project_name>` Project
---

**Summary:** This project uses the CrewAI framework to orchestrate autonomous agents that collaborate on tasks. The workflow typically involves reading input data (e.g., resumes, job descriptions), analyzing requirements, and producing optimized outputs.

### 📁 Project Structure (Example)

*   `src/main.py`: Entry point. Loads configurations, starts the Crew, and saves results.
*   `src/crew.py`: Defines the Crew, agents, and tasks.
*   `src/config/agents.yaml`: Defines the agents.
*   `src/config/tasks.yaml`: Defines the tasks.
*   `src/tools/<tool_name>.py`: Custom tools for agents.
*   `input/`: Input files (e.g., `.tex`, `.pdf`, `.txt`).
*   `output/`: Directory to save results.
*   `.env`: Environment variables (API keys, etc.).
*   `pyproject.toml`: Project metadata and dependencies (managed by `uv`).
*   `requirements.txt`: Dependencies (may be outdated; `pyproject.toml` is primary).

### 🧠 Agents (`src/config/agents.yaml`)

1.  **<agent_name>**
    *   `role`: <role>
    *   `goal`: <goal>
    *   `backstory`: <backstory>
    *   `tool`: `<tool_name>`

*(Add more agents as needed)*

### 📝 Tasks (`src/config/tasks.yaml`)

1.  **<task_name>**
    *   `description`: <description>
    *   `expected_output`: <expected_output>
    *   `agent`: <agent_name>

*(Add more tasks as needed)*

### 🧰 Tools (`src/tools/`)

*   **`<tool_name>` (`<tool_file>.py`)**:
    *   `@tool("<tool_name>")`
    *   `description`: <tool_description>
    *   How it works: <tool_usage>

#### 📚 Using PDFs as Auxiliary Material

To provide agents with additional context, place relevant PDF files in a dedicated folder (e.g., `input/pdfs/`). Implement a tool (e.g., `PDFReaderTool`) that can extract and summarize content from these PDFs. Agents can then use this tool to reference domain knowledge or background material during task execution.

**Example Tool Usage:**
```python
@tool("PDFReaderTool")
def read_pdf(file_path: str) -> str:
    """Extracts and returns text from a PDF file."""
    # Implementation here
```

Agents can be configured to use this tool for research or context enrichment.

### ⚙️ Crew Flow (`src/crew.py`, `src/main.py`)

1.  **Configuration (`crew.py`)**: Instantiate the Crew with agents and tasks from YAML files. Set the process (e.g., `Process.sequential`).
2.  **Execution (`main.py`)**:
    *   Load environment variables.
    *   Configure the LLM API.
    *   Start the Crew with `crew.kickoff(inputs={...})`.
    *   Print and save the result.

### 🧩 Dependencies (`pyproject.toml`)

Main ones: `crewai`, `crewai-tools`, `python-dotenv`, and any libraries needed for your tools (e.g., `pylatexenc`, `PyPDF2`, `requests`). Managed with `uv`.

### ⚙️ Configuration (`.env`)

Store API keys and configuration variables here.

---
## 🤖 General and Copilot Instructions: CrewAI Framework
---

**Summary:** CrewAI ([Official Documentation](https://docs.crewai.com/)) enables the orchestration of autonomous AI agents. See the [VS Code Custom Instructions article](https://code.visualstudio.com/blogs/2025/03/26/custom-instructions) for more on customizing Copilot's behavior.

### 📚 Core CrewAI Concepts

*   **Agents:** Entities with `role`, `goal`, `backstory`, `tools`, and `memory`.
*   **Tasks:** Actions agents perform, defined by `description` and `expected_output`.
*   **Tools:** Python functions with the `@tool` decorator for external interactions.
*   **Crew:** Orchestrates agent collaboration and task execution.

### 📁 Standard CrewAI Project Structure

```bash
src/<project_name>/
├── config/
│   ├── agents.yaml      # Agent definitions
│   └── tasks.yaml       # Task definitions
├── crew.py              # Crew assembly
├── main.py              # Entry point
└── tools/
    └── <tool_name>.py   # Custom tools
```

### 💡 How Copilot Should Help

*   Suggest agent roles, goals, and backstories.
*   Propose task descriptions and outputs.
*   Assist in tool implementation and usage.
*   Validate YAML structure.
*   Troubleshoot CrewAI errors and suggest best practices.

### ✨ Best Practices

*   Enable agent memory if needed.
*   Use parallel or hierarchical processes for complex flows.
*   Use PDF and other document tools for research/context.

---
## ⚡ Instructions: `uv` Package Manager
---

**Summary:** `uv` ([Official Documentation](https://astral.sh/uv)) is a fast Python package and project manager. Use it for dependency management and virtual environments.

### Key Commands

*   `uv init`          # Create `pyproject.toml`
*   `uv add <package>` # Add dependency
*   `uv sync`          # Install dependencies
*   `uv venv`          # Create/reuse virtual environment
*   `uv run <command>` # Run in venv

---
# 🤖 Instructions for Updating Copilot's Internal Documentation
---

**Objective:** Keep this file updated with the latest best practices for CrewAI, `uv`, and your project.

## 🔄 Update Process

1.  Read this file.
2.  Identify technologies used.
3.  Search for recent documentation and compare.
4.  Update sections as needed.
5.  Optionally, add a note about the date and versions checked.

---
## 🔄 Instructions: Automatic Commits (Suggestion)
---

**Objective:** Maintain a clear history of changes.

### 📝 Suggested Commit Message Format

1.  **Prefix:** `[CrewAI]`, `[Tool]`, `[Config]`, `[Docs]`, `[Refactor]`, `[Fix]`, `[Feat]`
2.  **Description:** Clear and concise.
3.  **Body (Optional):** Additional details.

---

*Based on [VS Code Custom Instructions article](https://code.visualstudio.com/blogs/2025/03/26/custom-instructions).*
