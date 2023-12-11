import logging
import os

import sqlalchemy
from aiohttp import web

app = web.Application()

DB_USERNAME = os.environ.get("DB_USERNAME")
DB_HOST = os.environ.get("DB_HOST")
DB_NAME = os.environ.get("DB_NAME")
DB_PASS = os.environ.get("DB_PASS")
#localhost/aiohttptestserver
#db_engine = sqlalchemy.create_engine(f"postgresql+asyncpg://{DB_USERNAME}:{DB_PASS}@{DB_HOST}/{DB_NAME}",
                                     #echo=True)


def setting_logging() -> None:
    logging.basicConfig(
        level=logging.NOTSET,
        format="{name} - {levelname}: {message}",
        style="{"
    )
    logging.getLogger("asyncio").setLevel("CRITICAL")


def app_logger(app_name: str) -> logging.Logger:
    setting_logging()
    logger = logging.getLogger(app_name)
    return logger