from typing import Optional
import httpx 
# from first_api.models.deprecated.geolocation_model import GeoCodingAPILocation
# from first_api.models.deprecated.weather_model import WeatherModel
from models.location import SimpleLocation, GeoCodingAPILocation
from models.report import WeatherReport

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

    geocoding_location = GeoCodingAPILocation(
        lat=geocoding_data[0]["lat"],
        lon=geocoding_data[0]["lon"],
        display_name=geocoding_data[0]["name"]
    )
    
    return geocoding_location
    
def get_report_from_geocoding_location(loc: SimpleLocation, units: str) -> WeatherReport:
    """
    Returns a weather report for the specified location. The idea is to use the direct 
    geocoding API to get the latitude and longitude of the location, then use lat and lon 
    to call the free tier weather API.
    """
    coords: GeoCodingAPILocation = get_geocoding_location(loc.city, loc.state, loc.country)

    url = f"http://api.openweathermap.org/data/2.5/weather?lat={coords.lat}&lon={coords.lon}&units={units}&appid={api_key}"
    
    weather_response = httpx.get(url)

    weather_response.raise_for_status()

    weather_data = weather_response.json()

    weather_model = WeatherReport(**weather_data)

    return weather_model