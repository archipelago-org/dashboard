from archipelago.models.accu_price import AccuPriceResponse

DUMMY_PRICE = 3523


def fetch_price():
    response = AccuPriceResponse(spot=DUMMY_PRICE)
    return response
