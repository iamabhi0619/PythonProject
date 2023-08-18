from random import randint

def main():
    print("GUESS THE NUMBER")
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

    secret_number = randint(1, 50)
    
    def set_chances(difficulty_level):
        difficulty_to_chances = {"easy": 10, "medium": 7, "hard": 4}
        return difficulty_to_chances.get(difficulty_level, 0)
    
    message_by_difference = [
        "You have guessed the number correctly..!!",
        "You are very close!",
        "You are very close!",
        "You are getting closer.",
        "You are getting closer.",
        "You are getting closer.",
        "You are way off!",
        "You are way off!",
        "You are way off!",
        "You are way off!",
        # ... and so on
    ]
    
    def play_guessing_game(target_number):
        chances_left = set_chances(difficulty_level)
        while chances_left > 0:
            guessed_number = int(input("Enter the number you guessed: "))
            difference = abs(target_number - guessed_number)
            if difference < len(message_by_difference):
                print(message_by_difference[difference])
                if difference == 0:
                    break
            print("You are on the lower side" if guessed_number < target_number else "You are on the higher side")
            
            chances_left -= 1
    
    difficulty_level = input("Please choose your level (easy/medium/hard): ").lower()
    while difficulty_level not in ("hard", "medium", "easy"):
        difficulty_level = input("Enter a valid choice (Hard/Medium/Easy): ").lower()
    
    play_guessing_game(secret_number)

if __name__ == "__main__":
    main()
