class Votacao:
    def __init__(self, nome_v):
        self.nome_v = nome_v
        self.votos = {"João": 0, "Maria": 0, "Juliana": 0}
        self.status = False

    def stats(self):
        print("-"*30)
        print(" "*15, "Status da votação:", self.status)
        print("-"*30)
        if not self.status:
            op = input("Deseja Ativar a votação? y/n\n")
            if op == "y":
                self.status = True
            else:
                print("Votação continuará desativada.")
        else:
            op = input("Deseja desativar a votação? y/n\n")
            if op == "y":
                self.status = False
            else:
                print("Votação continuará ativada.")

    def votar(self):
        if not self.status:
            print("Votação Encerrada")
            return

        print("-"*30)
        print(" "*15,"Votação")
        print("-"*30)
        print("1) João")
        print("2) Maria")
        print("3) Juliana")
        print("-"*30, "\n\n")

        try:
            voto = int(input("Para quem vai seu voto? "))
            if voto == 1:
                self.votos["João"] += 1
            elif voto == 2:
                self.votos["Maria"] += 1
            elif voto == 3:
                self.votos["Juliana"] += 1
            else:
                print("Opção inválida!")
        except ValueError:
            print("Valor invalido")

    def menu(self):
        while True:
            print("-"*30)
            print(" "*15,"Menu")
            print("-"*30)
            print("1) Votar")
            print("2) Status da Votação")
            print("3) Resultado")
            print("0) Sair")
            print("-"*30, "\n\n")

            try:
                op = int(input("O que deseja? "))
                if op == 1:
                    self.votar()
                elif op == 2:
                    self.stats()
                elif op == 3:
                    print("Esse é o resultado da votação: ", self.votos)
                elif op == 0:
                    print("Saindo...")
                    break
                else:
                    print("Opção inválida!")
            except ValueError:
                print("Digite apenas números válidos")

