class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        print("O animal está fazendo algum som.")

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca = raca

    def fazer_som(self):
        print("O cachorro está latindo.")

# Criando uma instância da classe filha Cachorro
meu_cachorro = Cachorro("Rex", "Labrador")
meu_animal = Animal("Wyvern")
# Acessando atributos e métodos herdados da classe pai Animal
print(meu_cachorro.nome)  # Output: Rex
meu_cachorro.fazer_som()  # Output: O cachorro está latindo.
print(meu_animal.nome)
meu_animal.fazer_som()
