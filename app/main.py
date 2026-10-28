
from fastapi import FastAPI

from app.api.event_routes import router as event_router
from app.api.participant_routes import router as participant_router
from app.api.registration_routes import router as registration_router


app = FastAPI(
    title="Event Registration API",
    description="API untuk mengelola acara dan pendaftaran peserta.",
    version="1.0.0",
)


@app.get("/")
def home():
    return {
        "message": "Selamat datang di Event Registration API!"
    }


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(event_router)
app.include_router(participant_router)
app.include_router(registration_router)
