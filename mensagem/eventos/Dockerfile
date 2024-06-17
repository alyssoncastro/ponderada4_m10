FROM python:3.9-slim

WORKDIR /app

COPY eventos.py requirements.txt ./

RUN pip install -r requirements.txt

CMD ["python", "eventos.py"]
