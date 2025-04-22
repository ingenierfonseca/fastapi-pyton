from sqlalchemy import Column, Integer, String
from db.db import Base

class Book(Base):
    __tablename__ = "Book"

    Id = Column(Integer, primary_key=True, index=True)
    IdBible = Column("IdBiblia", Integer, nullable=False)
    Name = Column("Nombre", String(50))
    Abreviation = Column("Abreviatura", String(3))
    LongName = Column("NombreLargo", String(50))
    CountChapter = Column("CountCapitulos", Integer)