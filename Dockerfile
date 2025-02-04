FROM python:3.12.8-slim-bookworm

COPY . /project

WORKDIR /project

RUN apt-get update && apt-get install -y libpq-dev gcc && pip install -r requirements.txt

CMD ["fastapi", "run", "app/main.py", "--proxy-headers", "--port", "80"]