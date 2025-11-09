class Produto:

    def __init__(self, nome, preco, qe):

        self.nome = nome 
        self.preco = preco
        self.qe = qe 

    def exibir(self):

        print("-"*30)
        print("Dados do Produto:")
        print("Nome:", self.nome)
        print(f"Preço: R${self.preco:.2f}")
        print("Quantidade em estoque:",self.qe)
        print("-"*30)
    
    def atualizarqe(self):

        qe = int(input("Insira o novo valor em estoque: "))
        self.qe = qe

produto = Produto("Sabonete", 10.00, 50)
produto2 = Produto("Shampoo", 5.00, 20)

produto.exibir()
produto2.exibir()

produto.atualizarqe()
produto2.atualizarqe()

produto.exibir()
produto2.exibir()