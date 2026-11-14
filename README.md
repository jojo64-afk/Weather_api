# Weather API

A FastAPI + PostgreSQL service that fetches live weather data from the [Open-Meteo](https://open-meteo.com/) API, stores it in a relational database, and exposes it for querying. Containerized with Docker for portable, environment-independent deployment.

## What it does

- Fetches current weather (temperature, humidity, wind speed) for a fixed location via the Open-Meteo API
- Stores each reading as a row in PostgreSQL, using [SQLModel](https://sqlmodel.tiangolo.com/) for the ORM layer
- Prints all stored readings on each run

## Tech stack

- **Python**
- **FastAPI** — web framework (API layer)
- **SQLModel** — ORM built on SQLAlchemy + Pydantic
- **PostgreSQL** — database (hosted on [Neon](https://neon.tech))
- **Docker** — containerized runtime
- **uv** — dependency management

## Running locally

1. Install dependencies:
   ```bash
   uv sync
   ```
2. Create a `.env` file with your database connection string:

DATABASE_URL=postgresql://user:password@host/dbname

3. Run:
   ```bash
   uv run python api_pro.py
   ```

## Running with Docker

Build the image:
```bash
docker build -t weather-api .
```

Run it, passing in your environment variables:
```bash
docker run --env-file .env weather-api
```

This builds and runs the service inside an isolated container — no local Python, uv, or dependency setup required on the host machine beyond Docker itself.

## Notes

- `.env` is intentionally excluded from the image and from version control (see `.gitignore`) — credentials are always supplied at runtime, never baked into the image or committed.