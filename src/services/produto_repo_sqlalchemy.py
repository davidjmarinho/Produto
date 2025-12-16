from __future__ import annotations
from typing import List, Optional

from sqlalchemy.orm import Session

from src.models.produto import Produto
from src.models.produto_db import ProdutoDB
from src.services.produto_repo_base import ProdutoRepositoryBase

class ProdutoRepositorySQLAlchemy(ProdutoRepositoryBase):
    """
    Docstring for ProdutoRepositorySQLAlchemy
    Implementação do repositório de produtos usando SQLAlchemy e SQLite.
    """
    def __init__(self, db_session: Session) -> None:
        self._db_session = db_session

    def _db_to_entity(self, produto_db: ProdutoDB) -> Produto:
        """Converte uma instância do modelo ORM ProdutoDB para Produto entidade."""
        return Produto(
            id_=produto_db.id,
            nome=produto_db.nome,
            preco=produto_db.preco,
            ativo=produto_db.ativo
        )

    def listar(self) -> List[Produto]:
        produtos_db = self._db_session.query(ProdutoDB).all()
        #select * from produtos
        return [self._db_to_entity(p) for p in produtos_db]

    def buscar_por_id(self, id_:int) -> Optional[Produto]:
        produtos_db = self._db_session.query(ProdutoDB).filter(ProdutoDB.id == id_).first()
        #select * from produtos where id = {id_}
        if not produtos_db:
            return None
        return self._db_to_entity(produtos_db)

    def criar(self, nome:str, preco:float, ativo:bool=True) -> Produto:
        novo_produto_db = ProdutoDB(nome=nome, preco=preco, ativo=ativo)
        self._db_session.add(novo_produto_db)
        #INSERT INTO produtos (nome, preco, ativo) VALUES ("Caneta", 2.5, True)
        self._db_session.commit()
        self._db_session.refresh(novo_produto_db)
        return self._db_to_entity(novo_produto_db)

    def atualizar(self, id_:int, nome:str, preco:float, ativo:bool) -> Produto:
        produto_db = self._db_session.query(ProdutoDB).filter(ProdutoDB.id == id_).first()
        #select * from produtos where id = {id_}
        if not produto_db:
            raise ValueError("Produto não encontrado.")

        produto_db.nome = nome
        produto_db.preco = preco
        produto_db.ativo = ativo
        #UPDATE produtos SET nome = ..., preco = ..., ativo = ... WHERE id = {id_}
        self._db_session.commit()
        self._db_session.refresh(produto_db)
        return self._db_to_entity(produto_db)

    def remover(self, id_:int) -> bool:
        produto_db = self._db_session.query(ProdutoDB).filter(ProdutoDB.id == id_).first()
        #select * from produtos where id = {id_}
        if not produto_db:
            return False

        self._db_session.delete(produto_db)
        #DELETE FROM produtos WHERE id = {id_}
        self._db_session.commit()
        return True