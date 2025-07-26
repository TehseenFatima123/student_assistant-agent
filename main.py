from dotenv import load_dotenv
import os
from agents import OpenAIChatCompletionsModel
from agents import RunConfig

from agents import Agent, Runner, AsyncOpenAI

load_dotenv()
gemini_api_key= os.getenv("GEMINI_API_KEY")

# Check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=gemini_api_key,
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)
agents = Agent(
    name = "Student Assisstant",
    instructions = "You are a student assisstant. You help students in all the subjects"
)
#print = (f"HI,How can i help you?")
response = Runner.run_sync(
    agents,
    input = (f"Who invented the computer?"),
    run_config = config
)
print (response)