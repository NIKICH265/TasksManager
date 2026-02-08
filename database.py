from sqlalchemy.orm import DeclarativeBase, sessionmaker, mapped_column, Mapped
import sqlalchemy
from settings import settings


class Base(DeclarativeBase):
    pass


class DatabaseHelper:
    def __init__(self, path, echo):
        self.engine = sqlalchemy.create_engine(url=path, echo=echo)
        self.session_factory = sessionmaker(
            self.engine, autoflush=False, expire_on_commit=False, autocommit=False
        )

    def session_depends(self):
        with self.session_factory() as session:
            yield session

    def create_tables(self):
        Base.metadata.create_all(self.engine)


db_helper = DatabaseHelper(settings.db_path, settings.DEBUG)
