from fastapi import FastAPI
from ai import send

app = FastAPI()

@app.get('/')
async def home():
  return await send("hi")

