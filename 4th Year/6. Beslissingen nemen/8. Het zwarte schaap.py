N1 = int(input('N1: '))
N2 = int(input('N2: '))
N3 = int(input('N3: '))

if N2 == N3: #N1 is the black sheep
    print('Het eerste getal, nl.', N1, 'is het zwarte schaap.')
elif N1 == N3: #N2 is the black sheep
    print('Het tweede getal, nl.', N2, 'is het zwarte schaap.')
else: #N3 is the black sheep
    print('Het derde getal, nl.', N3, 'is het zwarte schaap.')
