def check(input_str, player=None):
    valid_choices = ['rock', 'paper', 'scissors']
    if input_str.lower().strip() in valid_choices:
        return input_str.lower().strip()
    else:
        raise ValueError(f"Invalid choice by {player if player else 'unknown'}. Please choose rock, paper, or scissors.")

p1 = check(input("Player 1, enter your choice (rock, paper, scissors): "), player="Player 1")
p2 = check(input("Player 2, enter your choice (rock, paper, scissors): "), player="Player 2")

if p1 == p2:
    print("It's a tie!")
elif (p1 == 'rock' and p2 == 'scissors') or (p1 == 'paper' and p2 == 'rock') or (p1 == 'scissors' and p2 == 'paper'):
    print("Player 1 wins!")
else:
    print("Player 2 wins!")