from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from starlette.requests import Request

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def paginaInicial(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__== "_main_":
    import uvicorn
    uvicorn.run("main:app", port=8000, reload=True)