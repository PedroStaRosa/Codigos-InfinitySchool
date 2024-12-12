from classes.Pessoa import Pessoa

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
    