from datetime import date

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Cards(Base):
    __tablename__ = "cards"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    list_id: Mapped[int] = mapped_column(ForeignKey("lists.id"), nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    creator: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    date_added: Mapped[date] = mapped_column(nullable=False)
    labels: Mapped[str] = mapped_column(nullable=True)
