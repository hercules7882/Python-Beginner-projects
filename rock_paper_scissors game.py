import random
options = ('rock', 'paper', 'scissors')
playing = True
while playing:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter your choice(rock, paper, or scissors): ")
    print(f"You choose: {player}")
    print(f"Computer choose: {computer}")

    if player == computer:
        print("Draw!")
    elif player == 'rock' and computer == 'scissors':
        print("you win!")
    elif player == 'paper' and computer == 'rock':
        print("you win!")
    elif player == 'scissors' and computer == 'paper':
        print("you win!")
    else:
        print("you lose!")

    if not input("Do you want to play again?(y/n): ").lower() == 'y':
        playing = False
print("Thanks for playing!")

