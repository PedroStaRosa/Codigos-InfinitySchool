
from datetime import datetime


class Pessoa:
    def __init__(self, nome, telefone, email):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email
        
    @property
    def nome(self):
        return self.__nome
        
    @property
    def telefone(self):
        return self.__telefone
    
    def set_telefone(self, value):
        self.__telefone = value
        
    @property
    def email(self):
        return self.__email
    
    def set_email(self, value):
        self.__email = value

        
##############################################################


class Cliente(Pessoa):
    def __init__(self, nome, telefone, email, id, reserva = None):
        super().__init__(nome, telefone, email)
        self.__id = id
        self.__reserva = reserva
        
    @property    
    def id(self):
        return self.__id
    
    @property    
    def reserva(self):
        return self.__reserva


##############################################################


class Quarto:
    def __init__(self, numero_quarto,tipo_quarto,preco_diaria):
        self.__numero_quarto = numero_quarto
        self.__tipo_quarto = tipo_quarto
        self.__preco_diaria = preco_diaria
        self.__avaliable = True
        
    @property
    def numero_quarto(self):
        return self.__numero_quarto
    
    @property
    def tipo_quarto(self):
        return self.__tipo_quarto
    
    def set_tipo_quarto(self, value):
        ## VALIDADE TIPO DE QUARTOS POSSIVEIS
        if value:
            self.__tipo_quarto = value
    
    @property
    def preco_diaria(self):
        return self.__preco_diaria
    
    def set_preco_diaria(self, value):
        if value > 0:
            self.__preco_diaria = value
    
    @property
    def avaliable(self):
        return self.__avaliable
    
    def set_avaliable(self):
        # VAI INVERTER O BOLEANO NO CHECKIN E CHECKOUT
        self.__avaliable = not self.__avaliable
        
##############################################################

class Reserva:
    def __init__(self, cliente: Cliente, quarto_reservado: Quarto, checkin, chekout, status):
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
          
       
############################################################## 
        
        
class GerenciadorDeReservas:
    def __init__(self):
        self.__quartos = []
        self.__reservas= []
        self.__clientes = []

    @property
    def quartos(self): ## Verificar a disponibilidade dos quartos.
        return self.__quartos

    @property
    def reservas(self): ## Listar reserva.
        return self.__reservas

    @property
    def clientes(self): # informações de clientes.
        return self.__clientes
    
    def criar_reserva(self, nova_reserva):
        self.__reservas.append(nova_reserva)
    
    def update_reserva(self, reserva_id):
        pass
    
    def cancelar_reserva(self, reserva_id):
        pass
    
    def criar_quarto(self, quarto):
        self.__quartos.append(quarto)
        print(f"Quarto {quarto.numero_quarto} criado" )
        
    def cadastar_cliente(self, cliente: Cliente):
        self.__clientes.append(cliente)
        print(f"Cliente {cliente.id} - {cliente.nome} cadastrado com sucesso" )
    
