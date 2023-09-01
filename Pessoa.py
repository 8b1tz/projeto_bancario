from abc import ABC

class Pessoa(ABC):
    def __init__(self, nome, idade) -> None:
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome
    
    def set_nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def idade(self):
        return self._idade

    def set_idade(self, nova_idade):
        self._idade = nova_idade


class Cliente(Pessoa):
    def __init__(self, nome, idade, conta) -> None:
        super().__init__(nome, idade)
        self._conta = conta
    
    @property
    def conta(self):
        return self._conta
    
    def __repr__(self):
        return f"NOME {self.nome.upper()} IDADE {self.idade} CONTA --> {self.conta}"