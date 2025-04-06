import os
import subprocess
import sys

# Diretório do código-fonte
source_dir = "src"

# Verifica se o diretório existe
if not os.path.isdir(source_dir):
	print(f"Erro: Diretório '{source_dir}' não encontrado.")
	sys.exit(1)

# Verifica se pyreverse está instalado
try:
	subprocess.run(["pyreverse", "--help"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
except (subprocess.SubprocessError, FileNotFoundError):
	print("pyreverse não encontrado. Instalando pylint...")
	subprocess.check_call([sys.executable, "-m", "pip", "install", "pylint"])

# Comando para gerar diagramas UML
try:
	subprocess.run(["pyreverse", "-o", "png", "-p", "Diagrama", source_dir], check=True)
	print("Diagramas UML gerados com sucesso.")
except subprocess.SubprocessError as e:
	print(f"Erro ao gerar diagramas UML: {e}")
