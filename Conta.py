from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia: int, numero_da_conta: int, saldo: float = 0):
        self._agencia = agencia
        self._numero_da_conta = numero_da_conta
        self._saldo = saldo
    
    def deposito(self, valor: float) -> None:
        self._saldo += valor

    @abstractmethod
    def sacar(self, valor: float, autenticacao: bool) -> None:
        pass


class ContaCorrente(Conta):
    def __init__(
            self, agencia: int, numero_da_conta: int, saldo: float, 
            limit: float):
        super().__init__(agencia, numero_da_conta, saldo)
        self._limit = limit

    def sacar(self, valor: float, autenticacao: bool) -> None:
        if (valor > self._limit):
            print(f"Você não tem limite. Seu limite é {self._limit} e você\
 está tentando sacar {valor}")
        elif (valor > self._saldo):
            print(f"Você não tem saldo. Seu saldo é {self._saldo} e você está\
 tentando sacar {valor}")
        if (valor <= self._limit) and (self._saldo >= valor) and autenticacao:
            self._saldo -= valor
            self._limit -= valor
            print(f'Você conseguiu sacar {valor}. Seu saldo agora é\
 {self._saldo} e seu limite é {self._limit}')
        
    def __str__(self) -> str:
        return f'AGENCIA: {self._agencia} NUMERO: {self._numero_da_conta}\
 SALDO: {self._saldo} LIMITE: {self._limit}'


class ContaPoupanca(Conta):
    def __init__(self, agencia: int, numero_da_conta: int, saldo: float):
        super().__init__(agencia, numero_da_conta, saldo)

    def sacar(self, valor: float, autenticacao: bool):
        if (self._saldo >= valor) and autenticacao:
            self._saldo -= valor

    def __str__(self) -> str:
        return f'AGENCIA: {self._agencia} NUMERO: {self._numero_da_conta}\
 SALDO: {self._saldo}'
