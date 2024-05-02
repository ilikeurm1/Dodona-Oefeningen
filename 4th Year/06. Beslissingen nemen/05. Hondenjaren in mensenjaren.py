D = float(input())

if D <= 2:
    M = D * 10.5
else:
    M = (D - 2) * 4 + 21
    
print(f'Een hond van {D} jaar oud is {M} jaar in mensenleeftijd')
