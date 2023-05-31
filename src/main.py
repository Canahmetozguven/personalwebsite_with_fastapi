from fastapi import FastAPI
from src.controllers.controller import router as main_router
from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

router = APIRouter()
templates = Jinja2Templates(directory="src/views/templates")
static = StaticFiles(directory="src/static")

app = FastAPI()

app.mount("/static", static, name="static")

app.include_router(main_router)
