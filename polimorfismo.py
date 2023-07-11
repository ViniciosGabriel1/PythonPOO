class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!"

class Gato(Animal):
    def fazer_som(self):
        return "Miau!"
    
class Pombo(Animal):
    def fazer_som(self):
        return "Pru Pru!"

animais = [Cachorro(), Gato(),Pombo()]

for animal in animais:
    print(animal.fazer_som())

    print("-=========================-")

class Veiculo:
    def __init__(self, marca):
        self.marca = marca
    
    def acelerar(self):
        pass
    
    def frear(self):
        pass

class Carro(Veiculo):
    def acelerar(self):
        return "Carro acelerando..."
    
    def frear(self):
        return "Carro freando..."
    
class Moto(Veiculo):
    def acelerar(self):
        return "Moto acelerando..."
    
    def frear(self):
        return "Moto freando..."

class Bicicleta(Veiculo):
    def frear(self):
        return "Bicicleta freando..."

veiculos = [Carro("Ford"), Moto("Honda"), Bicicleta("Caloi")]

for veiculo in veiculos:
    print(veiculo.marca + ":")
    print(veiculo.acelerar())
    print(veiculo.frear())
    print("------")

