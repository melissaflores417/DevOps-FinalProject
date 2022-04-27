FROM python:3.10

WORKDIR /usr/src/app

RUN python3 -m pip install numpy

COPY . .

CMD [ "python3", "./poker_game.py"]