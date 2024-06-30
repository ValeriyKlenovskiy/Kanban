from sqlalchemy import ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Spaces(Base):
    __tablename__ = "spaces"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    owner_id: Mapped[int] = mapped_column(ForeignKey("spaces.id"), nullable=False)
    allowed_users: Mapped[list[int]] = mapped_column(JSON)
    ordering: Mapped[list[int]] = mapped_column(JSON)
