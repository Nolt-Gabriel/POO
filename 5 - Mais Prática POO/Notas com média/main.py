from media import Aluno

aluno = Aluno("Mateus")

aluno.adicionar(10.0)
aluno.adicionar(10.0)
aluno.adicionar(10.0)

print(aluno.exibir())

print(f"a média do aluno {aluno.nome} é {aluno.calcular():.2f}")