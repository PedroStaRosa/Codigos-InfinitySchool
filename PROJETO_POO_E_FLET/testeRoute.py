import flet as ft

def main(page: ft.Page):
    # Define a rota inicial
    page.title = "Flet URL Parameters"
    page.route = "/"

    # Callback para navegar entre as páginas
    def route_change(e):
        # Rota para a página inicial
        if page.route == "/":
            page.views.clear()
            numero = ft.TextField("Digite um número:")
            page.views.append(
                ft.View(
                    "/",
                    controls=[
                        ft.Text("Página Inicial"),
                        numero ,
                        ft.ElevatedButton(
                            text="Ir para Página 2",
                            on_click=lambda _: page.go(
                                f"/page2?number={numero.value}"
                            ),
                        ),
                    ],
                )
            )
        # Rota para a segunda página
        elif page.route.startswith("/page2"):
            # Obtendo o número da URL
            params = page.query.get("number")
            print(params)
            number = params
            page.views.clear()
            page.views.append(
                ft.View(
                    "/page2",
                    controls=[
                        ft.Text("Página 2"),
                        ft.Text(f"Número recebido: {number}"),
                        ft.ElevatedButton(
                            text="Voltar para a Página Inicial",
                            on_click=lambda _: page.go("/"),
                        ),
                    ],
                )
            )

        # Atualizar a interface
        page.update()

    # Callback para navegação do histórico
    def view_pop(e):
        page.views.pop()
        page.go(page.views[-1].route)

    # Configurar os callbacks
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # Inicializar o aplicativo
    page.go(page.route)

# Iniciar o app
ft.app(target=main)