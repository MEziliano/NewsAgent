import os
from dotenv import load_dotenv
from src.crew import NewsCrew
from src.utils.html_generator import get_html_template
import markdown

def main():
    load_dotenv()
    
    # Configure Ollama (Make sure Ollama is running)
    model = os.getenv("OLLAMA_MODEL", "llama3")

    # Sample RSS feeds (Tech/World News)
    rss_urls = [
        "https://feeds.bbci.co.uk/news/world/rss.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml"
    ]

    print("--- Starting News Agent (Ollama) ---")
    crew = NewsCrew(rss_urls, model_name=model)
    result = crew.run()
    
    print("\n\n--- Final Newsletter ---")
    print(result)

    # Save to HTML
    html_content = markdown.markdown(str(result))
    premium_html = get_html_template(html_content)
    
    with open("newsletter.html", "w", encoding="utf-8") as f:
        f.write(premium_html)
    
    print("\n--- Newsletter saved to newsletter.html (Open it to see the rich design!) ---")

if __name__ == "__main__":
    main()
