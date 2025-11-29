class Operacao:
    def calcular(self, a, b):
        
        raise NotImplementedError("Implemente em uma subclasse")


class Soma(Operacao):
    def calcular(self, a, b):
        return a + b


class Subtracao(Operacao):
    def calcular(self, a, b):
        return a - b


class Multiplicacao(Operacao):
    def calcular(self, a, b):
        return a * b


class Divisao(Operacao):
    def calcular(self, a, b):
        return a / b   


operacoes = [
    Soma(),
    Subtracao(),
    Multiplicacao(),
    Divisao()
]

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

for op in operacoes:
    resultado = op.calcular(a, b)
    print(f"{op.__class__.__name__}: {resultado}")

