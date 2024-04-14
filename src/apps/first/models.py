from sqlalchemy.orm import Mapped

from src.db.column_types import str_100
from src.db.connection import FirstBase


class Department(FirstBase):
    __tablename__ = "department"

    title: Mapped[str_100]
    description: Mapped[str_100]
    url: Mapped[str_100]

    def __str__(self):
        return self.title
