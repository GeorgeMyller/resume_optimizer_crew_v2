'''
This module defines the Crew object for the resume optimization process.
It orchestrates the agents and tasks involved in the process.
'''
# Set environment variable to disable chromadb's default embedding function
import os
os.environ['CHROMA_DISABLE_DEFAULT_EMBEDDING'] = "true"

from crewai import Crew, Process
from .config.tasks import tasks
from .config.agents import agents

crew = Crew(
    agents=list(agents.values()),
    tasks=list(tasks.values()),
    process=Process.sequential
)
