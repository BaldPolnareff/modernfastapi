from pydantic import BaseModel, Field
from typing import Optional

class SimpleLocation(BaseModel):
    city: str = Field(..., example="Rome")
    state: Optional[str] = Field(None, example="Lazio")
    country: str = Field(..., example="IT")

