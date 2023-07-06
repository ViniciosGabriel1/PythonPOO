class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def comer(self):
        print(f"{self.nome} está comendo.")

class Nadador:
    def nadar(self):
        print(f"{self.nome} está nadando.")

class Voador:
    def voar(self):
        print(f"{self.nome} está voando.")

class Peixe(Animal, Nadador):
    def __init__(self, nome):
        self.nome = nome

class Ave(Animal, Voador):
    def __init__(self, nome):
        self.nome = nome

class Pato(Ave, Nadador):
    def __init__(self, nome):
        self.nome = nome

peixe = Peixe("Nemo")
peixe.comer()
peixe.nadar()

pardal = Ave("Pardal")
pardal.comer()
pardal.voar()

pato = Pato("Donald")
pato.comer()
pato.nadar()
pato.voar()
