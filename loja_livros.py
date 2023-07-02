class Livro:
    def __init__(self, titulo, autor, ano_publicacao, preco):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.preco = preco

    def exibir_informacoes(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano de publicação: {self.ano_publicacao}")
        print(f"Preço: R${self.preco:.2f}")


class LojaLivros:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def exibir_catalogo(self):
        print(f"Catálogo da loja {self.nome}:")
        for livro in self.livros:
            livro.exibir_informacoes()
            print()


# Criar objetos Livro
livro1 = Livro("Aprendendo Python", "Guido van Rossum", 2021, 59.90)
livro2 = Livro("Python Cookbook", "David Beazley", 2018, 79.90)
livro3 = Livro("Clean Code", "Robert C. Martin", 2008, 89.90)

# Criar objeto LojaLivros
loja = LojaLivros("Minha Loja de Livros")

# Adicionar livros à loja
loja.adicionar_livro(livro1)
loja.adicionar_livro(livro2)
loja.adicionar_livro(livro3)

# Exibir catálogo da loja
loja.exibir_catalogo()
