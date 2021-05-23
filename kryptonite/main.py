from typing import Dict, List
from .settings import S
from binance.client import Client
from dataclasses import dataclass
from time import sleep
import threading
import time
import schedule
import logging
import pymongo
from .db import insert_doc

log = logging.getLogger("kryptonite")


@dataclass
class Pool_of_clients:
    """pool is necessary to ensure that only needed clients
    will be instantiated

    Returns
    -------
    [type]
        [description]
    """

    _binance = None

    @property
    def binance(self) -> Client:
        if self._binance is None:
            self._binance = Client()
        return self._binance

pool = Pool_of_clients()


def pretty_doc(doc: Dict) -> str:
    return ", ".join([f"{k}:{v}" for k, v in doc.items()])


def binance_job(symbols: List[str], store: bool):
    log.info("Call Binance for %d symbols", len(symbols))
    docs = pool.binance.get_ticker()

    as_dict = {x["symbol"]: x for x in docs}
    for symbol in symbols:
        log.debug("Asking for: %s", symbol)
        # j = binance_client.get_avg_price(symbol=symbol)
        doc = as_dict[symbol]
        doc["provider"] = "binance"
        if store:
            return insert_doc(doc)
        else:
            print("-", symbol, pretty_doc(doc))


def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()
