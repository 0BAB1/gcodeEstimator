FROM python:3.11.3

WORKDIR /app

COPY . .

CMD ["python", "main.py"]