"""
This module defines the Crew object for the resume optimization process.
It orchestrates the agents and tasks defined in the YAML configuration files.
"""
import os
from crewai import Crew, Process
from .config import agents  # Assuming agents are loaded from agents.yaml via this import
from .config import tasks    # Assuming tasks are loaded from tasks.yaml via this import

# Set environment variable to disable chromadb's default embedding function if needed
# os.environ['CHROMA_DISABLE_DEFAULT_EMBEDDING'] = "true" # Uncomment if chromadb is used and default embedding needs disabling

# Instantiate the Crew
# The agents and tasks are loaded from the imported dictionaries
resume_optimizer_crew = Crew(
    agents=list(agents.values()),
    tasks=list(tasks.values()),
    process=Process.sequential,  # Defines that tasks will run one after the other
    verbose=2 # Optional: Sets the verbosity level (0, 1, or 2)
    # memory=True # Optional: Enables memory for the crew
    # manager_llm=None # Optional: Define a manager LLM for hierarchical process
)

# Note: The actual kickoff and input handling will be in main.py as per instructions.
