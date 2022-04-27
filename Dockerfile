FROM python:3.10

WORKDIR /usr/src/app

RUN sudo install python3-pip
RUN sudo pip3 install numpy

COPY . .

CMD [ "python3", "./poker_game.py"]