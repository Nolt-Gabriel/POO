class Autor:
    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade


class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor     
        self.ano = ano

    def __str__(self):
        return f"'{self.titulo}' ({self.ano}) - {self.autor.nome}"


class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.catalogo = []     

    def adicionar_livro(self, livro):
        self.catalogo.append(livro)

    def remover_livro(self, livro):
        if livro in self.catalogo:
            self.catalogo.remove(livro)

    def buscar_livro_por_titulo(self, titulo):
        for livro in self.catalogo:
            if livro.titulo.lower() == titulo.lower():
                return livro
        return None

    def listar_catalogo(self):
        if not self.catalogo:
            print("Catálogo vazio.")
        else:
            for livro in self.catalogo:
                print(livro)

autor1 = Autor("George Orwell", "Britânico")
livro1 = Livro("1984", autor1, 1949)
livro2 = Livro("A Revolução dos Bichos", autor1, 1945)

bib = Biblioteca("Biblioteca Central")
bib.adicionar_livro(livro1)
bib.adicionar_livro(livro2)

bib.listar_catalogo()

encontrado = bib.buscar_livro_por_titulo("1984")
if encontrado:
    print("Achei:", encontrado)
