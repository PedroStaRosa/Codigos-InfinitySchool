Aqui está a documentação do código adaptada para o formato de um README:

---

# Sistema de Contas Bancárias

Este projeto implementa um sistema simples de contas bancárias em Python, com diferentes tipos de contas: Conta Corrente e Conta Poupança. A classe `Conta` serve como a base para as demais classes, compartilhando funcionalidades comuns, como depósitos, saques e exibição de saldo.

## Funcionalidades

- **Conta Corrente**: Permite a utilização de um cheque especial e cobra uma taxa de manutenção nos depósitos.
- **Conta Poupança**: Aplica juros sobre o saldo da conta mensalmente.

## Estrutura das Classes

### 1. `Conta`

A classe base que representa uma conta bancária genérica, com funcionalidades comuns para todas as contas.

#### Atributos:

- `numero_conta`: Número da conta bancária.
- `titular`: Titular da conta.
- `saldo`: Saldo da conta (inicialmente 0).

#### Métodos:

- `__init__(self, numero_conta, titular)`: Inicializa a conta com o número da conta, titular e saldo inicial.
- `depositar(self, valor)`: Realiza um depósito, desde que o valor seja positivo.
- `sacar(self, valor)`: Realiza um saque, desde que o valor seja positivo e haja saldo suficiente.
- `exibir_saldo(self)`: Exibe o saldo atual da conta.
- `resumo(self)`: Exibe um resumo da conta, incluindo o número da conta, titular e saldo.

---

### 2. `ContaCorrente` (Herda de `Conta`)

A classe `ContaCorrente` herda a classe `Conta` e adiciona funcionalidades específicas para gerenciar o limite de cheque especial e a taxa de manutenção.

#### Atributos:

- `taxa_manutencao`: Taxa de manutenção aplicada sobre o valor do depósito (em %).
- `limite_cheque_especial`: Limite de saldo do cheque especial disponível para a conta.
- `saldo_lim_especial`: Saldo disponível no cheque especial (inicialmente igual ao limite).

#### Métodos:

- `__init__(self, numero_conta, titular, taxa_manutencao, limite_cheque_especial)`: Inicializa a conta corrente com número, titular, taxa de manutenção e limite do cheque especial.
- `depositar(self, valor)`: Realiza um depósito e, se o saldo da conta for insuficiente, utiliza o cheque especial, descontando a taxa de manutenção do valor depositado.
- `sacar(self, valor)`: Realiza um saque utilizando tanto o saldo da conta quanto o limite do cheque especial, caso o saldo seja insuficiente.
- `resumo(self)`: Exibe um resumo detalhado da conta corrente, incluindo o saldo, saldo do cheque especial, taxa de manutenção e limite de cheque especial.

---

### 3. `ContaPoupanca` (Herda de `Conta`)

A classe `ContaPoupanca` herda de `Conta` e adiciona funcionalidades específicas para calcular e aplicar juros ao saldo da conta.

#### Atributos:

- `taxa_juros`: Taxa de juros aplicada ao saldo da conta (padrão de 0,5% ao mês).

#### Métodos:

- `__init__(self, numero_conta, titular)`: Inicializa a conta poupança com número da conta, titular e taxa de juros padrão.
- `adicionar_juros(self)`: Aplica a taxa de juros sobre o saldo da conta, adicionando os juros ao saldo.
- `resumo(self)`: Exibe um resumo detalhado da conta poupança, incluindo o saldo e a taxa de juros.

---

## Como Usar

### Exemplo de Execução

```python
# Criando uma conta corrente e uma conta poupança
conta_corrente = ContaCorrente(11111, "Pedro", 3, 1000)
conta_poupanca = ContaPoupanca(99999, "Sakura")

# Realizando operações na Conta Corrente
conta_corrente.depositar(599)  # Depósito
conta_corrente.sacar(499)  # Saque sem usar cheque especial
conta_corrente.sacar(399)  # Saque utilizando cheque especial
conta_corrente.depositar(800)  # Depósito que cobre o cheque especial
conta_corrente.sacar(2000)  # Saque utilizando o cheque especial
conta_corrente.depositar(100)  # Depósito parcial para cobrir o cheque especial

# Exibindo resumo da Conta Corrente
conta_corrente.resumo()

# Realizando operações na Conta Poupança
conta_poupanca.depositar(100)  # Depósito
conta_poupanca.adicionar_juros()  # Aplica juros
conta_poupanca.adicionar_juros()  # Aplica juros novamente
conta_poupanca.sacar(15)  # Saque
conta_poupanca.adicionar_juros()  # Aplica juros após saque

# Exibindo resumo da Conta Poupança
conta_poupanca.resumo()
```

### Saída Esperada:

O código realiza depósitos, saques e aplica juros nas contas, exibindo os saldos e resumos conforme a operação. O resumo inclui informações sobre o saldo da conta e, no caso da conta corrente, sobre o saldo do cheque especial e a taxa de manutenção.

---

## Como Contribuir

1. Faça um fork deste repositório.
2. Crie uma branch para a sua feature (`git checkout -b feature/nome-da-feature`).
3. Commit suas alterações (`git commit -am 'Adicionando nova feature'`).
4. Push para a branch (`git push origin feature/nome-da-feature`).
5. Abra um Pull Request.

---

## Considerações Finais

Este sistema simples simula operações bancárias básicas, incluindo a funcionalidade de cheque especial na conta corrente e aplicação de juros na conta poupança. Ele pode ser expandido para incluir mais tipos de contas, funcionalidades adicionais, como transferências e extratos bancários, e validações mais rigorosas.
