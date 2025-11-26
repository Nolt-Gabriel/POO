turma1 = {'azul', 'verde', 'vermelho', 'amarelo'}
turma2 = {'verde', 'vermelho', 'roxo', 'preto'}


cores_comuns = turma1 & turma2
print("Cores em ambas as turmas:", cores_comuns)


cores_exclusivas_turma1 = turma1 - turma2
print("Cores exclusivas da turma 1:", cores_exclusivas_turma1)
