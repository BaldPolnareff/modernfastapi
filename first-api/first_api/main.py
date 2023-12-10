from fastapi import FastAPI, Query, responses, status, Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from typing import Annotated, Union, Optional
import uvicorn 
from pathlib import Path
import json

from api import weather_api
from views import home
from services import openweather_service

app = FastAPI()

def configure(): 
    configure_mountpoints()
    configure_routing()
    configure_apikeys()

def configure_routing():
    app.include_router(weather_api.router)
    app.include_router(home.router)

def configure_mountpoints():
    app.mount("/static", StaticFiles(directory="static"), name="static")

def configure_apikeys():
    file = Path(__file__).parent / '.env/settings.json'
    if not file.is_file(): 
        raise Exception('No settings file found, please check settings_template.json')
    with open(file) as f:
        settings = json.load(f)
        openweather_service.api_key = settings["api_key"]

if __name__ == '__main__':
    configure()
    uvicorn.run(app, host='127.0.0.1', port=8000)
else: 
    configure()

