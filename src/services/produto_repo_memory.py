from __future__ import annotations
from typing import List, Dict, Optional

from src.models.produto import Produto
from src.services.produto_repo_base import ProdutoRepositoryBase

class ProdutoRepositoryMemory(ProdutoRepositoryBase):
    """
    Implementação em memória do repositório de produtos.
    """
    def __init__(self) -> None:
        self._produtos: Dict[int, Produto] = {}
        self._next_id: int = 1

    def criar(self, nome: str, preco: float, ativo: bool = True) -> Produto:
        produto = Produto(id_=self._next_id, nome=nome, preco=preco, ativo=ativo)
        self._produtos[self._next_id] = produto
        self._next_id += 1
        return produto

    def obter_por_id(self, id_: int) -> Optional[Produto]:
        return self._produtos.get(id_)

    def listar(self) -> List[Produto]:
        return list(self._produtos.values())

    def atualizar(self, id_: int, nome: str, preco: float, ativo: bool) -> Produto:
        produto = self._produtos.get(id_)
        if not produto:
            raise ValueError("Produto não encontrado.")
        produto = Produto(id_=id_, nome=produto.nome, preco=produto.preco, ativo=produto.ativo)
        self._produtos[id_] = produto
        return produto

    def deletar(self, id_: int) -> bool:
        if id_ in self._produtos:
            del self._produtos[id_]
        return False