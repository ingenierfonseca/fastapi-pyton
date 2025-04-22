from sqlalchemy.orm import Session
from fastapi import Depends
from db.db import get_db

class BaseRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db