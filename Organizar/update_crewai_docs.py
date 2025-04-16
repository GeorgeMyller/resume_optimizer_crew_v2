# Pair Programming Guidance Mechanism for Copilot and Gemini Code Assist

"""
Este script fornece orientações e práticas recomendadas para pair programming utilizando ferramentas como GitHub Copilot e Gemini Code Assist no contexto do projeto CrewAI.

Objetivo:
- Maximizar a colaboração entre programadores.
- Garantir que as sugestões de IA sejam relevantes e alinhadas com os objetivos do projeto.
- Facilitar a integração de novas ideias e práticas no fluxo de trabalho.
"""

import os
from pathlib import Path

# Caminhos importantes no projeto
PROJECT_ROOT = Path(__file__).parent.parent
AGENTS_FILE = PROJECT_ROOT / "src/config/agents.yaml"
TASKS_FILE = PROJECT_ROOT / "src/config/tasks.yaml"
TOOLS_DIR = PROJECT_ROOT / "src/tools"

# Função para exibir orientações gerais
def display_general_guidelines():
    print("""
    🧑‍💻 Orientações Gerais para Pair Programming com Copilot/Gemini:

    1. **Comunique-se constantemente:**
       - Explique suas intenções antes de escrever código.
       - Discuta as sugestões fornecidas pela IA com seu parceiro.

    2. **Use comentários claros:**
       - Adicione comentários para guiar a IA e seu parceiro.
       - Exemplo: # Criar um agente para análise de dados financeiros.

    3. **Valide as sugestões da IA:**
       - Sempre revise o código sugerido antes de aceitá-lo.
       - Teste as implementações para garantir que atendem aos requisitos.

    4. **Divida tarefas:**
       - Um programador pode focar na lógica principal enquanto o outro ajusta detalhes ou escreve testes.

    5. **Documente mudanças:**
       - Atualize os arquivos de documentação e YAML conforme necessário.
    """)

# Função para verificar consistência nos arquivos YAML
def validate_yaml_files():
    print("\n🔍 Validando arquivos YAML...")
    for file in [AGENTS_FILE, TASKS_FILE]:
        if not file.exists():
            print(f"⚠️ Arquivo não encontrado: {file}")
        else:
            print(f"✅ Arquivo encontrado: {file}")

# Função para sugerir melhorias no fluxo de trabalho
def suggest_workflow_improvements():
    print("""
    🚀 Sugestões para Melhorar o Fluxo de Trabalho:

    - **Integração de Ferramentas:**
      Use ferramentas personalizadas no diretório `src/tools` para automatizar tarefas repetitivas.

    - **Testes Automatizados:**
      Crie testes no diretório `tests/` para validar as implementações.

    - **Feedback Contínuo:**
      Utilize revisões de código para identificar melhorias e garantir qualidade.

    - **Orquestração de Tarefas:**
      Configure corretamente os arquivos `agents.yaml` e `tasks.yaml` para refletir as mudanças no projeto.
    """)

# Função principal
def main():
    print("\n=== Pair Programming Guidance ===")
    display_general_guidelines()
    validate_yaml_files()
    suggest_workflow_improvements()

if __name__ == "__main__":
    main()