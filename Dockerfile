FROM ubuntu:latest

RUN sudo apt-get update -y
RUN sudo apt-get install -y python
RUN pip3 install numpy

WORKDIR /usr/src/app

COPY . .

CMD [ "python3", "poker_game.py"]