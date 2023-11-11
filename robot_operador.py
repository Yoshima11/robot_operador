import time
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import pyRofex as pr

def login():
    print('Autenticación a Remarkets')
    user = input('Ingrese el usuario:')
    cuenta = input('Ingrese la cuenta:')
    password = input('Ingrese el password:')
    real = input('Entorno RAMARKET o LIVE (r/l)')
    if(real=='l' or real=='L'):
        try:
            resp = pr.initialize(
                user=user,
                password=password,
                account=cuenta,
                environment=pr.Environment.LIVE,
                active_token=token
            )
            print('Conexión establecida.')
        except:
            print('Fallo de autenticación. User o Password incorectos')
            return
    else:
        try:
            resp = pr.initialize(
                user=user,
                password=password,
                account=cuenta,
                environment=pr.Environment.REMARKET
            )
            print('Conexión establecida.')
        except:
            print('Fallo de autenticación. User o Password incorectos')
            return

login()
