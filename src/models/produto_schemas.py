from __future__ import annotations
from typing import Optional
from pydantic import BaseModel, Field

class ProdutoBase(BaseModel):
    nome: str = Field(..., example="Caneta")
    preco: float = Field(..., gt=0, example=2.5)
    ativo: bool = Field(default=True, example=True)

class ProdutoCreate(ProdutoBase):
    """
    DTO para criação de um produto (POST).
    """
    pass

class ProdutoUpdate(ProdutoBase):
    nome: Optional[str] = Field(None, example="Caneta", min_length=3, max_length=100)
    preco: Optional[float] = Field(None, gt=0, example=2.5, lt=10000, gt=0)
    ativo: Optional[bool] = Field(None, example=True)

class ProdutoResponse(ProdutoBase):
    id: int = Field(..., example=1)

    class Config:
        #from_attribute = True
        orm_mode = True