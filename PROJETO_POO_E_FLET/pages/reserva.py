import flet as ft
import datetime
from classes.Reserva import Reserva

from seed import hotel

def tela_reserva(page: ft.Page):
    
    def ir_para_home(e):
        page.go("/home")
    
    def fetch_client_by_id(cliente_id):
        
        for cliente in hotel.clientes:
            if cliente.id == int(cliente_id):
                print(cliente)
                return cliente
        else:
            return None
    
    cliente_info = ft.Text()
    def handle_cliente_by_id(e):
        cliente_selec = fetch_client_by_id(cliente_id.value)
        
        if cliente_selec:  
            print("cleienteee " , cliente_selec.nome)
                # Atualiza o texto do controle com as informações do cliente
            cliente_info.value = f"{cliente_selec.nome} - {cliente_selec.telefone} - {cliente_selec.email}"
            cliente_info.color = ft.Colors.BLACK87
        else:
            cliente_info.value = f"Cliente de Id {cliente_id.value} não encontrado"
            cliente_info.color = ft.Colors.RED_400
            
        if cliente_info not in page.controls:
            page.add(cliente_info)
        
        page.update()  # Atualiza a página para refletir as mudanças        
    quarto_reserva = page.query.get("quarto")
    quarto_encontrado = next((quarto for quarto in hotel.quartos if str(quarto.numero_quarto) == quarto_reserva), None)

    if quarto_encontrado:
        print(f"Diaria: {quarto_encontrado.preco_diaria}, tipo: {quarto_encontrado.tipo_quarto}")
    else:
        print("Quarto não encontrado")
        
    cliente_id = ft.TextField(label="Codigo do cliente")
    cliente_layout = ft.Container( content=ft.Row([ cliente_id, ft.IconButton(
                icon=ft.Icons.SEARCH,
                icon_color="blue400",
                icon_size=20,
                on_click=handle_cliente_by_id
            )]))
    
    checkin_date = ft.Text()
    def handle_change_checkin(e):
        checkin_date.value = f"{e.control.value.strftime('%d/%m/%Y')}"
        page.update(checkin_date)
    
    checkout_date = ft.Text()
    def handle_change_checkout(e):
        checkout_date.value = f"{e.control.value.strftime('%d/%m/%Y')}"
        page.update(checkout_date)
    
    
    checkin = ft.ElevatedButton(
        "Checkin",
        icon=ft.Icons.CALENDAR_MONTH,
        on_click=lambda e: page.open(
            ft.DatePicker(
                first_date=datetime.datetime(year=2023, month=10, day=1),
                last_date=datetime.datetime(year=2025, month=10, day=1),
                on_change=handle_change_checkin,

            )
        ))
    checkout = ft.ElevatedButton(
        "Checkout",
        icon=ft.Icons.CALENDAR_MONTH,
        on_click=lambda e: page.open(
            ft.DatePicker(
                first_date=datetime.datetime(year=2023, month=10, day=1),
                last_date=datetime.datetime(year=2025, month=10, day=1),
                on_change=handle_change_checkout,

            )
        ))
    
    def test(e):

        if checkout_date.value == None:
            print("Preencha data de checkout")
        elif checkin_date.value == None:
            print("Preencha data de checkin")
        else:
            print(checkout_date.value , "   ", checkin_date.value)
            
    def handle_booking(e):
        print("Reserva")
        cliente = fetch_client_by_id(cliente_id.value)
        if cliente:
            print("Cliente ", cliente.nome)
            print(f"Quarto {quarto_encontrado.numero_quarto}, tipo: {quarto_encontrado.tipo_quarto}, diaria {quarto_encontrado.preco_diaria}")
            print("Checkin", str(checkin_date.value))
            print("Checkout", str(checkout_date.value))
            
            nova_reserva = Reserva(cliente, quarto_encontrado,str(checkin_date.value),str(checkout_date.value))
            print(nova_reserva)
            quarto_encontrado.set_avaliable()
            hotel.criar_reserva(nova_reserva)
        else:
            print("Dados invalidos")
        for reserva in hotel.reservas:
            print(f"Cliente: {reserva.cliente.nome} - Quarto {reserva.quarto_reservado.numero_quarto} | Tipo: {reserva.quarto_reservado.tipo_quarto} | Checkout: {reserva.checkin.strftime("%d/%m")} - {reserva.chekout.strftime("%d/%m")}")

        # nova_reserva = Reserva()
        
    page.add(
        ft.Text(f"Quarto selecionado {quarto_reserva}"),
        cliente_layout,
        cliente_info,
        ft.Row([checkin,checkout,]),
        ft.Row([checkin_date, checkout_date]),
        ft.ElevatedButton("Testar", on_click=test),
        ft.ElevatedButton("Reservar", on_click=handle_booking),
        ft.ElevatedButton("Voltar para Home", on_click=ir_para_home)
    )