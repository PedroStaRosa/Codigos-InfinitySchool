import flet as ft
from classes.GerenciadorDeReservas import GerenciadorDeReservas 

from seed import hotel

def tela_home(page: ft.Page):
    def ir_para_cadastro(e):
        page.go("/cadastro")
    
    def handle_criar_reserva(quarto):
        page.go(f"/reserva?quarto={quarto.numero_quarto}")

    lista_clientes = ft.ListView(controls=[], spacing=10, padding=20)
    image = ft.Row( [ft.Image(
                src=f"https://static.vecteezy.com/system/resources/thumbnails/008/009/875/small_2x/panoramic-holiday-landscape-luxurious-beach-resort-hotel-swimming-pool-and-beach-chairs-or-loungers-under-umbrellas-with-palm-trees-blue-sunny-sky-summer-island-seaside-travel-vacation-background-photo.jpg",
                width=1200,
                height=200,
                fit=ft.ImageFit.COVER,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
            )], expand=1, wrap=False, scroll="always")
    
    for cliente in hotel.clientes:
        lista_clientes.controls.append(ft.Container(content=
                                            ft.Row([
                                                ft.Container( content=
                                                            ft.Row([
                                                                ft.IconButton(
                                                                    icon=ft.Icons.EDIT,
                                                                    icon_color=ft.colors.GREEN_400,
                                                                    icon_size=20,
                                                                    ),
                                                                ft.IconButton(
                                                                    icon=ft.Icons.DELETE,
                                                                    icon_color=ft.  colors.RED_400,
                                                                    icon_size=20,
                                                                )
                                                            ])
                                                        ),
                                                ft.Text(f"ID: {cliente.id} | Nome: {cliente.nome} - {cliente.telefone} - {cliente.email}"),
                                        ], 
                                            alignment=ft.MainAxisAlignment.START)))
        
    
    def quartos_disponiveis():
        quartos = []
        
        for quarto in hotel.quartos:
            if quarto.avaliable:
                quartos.append(ft.Row([
                    ft.FilledButton("Reservar",bgcolor=ft.Colors.GREEN_400, icon="add", on_click=lambda e, quarto=quarto: handle_criar_reserva(quarto)),
                    ft.Text(f"Quarto {quarto.numero_quarto} | Tipo: {quarto.tipo_quarto} | Diaria: R$ {quarto.preco_diaria}"),
                    ]))
        return quartos
    
    def quartos_reservados():
        quartos = []
        
        for reserva in hotel.reservas:
            totais = reserva.calcular_total()

            quartos.append(
                             ft.Text(f"Cliente: {reserva.cliente.nome} - Quarto {reserva.quarto_reservado.numero_quarto} | Tipo: {reserva.quarto_reservado.tipo_quarto} | Checkout: {reserva.checkin.strftime("%d/%m")} - {reserva.chekout.strftime("%d/%m")} ({totais["DIAS"]} dias), Total a pagar: R$ {totais["TOTAL"]:.2f}")
                             )
        return quartos
    
    
    layout = ft.Column([
        image,
        ft.Row([
            ft.Card(expand=1,
                
            content=ft.Column([
                ft.Text(f"  Disponiveis {len([quarto for quarto in hotel.quartos if quarto.avaliable])}",size=50,
                            color=ft.Colors.GREEN_700,
                            weight=ft.FontWeight.BOLD,
                            italic=True,
             ),
                ft.Container(
                content=ft.ListView(
                            controls=quartos_disponiveis(),
                            spacing=10,
                        
                ),
                height=200,
                padding=20
               
            )]) 
            ),
            ft.Card(expand=1,
                content=ft.Column(
                    [
                        ft.Text(f"  Reservados {len(hotel.reservas)}",
                            size=50,
                            color=ft.Colors.RED_700,
                            weight=ft.FontWeight.BOLD,
                            italic=True,
                        ),
                        ft.Container(
                            content=ft.Column(
                            [ 
                                ft.ListView(
                                   controls= quartos_reservados(), spacing=10,
                                )
                            ], scroll= True
                        ),
                        height=200,
                        padding=20,
                        )
                    ]
                ) 
            ),
        ]
        ),
        ft.Row([ 
                ft.Card(expand=1,    
                        content=ft.Column([
                            ft.Row([ft.Text("  Clientes Cadastrados",size=50,
                                        color=ft.Colors.GREEN_700,
                                        weight=ft.FontWeight.BOLD,
                                        italic=True,
                                    ),
                                    ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=ir_para_cadastro, bgcolor=ft.Colors.GREEN_400)
                                    ]),    
                            ft.Container(
                            content=lista_clientes,
                            height=150,
                            padding=5
                        )
                        ]) 
            )       
                ]),

            ]
        )
    
    page.add(
        ft.Column([layout]),
    )