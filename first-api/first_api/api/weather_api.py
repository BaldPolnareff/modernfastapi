from fastapi import APIRouter, Query, responses, status, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse, RedirectResponse

from models.location import SimpleLocation
from models.weather_model import WeatherModel

from services import openweather_service


router = APIRouter()

@router.get('/api/weather/{city}')
async def weather(loc: SimpleLocation = Depends(), units: str = 'metric') -> WeatherModel:
    """
    Returns a weather report for the specified location. The idea is to use the direct
    geocoding API to get the latitude and longitude of the location, then use lat and lon
    to call the free tier weather API.
    """    
    weather: WeatherModel = openweather_service.get_report_from_geocoding_location(city=loc.city, state=loc.state, country=loc.country, units=units)

    return weather