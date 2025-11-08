class QuantidadeIndisponivelError(Exception):
    def __init__(self, produto, requisitada, disponivel):
        super().__init__(
            f"Não há quantidade suficiente do produto '{produto}'. "
            f"Solicitada: {requisitada}, Disponível: {disponivel}"
        )

class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

class Estoque:
    def __init__(self):
        self.produtos = {}

    def adicionar(self, produto):
        self.produtos[produto.nome] = produto

    def remover(self, nome_produto, quantidade):
        if nome_produto not in self.produtos:
            raise ValueError("Produto não encontrado no estoque.")
        produto = self.produtos[nome_produto]
        if quantidade > produto.quantidade:
            raise QuantidadeIndisponivelError(produto.nome, quantidade, produto.quantidade)
        produto.quantidade -= quantidade
        print(f"{quantidade} unidade(s) de {produto.nome} removida(s). Restam {produto.quantidade}.")

# Demonstração do uso do try/except
estoque = Estoque()
p1 = Produto("Sabonete", 5)
estoque.adicionar(p1)

try:
    estoque.remover("Sabonete", 10)
except QuantidadeIndisponivelError as e:
    print("Erro tratado:", e)
