from sqlalchemy.orm import Mapped

from src.db.connection import SecondBase


class User(SecondBase):
    __tablename__ = "user"

    name: Mapped[str]
    family: Mapped[str]
    phone: Mapped[str]

    def __str__(self):
        return self.name
