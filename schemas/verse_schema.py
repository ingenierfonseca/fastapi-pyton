from pydantic import BaseModel, ConfigDict

class VerseSchema(BaseModel):
    Id: int
    IdBook: int
    Chapter: int
    Verse: int
    Content: str

    model_config = ConfigDict(from_attributes=True)

class PaginatedVerseResponse(BaseModel):
    total_items: int
    total_pages: int
    page: int
    limit: int
    data: list[VerseSchema]

    class Config:
        arbitrary_types_allowed = True