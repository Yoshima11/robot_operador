import sys
import argparse #para ingresar argumentos al iniciar el programa
import time
from datetime import datetime
import pandas as pd
import simplejson as sj
import matplotlib.pyplot as plt
import pyRofex as pr
from conexion import iniciar
from datos_ticker import datos_ticker

# recibe argumentos al ejecutar el programa.
parser = argparse.ArgumentParser(description='Robot de trading para Matba Rofex')
parser.add_argument('-t','--ticker')
parser.add_argument('-u','--user')
parser.add_argument('-a','--account')
parser.add_argument('-p','--password')
parser.add_argument('-e','--environment', help='Environment LIVE or REMARKET. Por defecto es REMARKET')
args = parser.parse_args()

iniciar(user=str(args.user), password=str(args.password), account=str(args.account), environment=str(args.environment))

while True:
    try:
        datos_ticker(str(args.ticker))
        time.sleep(1)
        print('Ctrl+c para salir.')

    except KeyboardInterrupt:
        print("Saliendo...")
        break
