FROM python:3.10

WORKDIR /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt


COPY . .

CMD [ "python3", "poker_game.py"]