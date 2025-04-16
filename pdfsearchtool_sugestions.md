Quer usar isso no CrewAI?

A gente precisa criar um embedder personalizado e passar ele para o PDFSearchTool. Exemplo:

✅ 1. Criaremos um embedder Gemini customizado para o PDFSearchTool:
# src/tools/gemini_embedder.py

from embedchain.interface.embedder import BaseEmbedder
import google.generativeai as genai

class GeminiEmbedder(BaseEmbedder):
    def __init__(self, model="embedding-001"):
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        self.model = genai.GenerativeModel(model)

    def embed(self, text: str):
        res = self.model.embed_content(content=text, task_type="retrieval_document")
        return res["embedding"]

    def embed_documents(self, texts):
        return [self.embed(t) for t in texts]

    def embed_query(self, text):
        return self.embed(text)
✅ 2. Usar isso com o PDFSearchTool
from embedchain.config import AppConfig
from src.tools.gemini_embedder import GeminiEmbedder
from crewai_tools import PDFSearchTool

config = AppConfig()
config.embedder = GeminiEmbedder()

pdf_tool = PDFSearchTool(
    pdf_url="https://arxiv.org/pdf/1706.03762.pdf",
    config=config
)
🧠 Recapitulando


Coisa	Pode usar com Gemini?	Observações
LLM (modelo de geração)	✅ Sim	Via langchain_google_genai
Embedder (busca semântica)	✅ Sim	Mas precisa implementação manual como acima
PDFSearchTool com Gemini Embedder	✅ Sim	Desde que integre com embedchain
🎁 Quer que eu gere esse projeto pra você já com o GeminiEmbedder funcionando? Posso mandar .zip pronto com tudo 😎


