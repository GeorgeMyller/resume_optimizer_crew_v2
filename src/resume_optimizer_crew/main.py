'''
This is the main module that runs the resume optimization crew.
It loads environment variables, configures the crew, and kicks off the optimization process.
'''
import os
import sys
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

if __name__ == "__main__":
    result = crew.kickoff(inputs={})
    print(result)
