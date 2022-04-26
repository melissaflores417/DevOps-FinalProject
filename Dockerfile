FROM ubuntu:latest

RUN python3 install pip3
RUN pip3 install numpy


WORKDIR /usr/src/app

COPY . .

CMD [ "python3", "tests.py"]