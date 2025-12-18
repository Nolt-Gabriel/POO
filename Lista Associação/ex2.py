class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.interesses = []      # associação: Cliente -> Produto

    def adicionar_interesse(self, produto):
        self.interesses.append(produto)

    def mostrar_lista(self):
        for produto in self.interesses:
            print(f"- {produto.nome} (R$ {produto.preco})")


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


cliente1 = Cliente("Ana", "ana@email.com")
produto1 = Produto("Mouse Gamer", 150.0)

cliente1.adicionar_interesse(produto1)
cliente1.mostrar_lista()
