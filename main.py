# Nome: Nicholas Gabriel Silva Soares
# Data de início: 12/02/2026
# Tema: Sistema de RPG

#Biblioteca random pra randomizar uns valores ai
import random

#Classe Personagem ==============================
class Personagem:

    #função com método mágico que é executado assim que se inicia uma isntância da classe
    def __init__(self, nome):
        self.__nome = nome
        self.__vida = 100
        self.__nivel = 1
    
    #encapsulamento para o nome
    def get_nome(self):
        return self.__nome
    
    #encapsulamento para a vida
    def get_vida(self):
        return self.__vida
    
    #ataque padrão de cada personagem
    def atacar(self):
        return 10

    #função para o personagem receber o dano e descontar na vida
    def receber_dano(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0

    #Checa se o personagem está vivo
    def esta_vivo(self):
        return self.__vida > 0

    #Método mágico Str que formata a saída caso seja printado o objeto 
    def __str__(self):
        return f"{self.__nome} | Vida: {self.__vida} | Nível: {self.__nivel}"

#=====================================================

#Classe guerreiro que vai herdar de personagem o nome
class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        #Dano padrão da classe baseado em atk fisico
        self.__forca = 20

    #Vai fazer o efeito de rpg de girar um "dado" vai tirar um número
    # entre 15 e 20 pra dar o dano
    # >>>> Polimorfismo, onde ele utiliza do método atacar de forma diferente<<<<<
    def atacar(self):
        return random.randint(15, self.__forca)

#Classe mago também vai herdar de personagem
class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        #Da classe mago temos a mana
        self.__mana = 30

    #Se tiver mais que 5 de mana o personagem vai atacar e gastar 5 de mana
    #Aí ele vai tirar um valor aleatório entre 20 e 35 para dar o dano mágico
    #Caso ele não tenha mana ele só vai retornar 5 de dano, mago buxa
    #>>>>>> Polimorfismo <<<<<<<<
    def atacar(self):
        if self.__mana >= 5:
            self.__mana -= 5
            return random.randint(20, 35)
        else:
            return 5

#Aqui é onde rola o jogo >:D ===================================
class Jogo:

    #Assim que a instancia da classe é criada ele cria essa lista contendo os personagens
    #da partida
    def __init__(self):
        self.personagens = []

    #Aqui criamos os personagens
    def criar_personagem(self):

        nome = input("Nome do personagem: ")
        print("1 - Guerreiro")
        print("2 - Mago")
        escolha = input("Escolha a classe: ")

        if len(self.personagens) == 2:
            #É um Duelo, mais de 3 pode não man
            print("Não pode adicionar mais de dois personagens ao Duelo!")
            return
        #Escolha das classes
        if escolha == "1": 
            #Já instância um objeto, ou seja aqui temos associação onde a Classe jogo contém 
            #Os objetos instânciados da classe Personagem, sem jogo, personagem não existe mas
            #A classe jogo não gerencia a classe guerreiro nem mago diretamente, então é Agregação
            personagem = Guerreiro(nome)

        elif escolha == "2":
            #Aqui também  
            personagem = Mago(nome)
        else:
            print("Classe inválida!")
            return

        # Adiciona os personagens na lista
        self.personagens.append(personagem)
        print("Personagem criado com sucesso!")

    #função para listar os personagens criados, aqui vamos utilizar daquele Str nas classes
    def listar_personagens(self):
        if not self.personagens:
            print("Nenhum personagem criado.")
        for p in self.personagens:
            #bem aqui
            print(p)

    #Aqui é onde a porradaria começa
    def batalhar(self):
        if len(self.personagens) < 2:
            #não tem como espancar você mesmo né, só com dois personagens
            print("É necessário ter 2 personagens.")
            return

        #Aqui dizemos quem é player 1 e quem é player 2
        p1 = self.personagens[0]
        p2 = self.personagens[1]

        #Farmando aura iniciando a batalha
        print(f"Batalha entre {p1.get_nome()} e {p2.get_nome()}!")

        #Aqui eles começam a se bater, player 1 primeiro
        while p1.esta_vivo() and p2.esta_vivo():
            dano = p1.atacar()
            p2.receber_dano(dano)
            print(f"{p1.get_nome()} causou {dano} de dano!")

            #Se o player 2 tankar, a rodada é dele
            if p2.esta_vivo():
                dano = p2.atacar()
                p1.receber_dano(dano)
                print(f"{p2.get_nome()} causou {dano} de dano!")

        #Se player 1 ta vivo, ele ganhou, senão, não sobrou nada pro beta do player 1
        if p1.esta_vivo():
            print(f"{p1.get_nome()} venceu!")
        else:
            print(f"{p2.get_nome()} venceu!")
#==============================================================


#Aqui é o menu classico =======================================
def menu():
    jogo = Jogo()

    while True:
        print("\n=== SISTEMA RPG ===")
        print("1 - Criar personagem")
        print("2 - Listar personagens")
        print("3 - Iniciar batalha")
        print("4 - Sair")

        opcao = input("Escolha: ")

        try:
            if opcao == "1":
                jogo.criar_personagem()
            elif opcao == "2":
                jogo.listar_personagens()
            elif opcao == "3":
                jogo.batalhar()
            elif opcao == "4":
                print("Encerrando jogo...")
                break
            else:
                print("Opção inválida!")
        except Exception as e:
            print("Erro:", e)


menu()
#=========================================================