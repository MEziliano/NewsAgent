from crewai import Agent, LLM
from .tools.rss_tool import RSSTool
from langchain_community.tools import DuckDuckGoSearchRun
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

class SearchInput(BaseModel):
    """Input for the Search Tool."""
    query: str = Field(..., description="The search query to look up on the internet.")

class DuckDuckGoTool(BaseTool):
    name: str = "Search Tool"
    description: str = "Search the internet for more context on news items."
    args_schema: Type[BaseModel] = SearchInput

    def _run(self, query: str) -> str:
        return DuckDuckGoSearchRun().run(query)

class NewsAgents:
    def __init__(self, model_name="llama3"):
        """
        Initialize the NewsAgents object.

        Args:
            model_name (str, optional): The name of the model to use for the LLM. Defaults to "llama3".

        Initializes the RSS Tool, Search Tool, and LLM model with the given model name.
        """
        self.rss_tool = RSSTool()
        self.search_tool = DuckDuckGoTool()
        self.llm = LLM(model=f"openai/{model_name}", base_url="http://localhost:11434/v1")

    def scanner_agent(self):
        """
        Return an Agent object representing the scanner agent.

        This agent is responsible for identifying the most relevant news from RSS feeds and other sources.
        It is given the RSS Tool and the LLM model, and is allowed to be verbose and does not allow delegation.

        Returns:
            Agent: An Agent object representing the scanner agent.
        """
        return Agent(
            role="News Scanner",
            goal="Identify the most relevant news from RSS feeds and other sources.",
            backstory="You are an expert in monitoring data streams. Your job is to extract the most important headlines from the provided sources.",
            tools=[self.rss_tool],
            llm=self.llm,
            verbose=True,
            allow_delegation=False
        )

    def analyst_agent(self):
        """
        Return an Agent object representing the analyst agent.

        This agent is responsible for providing context and evaluating the impact of the news found.
        It is given the Search Tool and the LLM model, and is allowed to be verbose and allows delegation.

        Returns:
            Agent: An Agent object representing the analyst agent.
        """
        return Agent(
            role="Market Analyst",
            goal="Provide context and evaluate the impact of the news found.",
            backstory="You are a seasoned analyst who understands market trends and social impact. You take headlines and find the deeper meaning.",
            tools=[self.search_tool],
            llm=self.llm,
            verbose=True,
            allow_delegation=True
        )

    def writer_agent(self):
        """
        Return an Agent object representing the writer agent.

        This agent is responsible for summarizing the findings and creating a concise and professional newsletter.
        It is given the LLM model, and is allowed to be verbose and does not allow delegation.

        Returns:
            Agent: An Agent object representing the writer agent.
        """
        return Agent(
            role="Senior Editor",
            goal="Create a concise and professional newsletter summarizing the findings.",
            backstory="You are a world-class editor. You transform complex information into easy-to-read, engaging newsletters.",
            llm=self.llm,
            verbose=True,
            allow_delegation=False
        )
