# basic rock paper scissors game
print("rock...")
print("paper...")
print("scissors...")

player1 = input("player 1 choose, rock, papaer or scissors: ")

for line in range(10):
    print("No Cheeting")

player2 = input("player 2 choose, rock, papaer or scissors: ")

if player1 == "rock" and player2 == "scissors":
    print("player1 wins")
elif player1 == player2:
    print("Draw")
else:
    print("something went wrong")
