class ElementoHTML:
    def __init__(self, tag, conteudo):
        self.tag = tag
        self.conteudo = conteudo

    def renderizar(self):
        return f"<{self.tag}>{self.conteudo}</{self.tag}>"


class PaginaWeb:
    def __init__(self, titulo):
        self.titulo = titulo
        self.elementos = []      # composição: Página CONTÉM ElementosHTML

    def adicionar_elemento(self, elemento):
        self.elementos.append(elemento)

    def renderizar(self):
        for elemento in self.elementos:
            print(elemento.renderizar())


# uso
pagina = PaginaWeb("Minha página")

h1 = ElementoHTML("h1", "Bem-vindo")
p = ElementoHTML("p", "Texto da página")

pagina.adicionar_elemento(h1)
pagina.adicionar_elemento(p)

pagina.renderizar()
