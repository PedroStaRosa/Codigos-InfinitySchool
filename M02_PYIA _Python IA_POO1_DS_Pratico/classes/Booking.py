# reserva.py

from datetime import datetime
from classes.Room import Room

class Booking:
    def __init__(self, room: Room, client: str, date_checkin: str, date_checkout: str, is_available: bool):
        self.room = room
        self.client = client
        self.date_checkin = datetime.strptime(date_checkin, "%d/%m/%Y") #GPT
        self.date_checkout = datetime.strptime(date_checkout, "%d/%m/%Y") #GPT
        self.room.available = is_available

    def calcular_total(self):
        dias = (self.date_checkout - self.date_checkin).days
        total = dias * self.room.price_diary
        return {"TOTAL": total, "DIAS": dias }

    def __str__(self):
        calc = self.calcular_total()

        return (f"Reserva de {self.client}, Quarto: {self.room.number}, "
                f"Check-in: {self.date_checkin.strftime('%d/%m/%Y')}, " #GPT
                f"Check-out: {self.date_checkout.strftime('%d/%m/%Y')}, " #GPT
                f"Dias: {calc["DIAS"]} dias , "
                f"Total: R$ {calc["TOTAL"]:.2f}")
