import logging

logging.basicConfig(filename='heranca_smartphone.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class SmartPhone:
    
    def __init__(self,modelo,valor,memoria_ram,mega_pixels) :
        self.modelo = modelo
        self.valor = valor
        self.memoria_ram = memoria_ram
        self.mega_pixels = mega_pixels

    
class Sansumg(SmartPhone):
    
    def __init__(self,modelo,valor,memoria_ram,mega_pixels) :
            super().__init__(modelo,valor, memoria_ram,mega_pixels)
        

    def Ligar(self):
         print(f"{self.modelo}, Ligando")
         logging.info(f"{self.modelo}, Ligando")

    def Desligar(self):
         print(f"{self.modelo}, Desligando")
         logging.info(f"{self.modelo}, Desligando")

    def exibir_especificacoes(self):
         print(f"Modelo : {self.modelo}")
         print(f"Valor : ${self.valor} Reais")
         print(f"Memória ram : {self.memoria_ram} GB")
         print(f"Mega pixels : {self.mega_pixels} ")
         logging.info(f"Exibindo especificações : {self.modelo} , $ {self.valor} REAIS , {self.memoria_ram} GB, {self.mega_pixels} MEGA PIXELS")


class Iphone(SmartPhone):
    
    def __init__(self,modelo,valor,memoria_ram,mega_pixels) :
            super().__init__(modelo,valor,memoria_ram,mega_pixels)

    def Ligar(self):
         print(f"{self.modelo}, Ligando")
         logging.info(f"{self.modelo}, Ligando")

    def Desligar(self):
         print(f"{self.modelo}, Desligando")
         logging.info(f"{self.modelo}, Desligando")

    def exibir_especificacoes(self):
         print(f"Modelo : {self.modelo}")
         print(f"Valor : ${self.valor} Reais")
         print(f"Memória ram : {self.memoria_ram} GB")
         print(f"Mega pixels : {self.mega_pixels} ")
         logging.info(f"Exibindo especificações : {self.modelo} , $ {self.valor} REAIS , {self.memoria_ram} GB, {self.mega_pixels} MEGA PIXELS")  


escolha_so =int(input("[1] para Samsung e [2] para Iphone : ")) 
while escolha_so < 1 or escolha_so > 2:
      escolha_so =int(input("Opção inválida ! , tente -> [1] para Samsung e [2] para Iphone : ")) 
else:
        if escolha_so == 1:
                modelo =str(input("Qual o modelo : "))
                valor = float(input("Qual o valor : "))
                memoria_ram = float(input("Quantos giga de ram  : "))
                mega_pixels = float(input("Qual a potência da câmera  : "))  
                smart_phone1 = Sansumg(modelo,valor,memoria_ram,mega_pixels)
                
                print("===================================")
                smart_phone1.Ligar()
                print("===================================")
                smart_phone1.Desligar()
                print("===================================")
                smart_phone1.exibir_especificacoes()
                print("===================================") 


        elif escolha_so == 2:
                modelo =str(input("Qual o modelo : "))
                valor = float(input("Qual o valor : "))
                memoria_ram = float(input("Quantos giga de ram  : "))
                mega_pixels = float(input("Qual a potência da câmera  : "))  
                smart_phone2 = Iphone(modelo,valor,memoria_ram,mega_pixels)
                
                print("===================================")
                smart_phone2.Ligar()
                print("===================================")
                smart_phone2.Desligar()
                print("===================================")
                smart_phone2.exibir_especificacoes()
                print("===================================") 

        else:
                print("Opção inválida !!")                







