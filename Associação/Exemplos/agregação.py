class CarrinhoDeCompras:

    def __init__(self):

        self.produtos = []

    def inserir_produto(self, produto):

        self.produtos.append(produto)
    
    def mostrar_lista(self):

        for produto in self.produtos:

            print(produto.nome, produto.valor)
    
class Produto:

    def __init__(self, nome, valor):

        self.nome = nome
        self.valor = valor


compras = CarrinhoDeCompras()
p1 = Produto("Sabonete Ivone", 35)
p2 = Produto("Shampoo Ivone", 50)

compras.inserir_produto(p1)
compras.inserir_produto(p2)
compras.inserir_produto(p2)
print(compras.mostrar_lista())