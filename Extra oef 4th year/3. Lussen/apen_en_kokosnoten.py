# https://dodona.be/nl/courses/107/series/1295/activities/654951832

import math

# Splitting function
def Split(Pirates, Coconuts, Coconuts_Monkey, Pirate_Count):

    For_Me = math.floor(Coconuts / Pirates)
    For_Monkey = Coconuts_Monkey + Coconuts % Pirates
    Coconuts_Left = Coconuts - (For_Me + For_Monkey)

    if For_Monkey == 0:
        print(f"{Coconuts} noten = {For_Me} noten voor piraat#{Pirate_Count} en geen noten voor de aap")
    elif For_Monkey == 1:
        print(f"{Coconuts} noten = {For_Me} noten voor piraat#{Pirate_Count} en 1 noot voor de aap")
    else:
        print(f"{Coconuts} noten = {For_Me} noten voor piraat#{Pirate_Count} en {For_Monkey} noten voor de aap")

    return Coconuts_Left

# Amount of pirates
Pirates = int(input())

# Amount of coconuts
Coconuts = int(input())

# Start amount of Monkey nuts
End_Monkey = 0

# Pirate counter
Pirate_Count = 1

for x in range(1, Pirates + 1):
    Coconuts = Split(Pirates, Coconuts, End_Monkey, x)

End_Pirates = math.floor(Coconuts / Pirates)
End_Monkey = Coconuts % Pirates

if End_Monkey == 0:
    print(f"elke piraat krijgt {End_Pirates} noten en geen noten voor de aap")
elif End_Monkey == 1:
    print(f"elke piraat krijgt {End_Pirates} noten en 1 noot voor de aap")
else:
    print(f"elke piraat krijgt {End_Pirates} noten en {End_Monkey} noten voor de aap")
