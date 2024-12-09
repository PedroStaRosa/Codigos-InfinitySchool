import flet as ft
import datetime
from classes.GerenciadorDeReservas import GerenciadorDeReservas
from classes.Quarto import Quarto
from classes.Cliente import Cliente
from classes.Reserva import Reserva

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

    

def main(page: ft.Page):
    
    seed()
    
    
    page.title = "Sistema de Gerenciamento de Reservas"
    page.scroll = "always"
    page.window.left = 400
    page.window.top = 200

    # Navegação entre as telas
    # def go_to(screen):
    #     # for view in [home_view, reservas_view, formulario_reserva_view, clientes_view]:
    #     for view in [home_view]:
    #         view.visible = False
    #     screen.visible = True
    #     page.update()

    # def page_home(e: ft.ControlEvent, paginal_atual):
    #     print(e.page)
    #     page.update()
    #     page.remove(paginal_atual)
    #     page.add(home_view)
    
    # def cad_cliente(e: ft.ControlEvent):
    #     print(e.page)
    #     page.remove(home_view)
    #     page.add(clientes_view)
    #     page.update()
        
    # def page_reservas(e: ft.ControlEvent):
    #     page.remove(home_view)
    #     page.add(formulario_reserva_view)
    #     page.update()
    
        # Função para navegar entre as páginas
    def navigate_to(view):
        page.controls.clear()  # Remove todos os controles da página
        page.controls.append(view)  # Adiciona a nova visualização
        page.update()

    # Definir ações para os botões
    # def page_home(e,paginal_atual):
    #     navigate_to(home_view)
    
    def home_layout():
        return home_view.controls.extend([
            ft.Row([
                ft.Card(expand=1,
                    content=ft.Column([
                        ft.Text(
                            "  Disponíveis", size=50,
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
                        ),
                    ])
                ),
                ft.Card(expand=1,
                    content=ft.Column([
                        ft.Text(
                            "  Reservados", size=50,
                            color=ft.Colors.RED_700,
                            weight=ft.FontWeight.BOLD,
                            italic=True,
                        ),
                        ft.Container(
                            content=ft.ListView(
                                controls=quartos_reservados(),
                                spacing=10,
                            ),
                            height=200,
                            padding=20,
                        ),
                    ])
                ),
            ]),
            ft.Container(
                content=ft.ListView(
                    controls=clientes_cadastrados(),
                    spacing=10,
                ),
                height=200,
                padding=20
            ),
            ft.Row(controls=[
                ft.ElevatedButton(
                    text="Clientes", width=150, height=50,
                    color=ft.Colors.WHITE, bgcolor=ft.Colors.BLUE_900,
                    on_click=lambda e: cad_cliente(e)
                ),
                ft.ElevatedButton(
                    text="Reservas", width=150, height=50,
                    color=ft.Colors.WHITE, bgcolor=ft.Colors.BLUE_900,
                    on_click=lambda e: page_reservas(e)
                ),
            ]),
        ])
    
    def page_home(e, paginal_atual):
    # Atualiza os componentes dinâmicos da home
        home_view.controls.clear()
        home_layout()
        # Navega para a home atualizada
        navigate_to(home_view)

    def cad_cliente(e):
        navigate_to(clientes_view)

    def page_reservas(e):
        navigate_to(formulario_reserva_view)

    def quartos_disponiveis():
        quartos = []
        
        for quarto in hotel.quartos:
            if quarto.avaliable:
                quartos.append(ft.Row([
                    ft.FilledButton("Reservar",bgcolor=ft.Colors.GREEN_400, icon="add", on_click=lambda e, quarto=quarto: handle_criar_reserva(e, quarto)),
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
    
    def handle_criar_reserva(e: ft.ControlEvent, quarto):
        page.remove(home_view)
        page.add(room_view)
       
        numero_quarto.value = quarto.numero_quarto
        print(f"Reserva solicitada para o quarto {quarto.numero_quarto}")
        page.update()
    
    def handle_change(e):
        print(f"Date changed: {e.control.value.strftime('%d/%m/%Y')}")
        # page.add(ft.Text(f"Date changed: {e.control.value.strftime('%d/%m/%Y')}"))

    def handle_dismissal(e):
        page.add(ft.Text(f"DatePicker dismissed"))
    
    def clientes_cadastrados():
        clientes = []
        
        for cliente in hotel.clientes:
            clientes.append( ft.Text(f"ID: {cliente.id}: Nome: {cliente.nome}, Fone: {cliente.telefone}, Email: {cliente.email}"))
        
        return clientes
    
    # Tela Inicial
    home_view =ft.Column( controls=[
        ft.Row([
            ft.Card(expand=1,
                
            content=ft.Column([
                ft.Text("  Disponiveis",size=50,
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
                        ft.Text("  Reservados",size=50,
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
        ft.Container(
                content=ft.ListView(
                            controls=clientes_cadastrados(),
                            spacing=10,
                        
                ),
                height=200,
                padding=20
               
            ),
        ft.Row(controls=[
            ft.ElevatedButton(text="Clientes" ,width=150, height=50,color=ft.Colors.WHITE,bgcolor=ft.Colors.BLUE_900,on_click=lambda e: cad_cliente(e)),
            ft.ElevatedButton(text="Reservas",width=150, height=50,color=ft.Colors.WHITE,bgcolor=ft.Colors.BLUE_900, on_click=lambda e: page_reservas(e)),
                ])
    ] )
    

    # Tela de Visualização de Reservas
    
    tb_cliente_id = ft.TextField(label="ID", value=1, disabled=True)
    tb_cliente_nome = ft.TextField(label="Nome")
    tb_cliente_fone = ft.TextField(label="Telefone")
    tb_cliente_email = ft.TextField(label="Email")
    resultado = ft.Text()
    
    def cadastrar_cliente(e):
        resultado.value = f"ID: {tb_cliente_id.value}, Nome: {tb_cliente_nome.value}, Fone: {tb_cliente_fone.value}, Email: {tb_cliente_email.value}"
        novo_cliente = Cliente(tb_cliente_nome.value,tb_cliente_fone.value,tb_cliente_email.value,tb_cliente_id.value)
        hotel.cadastar_cliente(novo_cliente)
        # TESTE DE CADASTRADO
        clientes = hotel.clientes
        for cliente in clientes:
            print(cliente.nome)
        page.update()
    
    clientes_view = ft.Column(
        [
            ft.Text("Cadastro de clientes.",
                        size=50,
                        color=ft.Colors.GREEN_700,
                        weight=ft.FontWeight.BOLD,
                        italic=True,),
            ft.ListView(
                [
                    ft.Column(
                        [
                          tb_cliente_id, tb_cliente_nome, tb_cliente_fone, tb_cliente_email
                        ]
                    )
                ],
                
            ),
            resultado,
            ft.ElevatedButton("Cadastrar", on_click=cadastrar_cliente),
            ft.ElevatedButton("Voltar", on_click=lambda e: page_home(e,clientes_view)),
        ],
    )

    # Formulário de Reserva
    formulario_reserva_view = ft.Column(
        [
            ft.Text("Formulário de Reserva", style="headlineMedium"),
            ft.Dropdown(
                label="Escolha o Cliente",
                options=[ft.dropdown.Option("Cliente A"), ft.dropdown.Option("Cliente B")],
            ),
            ft.Dropdown(
                label="Escolha o Quarto",
                options=[ft.dropdown.Option(f"Quarto {i+1}") for i in range(5)],
            ),
           ft.ElevatedButton(
            "Check-in",
            icon=ft.Icons.CALENDAR_MONTH,
            on_click=lambda e: page.open(
                ft.DatePicker(
                    first_date=datetime.datetime(year=2024, month=12, day=6),
                    last_date=datetime.datetime(year=2026, month=10, day=1),
                    on_change=handle_change,
                    on_dismiss=handle_dismissal,
                )
            ),
        ),
           ft.ElevatedButton(
            "Check-out",
            icon=ft.Icons.CALENDAR_MONTH,
            on_click=lambda e: page.open(
                ft.DatePicker(
                    first_date=datetime.datetime(year=2024, month=12, day=6),
                    last_date=datetime.datetime(year=2026, month=10, day=1),
                    on_change=handle_change,
                    # on_dismiss=handle_dismissal,
                )
            )),
            ft.ElevatedButton("Reservar", on_click=lambda _: print("Reserva criada")),
            ft.ElevatedButton("Voltar", on_click=lambda e: page_home(e,formulario_reserva_view)),
        ],
    )
    
    numero_quarto = ft.Text()
    
    room_view = ft.Column(
        [
            ft.Text("Detalhes do Quarto"),
            ft.ListView(
                [
                    ft.Row(
                        [
                          numero_quarto
                        ]
                    )
                ],
                height=200,
            ),
            ft.ElevatedButton("Voltar", on_click=lambda e: page_home(e,room_view)),
        ],
    )
    
    
    # Adicionando telas à página
    page.add(home_view)


# Executa a aplicação
ft.app(target=main)
