from __future__ import annotations
from typing import List, Optional

from src.models.produto import Produto
from src.services.produto_repo_base import ProdutoRepositoryBase

class ProdutoService:
    """
    Domínio das operações de produto.
    """
    def __init__(self, repo: ProdutoRepositoryBase) -> None:
        self._repo = repo

    def criar_produto(self, nome: str, preco: float, ativo: bool = True) -> Produto:
        return self._repo.criar(nome, preco, ativo)

    def obter_produto(self, id_: int) -> Optional[Produto]:
        return self._repo.obter_por_id(id_)

    def listar_produtos(self) -> List[Produto]:
        return self._repo.listar()

    def atualizar_produto(self, id_: int, nome: str, preco: float, ativo: bool) -> Produto:
        return self._repo.atualizar(id_, nome, preco, ativo)

    def deletar_produto(self, id_: int) -> bool:
        self._repo.deletar(id_)