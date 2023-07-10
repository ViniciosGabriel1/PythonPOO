from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def fazer_som(self):
        pass

    @abstractmethod
    def correr(self):
        pass

class Cachorro(Animal):

    def fazer_som(self):
        return "Au au!"

    def correr(self):
        return "O cachorro está correndo!"

cachorro = Cachorro()
print(cachorro.fazer_som())  # Saída: Au au!
print(cachorro.correr())  # Saída: O cachorro está correndo!

print("-================================-")


from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def fazer_som(self):
        pass

    @abstractmethod
    def mover(self):
        pass

class Mamifero(Animal):
    def mover(self):
        return f"{self.nome} está se movendo!"

class Felino(Mamifero):
    def fazer_som(self):
        return "Rugido!"

class Gato(Felino):
    def fazer_som(self):
        return "Miau!"

class Cachorro(Mamifero):
    def fazer_som(self):
        return "Au au!"

gato = Gato("Tom")
cachorro = Cachorro("Pluto")

print(gato.nome)  # Saída: Tom
print(gato.fazer_som())  # Saída: Miau!
print(gato.mover())  # Saída: Tom está se movendo!

print(cachorro.nome)  # Saída: Pluto
print(cachorro.fazer_som())  # Saída: Au au!
print(cachorro.mover())  # Saída: Pluto está se movendo!

