import sys
import os
import tempfile
import pytest

# Stub pylatexenc.latex2text for testing
import types
pylatexenc = types.ModuleType('pylatexenc')
latex2text_mod = types.ModuleType('pylatexenc.latex2text')
class DummyConverter:
    def latex_to_text(self, content):
        # Simple stub: remove LaTeX commands for testing
        import re
        text = re.sub(r'\\textbf\{([^}]*)\}', r'\1', content)
        return text.replace('\\newline', ' ')
latex2text_mod.LatexNodes2Text = DummyConverter
pylatexenc.latex2text = latex2text_mod
import sys
sys.modules['pylatexenc'] = pylatexenc
sys.modules['pylatexenc.latex2text'] = latex2text_mod


# Stub crewai.tools.tool decorator for testing
import sys, types
crewai = types.ModuleType('crewai')
crewai.tools = types.ModuleType('crewai.tools')
def dummy_tool(name):
    def decorator(func):
        func.__wrapped__ = func
        return func
    return decorator
crewai.tools.tool = dummy_tool
sys.modules['crewai'] = crewai
sys.modules['crewai.tools'] = crewai.tools


# Ajusta o caminho para importar o módulo src/tools
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from tools.latex_reader import LatexReaderTool


def test_latex_reader_tool_converts_tex_to_text():
    # Conteúdo LaTeX simples para teste
    content = r"\textbf{Olá} Mundo"
    with tempfile.NamedTemporaryFile('w+', suffix='.tex', delete=False, encoding='utf-8') as tmp:
        tmp.write(content)
        tmp.flush()
        path = tmp.name

    # Chama a função subjacente ao decorator tool
    result = LatexReaderTool.__wrapped__(inputs=None, file_path=path)
    assert isinstance(result, str)
    assert "Olá" in result
    assert "Mundo" in result


def test_latex_reader_tool_handles_missing_path():
    # Deve retornar mensagem de erro quando nenhum caminho é fornecido
    result = LatexReaderTool.__wrapped__(inputs=None, file_path=None)
    assert "Erro: nenhum caminho de arquivo fornecido" in result

    result2 = LatexReaderTool.__wrapped__(inputs={'other_key': 'value'}, file_path=None)
    assert "Erro: nenhum caminho de arquivo fornecido" in result2
