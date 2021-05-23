from typing import Set
from kryptonite.main import binance_client, binance_job
from kryptonite.settings import S


def test_24h_endpoint():
    assert isinstance(binance_client.get_ticker(), dict)



def test_binance_insert_doc():
    binance_job(['BTCUSDT'],True)