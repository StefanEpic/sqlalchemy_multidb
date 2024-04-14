from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped

from src.config import DB_URL_1, DB_URL_2
from src.db.column_types import int_pk

engines = {
    'first': create_async_engine(DB_URL_1),
    'second': create_async_engine(DB_URL_2)
}


async def get_first_session() -> AsyncSession:
    async_session = async_sessionmaker(engines['first'], class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        yield session


async def get_second_session() -> AsyncSession:
    async_session = async_sessionmaker(engines['second'], class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        yield session


class Base:
    __abstruct__ = True
    id: Mapped[int_pk]


class FirstBase(DeclarativeBase, Base):
    pass


class SecondBase(DeclarativeBase, Base):
    pass
