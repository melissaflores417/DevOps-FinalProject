FROM ubuntu:latest

RUN apt update
RUN apt install python3 -y
RUN pip install numpy


WORKDIR /usr/src/app

COPY . .

CMD [ "python3", "poker_game.py"]