from fastapi import APIRouter, Query, responses, status, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse

from models.location import SimpleLocation
from models.report import WeatherReport
from models.validation_error import ValidationError

from services import openweather_service
from services.fake_crud import get_reports, add_report
from local_data.fake_db.fake_reports import reports as db


router = APIRouter()

@router.get('/api/weather/{city}', response_model=WeatherReport)
async def weather(loc: SimpleLocation = Depends(), units: str = 'metric') -> WeatherReport:
    """
    Returns a weather report for the specified location. The idea is to use the direct
    geocoding API to get the latitude and longitude of the location, then use lat and lon
    to call the free tier weather API.
    """   
    try: 
        weather: WeatherReport = await openweather_service.get_report_from_geocoding_location(loc, units)
        return weather
    except ValidationError as ve:
        return JSONResponse(status_code=ve.status_code, content={f'{ve.status_code}': f'{ve.message}'})
    
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={f'{status.HTTP_500_INTERNAL_SERVER_ERROR}': f'{e}'})
    

@router.get('/api/reports', response_model=list[WeatherReport])
async def get_all_reports() -> list[WeatherReport]: 
    reports = get_reports()
    return reports

@router.post('/api/reports', status_code=status.HTTP_201_CREATED)
async def create_report(report: WeatherReport) -> list[dict]:
    add_report(report)
    return get_reports()