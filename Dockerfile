FROM python:3.10
FROM FROM ghcr.io/melissaflores417/devops-finalproject:main
WORKDIR /usr/src/app

COPY . .

CMD [ "python3", "./poker_game.py"]