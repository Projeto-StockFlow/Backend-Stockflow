# Arquivo de modelar as tabelas do banco de dados
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class VendedorEntrada(BaseModel):
    nome: str
    nome_loja: str
    email: str
    senha:str
    telefone: str

class Vendedor(VendedorEntrada):
    id_vendedor: int

class ProdutoEntrada(BaseModel):
    nome: str
    categoria: str
    quantidade: int
    descricao: str
    estoque_minimo: int
    id_vendedor: int

class Produto(ProdutoEntrada):
    id_produto: int



class MovimentacaoEntrada(BaseModel):
    tipo: str
    quantidade: int
    data_hora: datetime
    observacao: str
    id_produto: int


class Movimentacao(MovimentacaoEntrada):
    id_movimentacao: int