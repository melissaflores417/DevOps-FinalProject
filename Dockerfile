FROM python:3.10

WORKDIR /usr/src/app

RUN python3 install pip3
RUN pip3 install numpy

COPY . .

CMD [ "python3", "./poker_game.py"]