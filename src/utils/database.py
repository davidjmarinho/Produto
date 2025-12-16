from __future__ import annotations
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from src.models.produto_db import Base

SQLALCHEMYDATABASE_URL = "sqlite:///./data/produtos.db"

engine = create_engine(
    SQLALCHEMYDATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False, bind=engine)

def criar_tabelas() -> None:
    """
    Cria as tabelas no banco de dados.
    """
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
