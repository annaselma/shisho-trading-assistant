from api import utils
from models.model import AbstractModel
from models.Currency import Currency


class Price(AbstractModel):
    resource_name = 'prices'

    dataset: str = ''
    pair: str = ''
    exchange: str = ''
    current: float = 0
    lowest: float = 0
    highest: float = 0
    volume: float = 0
    currency: str = ''
    asset: str = ''
    dataset: str = ''
    openAt: str

    relations = {'currency': Currency, 'asset': Currency}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pair = self.get_pair()

    def get_pair(self):
        return utils.format_pair(self.currency, self.asset)