FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN pip install uv && uv sync --frozen --no-install-project

COPY api_pro.py ./

CMD ["uv", "run", "--no-sync", "python", "api_pro.py"]