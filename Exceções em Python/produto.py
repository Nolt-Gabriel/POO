class Produto:

    def __init__(self, nome, quantidade):

        self.nome = nome
        self.quantidade = quantidade 

    
    def criar_prod(self):

        nome = input("Qual o produto? ")
        quantidade = input("Quanto temos do produto? ")

        return nome, quantidade

    def remover(self, nome, quantidade, qtr):

        try:

            if qt < quantidade:

                print("Quantidade retirada com sucesso")

        except:

            print("A quatidade pedida excede a quantidade disponivel")




op = int(input("O que voce quer?\n1) Adicionar Produto\n2) Remover Produto\n "))
pr1 = Produto("", 0)
if op == 1:

    pr1.criar_prod()
    
elif op == 2:

    qtr = int(input("Quanto deseja remover? "))
    pr1.remover()



pr1 = Produto(nome, quantidade)
print("teste")