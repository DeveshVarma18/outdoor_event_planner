from fastapi import APIRouter
from fastapi.responses import JSONResponse
import requests
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

@router.get("/weather/{city}")
def get_weather(city: str):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        return JSONResponse(status_code=404, content={"error": "City not found"})
    data = response.json()
    weather_desc = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    return {"description": weather_desc, "temperature": temp}
