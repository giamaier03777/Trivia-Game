FROM python:3.8-slim

WORKDIR /app

COPY TriviaServer.py .
COPY questions.json .

EXPOSE 12345

CMD ["python", "TriviaServer.py"]
