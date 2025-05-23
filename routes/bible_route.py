from fastapi import APIRouter, Depends, Query
from middleware.verify_apikey import verifyApiKey
from controller.bible_controller import BibleController

bible = APIRouter(
    prefix="/api/bible",
    tags=["Bible"]
    #dependencies=[Depends(verifyApiKey)]
)


@bible.get("/")
def getBibles(controller: BibleController = Depends()):
    return controller.getAllBible()

@bible.get("/{id}")
def getBibles(id: int, controller: BibleController = Depends()):
    return controller.findBible(id)

@bible.get("/{id}/books")
def getBooks(id: int, controller: BibleController = Depends()):
    return controller.getBooksByBibleId(id)

@bible.get("/read/{id}/book-verses")
def read_verses_books(
    id: int,
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=1000),
    controller: BibleController = Depends()
):
    return controller.getVersesByBible(page, limit, id)

@bible.get("/read/{id}/book/{name}/{chapter}/{verse}")
def read_books(id: int, name: str, chapter: int, verse: str, controller: BibleController = Depends()):
    return controller.getVersesByBookChapterAndVerse(id, name, chapter, verse)

@bible.get("/read/search/{content}")
def read_books(content: str, controller: BibleController = Depends()):
    return controller.searchText(content)