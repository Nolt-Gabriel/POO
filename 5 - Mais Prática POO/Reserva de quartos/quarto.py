class Quarto:
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo
        self.ocupado = False

    def reservar(self):
        if self.ocupado:
            print(f"Quarto {self.numero} já está ocupado.")
        else:
            self.ocupado = True
            print(f"Quarto {self.numero} reservado com sucesso.")

    def liberar(self):
        if not self.ocupado:
            print(f"Quarto {self.numero} já está livre.")
        else:
            self.ocupado = False
            print(f"Quarto {self.numero} liberado.")

    def exibir_dados(self):
        status = "Ocupado" if self.ocupado else "Livre"
        print(f"Quarto {self.numero} - Tipo: {self.tipo} - Status: {status}")
