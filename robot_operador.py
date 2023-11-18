import time
import pyRofex as pr
import flet as ft
import datos

dat_inst = {}

pr.initialize(
    user=datos.user,
    password=datos.password,
    account=datos.account,
    environment=pr.Environment.REMARKET,
)

inst = ['GGAL/DIC23']
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

pr.init_websocket_connection(market_data_handler=market_data_handler)

pr.market_data_subscription(tickers=inst,entries=entr)

while True:
    time.sleep(60)
    print('\n', dat_inst)
    dat_inst = pr.get_market_data(
        ticker="GGAL/DIC23",
        entries=[pr.MarketDataEntry.LAST]
    )
    print('\n', dat_inst)

pr.close_websocket_connection()
