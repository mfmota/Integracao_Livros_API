import flet as ft  
import requests
from connect import get_livros
from urllib.parse import urlparse, parse_qs
def main(page: ft.Page):
    page.tittle = "Livros"
    page.window_width = 400

    def home_page():
        nome_input = ft.TextField(label="Nome do Livro",text_align=ft.TextAlign.LEFT)

        streaming_select = ft.Dropdown(
            options= [
                ft.dropdown.Option("AK", text="Amazon Kindle"),
                ft.dropdown.Option("F", text="Físico")
            ],
            label ="Selecione a streaming"
        )

        lista_livros = ft.ListView()

        def carregar_livros():
            lista_livros.controls.clear()

            for i in get_livros():
                lista_livros.controls.append(
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text(i['nome'], weight=ft.FontWeight.BOLD),     
                            ],
                            spacing=5,
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        bgcolor=ft.colors.BLACK12,
                        padding=15,
                        alignment=ft.alignment.center,
                        margin=3,
                        border_radius=10,
                        on_click=lambda e, livro_id=i['id']: page.go(f'/review?id={livro_id}')
                    )
                )
            page.update()

        def cadastrar(e):
            data = {
                'nome': nome_input.value,
                'streaming': streaming_select.value,
                'categorias': []
            }
            requests.post('http://127.0.0.1:8000/api/livros/', json=data)
            carregar_livros()
        cadastrar_btn = ft.ElevatedButton("Cadastrar", on_click=cadastrar)

        lista_livros = ft.ListView()

        carregar_livros()
        page.views.append(
            ft.View(
                "/",
                controls=[
                    nome_input,
                    streaming_select,
                    cadastrar_btn,
                    lista_livros,
                ]
            )
        )



    def review_page(livro_id):

        try:
            response = requests.get(f'http://127.0.0.1:8000/api/livros/id/{livro_id}')
            if response.status_code == 200:
                livro_data = response.json() 
                nome = livro_data.get("nome")  
                nota = livro_data.get("nota",0)
                comentarios = livro_data.get("comentarios","")
            else:
                nome = "Erro ao carregar livro"
                nota = 0
                comentarios = ""
        except Exception as ex:
            nome = f"Erro de conexão: {ex}"
            nota = 0
            comentarios = ""
        nota_input = ft.TextField(label="Nota:0-5", text_align=ft.TextAlign.LEFT, value=str(nota), width=100)
        comentario_input = ft.TextField(label="Comentário", multiline=True, expand=True, value=comentarios)

        def avaliar(e):
            data = {
            'nota': int(nota_input.value),
            'comentarios': comentario_input.value
            }

            try:
                response = requests.put(f'http://127.0.0.1:8000/api/livros/{livro_id}', json=data)
                if response.status_code == 200:
                    page.snack_bar = ft.SnackBar(ft.Text("Avaliação enviada com sucesso!"))
                    page.snack_bar.open = True
                    page.update()
                    page.go('/')
                else:
                    page.snack_bar = ft.SnackBar(ft.Text("Erro ao enviar a avaliação."))
                    page.snack_bar.open = True
            except Exception as ex:
                page.snack_bar = ft.SnackBar(ft.Text(f"Erro de conexão: {ex}"))
                page.snack_bar.open = True

        page.update()

        avaliar_btn = ft.ElevatedButton("Avaliar", on_click=avaliar)
        voltar_btn = ft.ElevatedButton("Voltar", on_click=lambda _: page.go('/'))
        page.views.append(
            ft.View(
                "/review",
                controls=[
                    ft.Text(f"Detalhes do livro : {nome}"),
                    nota_input,
                    comentario_input,
                    avaliar_btn,
                    voltar_btn
                ]
            )
        )


    def route_change(e):
        page.views.clear()
        if page.route == "/":
            home_page()
        elif page.route.startswith( '/review'):
            parsed_url = urlparse(page.route)
            query_params = parse_qs(parsed_url.query)
            livro_id = query_params.get('id', [None])[0]
            review_page(livro_id)

        page.update()
        
    

    page.on_route_change = route_change
    page.go('/')

ft.app(target=main)