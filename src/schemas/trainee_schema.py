from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List

class TraineeBase(BaseModel):
    type_id: str=Field(..., description="Tipo de documento del aprendiz (CC,TI,CE)", pattern="^(CC|TI|CE)$", example="CC")

    document: str = Field(..., description="Número de documento del aprendiz", min_length=6, max_length=10, pattern="^[0-9]+$", example="1234567890")

    name: str = Field(..., description="Nombre completo del aprendiz", min_length=3, max_length=10,  example="Juan Pérez")

    group_code: str = Field(..., description="Número de ficha del aprendiz", min_length=6, max_length=7, pattern="^[0-9]+$", example="1234567")

    program: str = Field(..., description="Programa de formación del aprendiz", min_length=2, max_length=4, example="ADSO")

    email: EmailStr = Field(..., description="Correo del aprendiz", example="juan.perez@gsena.edu.co")

class TraineeCreate(TraineeBase):
    pass

class TraineeUpdate(BaseModel):
    type_id: Optional[str]=Field(None, pattern="^(CC|TI|CE)$")
    document: Optional[str]=Field(None,min_length=6, max_length=10, pattern="^[0-9]+$",  )
    name: Optional[str]=Field(None, min_length=3)
    group_code: Optional[str]=Field(None,pattern="^[0-9]+$")
    program: Optional[str]=Field(None, min_length=2 )
    email: Optional[EmailStr]=None

class TaineeResponse(TraineeBase):
    data:Optional[list[TraineeBase]]=None #Datos consumidos de la api, Rick & Morty


