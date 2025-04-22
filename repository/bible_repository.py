from fastapi import HTTPException
from models.bible import Bible
from models.book import Book
from models.verse import Verse
from .base_repository import BaseRepository

class NotFoundError(Exception):
    def __init__(self, detail: str):
        self.detail = detail

class BibleRepository(BaseRepository):
    def getAllBible(self):
        try:
            bible = self.db.query(Bible).all()
            return bible
        except NotFoundError as e:
            raise HTTPException(status_code=404, detail=e.detail)
        
    def findBible(self, id: int):
        try:
            bible = self.db.query(Bible).where(Bible.Id == id).first()
            return bible
        except NotFoundError as e:
            raise HTTPException(status_code=404, detail=e.detail)
        
    def getBooksByBibleId(self, id: int):
        try:
            books = self.db.query(Book).where(Book.IdBible == id).all()
            return books
        except NotFoundError as e:
            raise HTTPException(status_code=404, detail=e.detail)
        
    def getVersesByBookChapterAndVerse(self, id: int, name: str, chapter: int, verse: int):
        try:
            bible = self.db.query(Bible).where(Bible.Id == id).first()

            if not bible:
                raise HTTPException(status_code=404, detail=f"Bible with ID {id} not found")
            
            b = self.db.query(Book).where(Book.Name == name).first()

            if not b:
                raise HTTPException(status_code=404, detail=f"Book with Name {name} not found")
            
            verse = self.db.query(Verse).where(
                (Verse.IdBook == b.Id) & 
                (Verse.Chapter == chapter) & 
                (Verse.Verse == verse)
            ).all()
            return verse
        except NotFoundError as e:
            raise HTTPException(status_code=404, detail=e.detail)
        
    def getVersesByBookChapterAndVerseRange(self, id: int, name: str, chapter: int, start: int, end: int):
        try:
            bible = self.db.query(Bible).where(Bible.Id == id).first()

            if not bible:
                raise HTTPException(status_code=404, detail=f"Bible with ID {id} not found")
            
            b = self.db.query(Book).where(Book.Name == name).first()

            if not b:
                raise HTTPException(status_code=404, detail=f"Book with Name {name} not found")
            
            verse = self.db.query(Verse).where(
                (Verse.IdBook == b.Id) & 
                (Verse.Chapter == chapter) & 
                (Verse.Verse >= start) & 
                (Verse.Verse <= end)
            ).all()
            return verse
        except NotFoundError as e:
            raise HTTPException(status_code=404, detail=e.detail)
    
    def searchText(self, text: str):
        try:
            results = [
                {
                    "id": id,
                    "book": name,
                    "chapter": chapter,
                    "verse": verse,
                    "content": content
                }
                for id, name, chapter, verse, content in self.db.query(
                    Verse.Id, Book.Name, Verse.Chapter, Verse.Verse, Verse.Content
                )
                .join(Book, Verse.IdBook == Book.Id)
                .filter(Verse.Content.contains(text))
                .all()
            ]
            return results
        except NotFoundError as e:
            raise HTTPException(status_code=404, detail=e.detail)