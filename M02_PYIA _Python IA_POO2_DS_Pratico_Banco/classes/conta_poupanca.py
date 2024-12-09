from conta import Conta

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