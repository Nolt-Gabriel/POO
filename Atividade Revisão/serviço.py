class Pessoa:

    def __init__(self, nome, cpf, endereco):

        self.nome = nome
        self._cpf = cpf
        self._email = _email

class funcionario(Pessoa):

    pass

class Professor(funcionario):

    def __init__(self, disciplina, id):

        super().__init__(nome, cpf, email)
        self.disciplina = disciplina
        self.id = id

class Aluno(Pessoa):

    def __init__(self, matricula, curso):

        super();__init__(nome, cpf, email)
        self.matricula = matricula
        self.curso = curso

class Diretor(Professor):

     def __init__(self):

        super().__init__()

