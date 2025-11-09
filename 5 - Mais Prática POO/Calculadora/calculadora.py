class Calculadora:

    def __init__(self):

        pass

    def somar(self,n1,n2):

        return n1 + n2

    def subtrair(self,n1,n2):

        return n1 - n2
    
    def dividir(self,n1,n2):

        return n1 / n2

    def multi(self,n1,n2):

        return n1 * n2

    def menu(self):

        while (True):

            print("1) Somar")
            print("2) Subtrair")
            print("3) Multiplicar")
            print("4) Dividir")
            print("5) Sair")

            op = int(input("\n\nEscolha uma opção: "))


            if op == 1:

                n1 = int(input("Digite o Primero número: "))
                n2 = int(input("Digite o Segundo número: "))
                print(self.somar(n1, n2))
            
            elif op == 2:

                n1 = int(input("Digite o Primero número: "))
                n2 = int(input("Digite o Segundo número: "))
                print(self.subtrair(n1, n2))

            elif op ==3:

                n1 = int(input("Digite o Primero número: "))
                n2 = int(input("Digite o Segundo número: "))
                print(self.multi(n1, n2))

            elif op == 4:

                n1 = int(input("Digite o Primero número: "))
                n2 = int(input("Digite o Segundo número: "))
                print(self.dividir(n1, n2))
            
            elif op == 5:

                print("Saindo....")
                break
    



