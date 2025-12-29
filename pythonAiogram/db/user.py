from datetime import datetime

from sqlalchemy import String, DATE, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.testing.schema import mapped_column
from .base import Base

class User(Base):
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(unique=True, nullable=False, primary_key=True)
    username: Mapped[str] = mapped_column(String(30), nullable=False)
    reg_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow
    )