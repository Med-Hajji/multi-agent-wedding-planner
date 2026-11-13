from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

load_dotenv()

gemini_model = init_chat_model(
    "gemini-3.8-flash",
    model_provider="google_genai",
    api_key=os.getenv("GEMINI_API_KEY")
)