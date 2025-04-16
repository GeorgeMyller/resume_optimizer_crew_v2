from crewai.tools import tool
from pylatexenc.latex2text import LatexNodes2Text


@tool("LatexReaderTool")
def LatexReaderTool(inputs: dict) -> str:
    """
    Extrai texto limpo e estruturado de um arquivo .tex de currículo.

    Espera um dict com chave: 'file_path'
    """
    file_path = inputs.get("file_path")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        clean_text = LatexNodes2Text().latex_to_text(content)
        return clean_text
    except Exception as e:
        return f"Erro ao ler arquivo .tex: {str(e)}"
