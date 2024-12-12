import flet as ft
from classes.Cliente import Cliente
from seed import hotel

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
