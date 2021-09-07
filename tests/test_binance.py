from typing import Set
from bson.objectid import ObjectId
from kryptonite.main import pool, binance_job
from kryptonite.settings import S


def test_24h_endpoint():
    assert isinstance(pool.binance.get_ticker(), list)


def test_binance_insert_doc():
    oid = binance_job(["BTCUSDT"], True)
    assert ObjectId.is_valid(oid)


def test_binance_show_doc():
    oid = binance_job(["BTCUSDT"], False)
    assert ObjectId.is_valid(oid)


