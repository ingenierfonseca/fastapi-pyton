from sqlalchemy import desc
from models.bible import Bible
from models.book import Book
from models.verse import Verse
from .base_repository import BaseRepository
from helpers.pagination import paginate
from helpers.not_found_error import NotFoundError

class BibleRepository(BaseRepository):
    def getAllBible(self):
        bible = self.db.query(Bible).all()
        return bible
        
    def findBible(self, id: int):
        bible = self.db.query(Bible).where(Bible.Id == id).first()

        if not bible:
            raise NotFoundError(f"Bible with ID {id} not found")
            
        return bible
        
    def getBooksByBibleId(self, id: int):
        books = self.db.query(Book).where(Book.IdBible == id).all()

        if not books:
            raise NotFoundError(f"Books with Bible with ID {id} not found")
            
        return books
        
    def getVersesByBible(self, page: int, limit: int, id: int):
        query = (
            self.db.query(Verse)
            .join(Book, Verse.IdBook == Book.Id)
            .where(Book.IdBible == id)
            .order_by(desc(Verse.Chapter))
        )
        total_items = query.count()

        if total_items == 0:
            raise NotFoundError(f"No verses found for Bible ID {id}")
            
        total_items, total_pages, items = paginate(query, page, limit)

        return items, total_items, total_pages
        
    def getVersesByBookChapterAndVerse(self, id: int, name: str, chapter: int, verse: int):
        bible = self.db.query(Bible).where(Bible.Id == id).first()

        if not bible:
            raise NotFoundError(f"Bible with ID {id} not found")
            
        b = self.db.query(Book).where(Book.Name == name).first()

        if not b:
            raise NotFoundError(f"Book with Name {name} not found")
            
        verse = self.db.query(Verse).where(
            (Verse.IdBook == b.Id) & 
            (Verse.Chapter == chapter) & 
            (Verse.Verse == verse)
        ).all()

        if not verse:
            raise NotFoundError(f"Verse not found")
            
        return verse
        
    def getVersesByBookChapterAndVerseRange(self, id: int, name: str, chapter: int, start: int, end: int):
        bible = self.db.query(Bible).where(Bible.Id == id).first()

        if not bible:
            raise NotFoundError(f"Bible with ID {id} not found")
            
        b = self.db.query(Book).where(Book.Name == name).first()

        if not b:
            raise NotFoundError(f"Book with Name {name} not found")
            
        verse = self.db.query(Verse).where(
            (Verse.IdBook == b.Id) & 
            (Verse.Chapter == chapter) & 
            (Verse.Verse >= start) & 
            (Verse.Verse <= end)
        ).all()

        if not verse:
            raise NotFoundError(f"Verse not found")
            
        return verse
    
    def searchText(self, text: str):
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