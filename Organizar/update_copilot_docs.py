import os
import requests
from pathlib import Path
from packaging import version

# Configurações do projeto
PROJECT_ROOT = Path(__file__).parent
DOCS_DIR = PROJECT_ROOT / "docs"
COPILOT_INSTRUCTIONS = PROJECT_ROOT / "copilot_instructions.md"
PYPI_URL = "https://pypi.org/pypi/crewai/json"
GITHUB_RAW_URL = "https://raw.githubusercontent.com/joaomdmoura/crewai/main/"

# Função para obter a versão instalada do CrewAI
def get_installed_version():
    try:
        import crewai
        return crewai.__version__
    except ImportError:
        return None

# Função para obter a versão mais recente do CrewAI no PyPI
def get_latest_version():
    response = requests.get(PYPI_URL)
    if response.status_code == 200:
        data = response.json()
        return data["info"]["version"]
    return None

# Função para baixar arquivos do GitHub

def download_file(file_name, save_path):
    url = GITHUB_RAW_URL + file_name
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, "w", encoding="utf-8") as f:
            f.write(response.text)
        print(f"✅ Arquivo atualizado: {save_path}")
    else:
        print(f"⚠️ Não foi possível baixar o arquivo: {file_name}")

# Função principal para verificar e atualizar
def main():
    print("\n=== Atualização do Copilot Docs ===")

    # Verificar versão instalada e mais recente
    installed_version = get_installed_version()
    latest_version = get_latest_version()

    if not installed_version:
        print("⚠️ CrewAI não está instalado no ambiente atual.")
    else:
        print(f"Versão instalada do CrewAI: {installed_version}")

    if latest_version:
        print(f"Última versão disponível no PyPI: {latest_version}")

        if not installed_version or version.parse(latest_version) > version.parse(installed_version):
            print("🔄 Atualização necessária. Baixando arquivos do GitHub...")

            # Criar diretório docs se não existir
            DOCS_DIR.mkdir(exist_ok=True)

            # Baixar README.md e CHANGELOG.md
            download_file("README.md", DOCS_DIR / "crewai_README_remote.md")
            download_file("CHANGELOG.md", DOCS_DIR / "crewai_CHANGELOG_remote.md")

            # Sugerir atualização do copilot_instructions.md
            if COPILOT_INSTRUCTIONS.exists():
                print("📄 Sugestão: Atualize o copilot_instructions.md com base nos novos arquivos baixados.")
            else:
                print("⚠️ Arquivo copilot_instructions.md não encontrado. Considere criá-lo.")
        else:
            print("✅ Você já está usando a versão mais recente do CrewAI.")
    else:
        print("⚠️ Não foi possível obter a última versão do CrewAI no PyPI.")

if __name__ == "__main__":
    main()