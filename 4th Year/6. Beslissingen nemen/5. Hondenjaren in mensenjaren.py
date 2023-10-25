AgeD = float(input('INput here'))

if AgeD <= 2:
    AgeM = AgeD * 10.5
else:
    AgeM = (AgeD - 2) * 4 + 21
    
print('Een hond van', AgeD, 'jaar oud is', AgeM, 'jaar in mensenleeftijd')
