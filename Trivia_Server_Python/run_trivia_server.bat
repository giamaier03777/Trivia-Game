@echo off
echo Stopping and removing any existing trivia-server containers...

docker ps -q --filter "name=trivia-server" | findstr . >nul && docker stop trivia-server

docker ps -aq --filter "name=trivia-server" | findstr . >nul && docker rm trivia-server

echo Building the trivia-server Docker image...
docker build -t trivia-server .

echo Running the trivia-server Docker container...
docker run -d -p 12345:12345 --name trivia-server trivia-server