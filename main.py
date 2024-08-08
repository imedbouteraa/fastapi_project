from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from views import router as ocr_router

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this according to your needs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ocr_router, prefix="/api")

@app.get("/")
async def read_root():
    return {"message": "Welcome to the OCR API. Please navigate to /api/ocr/driver_license/ to access the API."}
if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))  # Default to 8000 if PORT not set
    uvicorn.run(app, host="0.0.0.0", port=port)
