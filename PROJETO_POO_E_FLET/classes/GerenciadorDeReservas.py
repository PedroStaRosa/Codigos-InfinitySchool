from classes.Cliente import Cliente

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
    
    
