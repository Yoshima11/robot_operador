import sys
import argparse #para ingresar argumentos al iniciar el programa
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
parser.add_argument('-e','--environment', help='Environment LIVE or REMARKET. Por defecto es REMARKET')
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

def market_data_handler(message):
    print("Market Data Message Received: {0}".format(message))
    global mensaje
    mensaje = message
def order_report_handler(message):
    print("Order Report Message Received: {0}".format(message))
def error_handler(message):
    print("Error Message Received: {0}".format(message))
def exception_handler(e):
    print("Exception Occurred: {0}".format(e.message))

# Initiate Websocket Connection
pr.init_websocket_connection(
    market_data_handler=market_data_handler,
    order_report_handler=order_report_handler,
    error_handler=error_handler,
    exception_handler=exception_handler,
)

datos_ticker = [
    pr.MarketDataEntry.BIDS,
    pr.MarketDataEntry.OFFERS,
    pr.MarketDataEntry.LAST,
]
lista_tickers = [args.ticker]

pr.market_data_subscription(
    tickers=lista_tickers,
    entries=datos_ticker,
)

input('apreta enter')
pr.close_websocket_connection()
