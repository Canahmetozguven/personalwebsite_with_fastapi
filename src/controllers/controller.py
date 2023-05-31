
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.templating import Jinja2Templates
from src.workers.db_connection import read_data

router = APIRouter()
templates = Jinja2Templates(directory="src/views/templates")



@router.get("/", name="index")
async def index(request: Request):
    person = read_data()
    return templates.TemplateResponse("index.html", {"request": request, "person": person})

