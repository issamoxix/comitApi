FROM python:3.11-slim as base

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

EXPOSE 80

CMD ["fastapi", "run", "app.py", "--port", "80"]