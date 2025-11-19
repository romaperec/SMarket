from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class Base(DeclarativeBase): ...  # General metadata


# User Model
class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    # General block
    username: Mapped[str] = mapped_column(String(50))
    email: Mapped[str]
    password: Mapped[str]
    balance: Mapped[float]

    # Status
    is_admin: Mapped[bool] = mapped_column(default=False)
    is_seller: Mapped[bool] = mapped_column(default=False)
