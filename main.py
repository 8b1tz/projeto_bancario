from Banco import Banco
from Conta import ContaCorrente, ContaPoupanca
from Pessoa import Cliente

if __name__ == "__main__":
    banco = Banco()
    cliente_ju = Cliente('Julia', 17, ContaCorrente(12, 4444, 200, 100))
    cliente_ca = Cliente('Caio', 22, ContaPoupanca(35, 2311, 300))
    banco.adicionar_cliente(cliente_ju)
    banco.adicionar_conta(cliente_ju.conta)
    cliente_ju.conta.sacar(50, banco.autenticacao(cliente_ju))
    cliente_ju.conta.deposito(40)
    cliente_ju.conta.sacar(50, banco.autenticacao(cliente_ju))
    cliente_ju.conta.sacar(20, banco.autenticacao(cliente_ju))
    cliente_ju.conta.sacar(10, banco.autenticacao(cliente_ju))
    cliente_ju.conta.sacar(20, banco.autenticacao(cliente_ju))
    cliente_ju.conta.deposito(1)
    print(cliente_ju)