'''flet módulo para crear ventanas'''
import json
import flet as ft
import api_iol

access_token = ''
refresh_token = ''

def main(page: ft.Page):
    '''Ventana de la app'''
    page.title = 'Robot Operador'
    dlg = ft.AlertDialog(
        title=ft.Text("Request token error: User or password incorrect.")
    )
    def connect_iol(e):
        global access_token
        global refresh_token
        res = api_iol.connect_iol(user.value, password.value)
        user.value = ''
        password.value = ''
        page.update()
        if(res.status_code==200):
            user.disabled = True
            password.disabled = True
            get_token.disabled = True
            token_status.value = 'IOL token request accepted.'
            token_status.color = ft.colors.GREEN
            page.update()
            token = res.json()
            access_token = token['access_token']
            refresh_token = token['refresh_token']
        else:
            token_status.value = 'IOL token request rejected.'
            token_status.color = ft.colors.RED
            page.dialog = dlg
            dlg.open = True
            page.update()
    user = ft.TextField(label='user name:')
    password = ft.TextField(label='user password', password=True, can_reveal_password=True)
    get_token = ft.ElevatedButton(text='request iol token', on_click=connect_iol)
    token_status = ft.Text()
    row1 = ft.Row(
        controls=[
            user,
            password,
            get_token,
            token_status,
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
