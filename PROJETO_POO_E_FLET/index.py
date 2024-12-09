import flet as ft
import datetime
from classes.GerenciadorDeReservas import GerenciadorDeReservas
from classes.Quarto import Quarto
from classes.Cliente import Cliente
from classes.Reserva import Reserva

# Lista para armazenar as pessoas cadastradas
pessoas_cadastradas = []
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

# Função que renderiza a tela de Cadastro
def tela_cadastro(page: ft.Page):
    def cadastrar_pessoa(e):
        novo_cliente = Cliente(nome_input.value, telefone_input.value, email_input.value, id_user.value)
        hotel.cadastar_cliente(novo_cliente)
        page.go("/home")

    def ir_para_home(e):
        page.go("/home")
        
    nome_input = ft.TextField(label="Nome", autofocus=True)
    telefone_input = ft.TextField(label="Telefone")
    email_input = ft.TextField(label="Email")
    generate_id_user = len(hotel.clientes) + 1
    id_user = ft.TextField(label="ID", value=generate_id_user, disabled=True)
    cadastrar_button = ft.ElevatedButton("Cadastrar", on_click=cadastrar_pessoa)

    page.add(
        id_user,
        nome_input,
        telefone_input,
        email_input,
        cadastrar_button,
        ft.ElevatedButton("Voltar", on_click=ir_para_home)
    )

# Função que renderiza a tela inicial (Home)
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
                fit=ft.ImageFit.NONE,
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
        
        ft.ElevatedButton("Ir para Outra Tela", on_click=lambda e: page.go("/outra"))
    )
    
# Função para a tela adicional
def tela_outra(page: ft.Page):
    def ir_para_home(e):
        page.go("/home")

    page.add(
        ft.Text("Esta é outra tela!"),
        ft.ElevatedButton("Voltar para Home", on_click=ir_para_home)
    )
    
def tela_reserva(page: ft.Page):
    
        def ir_para_home(e):
            page.go("/home")
            
        quarto_reserva = page.query.get("quarto")
        quarto_encontrado = next((quarto for quarto in hotel.quartos if str(quarto.numero_quarto) == quarto_reserva), None)

        if quarto_encontrado:
            print(f"Diaria: {quarto_encontrado.preco_diaria}, tipo: {quarto_encontrado.tipo_quarto}")
        else:
            print("Quarto não encontrado")
        
        page.add(
        ft.Text(f"Quarto selecionado {quarto_reserva}"),
        ft.ElevatedButton("Voltar para Home", on_click=ir_para_home)
    )

# Função principal que inicializa a aplicação
def main(page: ft.Page):
    
    page.title = "Sistema de Gerenciamento de Reservas"
    page.scroll = "always"
    page.window.left = 400
    page.window.top = 200
    
    # Função de navegação centralizada
    def mostrar_tela(tela):
        page.clean()  # Limpa a página antes de adicionar o conteúdo
        tela(page)

    # Gerenciador de rotas
    def on_route_change(e):
        print(page.route)
        
        if page.route.startswith("/home"):
            mostrar_tela(tela_home)
            
        elif page.route.startswith("/cadastro"):
            mostrar_tela(tela_cadastro)
            
        elif page.route.startswith("/outra"):
            mostrar_tela(tela_outra)
            
        elif page.route.startswith("/reserva"):
            mostrar_tela(tela_reserva)

    # Definir o evento de mudança de rota
    page.on_route_change = on_route_change

    # Inicializar com a tela Home
    page.go("/home")

# Inicializando o Flet
seed()
ft.app(target=main)