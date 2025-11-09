class Agenda:

    def __init__(self,nome, telefone, email):

        self.nome = nome
        self.telefone = telefone
        self.email = email

    def exibir(self):

        print("Informações de contato:")
        print("Nome:", self.nome)
        print("Telefone:", self.telefone)
        print("Email:", self.email)

    def alterar(self):
        while (True):

            print("\n1) Telefone\n2) Email\n")
            op = int(input("\n\nO que deseja alterar? "))
            

            try:
                if op == 1:

                    tel = int(input("Digite o novo telefone: "))
                    self.telefone = tel
                    break
                elif op == 2:

                    email = input("Digite o Novo email: ")
                    self.email = email
                    break
            except:

                print("\nDados Invalidos")

    def menu(self):
        while (True):

            print("\n\n1) Exibir Informações do contato")
            print("2) Alterar Informações (Telefone, Email)")
            print("3) Sair")

            op = int(input("\n\nO que deseja fazer? "))
            

            try:

                if op == 1:

                    self.exibir()
                
                if op == 2:

                    self.alterar()

                if op == 3:

                    print("\nSaindo...")
                    break
            except:

                print("\nvalor invalido")
        
        

agenda = Agenda("João", 40028922, "joaozingameplays@gmail.com")

agenda.menu()