from archipelago.models.accu_info import AccuInfo

DUMMY_PRICE = 3523


class AccuService:

    def fetch_info(self):
        response = AccuInfo(spot=DUMMY_PRICE)
        return response
