from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List


@CrewBase
class Debate:
    """Debate crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def ekonomist(self) -> Agent:
        return Agent(
            config=self.agents_config["ekonomist"],  # type: ignore[index]
            verbose=True,
        )

    @agent
    def analist(self) -> Agent:
        return Agent(
            config=self.agents_config["analist"],  # type: ignore[index]
            verbose=True,
        )

    @task
    def arastir(self) -> Task:
        return Task(config=self.tasks_config["arastir"])

    @task
    def karsicik(self) -> Task:
        return Task(config=self.tasks_config["karsicik"])

    @task
    def kararal(self) -> Task:
        return Task(config=self.tasks_config["kararal"])

    @crew
    def crew(self) -> Crew:
        """Creates the Debate crew"""

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
