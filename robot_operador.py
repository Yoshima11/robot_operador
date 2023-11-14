import sys
import argparse #para ingresar argumentos al iniciar el programa
import time
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

dat_inst = ''
dat_old_inst = ''
dat_ord = ''
dat_old_ord = ''

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
    global dat_inst
    dat_inst = message
def order_report_handler(message):
    global dat_ord
    dat_ord = message
def error_handler(message):
    print("Error Message Received: {0}".format(message))
def exception_handler(e):
    print("Exception Occurred: {0}".format(e.message))

pr.init_websocket_connection(
    market_data_handler=market_data_handler,
    order_report_handler=order_report_handler,
    error_handler=error_handler,
    exception_handler=exception_handler
)
# reporte de instrumento
pr.market_data_subscription(
    tickers=inst,
    entries=entr,
)
# reporte de ordenes
pr.order_report_subscription()

while True:
    try:
        #datos = pd.DataFrame.from_dict(pr.get_market_data(args.ticker, entradas)) Pedir datos de ticker
        input('Enter para enviar una orden. Ctrl+C para salir')
        if(dat_old_inst != dat_inst):
            dat_old_inst = dat_inst
            print(pd.DataFrame.from_dict(dat_inst))
        if(dat_old_ord != dat_ord):
            dat_old_ord = dat_ord
            print(pd.DataFrame.from_dict(dat_ord))
        order = pr.send_order(
            ticker=args.ticker,
            side=pr.Side.BUY,
            size=2,
            price=55.8,
            order_type=pr.OrderType.LIMIT,
        )
    except KeyboardInterrupt:
        print("Saliendo...")
        exit()
