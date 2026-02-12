# Nome: Nicholas Gabriel Silva Soares
# Data de início: 12/02/2026
# Tema: Sistema de Gerenciamento de Biblioteca

class Pessoa:
    def __init__(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def __str__(self):
        return f"Nome: {self.__nome}"


class Aluno(Pessoa):
    def __init__(self, nome, matricula):
        super().__init__(nome)
        self.__matricula = matricula

    def get_matricula(self):
        return self.__matricula

    def __str__(self):
        return f"Aluno: {self.get_nome()} | Matrícula: {self.__matricula}"


class Livro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor
        self.__disponivel = True

    def emprestar(self):
        if self.__disponivel:
            self.__disponivel = False
            return True
        return False

    def __str__(self):
        status = "Disponível" if self.__disponivel else "Emprestado"
        return f"{self.__titulo} - {self.__autor} ({status})"


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.alunos = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        for livro in self.livros:
            print(livro)


def menu():
    biblioteca = Biblioteca()

    while True:
        print("\n=== SISTEMA BIBLIOTECA ===")
        print("1 - Cadastrar livro")
        print("2 - Listar livros")
        print("3 - Emprestar")
        print("4 - Sair")

        opcao = input("Escolha: ")

        try:
            if opcao == "1":
                titulo = input("Título: ")
                autor = input("Autor: ")
                livro = Livro(titulo, autor)
                biblioteca.adicionar_livro(livro)
                print("Livro cadastrado!")

            elif opcao == "2":
                biblioteca.listar_livros()

            elif opcao == "3":
                livro.emprestar()
                print("Livro emprestado com sucesso!")
            elif opcao == "4":
                print("Encerrando sistema...")
                break

            else:
                print("Opção inválida!")

        except Exception as e:
            print("Erro:", e)


menu()