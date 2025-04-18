from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db.db import Base, engine, SessionLocal
import models
from routes.bible import bible as bibleRoute

# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependencia
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#http://127.0.0.1:8000/docs
#http://127.0.0.1:8000/
@app.get("/")
def root():
    return {"message": "Hola marlon"}

app.include_router(bibleRoute)

@app.get("/books/")
def read_books(db: Session = Depends(get_db)):
    books = db.query(models.Book).all()
    return books