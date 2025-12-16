from __future__ import annotations
from typing import List
from fastapi import FastAPI, HTTPException, status

from src.models.produto_schemas import ProdutoCreate, ProdutoResponse, ProdutoUpdate
from src.services.produto_repo_memory import ProdutoRepositoryMemory
from src.services.produto_service import ProdutoService

app = (
    FastAPI(
        title="API de Produtos",
        version="1.0.0",
        description="API para gerenciamento de produtos.",))

repo = ProdutoRepositoryMemory()
produto_service = ProdutoService(repo)

@app.get("/", tags=["healthcheck"])
def read_root():
    return {"message": "API de Produtos está funcionando!"}

@app.get("/produtos/{produto_id}", response_model=ProdutoResponse, tags=["produtos"])
def obter_produto(produto_id: int):
    produto = produto_service.obter_produto(produto_id)

    if not produto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado.")
    return ProdutoResponse(id=produto.id, nome=produto.nome, preco=produto.preco, ativo=produto.ativo)

@app.get("/produtos/", response_model=List[ProdutoResponse], tags=["produtos"])
def listar_produtos():
    produtos = produto_service.listar_produtos()
    return [ProdutoResponse(id=p.id, nome=p.nome, preco=p.preco, ativo=p.ativo)
            for p in produtos]

@app.post("/produtos/", response_model=ProdutoResponse, status_code=status.HTTP_201_CREATED, tags=["produtos"])
def criar_produto(produto: ProdutoCreate):
    novo_produto = produto_service.criar_produto(produto.nome, produto.preco, produto.ativo)
    return ProdutoResponse(id=novo_produto.id, nome=novo_produto.nome, preco=novo_produto.preco, ativo=novo_produto.ativo)

@app.put("/produtos/{produto_id}", response_model=ProdutoResponse, tags=["produtos"])
def atualizar_produto(produto_id: int, produto: ProdutoUpdate):
    produto_existente = produto_service.obter_produto(produto_id)

    if not produto_existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado.")

    nome:str = produto.nome if produto.nome is not None else produto_existente.nome
    preco:float = produto.preco if produto.preco is not None else produto_existente.preco
    ativo:bool = produto.ativo if produto.ativo is not None else produto_existente.ativo

    produto_atualizado = produto_service.atualizar_produto(
        id_=produto_id,
        nome=nome,
        preco=preco,
        ativo=ativo
    )

    return ProdutoResponse(id=produto_atualizado.id, nome=produto_atualizado.nome, preco=produto_atualizado.preco, ativo=produto_atualizado.ativo)

@app.delete("/produtos/{produto_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["produtos"])
def deletar_produto(produto_id: int):
    produto_existente = produto_service.obter_produto(produto_id)

    if not produto_existente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado.")

    produto_service.deletar_produto(produto_id)