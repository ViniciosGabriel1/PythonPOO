class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f"Pessoa: {self.nome}"

    def __eq__(self, other):
        return self.nome == other.nome

    def __add__(self, other):
        return Pessoa(f"{self.nome} {other.nome}")

    def __len__(self):
        return len(self.nome)

pessoa1 = Pessoa("João")
pessoa2 = Pessoa("Maria")

print(pessoa1)  # Saída: Pessoa: João

print(pessoa1 == pessoa2)  # Saída: False

pessoa3 = pessoa1 + pessoa2
print(pessoa3)  # Saída: Pessoa: João Maria

print(len(pessoa1))  # Saída: 4

print("====================================")

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Ponto({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Ponto):
            return Ponto (self.x+ other.x, self.y + other.y)
        raise TypeError("Unsupported operand type for +")

ponto1 = Ponto(2, 3)
ponto2 = Ponto(40, 50)

print(ponto1," + ",ponto2)  # Saída: Ponto(2, 3)
print("=====")
soma_pontos = ponto1 + ponto2
print(soma_pontos)  # Saída: Ponto(6, 8)

print("==============")

class Animal:
    pass

class Cachorro(Animal):
    pass

class Gato(Animal):
    pass

animal = Gato()

print(isinstance(animal, Animal))  # Saída: True
print(isinstance(animal, Cachorro))  # Saída: False
print(isinstance(animal, Gato))  # Saída: True

'''
O primeiro print() verifica se o objeto animal é uma instância da classe Animal. Como Gato é uma subclasse de Animal, a função isinstance() retorna True.
O segundo print() verifica se o objeto animal é uma instância da classe Cachorro. Como Gato não é uma subclasse de Cachorro, a função isinstance() retorna False.
O terceiro print() verifica se o objeto animal é uma instância da classe Gato. Como Gato é a própria classe do objeto, a função isinstance() retorna True.'''


