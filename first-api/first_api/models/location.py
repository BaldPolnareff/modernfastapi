from pydantic import BaseModel, Field
from typing import Optional

class SimpleLocation(BaseModel):
    city: str = Field(..., example="Rome")
    state: Optional[str] = Field(None, example="Lazio")
    country: str = Field(..., example="IT")

class GeoCodingAPILocation(BaseModel):
    lat: float = Field(..., example=41.902782)
    lon: float = Field(..., example=12.496366)
    display_name: str = Field(..., example="Rome, Roma Capitale, Lazio, Italia")
    class Config:
        json_schema_extra = {
            "example": {
                "lat": 41.902782,
                "lon": 12.496366,
                "display_name": "Rome, Roma Capitale, Lazio, Italia"
            }
        }