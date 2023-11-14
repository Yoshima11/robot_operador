import pyRofex as pr
import robot_operador

class datos_ticker:
    def __init__(self, ticker):
        self.ticker = ticker
    def market_data_handler(self, message):
        return message
    def error_handler(self, message):
        print("Error Message Received: {0}".format(message))
    def exception_handler(self, e):
        print("Exception Occurred: {0}".format(e.message))

# Initiate Websocket Connection
    pr.init_websocket_connection(
        market_data_handler=market_data_handler,
        error_handler=error_handler,
        exception_handler=exception_handler,
        environment=pr.Environment.REMARKET,
    )
# Pide datos del activo
    pr.market_data_subscription(
        tickers=self.tickers,
        entries=[
            pr.MarketDataEntry.BIDS,
            pr.MarketDataEntry.OFFERS
        ],
    )
# Cierra conexión.
    pr.close_websocket_connection()
