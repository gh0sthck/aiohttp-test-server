from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base

from settings import DB_PASS, DB_HOST, DB_NAME, DB_USERNAME

engine = create_async_engine(f"postgresql+asyncpg://{DB_USERNAME}:{DB_PASS}@{DB_HOST}/{DB_NAME}")

Base = declarative_base()