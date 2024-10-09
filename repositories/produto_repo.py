
from typing import List, Optional
from models.produto_model import Produto
from sql.produto_sql import SQL_CRIAR_TABELA, SQL_INSERIR, SQL_OBTER_TODOS
from util import obter_conexao





def criar_tabela():
    with obter_conexao() as conexao:
        db = conexao.cursor()
        db.execute(SQL_CRIAR_TABELA)


def inserir(produto: Produto) -> Optional[Produto]:
    with obter_conexao() as conexao:
        db = conexao.cursor()
        db.execute(SQL_INSERIR,
           (produto.nome,
            produto.descricao,
            produto.estoque,
            produto.preco,
            produto.categoria))
        if db.rowcount > 0:
            Produto.id = db.lastrowid
            return Produto
        else:
            return None

def obter_todos() -> List[Produto]:
    with obter_conexao() as conexao:
        db = conexao.cursor()
        tuplas = db.execute(SQL_OBTER_TODOS).fetchall() 
        produtos = [Produto(*t) for t in tuplas]
        return produtos
        


