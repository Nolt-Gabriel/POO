class Cliente:
    def __init__(self, nome, mesa):
        self.nome = nome
        self.mesa = mesa

    def __str__(self):
        return f"{self.nome} (Mesa {self.mesa})"


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f}"

class ItemPedido:
    def __init__(self, produto, quantidade):
        self.produto = produto        
        self.quantidade = quantidade

    @property
    def subtotal(self):
        return self.produto.preco * self.quantidade

class Pedido:
    def __init__(self, cliente, taxa_servico=0.1):
        self.cliente = cliente           
        self.itens = []                  
        self.taxa_servico = taxa_servico  

    def adicionar_item(self, produto, quantidade):
        self.itens.append(ItemPedido(produto, quantidade))

    def remover_item(self, produto):
        self.itens = [i for i in self.itens if i.produto != produto]

    def calcular_subtotal(self):
        return sum(item.subtotal for item in self.itens)

    def calcular_total(self):
        subtotal = self.calcular_subtotal()
        return subtotal * (1 + self.taxa_servico)

    def __str__(self):
        linhas = [f"Pedido de {self.cliente}"]
        for item in self.itens:
            linhas.append(
                f"- {item.produto.nome} x{item.quantidade} = R$ {item.subtotal:.2f}"
            )
        linhas.append(f"Subtotal: R$ {self.calcular_subtotal():.2f}")
        linhas.append(f"Total (c/ taxa): R$ {self.calcular_total():.2f}")
        return "\n".join(linhas)

class Restaurante:
    def __init__(self, nome):
        self.nome = nome
        self.cardapio = []      
        self.pedidos = []       

    def adicionar_produto_cardapio(self, produto):
        self.cardapio.append(produto)

    def registrar_pedido(self, pedido):
        self.pedidos.append(pedido)

    def gerar_relatorio_dia(self):
        print(f"=== Relatório do {self.nome} ===")
        faturamento = 0
        for pedido in self.pedidos:
            print(pedido)
            print("-" * 30)
            faturamento += pedido.calcular_total()
        print(f"Faturamento total do dia: R$ {faturamento:.2f}")



rest = Restaurante("Restô Tech")


p1 = Produto("Hambúrguer", 25.0)
p2 = Produto("Refrigerante", 7.0)
p3 = Produto("Batata Frita", 12.0)

rest.adicionar_produto_cardapio(p1)
rest.adicionar_produto_cardapio(p2)
rest.adicionar_produto_cardapio(p3)


cli1 = Cliente("Ana", 5)
pedido1 = Pedido(cli1, taxa_servico=0.1)   

pedido1.adicionar_item(p1, 2)  
pedido1.adicionar_item(p2, 2)  

rest.registrar_pedido(pedido1)


cli2 = Cliente("João", 3)
pedido2 = Pedido(cli2, taxa_servico=0.1)
pedido2.adicionar_item(p1, 1)
pedido2.adicionar_item(p3, 1)

rest.registrar_pedido(pedido2)


rest.gerar_relatorio_dia()
