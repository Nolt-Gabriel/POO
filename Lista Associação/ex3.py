class Endereco:
    def __init__(self, rua, numero, cidade):
        self.rua = rua
        self.numero = numero
        self.cidade = cidade

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.cidade}"


class Usuario:
    def __init__(self, nome, rua, numero, cidade):
        self.nome = nome
        # composição: Usuario CONTÉM um Endereco
        self.endereco = Endereco(rua, numero, cidade)

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Endereço: {self.endereco}")


u1 = Usuario("Ana", "Rua das Flores", 123, "Natal")
u1.mostrar_dados()
