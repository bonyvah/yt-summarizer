from fastapi import FastAPI, Request, Body
from ai import send
from yt import get_transcript
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse)
async def home(request:Request):
  return templates.TemplateResponse("index.html", {"request":request})

@app.post('/')
async def summarize(data:dict= Body(...)):
  url = data.get('url')
  prompt = "summarize this text: \n" + get_transcript(url) + "only return pure text, do not format in markdown"
  return await send(prompt)
