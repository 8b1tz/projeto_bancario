from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, numero_da_conta, saldo):
        self._agencia = agencia
        self._numero_da_conta = numero_da_conta
        self._saldo = saldo
    
    def deposito(self, valor):
        self._saldo += valor

    @abstractmethod
    def sacar(self, valor, autenticacao):
        pass

class ContaCorrente(Conta):
    def __init__(self, agencia, numero_da_conta, saldo, limite) -> None:
        super().__init__(agencia, numero_da_conta, saldo)
        self._limite = limite

    def sacar(self, valor, autenticacao):
        if (valor > self._limite ):
            print("Você não tem limite")
        elif (valor > self._saldo):
            print("Você não tem saldo")
        if (valor <= self._limite ) and (self._saldo >= valor) and autenticacao:
            self._saldo -= valor
            self._limite -= valor
            print(f'Você conseguiu sacar {valor}')
        
    def __str__(self):
        return f'AGENCIA: {self._agencia} NUMERO: {self._numero_da_conta} SALDO: {self._saldo} LIMITE{self._limite}'

class ContaPoupanca(Conta):
    def __init__(self, agencia, numero_da_conta, saldo):
        super().__init__(agencia, numero_da_conta, saldo)

    def sacar(self, valor, autenticacao):
        if (self._saldo >= valor) and autenticacao:
            self._saldo -= valor

    def __str__(self):
        return f'AGENCIA: {self._agencia} NUMERO: {self._numero_da_conta} SALDO: {self._saldo}'
