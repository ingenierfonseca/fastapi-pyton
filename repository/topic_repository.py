from fastapi import HTTPException
from models.topic import Topic
from models.topic_detail import TopicDetail
from .base_repository import BaseRepository

class NotFoundError(Exception):
    def __init__(self, detail: str):
        self.detail = detail

class TopicRepository(BaseRepository):
    def getAll(self):
        try:
            topics = self.db.query(Topic).all()
            return topics
        except NotFoundError as e:
            raise HTTPException(status_code=404, detail=e.detail)
        
    def createTopic(self, topic: Topic):
        try:
            #view = self.db.query(View).where(View.Id == topic.IdView).first()

            #if not view:
                #raise HTTPException(status_code=404, detail=f"View with ID {topic.IdView} not found")
            
            #doctrine = self.db.query(Doctrine).where(Doctrine.Id == topic.IdDoctrine).first()

            #if not doctrine:
                #raise HTTPException(status_code=404, detail=f"Doctrine with ID {topic.IdDoctrine} not found")
            
            self.db.add(topic)
            self.db.commit()
            self.db.refresh(topic)
            return topic
        except NotFoundError as e:
            raise HTTPException(status_code=404, detail=e.detail)
        
    def findTopic(self, id: int):
        try:
            topic = self.db.query(Topic).where(Topic.Id == id).first()
            return topic
        except NotFoundError as e:
            raise HTTPException(status_code=404, detail=e.detail)
        
    def getTopicByViewId(self, id: int):
        try:
            topics = self.db.query(Topic).where(Topic.IdView == id).all()
            return topics
        except NotFoundError as e:
            raise HTTPException(status_code=404, detail=e.detail)
        
    def getTopicByDoctrineId(self, id: int):
        try:
            topics = self.db.query(Topic).where(Topic.IdDoctrine == id).all()
            return topics
        except NotFoundError as e:
            raise HTTPException(status_code=404, detail=e.detail)
        
    def getTopicDetail(self, id: int):
        try:
            topic = self.db.query(Topic).where(Topic.Id == id).first()

            if not topic:
                raise HTTPException(status_code=404, detail=f"Topic with ID {id} not found")
            
            detail = self.db.query(TopicDetail).where(TopicDetail.IdTopic == id).all()
            return detail
        except NotFoundError as e:
            raise HTTPException(status_code=404, detail=e.detail)
        
    def findTopicDetail(self, id: int):
        try:
            detail = self.db.query(TopicDetail).where(TopicDetail.Id == id).first()
            return detail
        except NotFoundError as e:
            raise HTTPException(status_code=404, detail=e.detail)
    
    def searchText(self, text: str):
        try:
            results = [
                {
                    "id": id,
                    "topic": name,
                    "content": content
                }
                for id, name, content in self.db.query(
                    TopicDetail.Id, Topic.Name, TopicDetail.Content
                )
                .join(Topic, TopicDetail.IdTopic == Topic.Id)
                .filter(TopicDetail.Content.contains(text))
                .all()
            ]
            return results
        except NotFoundError as e:
            raise HTTPException(status_code=404, detail=e.detail)