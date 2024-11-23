class Employee:
    def __init__(self, name: str, function: str, salary: float):
        self.name = name
        self.function = function
        self.salary = salary

    def __str__(self):
        return f"Nome: {self.name}, Função: {self.function}, Salário: R${self.salary:.2f}"
