from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Reset(Base):
    __tablename__ = 'reset'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    token: Mapped[str] = mapped_column(nullable=False)
