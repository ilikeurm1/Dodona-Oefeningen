# ---> Variables <---

Options = ['rock', 'paper', 'scissors']
Worked = None # I just make this for checks

# ---> Inputs <---

player1 = input('RPC 1: ')
player2 = input('RPC 2: ')

# ---> Outputs <---

if player1 in Options and player2 in Options:
	Worked = True
	if player1 == player2: # tie
		print(f'tie')
	elif player1 == 'rock':
		if player2 == 'paper':
			print('player2 wins')
		else:
			print('player1 wins')
	elif player1 == 'paper':
		if player2 == 'scissors':
			print('player2 wins')
		else:
			print('player1 wins')
	elif player1 == 'scissors':
		if player2 == 'rock':
			print('player2 wins')
		else:
			print('player1 wins')
else:
	Worked = False
	if not Worked:
			print('Invalid input')