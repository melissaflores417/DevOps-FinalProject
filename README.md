# DevOps-FinalProject

This project is for CS491. It is a simple OOP Poker game that includes integration and unit tests. 

The project demonstrates unit testing of the function within the hand class as well integration testing to test the interaction between functions from the hand class and the player class. 

For automated tests, build and deployment, I utilized Github actions and Docker. 

How to trigger automation:
Simply make a change to a file such as adding a new blank line.
- Commit changes
- Push to repository 
- Watch it do its thing

Test coverage:
Coverage reached 100% in hand.py, 77% in player.py

docker instructions: 
docker pull ghcr.io/melissaflores417/devops-finalproject:main

There is an issue when running:
docker run ghcr.io/melissaflores417/devops-finalproject:main

It is not recognizing the numpy import, however when you run, 
python3 poker_game.py regularly, it runs fine.

