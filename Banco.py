     
from Pessoa import Cliente

class Banco:
    def __init__(self) -> None:
        self._contas = []
        self._clientes = []

    def adicionar_conta(self, conta):
        self._contas.append(conta)
    
    def remover_conta(self, conta):
        self._contas.remove(conta)
    
    def adicionar_cliente(self, cliente):
        self._clientes.append(cliente)
    
    def remover_cliente(self, cliente):
        self._clientes.remove(cliente)

    def autenticacao(self, cliente : Cliente):
        if (cliente in self._clientes) and (cliente.conta in self._contas):
            return True
        return False