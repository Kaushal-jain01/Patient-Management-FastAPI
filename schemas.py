from pydantic import BaseModel, Field
from typing import Optional, Literal

class PatientBase(BaseModel):
    name: str
    city: str
    age: int = Field(gt=0)
    gender: Literal["male", "female", "others"]
    height: float = Field(gt=0)
    weight: float = Field(gt=0)

class PatientCreate(PatientBase):
    id: str

class PatientUpdate(BaseModel):
    name: Optional[str] = None
    city: Optional[str] = None
    age: Optional[int] = Field(default=None, gt=0)
    gender: Optional[Literal["male", "female", "others"]] = None
    height: Optional[float] = Field(default=None, gt=0)
    weight: Optional[float] = Field(default=None, gt=0)

class PatientResponse(PatientCreate):
    bmi: float
    verdict: str
