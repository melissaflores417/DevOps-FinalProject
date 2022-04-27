FROM ubuntu:latest

RUN pip3 install numpy


WORKDIR /usr/src/app

COPY . .

CMD [ "python3", "poker_game.py"]