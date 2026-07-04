from datetime import datetime
from sqlalchemy import Enum

from sqlalchemy import Boolean, Column, DateTime, Integer, String

from core.db import Base
from enums.all_enums import UserRole


class UserModel(Base):
    __tablename__ = "users_table"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, index=True, unique=True, nullable=False)
    password = Column(String, index=True, nullable=False)
    role = Column(Enum(UserRole), nullable=False, default=UserRole.USER)
    is_verified = Column(Boolean, default=True, nullable=False)

    created_at = Column(DateTime, default=datetime.now, nullable=False)

    updated_at = Column(
        DateTime, default=datetime.now, onupdate=datetime.now, nullable=False
    )
