from random import randint

#score
us = 0
cs = 0
tie = 0
t = ["rock", "paper", "scissors"]
print("<-- Welcome TO Game of Childhood -->")
print()
print("""
    Rules of the game:
    Game will be of 5 round
    You will be playing with computer choice.
    Rock vs Scissors --> Rock Wins..!!
    Scissors vs Paper --> Scissors Wins..!!
    Paper vs Rock --> Paper Wins..!!
    Initial Score of your and compuer will be zero(0)""")
print()
name = input("Enter Your Name:- ")
print("Hello",name,"Welcome to the game..!!")
print()
#loop
n = 0
while(n<5):
    print("<--- ROUND",n+1,"--->")
    print("Rock / Paper / Scissors")
    user_choice = input("Enter your choice:- ").lower()
    while user_choice not in ("rock", "paper", "scissors"):
        user_choice = input("Enter a valid choice(Rock/Paper/Scissors):- ").lower()
    comp_choice = t[randint(0,2)]
    print("Computer choice:-",comp_choice)

    #contition
    if user_choice == comp_choice:
        print("its a tie")
        tie += 1
    elif user_choice == "paper":
        if comp_choice == "rock":
            print("You Wins..!! Paper covers the Rock")
            us += 1
        else:
            print("You loos..!! Scissors cuts the Paper")
            cs += 1
    elif user_choice == "rock":
        if comp_choice == "scissors":
            print("You Wins..!! Rock smashes the Scissors")
            us += 1
        else:
            print("You loos..!! Paper covers the Rock")
            cs += 1
    elif user_choice == "scissors":
        if comp_choice == "paper":
            print("You Wins..!! scissors cuts the Paper")
            us += 1
        else:
            print("You loos..!! Rock smashes the Scissors")
            cs += 1
    print("You score= ",us)
    print("Computer score= ",cs)
    print("Ties= ",tie)
    print()
    print()
    n += 1

print(name,"Score--> ",us)
print("Computer Score-->",cs)
print("Ties-->",tie)
if(us>cs):
    print(name,",You wins the game..!!")
elif(cs>us):
    print("Computer Wins the game..!!")
else:
    print("All Five where Ties..!!")
print("Thank You..!!")