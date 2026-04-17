from crewai import Task

class NewsTasks:
    def scan_news_task(self, agent, urls):
        """     
        Create a task for the scanner agent to scan the given RSS feeds
        and return a list of the top 3-5 news items including title, link, and a brief summary for each.

        Args:
            agent (Agent): The scanner agent responsible for executing this task.
            urls (List[str]): A list of RSS feed URLs to scan.

        Returns:
            Task: A task representing the scanning of the given RSS feeds.
        """
        return Task(
            description=f"Scan the following RSS feeds for the latest important news: {urls}",
            expected_output="A list of the top 3-5 news items including title, link, and a brief summary for each.",
            agent=agent
        )

    def analyze_news_task(self, agent):
        """Create a task for the analyst agent to analyze the news items provided by the scanner agent.

        The analyst should use the search tool to find more context if needed and evaluate why these news items are important.
        The expected output is a detailed analysis for each news item, providing context, potential impacts, and relevance.

        Args:
            agent (Agent): The analyst agent responsible for executing this task.

        Returns:
            Task: A task representing the analysis of the news items.
        """
        return Task(
            description="Analyze the news items provided by the scanner. Use the search tool to find more context if needed and evaluate why these news items are important.",
            expected_output="A detailed analysis for each news item, providing context, potential impacts, and relevance.",
            agent=agent
        )

    def write_newsletter_task(self, agent):
        """     
        Create a task for the writer agent to write a professional newsletter based on the analysis provided by the analyst agent.

        The expected output is a full newsletter in Markdown format, ready for distribution.

        Args:
            agent (Agent): The writer agent responsible for executing this task.

        Returns:
            Task: A task representing the writing of a newsletter.
        """
        return Task(
            description="Based on the analysis, write a professional newsletter. It should be structured with a catchy title, a summary of each news item with its impact, and a concluding thought.",
            expected_output="A full newsletter in Markdown format, ready for distribution.",
            agent=agent
        )
