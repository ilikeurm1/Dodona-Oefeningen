C = float(input())
print(f"{C} graden Celsius staat gelijk aan {round(C * 1.8 + 32, 2)} graden Fahrenheit")

if C > 0 and C < 100: # vloeibaar
    print('Het water is vloeibaar')
elif C >= 100: # gas
    print('Het water kookt')
else: # vast
    print('Het water bevriest')

# C = float(input())
# F = round(C * 1.8 + 32, 2)
