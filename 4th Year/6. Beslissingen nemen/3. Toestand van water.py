TempC = float(input('temperature in C: '))
TempF = TempC * 1.8 + 32

print(f'{TempC}graden Celsius staat gelijk aan {round(TempF, 2)} graden Fahrenheit')
if TempC > 0 and TempC < 100: # vloeibaar
    print('Het water is vloeibaar')
elif TempC >= 100: # gas
    print('Het water kookt')
else: # vast
    print('Het water bevriest')
    