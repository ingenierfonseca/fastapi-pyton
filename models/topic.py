from sqlalchemy import Column, Integer, String
from db.db import Base

class Topic(Base):
    __tablename__ = "Topic"

    Id = Column(Integer, primary_key=True, index=True)
    Name = Column("Nombre", String(50))
    Description = Column("Descripcion", String(500))
    IdView = Column("IdView", Integer)
    IdDoctrine = Column("IdDoctrine", Integer)