'''
This is the main module that runs the resume optimization crew.
It loads environment variables, configures the crew, and kicks off the optimization process.
'''
import os
import sys
from datetime import datetime
sys.path.append('/Users/georgesouza/Desktop/Python2025/Curriculo/resume_optimizer_crew_v2/src')
from resume_optimizer_crew.crew import crew
from dotenv import load_dotenv

# Load environment variables from .env file

# Load variables from .env file
load_dotenv()

# Check if required environment variables exist
if not os.environ.get("OPENAI_API_KEY"):
    print("Warning: OPENAI_API_KEY not found in .env file")

if not os.environ.get("OPENAI_API_BASE"):
    # Set default API base if not provided
    os.environ["OPENAI_API_BASE"] = "https://generativelanguage.googleapis.com/v1beta"
    
if not os.environ.get("OPENAI_MODEL_NAME"):
    # Set default model if not provided
    os.environ["OPENAI_MODEL_NAME"] = "gemini-pro"

def generate_unique_filename(base_name="output", extension=".tex"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{base_name}_{timestamp}{extension}"

if __name__ == "__main__":
    result = crew.kickoff(inputs={})
    print(result)
    unique_filename = generate_unique_filename(base_name="novo_curriculo")
    output_path = os.path.join("output", unique_filename)
    # Salvar o arquivo com o nome único
    with open(output_path, "w") as output_file:
        output_file.write("Conteúdo gerado pelo CrewAI")  # Substitua pelo conteúdo real
    print(f"Arquivo gerado: {output_path}")
