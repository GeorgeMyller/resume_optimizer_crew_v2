from crewai_tools import tool, ScrapeWebsiteTool

@tool("WebScraperTool")
def WebScraperTool(website_url: str) -> str:
    """
    Lê a descrição da vaga diretamente de uma URL.
    """
    try:
        scraper = ScrapeWebsiteTool(website_url=website_url)
        job_description = scraper.run()
        return job_description
    except Exception as e:
        return f"Erro ao acessar a URL: {str(e)}"
