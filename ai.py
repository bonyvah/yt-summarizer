from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def send(prompt):
  response = client.responses.create(
    model="gpt-4.1-nano-2025-04-14",
    input=prompt,
    temperature=0.2,
    max_output_tokens=300
  )
  return response.output_text