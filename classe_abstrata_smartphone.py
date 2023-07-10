from abc import ABC, abstractmethod

class Smartphone(ABC):
    def __init__(self, modelo):
        self.modelo = modelo

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class Iphone(Smartphone):
    def ligar(self):
        return f"{self.modelo} está ligando !!"
    
    def desligar(self):
        return f"{self.modelo} está desligando !!"
    

class Sansumg(Smartphone):
    def ligar(self):
        return f"{self.modelo} está ligando !!"
    
    def desligar(self):
        return f"{self.modelo} está desligando !!"
    

sansumg = Sansumg("Galaxy S22 Ultra")
iphone = Iphone("8 Plus")


print(iphone.ligar())
print(iphone.desligar())
print("-=================-")

print(sansumg.ligar())
print(sansumg.desligar())