from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette.requests import Request
from util import ler_html, salvar_cadastro, salvar_contato

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def paginaInicial(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/cadastro")
def get_cadastro(request: Request):
    html = ler_html("cadastro")
    return HTMLResponse(html)

@app.post("/post_cadastro")
def post_cadastro(
    request: Request, 
    nome: str = Form(...), 
    data_nascimento: str = Form(...), 
    email: str = Form(...), 
    senha: str = Form(...), 
    confirmacao_senha: str = Form(...)):
    if senha == confirmacao_senha:
        salvar_cadastro(nome, data_nascimento, email, senha)
        return RedirectResponse("/cadastro_recebido", 303)
    else:
        return RedirectResponse("/cadastro", 303)

if __name__== "_main_":
    import uvicorn
    uvicorn.run("main:app", port=8000, reload=True)