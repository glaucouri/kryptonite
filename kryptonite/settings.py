from typing import Set, List
from logging import ERROR, WARNING

from pydantic import (
    BaseModel,
    BaseSettings,
    PyObject,
    RedisDsn,
    PostgresDsn,
    Field,
)


class Settings(BaseSettings):
    every_sec: int = 5
    redis_dsn: RedisDsn = "redis://user:pass@localhost:6379/1"
    log_verbosity: int = ERROR


    # Binance
    binance_enabled: bool = False
    binance_api_key: str = None
    binance_api_secret: str = None
    binance_symbols: Set[str] = {"BNBBTC", "ADABTC", "ETHEUR"}


    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        
