player1 = input()
player2 = input()

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
