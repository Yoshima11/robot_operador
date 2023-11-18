'''flet módulo para crear ventanas'''
import flet as ft
import api_iol

def main(page: ft.Page):
    '''Ventana de la app'''
    page.title = 'Robot Operador'
    def connect_iol(e):
        token = api_iol.connect_iol(user.value, password.value)
        access_token = token['access_token']
        refresh_token = token['refresh_token']
        print(access_token)
    user = ft.TextField(label='user name:')
    password = ft.TextField(label='user password', password=True, can_reveal_password=True)
    get_token = ft.ElevatedButton(text='connect', on_click=connect_iol)
    row1 = ft.Row(
        controls=[
            user,
            password,
            get_token,
        ],
    )
    col = ft.Column(
        controls=[
            row1,
        ],
    )
    page.add(
        col
    )
ft.app(port=8550, target=main, view=ft.AppView.WEB_BROWSER)
