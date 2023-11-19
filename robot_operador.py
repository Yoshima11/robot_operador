'''flet módulo para crear ventanas'''
import threading
import time
import json
import flet as ft
import api_iol

access_token = ''
refresh_token = ''

def main(page: ft.Page):
    '''Ventana de la app'''
    page.title = 'Robot Operador'
    dlg_error = ft.AlertDialog(
        title=ft.Text("Request token error: invalid username or password."),
    )
    def dis_log_controls():
        '''Desactiva los campos del login una vez conseguido el access token'''
        user.value = ''
        password.value = ''
        user.disabled = True
        password.disabled = True
        get_token.disabled = True
        token_status.value = '---[IOL token request accepted.]---'
        token_status.color = ft.colors.GREEN
        page.update()
    def refresh_iol():
        '''Cada 15 min actualiza token'''
        global access_token
        global refresh_token
        while True:
            time.sleep(900)
            res = api_iol.ref_token(refresh_token)
            tokens = res.json()
            access_token = tokens['access_token']
            refresh_token = tokens['refresh_token']
    def access_iol(e):
        '''solicita token por primera vez'''
        global access_token
        global refresh_token
        res = api_iol.req_token(user.value, password.value)
        if res.status_code==200: #200: solicitud token aceptada.
            dis_log_controls()
            token = res.json()
            access_token = token['access_token']
            refresh_token = token['refresh_token']
            page.update()
            refresh = threading.Thread(target=refresh_iol) #solicitar refresh token cada 15 min.
            refresh.start()
        else: #401 es el código si los datos no son correctos.
            token_status.value = '---[IOL token request rejected.]---'
            token_status.color = ft.colors.RED
            page.dialog = dlg_error
            dlg_error.open = True
            page.update()

    user = ft.TextField(label='user name:')
    password = ft.TextField(label='user password', password=True, can_reveal_password=True)
    get_token = ft.ElevatedButton(text='request iol token', on_click=access_iol)
    token_status = ft.Text()
    mensaje = ft.Text()
    row1 = ft.Row(
        controls=[
            user,
            password,
            get_token,
        ],
    )
    row2 = ft.Row(
        controls=[
            token_status,
        ]
    )
    row3 = ft.Row(
        controls=[
           mensaje,
        ],
    )
    col = ft.Column(
        controls=[
            row1,
            row2,
            row3,
        ],
    )
    page.add(
        col
    )
ft.app(port=8550, target=main, view=ft.AppView.WEB_BROWSER)
