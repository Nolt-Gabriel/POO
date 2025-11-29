class MetodoPagamento:
    def pagar(self, valor):
        raise NotImplementedError("Implemente em uma subclasse")


class CartaoCredito(MetodoPagamento):
    def pagar(self, valor):
        print(f"Pagando R${valor:.2f} com cartão de crédito.")


class Boleto(MetodoPagamento):
    def pagar(self, valor):
        print(f"Gerando boleto no valor de R${valor:.2f}.")


class Pix(MetodoPagamento):
    def pagar(self, valor):
        print(f"Realizando pagamento PIX de R${valor:.2f}.")


def processar_pagamento(metodo: MetodoPagamento, valor: float):
    metodo.pagar(valor)  


m1 = CartaoCredito()
m2 = Boleto()
m3 = Pix()

processar_pagamento(m1, 100.0)
processar_pagamento(m2, 250.5)
processar_pagamento(m3, 50.0)
