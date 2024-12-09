class Conta:
    def __init__(self, numero_conta, titular):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso! Seu saldo agora é R$ {self.saldo:.2f}")
        else:
            print("Valor inválido!")

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de R$ {valor:.2f} realizado com sucesso! Seu saldo agora é R$ {self.saldo:.2f}")
            else:
                print("Saldo insuficiente!")
        else:
             print("Valor inválido!")

    def exibir_saldo(self):
        print(f"Saldo: R${self.saldo}")

    def resumo(self):
        print("## RESUMO DA CONTA.\n#")
        print(f"# Conta: {"Conta Corrente " if self.__class__.__name__ == "ContaCorrente" else "Conta Poupança"}")
        print(f"# Número da conta: {self.numero_conta}")
        print(f"# Titular: {self.titular}")
        print(f"# Saldo: R$ {self.saldo:.2f}")