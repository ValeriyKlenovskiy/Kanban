from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Verification(Base):
    __tablename__ = 'verification'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    token: Mapped[str] = mapped_column(nullable=False)
