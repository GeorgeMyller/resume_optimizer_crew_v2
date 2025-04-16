from crewai.tools import tool
from pylatexenc.latex2text import LatexNodes2Text


@tool("LatexReaderTool")
def LatexReaderTool(file_path: str = None) -> str:
    """
    Extrai texto limpo e estruturado de um arquivo .tex de currículo.

    Você pode passar o caminho do arquivo .tex diretamente como `file_path`.
    """
    if not file_path:
        return "Erro: nenhum caminho de arquivo fornecido para LatexReaderTool."
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        clean_text = LatexNodes2Text().latex_to_text(content)
        return clean_text
    except Exception as e:
        return f"Erro ao ler arquivo .tex: {str(e)}"
