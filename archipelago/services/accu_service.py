from archipelago.models.accu_info import AccuInfo

DUMMY_PRICE = 3523


def fetch_info():
    response = AccuInfo(spot=DUMMY_PRICE)
    return response
