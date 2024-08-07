from sqlalchemy import ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Backgrounds(Base):
    __tablename__ = "backgrounds"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    image_id: Mapped[int] = mapped_column(nullable=False)
