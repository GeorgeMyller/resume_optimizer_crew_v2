"""
This module defines the Crew object for the resume optimization process.
It orchestrates the agents and tasks defined in the YAML configuration files.
"""
import os
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
# Import necessary tools and config
from crewai_tools import FileReadTool, ScrapeWebsiteTool, PDFSearchTool
from tools.latex_reader import LatexReaderTool 
from dotenv import load_dotenv
from embedchain.config import AppConfig
from src.tools.gemini_embedder import GeminiEmbedder
from embedchain.embedder.base import BaseEmbedder

load_dotenv()


@CrewBase
class ResumeOptimizerCrew():
    """Resume Optimizer Crew"""

    @agent
    def curriculum_reader(self) -> Agent:
        # Crie a configuração específica para o embedder
        embedder_config = {
            "provider": "google",
            "config": {
            "model": "models/embedding-001",
            }
        }
        # Crie o dicionário de configuração para o App/PDFSearchTool
        # Inclua apenas as chaves esperadas pelo embedchain (neste caso, 'embedder')
        tool_config = {
            "embedder": embedder_config
        }

        return Agent(
            config=self.agents_config['curriculum_reader'],
            tools=[
                LatexReaderTool,
                PDFSearchTool(
                    pdf_url="src/input",
                    config=tool_config 
                    )],
            verbose=True,
            llm=LLM("gemini/gemini-1.5-flash", credentials=os.getenv('GOOGLE_API_KEY')),
        )

    @agent
    def job_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config['job_analyzer'],
            tools=[ScrapeWebsiteTool()],
            verbose=True,
            allow_delegation=False,
            llm=LLM("gemini/gemini-1.5-flash", credentials=os.getenv('GOOGLE_API_KEY'))
        )

    @agent
    def resume_editor(self) -> Agent:
        return Agent(
            config=self.agents_config['resume_editor'],
            tools=[],
            verbose=True,
            llm=LLM("gemini/gemini-1.5-flash", credentials=os.getenv('GOOGLE_API_KEY')),
            output_file='output/novo_curriculo.tex'
        )

    @task
    def extract_curriculum_data(self) -> Task:
        return Task(
            config=self.tasks_config['extract_curriculum_data'],
            agent=self.curriculum_reader()
        )

    @task
    def analyze_job_description(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_job_description'],
            agent=self.job_analyzer()
        )

    @task
    def adjust_resume_for_job(self) -> Task:
        return Task(
            config=self.tasks_config['adjust_resume_for_job'],
            agent=self.resume_editor()
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
