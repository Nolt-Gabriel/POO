boletim = {
    'João': 7.5,
    'Maria': 6.0,
    'Carlos': 5.3,
    'Ana': 9.2,
    'Bruno': 4.8,
    'Paula': 6.5
}

print("Alunos com nota acima da média (6.0):")
for aluno, nota in boletim.items():
    if nota > 6.0:
        print(aluno, ":", nota)
