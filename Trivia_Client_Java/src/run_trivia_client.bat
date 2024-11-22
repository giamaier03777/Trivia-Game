@echo off
echo Stopping and removing any existing trivia-client containers...

:: Oprește containerul trivia-client dacă rulează
docker ps -q --filter "ancestor=trivia-client" | findstr . >nul && docker stop trivia-client

:: Șterge containerul trivia-client dacă există
docker ps -aq --filter "ancestor=trivia-client" | findstr . >nul && docker rm trivia-client

echo Building the trivia-client Docker image...
docker build -t trivia-client .

echo Running the trivia-client Docker container...
docker run -it --rm --name trivia-client --network="host" trivia-client /bin/bash
