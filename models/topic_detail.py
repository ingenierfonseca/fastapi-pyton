from sqlalchemy import Column, Integer, String
from db.db import Base

class TopicDetail(Base):
    __tablename__ = "TopicDetail"

    Id = Column(Integer, primary_key=True, index=True)
    Content = Column("Content", String(max))
    IdTopic = Column("IdTopic", Integer)