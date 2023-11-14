import pyRofex as pr
import pandas as pd

def datos_ticker(ticker):
    entradas=[
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
    salida = pr.get_market_data(ticker, entradas)
    return pd.DataFrame.from_dict(salida)
