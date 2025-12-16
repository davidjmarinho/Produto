from __future__ import annotations
from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ProdutoDB(Base):
    """
    Docstring for ProdutoDB
    Modelo ORM para a tabela de produtos no banco de dados.
    """
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False)
    ativo = Column(Boolean, default=True)

    def __repr__(self) -> str:
        return f"<ProdutoDB(id={self.id}, nome='{self.nome}', preco={self.preco}, ativo={self.ativo})>"