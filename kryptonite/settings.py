from typing import Any, Set, List
from logging import ERROR, WARNING, getLogger

from pydantic import (
    BaseModel,
    BaseSettings,
    PyObject,
    AnyUrl,
    Field,
)


"""Settings priority:
 1. env variables
      remember the quoting, eg: 
      > export binance_symbols=[\"BTCEUR\"]

 2. .env file on current directory - see docker documentation
 
 3. default values
"""

class Settings(BaseSettings):
    every_sec: int = 5
    mongo_dsn: AnyUrl = "mongodb://localhost:27017/"
    mongo_db_name: str = "kryptonite"
    mongo_coll_name: str = "symbols"
    log_verbosity: int = 10

    # Binance
    binance_enabled: bool = False
    binance_api_key: str = None
    binance_api_secret: str = None
    binance_symbols: Set[str] = {"BNBBTC", "ADABTC", "ETHEUR"}

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


S = Settings()

log = getLogger("kryptonite")