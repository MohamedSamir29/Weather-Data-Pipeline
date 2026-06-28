import os

#API

API_BASE_URL = "https://api.open-meteo.com/v1/forecast"

API_PARAMS = {
    "hourly": [
        "temperature_2m",
        "relative_humidity_2m",
        "precipitation",
        "wind_speed_10m",
        "weather_code",
    ],
    "timezone": "Africa/Cairo",
    "past_days": 1,
}

#Database

DB_CONFIG = {
    "host":     os.environ.get("POSTGRES_HOST",     "localhost"),
    "port":     int(os.environ.get("POSTGRES_PORT", 5432)),
    "dbname":   os.environ.get("POSTGRES_DB",       "weather_db"),
    "user":     os.environ.get("POSTGRES_USER",     "postgres"),
    "password": os.environ.get("POSTGRES_PASSWORD", "postgres"),
}

#Logging

LOG_FILE = "logs/pipeline.log"