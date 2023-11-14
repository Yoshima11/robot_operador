import sys
import argparse #para ingresar argumentos al iniciar el programa
import time
from datetime import datetime
import pandas as pd
import simplejson as sj
import matplotlib.pyplot as plt
import pyRofex as pr
from conexion import conectar
from datos_ticker import datos_ticker

# recibe argumentos al ejecutar el programa.
parser = argparse.ArgumentParser(description='Robot de trading para Matba Rofex')
parser.add_argument('-t','--ticker')
parser.add_argument('-u','--user')
parser.add_argument('-a','--account')
parser.add_argument('-p','--password')
parser.add_argument('-e','--environment', help='Environment LIVE or REMARKET. Por defecto es REMARKET')
args = parser.parse_args()

conectar(
    user=args.user,
    password=args.password,
    account=args.account,
    environment=args.environment,
)

while True:
    try:
        datos = datos_ticker(args.ticker)
        print(datos)
        time.sleep(1)
        input('<Enter> para continuar o <Ctrl+C> para salir')
    except KeyboardInterrupt:
        print("Saliendo...")
        break
