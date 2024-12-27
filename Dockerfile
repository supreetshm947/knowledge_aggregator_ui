FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN pip install poetry
RUN poetry install --no-root --only main

COPY app/ .

EXPOSE 8501

CMD ["poetry", "run", "streamlit", "run", "index.py", "--server.port=8501", "--server.address=0.0.0.0"]
