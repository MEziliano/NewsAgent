from crewai import Task

class NewsTasks:
    def scan_news_task(self, agent, urls):
        return Task(
            description=f"Scan the following RSS feeds for the latest important news: {urls}",
            expected_output="A list of the top 3-5 news items including title, link, and a brief summary for each.",
            agent=agent
        )

    def analyze_news_task(self, agent):
        return Task(
            description="Analyze the news items provided by the scanner. Use the search tool to find more context if needed and evaluate why these news items are important.",
            expected_output="A detailed analysis for each news item, providing context, potential impacts, and relevance.",
            agent=agent
        )

    def write_newsletter_task(self, agent):
        return Task(
            description="Based on the analysis, write a professional newsletter. It should be structured with a catchy title, a summary of each news item with its impact, and a concluding thought.",
            expected_output="A full newsletter in Markdown format, ready for distribution.",
            agent=agent
        )
