N = [int(input()) for _ in range(3)] # Get the 3 numbers

if N[1] == N[2]: #N1 is the black sheep
    print(f'Het eerste getal, nl. {N[0]} is het zwarte schaap.')
elif N[0] == N[2]: #N2 is the black sheep
    print(f'Het tweede getal, nl. {N[1]} is het zwarte schaap.')
else: #N3 is the black sheep
    print(f'Het derde getal, nl. {N[2]} is het zwarte schaap.')

# N1 = int(input('N1: '))
# N2 = int(input('N1: '))
# N3 = int(input('N1: '))

# if N2 == N3: #N1 is black
#     print(f'Het eerste getal, nl. {N1} is het zwarte schaap.')
# elif N1 == N3: #N2 is black
#     print(f'Het tweede getal, nl. {N2} is het zwarte schaap.')
# else: #N3 is black
#     print(f'Het derde getal, nl. {N3} is het zwarte schaap.')
