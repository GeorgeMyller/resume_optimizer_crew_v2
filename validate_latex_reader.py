import sys
import os
# Ajusta o caminho para encontrar o pacote src/tools
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
import tempfile
from tools.latex_reader import LatexReaderTool

def main():
    # Cria um arquivo .tex temporário para teste
    content = r"\textbf{Teste}\newline Conteúdo"
    with tempfile.NamedTemporaryFile('w+', suffix='.tex', delete=False, encoding='utf-8') as tmp:
        tmp.write(content)
        tmp.flush()
        path = tmp.name
    # Executa a ferramenta
    # Invoke the raw function behind the Tool decorator
    result = LatexReaderTool.__wrapped__(inputs=None, file_path=path)
    print("Resultado da conversão:", result)
    # Valida o output
    if "Teste" in result and "Conteúdo" in result:
        print("Sucesso: LatexReaderTool está funcionando corretamente.")
        sys.exit(0)
    else:
        print("Erro: saída inesperada da ferramenta.")
        sys.exit(1)

if __name__ == '__main__':
    main()
