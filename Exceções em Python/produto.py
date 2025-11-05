class Produto:

    def __init__(self, produto, quantidade):

        self.produto = produto
        self.quantidade = quantidade 

    
    def remover(self, produto, quantidade):

        try:

            qt = int(input("Digite a quantidade que você deseja retirar do produto: "))

        except Exception as error:

            print(error.__class__)


pr1 = Produto("Teclado", 10)

try:

    Produto.remover(pr1, 10)

except Exception as error:


    print("O erro foi:", error)