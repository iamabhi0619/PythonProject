from random import randint
from pyfiglet import figlet_format
# text=pyfiglet.print_figlet(text="Guess The Number",colour="BLUE",font="isometric1")
# print(text)
print(figlet_format("Guess The Number", font = "isometric1"))
print("Guess the number between 1 to 50..!!")
print("""
Easy Level:
Difficulty: Easy
Number of Chances: 10
      
Medium Level:
Difficulty: Medium
Number of Chances: 7
      
Hard Level:
Difficulty: Hard
Number of Chances: 4
""")

chance = 0
ai = randint(1,50)
def turn(level):
    global chance
    if(level == "easy"):
        chance = 9
    elif(level == "medium"):
        chance = 6
    elif(level == "hard"):
        chance = 3
    return chance
def guess(ch,gn,ai):
    while ch > 0:
        print(ai)
        if gn == ai:
            print("You have gussed the number correctly..!!")
            break
        elif gn < ai:
            print("You are on lower side")
        elif gn > ai:
            print("You are on higher side")

        gn = int(input("Trying gussing the number again:- "))
        
        ch -= 1  # Decrement chances

    if ch == 0:
        print("Out of chances. The number was:", ai)
#value of chance
level = input("Please choose your lavel:- ").lower()
while level not in ("hard", "medium", "easy"):
    level = input("Enter a valid choice(Hard/Medium/easy):- ").lower()    
turn(level)
ch = int(input("Enter the number you gussed:- "))
guess(chance,ch,ai)