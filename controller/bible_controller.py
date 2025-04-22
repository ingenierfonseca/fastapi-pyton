from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from repository.bible_repository import BibleRepository

class BibleController:
    bibleRepository: BibleRepository
    def __init__(
        self,
        bibleRepository: BibleRepository = Depends()
    ) -> None:
        self.bibleRepository = bibleRepository
    #def __init__(self, db: Session):
        #self.repo = BibleRepository(db)

    def getAllBible(self):
        return self.bibleRepository.getAllBible()
        
    def findBible(self, id: int):
        return self.bibleRepository.findBible(id)
    
    def getBooksByBibleId(self, id: int):
        return self.bibleRepository.getBooksByBibleId(id)
    
    def getVersesByBookChapterAndVerse(self, id: int, name: str, chapter: int, verse: str):
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
    
    def searchText(self, text: str):
        return self.bibleRepository.searchText(text)