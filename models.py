from typing import Optional
from sqlalchemy.orm import mapped_column, Mapped
from database import Base


class Tasks(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str] = mapped_column(nullable=True)
    completed: Mapped[bool] = mapped_column(default=False)
