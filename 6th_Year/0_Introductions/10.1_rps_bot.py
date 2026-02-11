import random

winning_combos = {
    'rock': 'paper',
    'paper': 'scissors',
    'scissors': 'rock'
}

beatable: bool = False

def check(input_str: str, player: str | None = None) -> str:
    valid_choices = ['rock', 'paper', 'scissors']
    input_str = input_str.lower().strip()
    if input_str in valid_choices:
        return input_str
    else:
        raise ValueError(f"Invalid choice by {player if player else 'unknown'}. Please choose rock, paper, or scissors.")

p: str = check(input("Enter your choice (rock, paper, scissors): "), player="Player")
comp: str = random.choice(['rock', 'paper', 'scissors']) if beatable else random.choice([winning_combos[p], p]) # if not beatable, computer will choose to tie or win
print(f"Computer chose: {comp}")

if p == comp:
    print("It's a tie!")
elif winning_combos[p] != comp:
    print("Player wins!")
else:
    print("Computer wins!")
