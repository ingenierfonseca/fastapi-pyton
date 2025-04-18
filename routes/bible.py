from fastapi import APIRouter

bible = APIRouter()

@bible.get("/")
def getBiblesType():
    return ["Reina Valera 1960", "Libro del mormon"]