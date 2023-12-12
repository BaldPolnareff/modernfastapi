from fastapi import APIRouter, Request, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles 
from starlette.templating import Jinja2Templates
from typing import Annotated, Union, Optional

router = APIRouter()

templates = Jinja2Templates(directory="templates")

# router.mount("/static", StaticFiles(directory="static"), name="static")

@router.get('/', include_in_schema=False)
async def index(request: Request):
    return templates.TemplateResponse("home/index.html", {"request": request})

@router.get('/logo/{format}')
def favicon(format: str):
    if format == 'png':
        return RedirectResponse(url='/static/img/cloud.png')
    elif format == 'svg':
        return RedirectResponse(url='/static/img/cloud.svg')
    else:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found.")
    
@router.get('/about')
def about(request: Request):
    return templates.TemplateResponse("home/about.html", {"request": request})