class Produto:
    produtos = []

    def __init__(self, nome, quantidade, preco_unitario):
        self.nome = nome
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

    @classmethod
    def adicionar_produto(cls, produto):
        cls.produtos.append(produto)

    @classmethod
    def valor_total_estoque(cls):
        return sum(produto.quantidade * produto.preco_unitario for produto in cls.produtos)

    @classmethod
    def produto_maior_quantidade(cls):
        return max(cls.produtos, key=lambda produto: produto.quantidade)

    @classmethod
    def produto_menor_preco(cls):
        return min(cls.produtos, key=lambda produto: produto.preco_unitario)

    @classmethod
    def listar_produtos(cls):
        for produto in cls.produtos:
            print("Produto:", produto.nome)
            print("Quantidade:", produto.quantidade)
            print("Preço Unitário:", produto.preco_unitario)
            print("-----------------------------")

# Exemplo de uso dos métodos de classe

# Adicionar produtos ao estoque
produto1 = Produto("Arroz", 10, 5)
produto2 = Produto("Feijão", 5, 4)
produto3 = Produto("Macarrão", 8, 3)

Produto.adicionar_produto(produto1)
Produto.adicionar_produto(produto2)
Produto.adicionar_produto(produto3)

# Calcular valor total do estoque
print("Valor Total do Estoque:", Produto.valor_total_estoque())

# Encontrar produto com maior quantidade
produto_maior_quantidade = Produto.produto_maior_quantidade()
print("Produto com Maior Quantidade:")
print("Nome:", produto_maior_quantidade.nome)
print("Quantidade:", produto_maior_quantidade.quantidade)
print("Preço Unitário:", produto_maior_quantidade.preco_unitario)

# Encontrar produto com menor preço unitário
produto_menor_preco = Produto.produto_menor_preco()
print("Produto com Menor Preço Unitário:")
print("Nome:", produto_menor_preco.nome)
print("Quantidade:", produto_menor_preco.quantidade)
print("Preço Unitário:", produto_menor_preco.preco_unitario)

# Listar todos os produtos e suas quantidades
print("--- Lista de Produtos ---")
Produto.listar_produtos()
