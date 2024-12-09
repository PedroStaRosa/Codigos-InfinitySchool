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


class ContaCorrente(Conta):
    def __init__(self, numero_conta, titular, taxa_manutencao, limite_cheque_especial):
        super().__init__(numero_conta, titular)
        self.taxa_manutencao = taxa_manutencao
        self.limite_cheque_especial = limite_cheque_especial
        self.saldo_lim_especial = limite_cheque_especial

    def depositar(self, valor):
        if valor > 0:

            if (self.saldo + self.saldo_lim_especial) < self.limite_cheque_especial:

                valor_descontado_tx_cheque_especial = valor * (self.taxa_manutencao / 100)
                valor_liquido = valor - valor_descontado_tx_cheque_especial
                diferenca_a_cobrir = self.limite_cheque_especial - self.saldo_lim_especial

                self.saldo_lim_especial += valor_liquido
                
                if self.saldo_lim_especial > self.limite_cheque_especial:

                    valor_restante = self.saldo_lim_especial - self.limite_cheque_especial
                    

                    print(f"Depósito de R$ {valor} foi descontado R$ {valor_descontado_tx_cheque_especial} de taxa e cobriu os R$ {diferenca_a_cobrir} do cheque especial.")
                    self.saldo_lim_especial = self.limite_cheque_especial
                    self.saldo += valor_restante
                    
                    if self.saldo > 0:
                        print(f"Seu saldo agora é R$ {self.saldo:.2f}")
                    return
                else:
                    
                    print(f"Depósito de R$ {valor} cobriu R$ {valor_liquido} dos R$ {diferenca_a_cobrir} devidos do cheque especial. Taxa de manutenção R$ {valor_descontado_tx_cheque_especial} descontada.")
                    return
            else:
                self.saldo += valor
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso! Seu saldo agora é R$ {self.saldo:.2f}")
        else:
            print("Valor inválido!")

    def sacar(self, valor):
            if valor > 0:
                saldo_disponivel = self.saldo + self.saldo_lim_especial

                if valor <= saldo_disponivel:  
                    if valor <= self.saldo: 
                        self.saldo -= valor 
                    else:  
                        valor_restante = valor - self.saldo 
                        self.saldo = 0 
                        if valor_restante <= self.saldo_lim_especial:
                            self.saldo_lim_especial -= valor_restante  
                        else:
                            print("Saldo insuficiente, incluindo o limite de cheque especial!")
                            return

                    print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
                    print(f"Saldo atual: R$ {self.saldo:.2f}")
                    print(f"Limite de cheque especial restante: R$ {self.saldo_lim_especial:.2f}")
                else:
                    print(f"Saque de R$ {valor:.2f} negado, Saldo insuficiente!")
            else:
                print("Valor inválido!")

    def resumo(self):
        super().resumo()
        print(f"# Saldo cheque especial: R$ {self.saldo_lim_especial:.2f}")
        print("#--------------------")
        print(f"# Taxa de manutenção: {self.taxa_manutencao}% ")
        print(f"# Limite de cheque especial: R$ {self.limite_cheque_especial:.2f}")
        print(f"#\n################")


class ContaPoupanca(Conta):
    def __init__(self, numero_conta, titular):
        super().__init__(numero_conta, titular)
        self.taxa_juros = 0.005 # TAXA DE JUROS VAI DIRETO NA CLASSE, POIS QUEM DEFINE A TX É O BCB. ( TX EM 30/11 = 0,5 a.m)

    def adicionar_juros(self):
        juros = self.saldo * self.taxa_juros
        self.saldo += juros
        print(f"Juros de R$ {juros:.3f} adicionados ao saldo!")

    def resumo(self):
        super().resumo()
        print(f"# Taxa de juros: {self.taxa_juros * 100}% ao mês")
        print(f"#\n################")

conta_corrente = ContaCorrente(11111, "Pedro", 3 ,1000)
conta_poupanca = ContaPoupanca(99999, "Sakura")

print("\n--- Conta Corrente ---")
conta_corrente.depositar(599) # DEPOSITA

conta_corrente.sacar(499) # SALDO DE 100 E NÃO UTILIZA O CHEQUE

conta_corrente.sacar(399) # SALDO DE 0 E RETIRA 299 DO CHEQUE

conta_corrente.sacar(29) # SALDO DE 0 E RETIRA 29 DO CHEQUE

conta_corrente.depositar(800) # COBRE O CHE_ESPECIAL E SOMA O RESTANTE NO SALDO DA CONTA
conta_corrente.depositar(700) # SOMA NO SALDO DA CONTA

conta_corrente.sacar(2000) # SALDO ATUAL ERA DE 1148... IRA TIRAR A DIFERENÇA DO CHQ_ESPECIAL (852,00), FICANDO 148 DE LIMITE ESPECIAL
conta_corrente.depositar(100) # TESTE PARA COBRIR PARCIALMENTE O LIMITE ESPECIAL COM O DESCONTO DA TX MANUTENÇÃO.

conta_corrente.resumo()

print("\n--- Conta POUPANÇA ---")
conta_poupanca.depositar(100) 
conta_poupanca.adicionar_juros() # SIMULA UM MÊS DE JUROS
conta_poupanca.adicionar_juros() # SIMULA UM MÊS DE JUROS SOBRE SALDO PASSADO
conta_poupanca.adicionar_juros() # SIMULA UM MÊS DE JUROS SOBRE SALDO PASSADO
conta_poupanca.adicionar_juros() # SIMULA UM MÊS DE JUROS SOBRE SALDO PASSADO
conta_poupanca.sacar(15)
conta_poupanca.adicionar_juros() # SIMULA UM MÊS DE JUROS SOBRE SALDO PASSADO
conta_poupanca.depositar(100)
conta_poupanca.depositar(100)
conta_poupanca.adicionar_juros() # SIMULA UM MÊS DE JUROS SOBRE SALDO PASSADO
conta_poupanca.adicionar_juros() # SIMULA UM MÊS DE JUROS SOBRE SALDO PASSADO
conta_poupanca.adicionar_juros() # SIMULA UM MÊS DE JUROS SOBRE SALDO PASSADO
conta_poupanca.adicionar_juros() # SIMULA UM MÊS DE JUROS SOBRE SALDO PASSADO
conta_poupanca.depositar(100) 
conta_poupanca.adicionar_juros() # SIMULA UM MÊS DE JUROS SOBRE SALDO PASSADO
conta_poupanca.adicionar_juros() # SIMULA UM MÊS DE JUROS SOBRE SALDO PASSADO
print('\n')
conta_poupanca.resumo()

    

        