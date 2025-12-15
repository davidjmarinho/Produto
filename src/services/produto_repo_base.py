from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Optional

from src.models.produto import Produto

class ProdutoRepositoryBase(ABC):

    """
    Classe base abstrata para o repositório de produtos.
    """
    @abstractmethod
    def criar(self, nome:str, preco:float, ativo:bool) -> Produto:
        raise NotImplementedError

    @abstractmethod
    def obter_por_id(self, id_: int) -> Optional[Produto]:
        raise NotImplementedError

    @abstractmethod
    def listar(self) -> List[Produto]:
        raise NotImplementedError

    @abstractmethod
    def atualizar(self, id_:int, nome:str, preco:float, ativo:bool) -> Produto:
        raise NotImplementedError

    @abstractmethod
    def deletar(self, id_: int) -> None:
        raise NotImplementedError