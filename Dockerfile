FROM python:3.10

WORKDIR /usr/src/app

RUN pip3 install numpy

COPY . .

CMD [ "python3", "./poker_game.py"]