from typing import Optional
import httpx 
from httpx import Response
# from first_api.models.deprecated.geolocation_model import GeoCodingAPILocation
# from first_api.models.deprecated.weather_model import WeatherModel
from models.location import SimpleLocation, GeoCodingAPILocation
from models.report import WeatherReport
from models.validation_error import ValidationError
from fastapi import status

api_key: Optional[str] = None

async def get_geocoding_location(city: str, state: Optional[str], country: str) -> GeoCodingAPILocation:
    """
    Returns a weather report for the specified location. The idea is to use the direct 
    geocoding API to get the latitude and longitude of the location, then use lat and lon 
    to call the free tier weather API.
    """
    query = f"{city},{country}"
    q = f"{city},{state},{country}" if state else query
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={q}&appid={api_key}"

    if state: 
        q += f",{state}"

    async with httpx.AsyncClient() as client:
        geocoding_response: Response = await client.get(url)
        if geocoding_response.status_code != status.HTTP_200_OK:
            raise ValidationError(message = geocoding_response.text, status_code = geocoding_response.status_code)
        elif not len(geocoding_response.json()):
            raise ValidationError(message = "Invalid location", status_code = status.HTTP_404_NOT_FOUND)

    geocoding_data = geocoding_response.json() # it's a single element list :/

    geocoding_location = GeoCodingAPILocation(
        lat=geocoding_data[0]["lat"],
        lon=geocoding_data[0]["lon"],
        display_name=geocoding_data[0]["name"]
    )
    
    return geocoding_location
    
async def get_report_from_geocoding_location(loc: SimpleLocation, units: str) -> WeatherReport:
    """
    Returns a weather report for the specified location. The idea is to use the direct 
    geocoding API to get the latitude and longitude of the location, then use lat and lon 
    to call the free tier weather API.
    """
    coords: GeoCodingAPILocation = await get_geocoding_location(loc.city, loc.state, loc.country)

    url = f"http://api.openweathermap.org/data/2.5/weather?lat={coords.lat}&lon={coords.lon}&units={units}&appid={api_key}"
    
    async with httpx.AsyncClient() as client:
        weather_response: Response = await client.get(url)
        if weather_response.status_code != status.HTTP_200_OK:
            raise ValidationError(message = weather_response.text, status_code = weather_response.status_code)

    weather_data = weather_response.json()

    weather_model = WeatherReport(**weather_data)

    return weather_model