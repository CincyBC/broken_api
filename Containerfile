FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY . /main_app

WORKDIR /main_app
RUN uv sync --frozen --no-cache
ENV PYTHONUNBUFFERED=1

CMD ["/main_app/.venv/bin/uvicorn", "app.main:app", "--port", "8000", "--host", "0.0.0.0"]
