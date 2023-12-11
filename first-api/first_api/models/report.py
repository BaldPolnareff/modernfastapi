from pydantic import BaseModel, Field

class WeatherReport(BaseModel): 
    coord: dict = Field(..., example={
        "lon": 12.4964,
        "lat": 41.9028
    })
    weather: list = Field(..., example=[
        {
            "id": 803,
            "main": "Clouds",
            "description": "broken clouds",
            "icon": "04d"
        }
    ])
    base: str = Field(..., example="stations")
    main: dict = Field(..., example={
        "temp": 294.15,
        "feels_like": 293.45,
        "temp_min": 293.15,
        "temp_max": 295.15,
        "pressure": 1016,
        "humidity": 78
    })
    visibility: int = Field(..., example=10000)
    wind: dict = Field(..., example={
        "speed": 1.54,
        "deg": 0, 
        "gust": 3.09
    })
    clouds: dict = Field(..., example={
        "all": 75
    })
    dt: int = Field(..., example=1621994454)
    sys: dict = Field(..., example={
        "type": 2,
        "id": 2008959,
        "country": "IT",
        "sunrise": 1621950814,
        "sunset": 1622008230
    })
    timezone: int = Field(..., example=7200)
    id: int = Field(..., example=3169070)
    name: str = Field(..., example="Rome")
    cod: int = Field(..., example=200)