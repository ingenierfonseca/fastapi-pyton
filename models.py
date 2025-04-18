from sqlalchemy import Column, Integer, String
from db.db import Base

class Book(Base):
    __tablename__ = "TipoBiblia"

    Id = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(255), nullable=False)
    #abreviatura = Column(String(10))