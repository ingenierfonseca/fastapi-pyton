from pydantic import BaseModel, Field, ConfigDict, field_validator
from typing import Optional

class TopicRequest(BaseModel):
    Name: str
    Description: str = Field(..., max_length=500)
    IdView: int
    IdDoctrine: int

    @field_validator('Name')
    def validate_name(cls, value):
        if not value:
            raise ValueError("El campo 'Name' es obligatorio")
        if not value.strip():
            raise ValueError("El campo 'Name' no puede estar vacío")
        if len(value) > 50:
            raise ValueError("El campo 'Name' no debe superar 50 caracteres")
        return value

class TopicUpdateRequest(BaseModel):
    Id: int
    Name: Optional[str] = None
    Description: Optional[str] = Field(None, max_length=500)
    IdView: Optional[int] = None
    IdDoctrine: Optional[int] = None

    @field_validator('Name')
    def validate_name(cls, value):
        #if not value:
            #raise ValueError("El campo 'Name' es obligatorio")
        if not value.strip():
            raise ValueError("El campo 'Name' no puede estar vacío")
        if len(value) > 50:
            raise ValueError("El campo 'Name' no debe superar 50 caracteres")
        return value

class TopicResponse(BaseModel):
    Id: int
    Name: str
    Description: str
    IdView: int
    IdDoctrine: int

    model_config = ConfigDict(from_attributes=True)