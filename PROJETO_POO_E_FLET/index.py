import flet as ft
from seed import seed

from pages.home import tela_home
from pages.cadastro_cliente import tela_cadastro
from pages.reserva import tela_reserva

def main(page: ft.Page):
    
    page.title = "Sistema de Gerenciamento de Reservas"
    page.scroll = "always"
    # page.window_full_screen = True
    page.window_width = 1920 
    page.window_height = 1080 


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
            
        elif page.route.startswith("/reserva"):
            mostrar_tela(tela_reserva)

    # Definir o evento de mudança de rota
    page.on_route_change = on_route_change

    # Inicializar com a tela Home
    page.go("/home")

# Inicializando o Flet
seed()
ft.app(target=main)