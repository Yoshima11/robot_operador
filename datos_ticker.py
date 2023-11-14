import pyRofex as pr

def datos_ticker(ticker):
    def market_data_handler(message):
        print("Market Data Message Received: {0}".format(message))
    def error_handler(self, message):
        print("Error Message Received: {0}".format(message))
    def exception_handler(self, e):
        print("Exception Occurred: {0}".format(e.message))
    
    pr.init_websocket_connection(
        market_data_handler=market_data_handler,
        error_handler=error_handler,
        exception_handler=exception_handler,
        environment=pr.Environment.REMARKET,
    )

    pr.market_data_subscription(
        tickers=ticker,
        entries=[
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
        ],
    )

    pr.close_websocket_connection()
