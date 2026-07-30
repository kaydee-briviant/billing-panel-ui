from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String

class Base(DeclarativeBase):
    pass

class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key=True)
    plan_type: Mapped[str] = mapped_column(String(100))
    credits: Mapped[int | None] = mapped_column(Integer)

    def __repr__(self):
        return (
            f"<Account(id={self.id}, "
            f"plan_type={self.plan_type!r}, "
            f"credits={self.credits!r})>"
        )
