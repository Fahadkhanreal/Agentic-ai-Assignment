import os 
from dotenv import load_dotenv
from agents import OpenAIChatCompletionsModel , AsyncOpenAI  , set_tracing_disabled

# --------------------------------------------------------

load_dotenv()
set_tracing_disabled(disabled=True)
api_key = os.getenv("GEMINI_API_KEY")


client = AsyncOpenAI(api_key=api_key, base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

Model = OpenAIChatCompletionsModel(model="gemini-2.5-flash" , openai_client=client)
