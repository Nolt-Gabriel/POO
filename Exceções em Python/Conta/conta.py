class SaldoInsuficienteError (Exception):

    pass

class Conta:

    def __init__(self, nome, saldo):

        self.nome = nome
        self.saldo = saldo


    def sacar(self, saque):

        if self.saldo < saque:

            raise SaldoInsuficienteError(f"Saldo insuficiente: saldo atual = {self.saldo} , tentativa de saque = {saque}")

        self.saldo -= saque

        print(f"O saque de {saque} , foi um sucesso!")


cliente = Conta("Gabriel", 500)
print(cliente.saldo)
cliente.sacar(600)
print(cliente.saldo)