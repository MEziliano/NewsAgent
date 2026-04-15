from crewai import Crew, Process
from .agents import NewsAgents
from .tasks import NewsTasks

class NewsCrew:
    def __init__(self, urls, model_name="llama3"):
        self.urls = urls
        self.agents = NewsAgents(model_name=model_name)
        self.tasks = NewsTasks()

    def run(self):
        # Initialize agents
        scanner = self.agents.scanner_agent()
        analyst = self.agents.analyst_agent()
        writer = self.agents.writer_agent()

        # Initialize tasks
        scan_task = self.tasks.scan_news_task(scanner, self.urls)
        analyze_task = self.tasks.analyze_news_task(analyst)
        write_task = self.tasks.write_newsletter_task(writer)

        # Create and run the crew
        crew = Crew(
            agents=[scanner, analyst, writer],
            tasks=[scan_task, analyze_task, write_task],
            process=Process.sequential,
            verbose=True
        )

        return crew.kickoff()
