import random

random_number = random.randint(1, 10)
# guess = 0

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess > random_number:
        print("Too high")
    elif guess < random_number:
        print("Too low")
    else:
        print("You guessed it! You won!")
        play_again = input("Play again?? (y/n) ")
        if play_again == "y":
            random_number = random.randint(1, 10)
            # guess = None
        else:
            print("Ok, thanks for playing")
            break
