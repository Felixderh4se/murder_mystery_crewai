from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_openai import ChatOpenAI

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
	def MasterAgent(self) -> Agent:
		return Agent(
			config=self.agents_config['MasterAgent'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)

	@agent
	def DetectiveAgent(self) -> Agent:
		return Agent(
			config=self.agents_config['DetectiveAgent'],
			verbose=True
		)

	@agent
	def SuspectAgent(self) -> Agent:
		return Agent(
			config=self.agents_config['SuspectAgent'],
			verbose=True
		)

	@agent
	def WitnessAgent(self) -> Agent:
		return Agent(
			config=self.agents_config['WitnessAgent'],
			verbose=True
		)

	@agent
	def VictimAgent(self) -> Agent:
		return Agent(
			config=self.agents_config['VictimAgent'],
			verbose=True
		)

	@task
	def SuspectAgent(self) -> Task:
		return Task(
			config=self.tasks_config['SuspectAgent']
		)

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task'],
			output_file='report.md'
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