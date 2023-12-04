import asyncio
import logging

from aiohttp import web

from settings import app_logger, app


def main() -> None:
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    web.run_app(app, host="localhost")


if __name__ == "__main__":
    logger: logging.Logger = app_logger(__name__)
    try:
        main()
    except Exception as error:
        logger.error(error)