from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    username: Mapped[str] = mapped_column(String(length=255), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(length=255), nullable=False)
    cash: Mapped[int] = mapped_column(BigInteger, default=1000)

    def __str__(self):
        return f"{self.id}/{self.username}/"