import os
from datetime import datetime
from dotenv import load_dotenv
from src.crew import NewsCrew

def main():
    load_dotenv()
    
    # Configure Ollama (Make sure Ollama is running)
    model = os.getenv("OLLAMA_MODEL", "llama3")

    # Define as categorias de notícias e seus feeds RSS
    news_categories = {
        "1": {"name": "Mundo", "urls": ["https://feeds.bbci.co.uk/news/world/rss.xml", "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"]},
        "2": {"name": "Tecnologia", "urls": ["https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml", "https://feeds.bbci.co.uk/news/technology/rss.xml"]},
        "3": {"name": "Finanças", "urls": ["https://rss.nytimes.com/services/xml/rss/nyt/Business.xml", "https://feeds.bbci.co.uk/news/business/rss.xml"]},
        "4": {"name": "Geral (Todos)", "urls": [
            "https://feeds.bbci.co.uk/news/world/rss.xml",
            "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
            "https://rss.nytimes.com/services/xml/rss/nyt/Business.xml"
        ]}
    }

    print("\n=== Selecione o tipo de notícias desejado ===")
    for key, data in news_categories.items():
        print(f"[{key}] {data['name']}")
    
    choice = input("\nDigite o número da opção (Padrão: 4): ").strip()
    
    # Se a escolha for inválida, assume 4
    selected_category = news_categories.get(choice, news_categories["4"])
    rss_urls = selected_category["urls"]
    category_name = selected_category["name"]

    print(f"\n--- Iniciando News Agent (Ollama) - Categoria: {category_name} ---")
    crew = NewsCrew(rss_urls, model_name=model)
    result = crew.run()
    
    print("\n\n--- Final Newsletter ---")
    print(result)

    # Save to Markdown
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    markdown_content = f"# Newsletter ({category_name}) - Executada em {current_date}\n\n{str(result)}"
    
    with open("newsletter.md", "w", encoding="utf-8") as f:
        f.write(markdown_content)
    
    print("\n--- Newsletter saved to newsletter.md ---")

if __name__ == "__main__":
    main()
