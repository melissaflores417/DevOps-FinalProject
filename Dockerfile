FROM ubuntu:latest

RUN python3 -m pip3



WORKDIR /usr/src/app

COPY . .

CMD [ "python3", "-m", "unittest", "tests.py"]