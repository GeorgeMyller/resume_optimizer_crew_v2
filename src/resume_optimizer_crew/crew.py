'''
This module defines the Crew object for the resume optimization process.
It orchestrates the agents and tasks involved in the process.
'''
from crewai import Crew, Process
from resume_optimizer_crew.config.tasks import tasks
from resume_optimizer_crew.config.agents import agents

crew = Crew(
    agents=list(agents.values()),
    tasks=list(tasks.values()),
    process=Process.sequential
)
