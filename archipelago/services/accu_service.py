from archipelago.models.accu_price import AccuPriceResult

DUMMY_PRICE = 3523


def fetch_spot_price():
    result = AccuPriceResult(spot=DUMMY_PRICE)
    return result
