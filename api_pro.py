
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select
import requests



class WeatherReading(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    fetched_at: str
    temperature_c: float
    humidity_pct: float
    wind_speed_kmh: float

import os
from dotenv import load_dotenv

load_dotenv()
postgres_url = os.environ.get("DATABASE_URL")
engine = create_engine(postgres_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

create_db_and_tables()
def fetch_and_save_weather():
    response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=47.53&longitude=21.63&current=temperature_2m,relative_humidity_2m,wind_speed_10m")

    data = response.json()

    current = data["current"]


    new_reading = WeatherReading(
    fetched_at= current["time"],
    temperature_c= current["temperature_2m"],
    humidity_pct= current["relative_humidity_2m"],
    wind_speed_kmh=current["wind_speed_10m"]
    )

    with Session(engine) as session:
        session.add(new_reading)
        session.commit()

    with Session(engine) as session:
        results = session.exec(select(WeatherReading)).all()
        print(results)
fetch_and_save_weather()
