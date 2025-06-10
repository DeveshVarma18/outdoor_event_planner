from fastapi import FastAPI
from src.db import models, database
from src.api import events, weather
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Outdoor Event Planner")

# Create database tables
models.Base.metadata.create_all(bind=database.engine)

# Include routers
app.include_router(events.router, prefix="/events", tags=["events"])
app.include_router(weather.router, prefix="/weather", tags=["weather"])

@app.get("/", summary="Root endpoint")
def read_root():
    return {"message": "Welcome to Outdoor Event Planner API"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or set your frontend URL instead of "*"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

