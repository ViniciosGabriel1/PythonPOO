import logging

logging.basicConfig(filename='try_except.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class ContaBancaria:
    def __init__(self, nome_titular, saldo_inicial):
        logging.info(f"Iniciando com {nome_titular} e {saldo_inicial}")
        self.nome_titular = nome_titular
        self.saldo = saldo_inicial
    
    def depositar(self, valor):
        self.saldo += valor
        logging.info(f"Saldo depositado {valor}")

        if valor == 0:
          print("Deposito não efetuado")
          logging.info(f"Deposito não efetuado :  {self.saldo}")   
    
    def sacar(self, valor):
        if valor == 0:
          print(f"Valor inválido para efetuar o saque {valor}")
          logging.info(f"Saque não efetuado :  {self.saldo}")   

        elif self.saldo >= valor:
            self.saldo -= valor
            print("Saque realizado com sucesso.")
            logging.info(f"Saldo sacado {self.saldo}")
        else:
            print("Saldo insuficiente.")
            logging.info(f"Saldo insuficiente: {self.saldo}")
    
    def transferir(self, outra_conta, valor):
        if valor == 0:
            print("Tranferência não realizada .")
            logging.info(f" Tranferência não realizada . R$ {self.saldo}")

        elif self.saldo >= valor:
             self.saldo -= valor
             outra_conta.depositar(valor)
             print(f"Transferência realizada com sucesso  ")
             logging.info(f" Transferência realizada com sucesso .  R$ {valor} para {outra_conta}")
        else:
            print("Saldo insuficiente.")

    
    def exibir_informacoes(self):
        print(f"Usuário: R${self.nome_titular}")
        print(f"Seu saldo atual é : R${self.saldo:.2f}")
        



nome_titular=str(input("Qual o nome do titular ? "))
saldo_inicial=float(input("Qual o seu saldo atual ? "))

conta1 = ContaBancaria(nome_titular,saldo_inicial)
conta2 = ContaBancaria(nome_titular,saldo_inicial)

valor_saque = float(input("Quanto quer sacar ?"))
conta1.sacar(valor_saque)

valor_deposito = float(input("Quanto quer depositar ?"))
conta1.depositar(valor_deposito)

valor_transferencia = float(input("Quanto quer transferir ? "))
conta1.transferir(conta2,valor_transferencia)


conta1.exibir_informacoes()