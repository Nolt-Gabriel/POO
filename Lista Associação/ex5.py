class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class Carrinho:
    def __init__(self):
        self.produtos = []   # agregação: recebe objetos Produto externos

    def adicionar(self, produto):
        self.produtos.append(produto)

    def remover(self, produto):
        if produto in self.produtos:
            self.produtos.remove(produto)

    def calcular_total(self):
        total = 0
        for p in self.produtos:
            total += p.preco
        return total

p1 = Produto("Mouse", 80.0)
p2 = Produto("Teclado", 120.0)

carrinho = Carrinho()
carrinho.adicionar(p1)
carrinho.adicionar(p2)

print("Total:", carrinho.calcular_total())
