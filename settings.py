import logging

from aiohttp import web

app = web.Application()


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