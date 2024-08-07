from datetime import date

from sqlalchemy import ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Lists(Base):
    __tablename__ = "lists"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    board_id: Mapped[int] = mapped_column(ForeignKey("boards.id"), nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    creator: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    date_added: Mapped[date] = mapped_column(nullable=False)
    ordering: Mapped[list[int]] = mapped_column(JSON)
