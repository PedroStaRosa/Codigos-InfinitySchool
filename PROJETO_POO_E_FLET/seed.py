from classes.Quarto import Quarto
from classes.Cliente import Cliente
from classes.Reserva import Reserva
from classes.GerenciadorDeReservas import GerenciadorDeReservas

hotel = GerenciadorDeReservas()

def seed():
    quarto1 = Quarto(101,"Luxo",500)
    quarto2 = Quarto(102,"Standard",250)
    quarto3 = Quarto(103,"Luxo",500)
    quarto4 = Quarto(104,"Standard",250)
    quarto5 = Quarto(105,"Presidencial",990)
    quarto6 = Quarto(106,"Presidencial",990)
    quarto7 = Quarto(107,"Ventilador",50.99)
    quarto8 = Quarto(108,"Duplo",199)
    quarto9 = Quarto(109,"Presidencial",990)
    quarto10 = Quarto(110,"Master Bluster",1990)
    
    
    hotel.criar_quarto(quarto1)
    hotel.criar_quarto(quarto2)
    hotel.criar_quarto(quarto3)
    hotel.criar_quarto(quarto4)
    hotel.criar_quarto(quarto5)
    hotel.criar_quarto(quarto6)
    hotel.criar_quarto(quarto7)
    hotel.criar_quarto(quarto8)
    hotel.criar_quarto(quarto9)
    hotel.criar_quarto(quarto10)
    
    cliente = Cliente("Pedro","819989839","pedro@pedro.com",123)
    cliente2 = Cliente("Maria","819985239","maria@maria.com",124)
    
    reserva = Reserva(cliente,quarto7,"21/11/2024","31/12/2024","Pago")
    quarto7.set_avaliable()
    hotel.criar_reserva(reserva)
    
    reserva2 = Reserva(cliente2,quarto10,"21/12/2024","31/12/2024","Pendente")
    quarto10.set_avaliable()
    hotel.criar_reserva(reserva2)
    
    hotel.cadastar_cliente(cliente)
    

    for quarto in hotel.quartos:
        print(f"numero: {quarto.numero_quarto}, status {quarto.avaliable}")
