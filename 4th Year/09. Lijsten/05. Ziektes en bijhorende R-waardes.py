ziekte = ['Griep', 'Ebola', 'Covid', 'Sars', 'Pokken', 'Bof', 'Mazelen']
R_waarde = [2.1, 2.5, 3.9, 5, 6, 7, 18]

for x in range(len(ziekte)):
    print(f"{ziekte[x]} heeft een R-waarde van: {R_waarde[x]}")
