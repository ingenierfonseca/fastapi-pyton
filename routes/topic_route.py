from fastapi import APIRouter, Depends, Path
from middleware.verify_apikey import verifyApiKey
from controller.topic_controller import TopicController
from schemas.topic_schema import TopicRequest, TopicUpdateRequest, TopicResponse

topic = APIRouter(
    prefix="/api/topic",
    tags=["Topic"]
    #dependencies=[Depends(verifyApiKey)]
)

ID_VALIDATION = Path(
    ...,
    ge=1
)

@topic.get("/")
def getAll(controller: TopicController = Depends()):
    return controller.getAll()

@topic.post("/", response_model=TopicResponse)
def createTopic(topic: TopicRequest, controller: TopicController = Depends()):
    return controller.createTopic(topic)

@topic.patch("/{id}", response_model=TopicResponse)
def createTopic(topic: TopicUpdateRequest, id: int = ID_VALIDATION, controller: TopicController = Depends()):
    return controller.updateTopic(id, topic)

@topic.get("/{id}")
def findTopic(id: int = ID_VALIDATION, controller: TopicController = Depends()):
    return controller.findTopic(id)

@topic.get("/view/{id}")
def getTopicByViewId(id: int, controller: TopicController = Depends()):
    return controller.getTopicByViewId(id)

@topic.post("/view")
def getTopicByViewId(id: int, controller: TopicController = Depends()):
    return controller.getTopicByViewId(id)

@topic.get("/doctrine/{id}")
def getTopicByDoctrineId(id: int, controller: TopicController = Depends()):
    return controller.getTopicByDoctrineId(id)

@topic.get("/{id}/detail")
def getTopicDetail(id: int, controller: TopicController = Depends()):
    return controller.getTopicDetail(id)

@topic.get("/detail/{id}")
def findTopicDetail(id: int, controller: TopicController = Depends()):
    return controller.findTopicDetail(id)

@topic.get("/read/search/{content}")
def searchText(content: str, controller: TopicController = Depends()):
    return controller.searchText(content)