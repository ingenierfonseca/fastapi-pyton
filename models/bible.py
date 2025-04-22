from sqlalchemy import Column, Integer, String
from db.db import Base

class Bible(Base):
    __tablename__ = "Biblia"

    Id = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(255), nullable=False)