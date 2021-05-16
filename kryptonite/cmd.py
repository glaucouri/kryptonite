# -*- coding: utf-8
"""
kryptonite main cli (Command Line Interface)
"""
import click
import time
from .main import schedule, log, run_threaded, binance
from .settings import Settings
import logging
from functools import partial


@click.command()
@click.option("-v", "--verbose", count=True, help="Verbose output (repeat for increased verbosity)")
@click.option("-d", "--delay", type=int, help="Main loop delay")
@click.option("--dry_run", is_flag=True, help="Do not store acquired data. stdout only. ")
def cli(**kwargs):
    # settings override
    overrides = {}

    """
    Set logging verbosity, default=ERROR

    verbosity v:WARNING,
              vv:INFO,
              vvv+:DEBUG

    """

    v = kwargs["verbose"]
    if v > 2:
        overrides["log_verbosity"] = logging.DEBUG
    elif v > 1:
        overrides["log_verbosity"] = logging.INFO
    elif v:
        overrides["log_verbosity"] = logging.WARNING

    if kwargs["delay"]:
        overrides["every_sec"] = kwargs["delay"]

    """Setting initialization """
    S = Settings(**overrides)
    
    logging.basicConfig(format="%(asctime)s %(message)s")
    log.setLevel(S.log_verbosity)

    if S.binance_enabled:
        log.info("Scheduling binance every %ss", S.every_sec)
        schedule.every(S.every_sec).seconds.do(
            run_threaded, partial(binance, S.binance_symbols, bool(kwargs.get("dry_run")))
        )

    """Main loop """
    while 1:
        schedule.run_pending()
        time.sleep(0.1)
