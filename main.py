from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from views import router as ocr_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ocr_router, prefix="/api")

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/driver_license", response_class=HTMLResponse)
async def driver_license(request: Request):
    return templates.TemplateResponse("driver_license.html", {"request": request})

@app.get("/carte_crise", response_class=HTMLResponse)
async def carte_crise(request: Request):
    return templates.TemplateResponse("carte_crise.html", {"request": request})

@app.get("/idcard", response_class=HTMLResponse)
async def idcard(request: Request):
    return templates.TemplateResponse("idcard.html", {"request": request})
