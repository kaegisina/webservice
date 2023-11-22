import uvicorn
from fastapi import FastAPI
from fastapi import responses
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"))


@app.get("/text/{text2}")
async def test(text2):
    return {"resultat": text2}

@app.get("/addiere")
async def addiere(a: int = 0, b: int = 0):
    return {"resultat": a+b}

@app.get("/")
async def root():
    return {"Version": "1.0"}

@app.get("/hallo")
async def root():
    return {"Hello": "World"}

@app.get("/bild")
async def bild():
    return responses.FileResponse("static/Katze.jpeg")

@app.get("/web")
async def web():
    return responses.HTMLResponse("<h1>Titel</h1><img src='static/Katze.jpeg' width='30%' />")



uvicorn.run(app, host="127.0.0.1", port=8000)