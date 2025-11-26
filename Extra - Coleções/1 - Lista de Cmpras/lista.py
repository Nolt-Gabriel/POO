class ListaCompras:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)
        print(f"{item} foi adicionado à lista.")

    def remover_item(self, item):
        if item in self.itens:
            self.itens.remove(item)
            print(f"{item} foi removido da lista.")
        else:
            print(f"{item} não está na lista.")

    def mostrar_lista(self):
        print("Itens da lista:")
        for item in self.itens:
            print(f"- {item}")


lista = ListaCompras()
lista.adicionar_item("Arroz")
lista.adicionar_item("Feijão")
lista.adicionar_item("Tomate")
lista.mostrar_lista()


lista.remover_item("Feijão")


lista.adicionar_item("Frango")
lista.mostrar_lista()
