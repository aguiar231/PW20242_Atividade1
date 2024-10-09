from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from util import ler_html, salvar_contato, salvar_cadastro
from models.produto_model import Produto
from repositories import produto_repo
import uvicorn

produto_repo.criar_tabela()
app = FastAPI()


templates = Jinja2Templates(directory='templates')

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def get_root(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})

@app.get("/cadastro")
def get_cadastro(request: Request):
    return templates.TemplateResponse('cadastro.html', {"request": request})

@app.post("/post_cadastro")
def post_cadastro(
    request: Request,
    nome: str = Form(...),
    descricao: str = Form(...),
    estoque: str = Form(...),
    preco: str = Form(...),
    categoria: str = Form(...)): 
    produto = Produto(None, nome, descricao, estoque, preco, categoria)
    produto = produto_repo.inserir(produto)
    if produto:
            return RedirectResponse("/cadastro_recebido", 303)
    else: 
            return RedirectResponse("/cadastro", 303)

@app.get("/cadastro_recebido")
def get_cadastro_recebido(request: Request):
    if get_cadastro_recebido:
        return templates.TemplateResponse('cadastro_recebido.html', {"request": request})
    else:
        return templates.TemplateResponse('cadastro.html', {"request": request})
         
@app.get("/cadastro")
def get_cadastro(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

if __name__ == "__main__":
 uvicorn.run("main:app", port=8000, reload=True)