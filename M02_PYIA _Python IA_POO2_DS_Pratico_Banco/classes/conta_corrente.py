from conta import Conta

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