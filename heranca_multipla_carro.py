class Carro:
    def __init__(self, modelo):
        self.modelo = modelo

    def acelerar(self):
        print(f"{self.modelo} está acelerando ")   

    def freiar(self):
        print(f"{self.modelo} está freiando ") 
    
    def desligar(self):
        print(f"{self.modelo} está desligando ")

class Cor_carro:
    def __init__(self,cor):
        self.cor = cor

    def selecionar_cor(self):
        print(f"{self.cor} selecionada para o {self.modelo} ")

class Bmw(Carro,Cor_carro):
    def __init__(self, modelo,cor):
        super().__init__(modelo)
        self.cor=cor

class Bugatti(Carro,Cor_carro):
    def __init__(self, modelo,cor):
        super().__init__(modelo)
        self.cor = cor


modelo =str(input("Qual o modelo da BMW? "))
cor = str(input("Qual a cor para a BMW? "))        

bmw = Bmw(modelo,cor)
bmw.acelerar()
bmw.freiar()
bmw.desligar()
bmw.selecionar_cor()

modelo =str(input("Qual o modelo do bugatti ? "))
cor = str(input("Qual a cor para bugatti ? "))  

bugatti = Bugatti("VEYRON " , "Verde")
bugatti.acelerar()
bugatti.freiar()
bugatti.desligar()
bugatti.selecionar_cor()







    


