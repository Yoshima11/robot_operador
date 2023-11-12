import sys
import argparse #para ingresar datos por linea de comando
import time
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import pyRofex as pr

# recibe argumentos al ejecutar el programa.
parser = argparse.ArgumentParser(description='Robot de trading para Matba Rofex')
parser.add_argument('-t','--ticker')
parser.add_argument('-u','--user')
parser.add_argument('-a','--account')
parser.add_argument('-p','--password')
parser.add_argument('-e','--environment', help='Environment LIVE or REMARKET')
args = parser.parse_args()

#se conecta, o no.
if(str(args.environment).upper()=='LIVE'): 
    try:
        pr.initialize(
            user=args.user,
            password=args.password,
            account=args.account,
            environment=pr.Environment.LIVE,
        )
        print('Conexión establecida en el entorno LIVE.')
    except Exception as error:
        print('Fallo de autenticación del entorno LIVE.')
        print(error)
else:
    try:
        pr.initialize(
            user=args.user,
            password=args.password,
            account=args.account,
            environment=pr.Environment.REMARKET,
        )
        print('Conexión establecida en el entorno REMARKET.')
    except Exception as error:
        print('Fallo de autenticación del entorno REMARKET.')
        print(error)
