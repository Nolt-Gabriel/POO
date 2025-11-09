class Tarefa:

    def __init__(self, titulo, desc):

        self.titulo = titulo
        self.desc = desc
        self.status = False


    def concluida(self):

        self.status = True

    def finalizada(self):

        if self.status == True:

            print("Essa tarefa esta finalizada")

    def exibir(self):

        print("-"*35)
        print("Informações da Tarefa:\n")
        print("-Titulo:", self.titulo)
        print("-Descrição:", self.desc)
        print("-Status:", self.status, "\n")
        print("-"*35)

tarefa = Tarefa("Jogar", "Zerar Terraria")
tarefa2 = Tarefa("Fazer o Dever", "Atividade de Matemática")

tarefa.exibir()

tarefa2.concluida()

tarefa2.exibir()

