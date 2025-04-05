from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileReadTool, CSVSearchTool
from dotenv import load_dotenv
import os

load_dotenv()

# Uncomment the following line to use an example of a custom tool
# from machcv.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class MatchcvCrew():
    """Matchcv crew"""

    @agent
    def cv_reader(self) -> Agent:
        return Agent(
            config=self.agents_config['cv_reader'],
            tools=[FileReadTool()],
            verbose=True,
            llm=LLM("gemini/gemini-1.5-flash", credentials=os.getenv('GOOGLE_API_KEY'))
        )
    @agent
    def job_opportunities_parser(self) -> Agent:
        return Agent(
            config=self.agents_config['job_opportunities_parser'],
            tools=[
                FileReadTool(),
                #CSVSearchTool()
            ],
            verbose=True,
            allow_delegation=False,
            llm=LLM("gemini/gemini-1.5-flash", credentials=os.getenv('GOOGLE_API_KEY'))
        )
    
    @agent
    def matcher(self) -> Agent:
        return Agent(
            config=self.agents_config['matcher'],
            tools=[
                FileReadTool(),
                #CSVSearchTool()
           ],
            verbose=True,
            llm=LLM("gemini/gemini-1.5-flash", credentials=os.getenv('GOOGLE_API_KEY')),
            output_file='new_cv.md'
        )
    
   
    @task
    def read_cv_task(self) -> Task:
        return Task(
            config=self.tasks_config['read_cv_task'],
            agent=self.cv_reader()
        )

    @task
    def match_cv_task(self) -> Task:
        return Task(
            config=self.tasks_config['match_cv_task'],
            agent=self.matcher()
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )