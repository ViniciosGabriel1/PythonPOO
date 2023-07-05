class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario
    
    def apresentar(self):
        super().apresentar()
        print(f"Sou um funcionário e meu salário é R${self.salario}.")

class Gerente(Funcionario):
    def __init__(self, nome, idade, salario, departamento):
        super().__init__(nome, idade, salario)
        self.departamento = departamento
    
    def apresentar(self):
        super().apresentar()
        print(f"Sou um gerente do departamento {self.departamento}.")


print("Informações da pessoa: ")


pessoa=str(input("Seu nome : "))   
idade = int(input("Sua idade : "))
p1 = Pessoa(pessoa, idade)


print("Informações do funcionário: ")
nome=str(input("Seu nome : "))   
idade = int(input("Sua idade : "))
salario = float(input("Seu salário : "))
p2 = Funcionario(nome, idade, salario)
        

print("Informações do Gerente: ")

nome=str(input("Seu nome : "))   
idade = int(input("Sua idade : "))
salario = float(input("Seu salário : "))
departamento = str(input("Qual seu departamento : "))
p3 = Gerente(nome, idade, salario, departamento)



p1.apresentar()
print("-----------")
p2.apresentar()
print("-----------")
p3.apresentar()