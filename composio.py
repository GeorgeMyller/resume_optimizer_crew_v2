from google import genai
from composio_gemini import ComposioToolSet
from dotenv import load_dotenv 

load_dotenv()


# Inicialize os clientes
gemini_client = genai.Client(api_key=get.os"sua-chave-de-api-do-gemini")
composio_toolset = ComposioToolSet(api_key="sua-chave-de-api-do-composio")

tools = composio_toolset.get_tools()

# Configure e liste as ferramentas disponíveis
apps = ["App.GITHUB", "App.CUSTOM"]  # Substitua pelos aplicativos relevantes
config = genai.types.GenerateContentConfig(tools=tools)

# Exemplo de uso de uma ferramenta
for tool in tools:
    print(f"Ferramenta disponível: {tool}")

# Execute uma ação com o cliente Gemini
chat = gemini_client.chats.create(model="gemini-2.0-flash", config=config)
response = chat.send_message("Exemplo de mensagem para o modelo Gemini")
print(response.text)

# Crie uma instância de chat com o modelo Gemini
chat = gemini_client.chats.create(model="gemini-2.0-flash", config=config)

# Envie uma mensagem ou comando para o modelo
response = chat.send_message("Por favor, otimize este currículo para uma vaga de desenvolvedor Python.")

# Exiba a resposta do modelo
print("Resposta do modelo:", response.text)
