from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class Debate():
    """Debate crew"""

    agents = "config/agents.yaml"
    tasks = "config/tasks.yaml"

    @agent
    def debatedor(self) -> Agent:
        return Agent(
            config=self.agents_config['debatedor'],
            verbose=True
        )

    @agent
    def juiz(self) -> Agent:
        return Agent(
            config=self.agents_config['juiz'],
            verbose=True
        )
    

    @task
    def realizar_proposta(self) -> Task:
        return Task(
            config=self.tasks_config['realizar_proposta'], # type: ignore[index]
        )

    @task
    def negar_proposta(self) -> Task:
        return Task(
            config=self.tasks_config['negar_proposta'], # type: ignore[index]
            #output_file='report.md'
        )
    
    @task
    def decide(self) -> Task:
        return Task(
            config=self.tasks_config['decide'], # type: ignore[index]
            #output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Debate crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
