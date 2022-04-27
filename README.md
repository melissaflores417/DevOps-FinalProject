# DevOps-FinalProject

This project is for CS491. It is a simple OOP Poker game that includes integration and unit tests. 

The project demonstrates unit testing of the function within the hand class as well integration testing to test the interaction between functions from the hand class and the player class. 

For automated tests, build and deployment, I utilized Github actions and Docker. 

To run the program:
python3 poker_game.py

How to trigger automation:
Simply make a change to a file such as adding a new blank line.
- Commit changes
- Push to repository 
- Watch it do its thing

docker instructions: 
docker pull ghcr.io/melissaflores417/devops-finalproject:main
docker build -t melissaflores417/cs491
docker push melissaflores417/cs491
