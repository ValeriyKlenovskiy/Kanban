from sqlalchemy import ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Boards(Base):
    __tablename__ = "boards"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    space_id: Mapped[int] = mapped_column(ForeignKey("spaces.id"), nullable=False)
    background_id: Mapped[int] = mapped_column(ForeignKey("backgrounds.id"), nullable=False)
    ordering: Mapped[list[int]] = mapped_column(JSON)
