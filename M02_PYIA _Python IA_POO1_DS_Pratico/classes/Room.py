class Room:
    def __init__(self, number: int, type: str, price_diary: float, available: bool = True):
        self.number = number
        self.type = type
        self.price_diary = price_diary
        self.available = available

    def __str__(self):
        status = "Disponível" if self.available else "Ocupado"
        return f"Quarto {self.number} - {self.type}, Preço: R${self.price_diary:.2f} - {status}"
