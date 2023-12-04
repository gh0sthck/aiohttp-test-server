from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base

engine = create_async_engine("postgresql+asyncpg://postgres:root@localhost/aiohttptestserver")

Base = declarative_base()