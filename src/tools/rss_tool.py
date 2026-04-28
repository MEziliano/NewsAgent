import feedparser
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import List, Dict, Type

class RSSInput(BaseModel):
    """Input for the RSS Feed Reader tool."""
    urls: List[str] = Field(..., description="A list of RSS feed URLs to parse.")

class RSSTool(BaseTool):
    name: str = "RSS Feed Reader"
    description: str = "Reads and parses RSS feeds from a list of URLs. Returns a list of entries with title, link, and summary."
    args_schema: Type[BaseModel] = RSSInput

    def _run(self, urls: List[str]) -> List[Dict[str, str]]:
        all_entries = []
        for url in urls:
            feed = feedparser.parse(url)
            for entry in feed.entries[:5]: # Get latest 5 from each
                all_entries.append({
                    "title": entry.title,
                    "link": entry.link,
                    "summary": entry.get("summary", "No summary available"),
                    "published": entry.get("published", "No date available")
                })
        return all_entries
