from crewai.tools import tool
from pylatexenc.latex2text import LatexNodes2Text


@tool("LatexReaderTool")
def LatexReaderTool(inputs: dict = None, file_path: str = None) -> str:
    """
    Extrai texto limpo e estruturado de um arquivo .tex de currículo.

    Você pode passar o caminho do arquivo .tex diretamente como `file_path` ou via um dict `inputs` com chave 'file_path'.
    """
    # Determine the file path from provided arguments
    path = None
    if file_path:
        path = file_path
    elif inputs and isinstance(inputs, dict):
        path = inputs.get('file_path')
    if not path:
        return "Erro: nenhum caminho de arquivo fornecido para LatexReaderTool."
    try:
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
        clean_text = LatexNodes2Text().latex_to_text(content)
        return clean_text
    except Exception as e:
        return f"Erro ao ler arquivo .tex: {str(e)}"
