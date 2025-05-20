from fastapi import HTTPException, Depends
from repository.topic_repository import TopicRepository
from models.topic import Topic
from schemas.topic_schema import TopicRequest, TopicUpdateRequest, TopicResponse

class TopicController:
    bibleRepository: TopicRepository
    def __init__(
        self,
        topicRepository: TopicRepository = Depends()
    ) -> None:
        self.topicRepository = topicRepository

    def getAll(self):
        return self.topicRepository.getAll()
    
    def createTopic(self, topicData: TopicRequest):
        topic = Topic(**topicData.model_dump())
        created_topic = self.topicRepository.createTopic(topic)
        return TopicResponse.model_validate(created_topic)
    
    def updateTopic(self, id: int, topicData: TopicUpdateRequest):
        topic = Topic(**topicData.model_dump())
        created_topic = self.topicRepository.updateTopic(id, topic)
        return TopicResponse.model_validate(created_topic)
        
    def findTopic(self, id: int):
        return self.topicRepository.findTopic(id)
    
    def getTopicByViewId(self, id: int):
        return self.topicRepository.getTopicByViewId(id)
    
    def getTopicByDoctrineId(self, id: int):
        return self.topicRepository.getTopicByDoctrineId(id)
    
    def getTopicDetail(self, id: int):
        return self.topicRepository.getTopicDetail(id)
    
    def findTopicDetail(self, id: int):
        return self.topicRepository.findTopicDetail(id)
    
    def searchText(self, text: str):
        return self.topicRepository.searchText(text)