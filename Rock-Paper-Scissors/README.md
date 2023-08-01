# Rock-Paper-Scissors Game in Python

![Rock-Paper-Scissors](rock_paper_scissors.png)

This is a simple rock-paper-scissors game implemented in Python. The game allows you to play against the computer and keeps track of your score and the computer's score.

## How to Play

1. Clone or download the repository to your local machine.
2. Make sure you have Python installed on your computer.
3. Run the `rock_paper_scissors.py` script using Python.
4. Follow the on-screen instructions to enter your choice (rock, paper, or scissors) for each round of the game.
5. The computer will randomly choose its move, and the winner of each round will be determined according to the classic rock-paper-scissors rules.
6. The game will run for 5 rounds, and at the end of the game, the overall winner will be announced.

## Rules of the Game

- Rock vs Scissors --> Rock Wins
- Scissors vs Paper --> Scissors Wins
- Paper vs Rock --> Paper Wins

## Features

- Interactive user interface with text-based prompts.
- Simple input validation to ensure the user enters a valid choice.
- Random computer choice using Python's `random` module.
- Score tracking for the user and computer.
- Overall winner determination after 5 rounds.

## Screenshots

_Include some screenshots of the game in action (optional)_

## Example Usage

```bash
$ python rock_paper_scissors.py
<-- Welcome TO Game of Childhood -->

Rules of the game:
Game will be of 5 rounds
You will be playing with the computer's choice.
Rock vs Scissors --> Rock Wins..!!
Scissors vs Paper --> Scissors Wins..!!
Paper vs Rock --> Paper Wins..!!
Initial Score of yours and the computer will be zero(0)

Enter Your Name: John
Hello John, Welcome to the game..!!

Round 1: Enter your choice (Rock/Paper/Scissors): rock
Computer choice: scissors
You Win..!! Rock smashes the Scissors
Your score= 1
Computer score= 0
Ties= 0

Round 2: Enter your choice (Rock/Paper/Scissors): paper
Computer choice: rock
You Win..!! Paper covers the Rock
Your score= 2
Computer score= 0
Ties= 0

...

John Score--> 3
Computer Score--> 1
Ties--> 1
John, You win the game..!!

Thank You..!!
