from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class Usuario:
    id: Optional[int] = None
    nome: Optional[str] = None
    descricao: Optional[str] = None
    estoque: Optional[int] = None
    preco: Optional[int] = None
    categoria: Optional[str] = None