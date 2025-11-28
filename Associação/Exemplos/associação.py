class Crianca:

    def __init__(self, nome):

        self.nome = nome
        self.video_game = None

    @property
    def videogame(self):

        return self.video_game

    @videogame.setter
    def videogame(self, nome):

        self.video_game = nome
    

class VideoGame:

    def __init__(self, nome):

        self.nome = nome

    def jogar(self):

        print("Estou jogando PS5")

crianca = Crianca("Arthur")
videogame = VideoGame("PS5")

crianca.video_game = videogame
crianca.video_game.jogar()