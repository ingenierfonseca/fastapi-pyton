from fastapi import FastAPI
from db.db import Base, engine
from routes.bible_route import bible as bibleRoute
from middleware.apikey_middleware import APIKeyMiddleware

# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI()

#http://127.0.0.1:8000/docs
#http://127.0.0.1:8000/
@app.get("/")
def root():
    return {"message": "Bienvenido a api upci"}

# Middleware global
# app.add_middleware(APIKeyMiddleware)
app.include_router(bibleRoute)