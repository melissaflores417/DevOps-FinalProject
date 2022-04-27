FROM python:3.10

WORKDIR /usr/src/app

COPY . .

CMD [ "python3", "./poker_game.py"]