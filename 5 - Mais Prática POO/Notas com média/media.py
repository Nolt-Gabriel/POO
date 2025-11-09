class Aluno:

    def __init__(self, nome):

        self.nome = nome
        self.notas = []

    def adicionar(self, nota):

        self.notas.append(nota)
        return self.notas
    def calcular(self):

        if len(self.notas) == 0:

            return 0

        return sum(self.notas)/len(self.notas)
    
    def exibir(self):

        return self.notas

