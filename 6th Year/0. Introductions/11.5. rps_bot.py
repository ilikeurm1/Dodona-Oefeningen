import random

def check(input_str, player=None):
    valid_choices = ['rock', 'paper', 'scissors']
    if input_str.lower().strip() in valid_choices:
        return input_str.lower().strip()
    else:
        raise ValueError(f"Invalid choice by {player if player else 'unknown'}. Please choose rock, paper, or scissors.")

comp = random.choice(['rock', 'paper', 'scissors'])
p = check(input("Enter your choice (rock, paper, scissors): "), player="Player")

if p == comp:
    print("It's a tie!")
elif (p == 'rock' and comp == 'scissors') or (p == 'paper' and comp == 'rock') or (p == 'scissors' and comp == 'paper'):
    print("Player wins!")
else:
    print("Computer wins!")
