from typing import Optional
import httpx 
from models.geolocation_model import GeoCodingAPILocation
from models.weather_model import WeatherModel

api_key: Optional[str] = None

def get_geocoding_location(city: str, state: Optional[str], country: str) -> GeoCodingAPILocation:
    """
    Returns a weather report for the specified location. The idea is to use the direct 
    geocoding API to get the latitude and longitude of the location, then use lat and lon 
    to call the free tier weather API.
    """
    query = f"{city},{country}"
    q = f"{city},{state},{country}" if state else query
    url = f"http://api.openweathermap.org/geo/1.0/direct?q=q&appid={api_key}"

    if state: 
        q += f",{state}"

    geocoding_response = httpx.get(url)

    geocoding_response.raise_for_status()

    geocoding_data = geocoding_response.json() # it's a single element list :/

    geocoding_location = GeoCodingAPILocation(**geocoding_data[0])
    
    return geocoding_location
    
def get_report_from_geocoding_location(city: str, state: Optional[str], country: str, units: str) -> WeatherModel:
    """
    Returns a weather report for the specified location. The idea is to use the direct 
    geocoding API to get the latitude and longitude of the location, then use lat and lon 
    to call the free tier weather API.
    """
    loc: GeoCodingAPILocation = get_geocoding_location(city, state, country)

    url = f"http://api.openweathermap.org/data/2.5/onecall?lat={loc.lat}&lon={loc.lon}&units={units}&appid={api_key}"
    
    weather_response = httpx.get(url)

    weather_response.raise_for_status()

    weather_data = weather_response.json()

    weather_model = WeatherModel(**weather_data)

    return weather_model