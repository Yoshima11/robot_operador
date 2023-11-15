import sys
import argparse #para ingresar argumentos al iniciar el programa
import time
import keyboard
from datetime import datetime
import pandas as pd
import simplejson as sj
import matplotlib.pyplot as plt
import pyRofex as pr

parser = argparse.ArgumentParser(description='Robot de trading para Matba Rofex') # recibe argumentos al ejecutar el programa.
parser.add_argument('-t','--ticker')
parser.add_argument('-u','--user')
parser.add_argument('-a','--account')
parser.add_argument('-p','--password')
parser.add_argument('-e','--environment', help='Environment LIVE o REMARKET. Por defecto es REMARKET')
args = parser.parse_args()

dat_inst = {}
dat_old_inst = {}
dat_ord = {}
dat_old_ord = {}

def env(env):
    if(str(env).upper()=='LIVE'):
        return pr.Environment.LIVE
    else:
        return pr.Environment.REMARKET

try:
    pr.initialize(
        user=args.user,
        password=args.password,
        account=args.account,
        environment=env(args.environment),
    )
    print('Conexión establecida.')
    time.sleep(1)
except Exception as error:
    print('Fallo de autenticación.')
    print(error)
    parser.print_help()
    time.sleep(1)
    exit()

inst = [args.ticker]
entr=[
    pr.MarketDataEntry.BIDS,
    pr.MarketDataEntry.OFFERS,
    pr.MarketDataEntry.LAST,
    pr.MarketDataEntry.OPENING_PRICE,
    pr.MarketDataEntry.CLOSING_PRICE,
    pr.MarketDataEntry.SETTLEMENT_PRICE,
    pr.MarketDataEntry.HIGH_PRICE,
    pr.MarketDataEntry.LOW_PRICE,
    pr.MarketDataEntry.TRADE_VOLUME,
    pr.MarketDataEntry.OPEN_INTEREST,
    pr.MarketDataEntry.INDEX_VALUE,
    pr.MarketDataEntry.TRADE_EFFECTIVE_VOLUME,
    pr.MarketDataEntry.NOMINAL_VOLUME,
]

def market_data_handler(message):
    print('\nmarket data handler')
    global dat_ord
    dat_ord = message
def order_report_handler(message):
    print('\nmarket order handler')
    global dat_ord
    dat_ord = message
def error_handler(message):
    print("Error Message Received: {0}".format(message))
def exception_handler(e):
    print("Exception Occurred: {0}".format(e.message))
def inst_data_handler(message):
    print('\nInstrumento data handler')
    global dat_inst
    dat_inst = message
pr.init_websocket_connection(
    market_data_handler=market_data_handler,
    order_report_handler=order_report_handler,
    error_handler=error_handler,
    exception_handler=exception_handler
)
print('websocket conectado')
# reporte de instrumento
pr.market_data_subscription(
    handler=inst_data_handler,
    tickers=inst,
    entries=entr,
)
# reporte de ordenes
pr.order_report_subscription(snapshot=True)
precio = 10
while True:
    try:
        if(dat_old_inst != dat_inst):
            dat_old_inst = dat_inst
            print(dat_inst)
        if(dat_old_ord != dat_ord):
            dat_old_ord = dat_ord
            print(dat_ord)
        order = pr.send_order(
            ticker=args.ticker,
            side=pr.Side.BUY,
            size=10,
            price=precio+1,
            order_type=pr.OrderType.LIMIT,
        )
        print('orden enviada', order)
        time.sleep(2)
        cancel_order = pr.cancel_order(order["order"]["clientId"])
        print('orden cancelada')
        time.sleep(2)
        input('Enter para enviar una orden, Ctrl+C para salir.')
    except (Exception, KeyboardInterrupt):
        print("\nSaliendo...")
        break

pr.close_websocket_connection()
print('cerrado websocker conexion.')