class Funcionario:
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo

    def __str__(self):
        return f"{self.nome} ({self.cargo})"


class Tarefa:
    def __init__(self, titulo, descricao, responsavel, status="Pendente"):
        self.titulo = titulo
        self.descricao = descricao
        self.responsavel = responsavel  
        self.status = status             

    def __str__(self):
        return f"[{self.status}] {self.titulo} - {self.responsavel.nome}"

class Cronograma:
    def __init__(self, data_inicio, data_entrega_prevista, data_conclusao=None):
        self.data_inicio = data_inicio
        self.data_entrega_prevista = data_entrega_prevista
        self.data_conclusao = data_conclusao

    def __str__(self):
        return (f"Início: {self.data_inicio}, "
                f"Previsto: {self.data_entrega_prevista}, "
                f"Conclusão: {self.data_conclusao or 'não concluído'}")

class Projeto:
    def __init__(self, nome, gerente, data_inicio, data_prevista):
        self.nome = nome
        self.gerente = gerente                 
        self.tarefas = []                      
        self.cronograma = Cronograma(          
            data_inicio, data_prevista
        )

    
    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    
    def atualizar_status_tarefa(self, titulo, novo_status):
        for tarefa in self.tarefas:
            if tarefa.titulo == titulo:
                tarefa.status = novo_status
                break

    
    def listar_tarefas_por_status(self, status):
        return [t for t in self.tarefas if t.status == status]

   
    def esta_concluido(self):
        if not self.tarefas:
            return False
        return all(t.status == "Concluída" for t in self.tarefas)


gerente = Funcionario("Ana", "Gerente de Projetos")
dev1 = Funcionario("João", "Desenvolvedor")
dev2 = Funcionario("Maria", "QA")


projeto = Projeto("Sistema X", gerente, "01/01/2025", "31/03/2025")


t1 = Tarefa("Implementar login", "Tela e API de login", dev1)
t2 = Tarefa("Testar login", "Testes funcionais de login", dev2)
t3 = Tarefa("Documentar módulo", "Documentação da feature", dev1)


projeto.adicionar_tarefa(t1)
projeto.adicionar_tarefa(t2)
projeto.adicionar_tarefa(t3)


projeto.atualizar_status_tarefa("Implementar login", "Concluída")
projeto.atualizar_status_tarefa("Testar login", "Em andamento")


print("Tarefas em andamento:")
for t in projeto.listar_tarefas_por_status("Em andamento"):
    print(" -", t)

print("\nProjeto concluído?", projeto.esta_concluido())
print("Cronograma:", projeto.cronograma)
