# hotel.py

from classes.Employee import Employee
from classes.Room import Room
from classes.Booking import Booking

class Hotel:
    def __init__(self, hotel_name: str):
        self.name = hotel_name
        self.employees = []
        self.rooms = []
        self.bookings = []

    def add_employee(self, employee: Employee):
        self.employees.append(employee)
        print(f"Funcionário {employee.name} adicionado com sucesso.")
    
    def rooms_seed(self):
        rooms_available = [
            Room(0, "Ventilador", 19.90),
            Room(101, "Standard", 350.00),
            Room(102, "Standard", 350.00),
            Room(103, "Luxo", 550.00),
            Room(104, "Luxo", 550.00),
            Room(105, "Luxo", 550.00),
            Room(106, "Master", 750.0,),
            Room(107, "Master", 750.00),
            Room(108, "Presidencial", 1000.00),
            Room(109, "Presidencial", 1000.00),
            Room(110, "Rei", 50000.00),
        ]
        for room in rooms_available:
            self.rooms.append(room)    
       
    def list_all_rooms(self):
        print("\nQuartos do Hotel:")
        for room in self.rooms:
            print(room)
    
    def list_all_available_rooms(self):
        print("\nQuartos disponiveis do Hotel:")
        for room in self.rooms:
            if room.available:
                print(room)

    def add_booking(self, client: str, room_number: int, date_checkin: str, date_checkout: str):

        checked_room = None
        for room in self.rooms:
            if room.number == room_number:
                if room.available:
                    checked_room = room

        if room:
            booking = Booking(checked_room, client, date_checkin, date_checkout, False)
            self.bookings.append(booking)
            print(f"Reserva realizada com sucesso para {client}.")
        else:
            print(f"Quarto {room_number} não está disponível.")

    def remove_booking(self, selected_room):

        for booking in self.bookings:
            print(booking)
            if booking.room.number == selected_room:
                self.bookings.remove(booking)
                for room in self.rooms:
                    print(room)
                    if room.number == selected_room:
                        room.available = True
                        print("Entrou" , room)
                        break
                break
        else:
            print("-> Quarto informado não esta reservado ou nao existe.")
            

    def list_employee(self):
        print("\nFuncionários do Hotel:")
        for employee in self.employees:
            print(employee)


    def list_booking(self):
        print("\nReservas do Hotel:")
        for booking in self.bookings:
            print(booking)
