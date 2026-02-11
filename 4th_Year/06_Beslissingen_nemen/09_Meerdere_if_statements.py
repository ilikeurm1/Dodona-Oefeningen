Number = int(input())

Correct = 0

# Tests to see how many statements are correct
if Number % 2 == 0:
    print('Even getal')
    Correct += 1
if Number > 0:
    print('Positief getal')
    Correct += 1    
if Number > 100:
    print('Groter dan 100')
    Correct += 1
if Number > 1000:
    print('Groter dan 1000')
    Correct += 1

if Correct == 0:
    print('Dit getal voldeed aan geen enkele voorwaarde')
elif Correct == 1:
    print('Dit getal voldeed aan 1 voorwaarde') # Moet erbij voor de "n" achteraan "voorwaardeN"
elif Correct == 4:
    print('Dit getal voldeed aan alle voorwaarden')
else:
    print(f'Dit getal voldeed aan {Correct} voorwaarden')
