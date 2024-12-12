from classes.Cliente import Cliente
from classes.Quarto import Quarto
from datetime import datetime

class Reserva:
    def __init__(self, cliente: Cliente, quarto_reservado: Quarto, checkin, chekout, status = "A pagar"):
        self.__cliente = cliente
        self.__quarto_reservado = quarto_reservado
        self.__checkin = datetime.strptime(checkin, "%d/%m/%Y") #GPT
        self.__chekout = datetime.strptime(chekout, "%d/%m/%Y") #GPT
        self.__status = status

    def calcular_total(self):
        dias = (self.__chekout - self.__checkin).days
        total = dias * self.__quarto_reservado.preco_diaria
        return {"TOTAL": total, "DIAS": dias }

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, value):
        self.__cliente = value

    @property
    def quarto_reservado(self):
        return self.__quarto_reservado

    @quarto_reservado.setter
    def quarto_reservado(self, value):
        self.__quarto_reservado = value

    @property
    def checkin(self):
        return self.__checkin

    @checkin.setter
    def checkin(self, value):
        self.__checkin = value

    @property
    def chekout(self):
        return self.__chekout

    @chekout.setter
    def chekout(self, value):
        self.__chekout = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

        
        
        
    