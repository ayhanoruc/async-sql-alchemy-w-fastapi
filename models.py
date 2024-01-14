from database import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Text
from datetime import datetime

"""
class Note:
    id str
    title str
    content str
    created_at datetime

"""

class Note(Base):
    __tablename__ = "notes"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(default= datetime.utcnow())

    def __str__(self) -> str:
        return f"< Note: title={self.title}, created_at={self.created_at} >"
