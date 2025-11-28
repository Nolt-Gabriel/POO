class Cliente:

    def __init__(self, nome):

        self.nome = nome
        self.endereco = []

 
    def adicionar_endereco(self, cidade, estado):

        self.endereco.append(Endereco(cidade, estado))
    

    def mostrar_enderecos(self):

        for end in self.endereco:

            print(end.cidade, end.estado)


class Endereco:

    def __init__(self, cidade, estado):

        self.cidade = cidade
        self.estado = estado

c1 = Cliente("Arthur")
c1.adicionar_endereco("Natal", "RN")
c1.mostrar_enderecos()