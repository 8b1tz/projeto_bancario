from abc import ABC

from Conta import Conta


class Pessoa(ABC):
    def __init__(self, nome: str, idade: int) -> None:
        self._nome = nome
        self._idade = idade

    @property
    def nome(self) -> str:
        return self._nome
    
    def set_nome(self, novo_nome: str):
        self._nome = novo_nome

    @property
    def idade(self) -> int:
        return self._idade

    def set_idade(self, nova_idade: int):
        self._idade = nova_idade


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int, conta: Conta) -> None:
        super().__init__(nome, idade)
        self._conta = conta
    
    @property
    def conta(self) -> Conta:
        return self._conta
    
    def __repr__(self) -> str:
        return f"NOME: {self.nome} IDADE: {self.idade} CONTA: {self.conta}"