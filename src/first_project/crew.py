from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_openai import ChatOpenAI
from .tools.custom_tool import MyCustomTool

# Uncomment the following line to use an example of a custom tool
# from first_project.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class FirstProjectCrew():
	"""FirstProject crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'


	@agent
	def CaseComposerAgent(self) -> Agent:
		return Agent(
			config=self.agents_config['CaseComposerAgent'],
			verbose=True,
			max_iter=2
		)

	@agent
	def MasterAgent(self) -> Agent:
		return Agent(
			config=self.agents_config['MasterAgent'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True,
			max_iter=2
		)


	@agent
	def DetectiveAgent(self) -> Agent:
		return Agent(
			config=self.agents_config['DetectiveAgent'],
			verbose=True,
			max_iter=2
		)

	@agent
	def SuspectAgent(self) -> Agent:
		return Agent(
			config=self.agents_config['SuspectAgent'],
			verbose=True,
			max_iter=2
		)

	@agent
	def WitnessAgent(self) -> Agent:
		return Agent(
			config=self.agents_config['WitnessAgent'],
			verbose=True,
			max_iter=2
		)

	@agent
	def VictimAgent(self) -> Agent:
		return Agent(
			config=self.agents_config['VictimAgent'],
			verbose=True,
			max_iter=2
		)


	@task
	def pacing_task(self) -> Task:
		return Task(
			config=self.tasks_config['pacing_task']
		)

	@task
	def compose_case_task(self) -> Task:
		return Task(
			config=self.tasks_config['compose_case_task']
		)

	@task
	def hint_provision_task(self) -> Task:
		return Task(
			config=self.tasks_config['hint_provision_task']
		)

	@task
	def alibi_task(self) -> Task:
		return Task(
			config=self.tasks_config['alibi_task']
		)

	@task
	def information_relay_task(self) -> Task:
		return Task(
			config=self.tasks_config['information_relay_task']
		)

	@task
	def clue_backstory_task(self) -> Task:
		return Task(
			config=self.tasks_config['clue_backstory_task']
		)

	@task
	def conclusion_drawing_task(self) -> Task:
		return Task(
			config=self.tasks_config['conclusion_drawing_task']
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the FirstProject crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)