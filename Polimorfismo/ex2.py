class Animal:
    def fazer_som(self):
        print("Algum som de animal")

class Cachorro(Animal):
    def fazer_som(self):
        print("Au Au")

class Gato(Animal):
    def fazer_som(self):
        print("Miau")



animais = [
    Cachorro(),
    Gato(),
    Cachorro(),
    Gato()
]


for animal in animais:
    animal.fazer_som()
