from typing import List

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True)

    books: Mapped[List["Book"]] = relationship(back_populates="user")


class Book(Base):
    __tablename__ = "book"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    titulo: Mapped[str] = mapped_column(nullable=False)
    id_user: Mapped[int] = mapped_column(ForeignKey("users.id"))

    users: Mapped["User"] = relationship(back_populates="book")