from sqlalchemy import String
from sqlalchemy.orm import mapped_column
from typing_extensions import Annotated

int_pk = Annotated[int, mapped_column(primary_key=True)]
str_100 = Annotated[str, mapped_column(String(100))]
