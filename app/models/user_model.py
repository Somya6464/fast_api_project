from core.db import Base
from sqlalchemy import Column, Integer, String

class UserModel(Base):
    __tablename__ = "users_table"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, index=True)
    password = Column(String, index=True)
    role = Column(String, index=True)