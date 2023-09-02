     
from Conta import Conta
from Pessoa import Cliente


class Banco:
    def __init__(self) -> None:
        self._contas: list = []
        self._clientes: list = []

    def adicionar_conta(self, conta: Conta):
        self._contas.append(conta)
    
    def remover_conta(self, conta: Conta):
        self._contas.remove(conta)
    
    def adicionar_cliente(self, cliente: Cliente):
        self._clientes.append(cliente)
    
    def remover_cliente(self, cliente: Cliente):
        self._clientes.remove(cliente)

    def autenticacao(self, cliente: Cliente) -> bool:
        if (cliente in self._clientes) and (cliente.conta in self._contas):
            return True
        return False