from sqlalchemy import Column, Integer, String
from db.db import Base

class Verse(Base):
    __tablename__ = "Verse"

    Id = Column(Integer, primary_key=True, index=True)
    IdBook = Column("IdBook", Integer, nullable=False)
    Chapter = Column("Capitulo", Integer)
    Verse = Column("Versiculo", Integer)
    Content = Column("Verso", String(500))

    class Config:
        orm_mode = True 