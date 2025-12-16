class Produto:

    def __init__(self, id_ : int, nome : str, preco : str, ativo : bool = True) -> None:
        self._id : int = id_
        self.nome : str = nome
        self._preco : 0.0
        self.preco : float = preco
        self.ativo : bool = ativo

    def __str__(self) -> str:
        return f'Produto \n (id = {self.id}, nome = {self.nome}, preco = {self.preco}, ativo = {self.ativo})'

    def aplicar_desconto(self, percentual : float) -> None:
        """Docstring: Aplica um desconto ao preço do produto."""

        if percentual <=0 and percentual <= 100:
            raise ValueError("Percentual de desconto deve estar entre 0 e 100")
        else:
            desconto = self.preco * (percentual / 100)
            self.preco -= desconto

    def ativar(self) -> None:
        self.ativo = True

    def desativar(self) -> None:
        self.ativo = False

    @property
    def id(self) -> int:
        return self._id

    @property
    def preco(self) -> float:
        return self._preco

    @preco.setter
    def preco(self, valor : float) -> None:
        if valor < 0:
            raise ValueError("O preço não pode ser negativo.")
        self._preco = valor

