from fastapi import HTTPException, HTTPException, Depends
from repository.bible_repository import BibleRepository
from schemas.verse_schema import PaginatedVerseResponse, VerseSchema
from helpers.not_found_error import NotFoundError

class BibleController:
    bibleRepository: BibleRepository
    def __init__(
        self,
        bibleRepository: BibleRepository = Depends()
    ) -> None:
        self.bibleRepository = bibleRepository

    def getAllBible(self):
        return self.bibleRepository.getAllBible()
        
    def findBible(self, id: int):
        try:
            return self.bibleRepository.findBible(id)
        except NotFoundError as e:
            raise HTTPException(status_code=404, detail=str(e))
    
    def getBooksByBibleId(self, id: int):
        try:
            return self.bibleRepository.getBooksByBibleId(id)
        except NotFoundError as e:
            raise HTTPException(status_code=404, detail=str(e))
    
    def getVersesByBible(self, page: int, limit: int, id: int):
        try:
            items, total_items, total_pages = self.bibleRepository.getVersesByBible(page, limit, id)

            return PaginatedVerseResponse(
                total_items=total_items,
                total_pages=total_pages,
                page=page,
                limit=limit,
                data=[VerseSchema.model_validate(v) for v in items]
            )
        except NotFoundError as e:
            raise HTTPException(status_code=404, detail=str(e))
        except Exception as e:
            #logger.exception("Unexpected error in getVersesByBible")
            raise HTTPException(status_code=500, detail="Internal server error")
    
    def getVersesByBookChapterAndVerse(self, id: int, name: str, chapter: int, verse: str):
        try:
            if '-' in verse:
                try:
                    start, end = verse.split('-')
                    if not (start.isdigit() and end.isdigit()):
                        raise ValueError
                    start, end = int(start), int(end)
                except ValueError:
                    raise HTTPException(status_code=400, detail="Versículo inválido. Usa el formato '1' o '1-10'.")
                
                start, end = map(int, verse.split('-'))
                return self.bibleRepository.getVersesByBookChapterAndVerseRange(id, name, chapter, start, end)
            else:
                if not verse.isdigit():
                    raise HTTPException(status_code=400, detail="Versículo inválido. Usa solo números.")
                verse = int(verse)
                return self.bibleRepository.getVersesByBookChapterAndVerse(id, name, chapter, verse)
        except NotFoundError as e:
            raise HTTPException(status_code=404, detail=str(e))
    
    def searchText(self, text: str):
        try:
            return self.bibleRepository.searchText(text)
        except NotFoundError as e:
            raise HTTPException(status_code=404, detail=str(e))