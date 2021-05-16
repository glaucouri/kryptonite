from typing import Dict, List
from .settings import Settings
from binance.client import Client
from time import sleep
import threading
import time
import schedule
import logging

log = logging.getLogger("kryptonite")


client = Client()


def pretty_doc(doc: Dict) -> str:
    return ", ".join([f"{k}:{v}" for k, v in doc.items()])


def binance(symbols: List[str], store: bool):
    log.info("Call Binance for: %s", symbols)
    for symbol in symbols:
        log.debug("Asking for: %s", symbol)
        j = client.get_avg_price(symbol=symbol)
        if store:
            pass
        else:
            print('-', symbol, pretty_doc(j))


def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()
