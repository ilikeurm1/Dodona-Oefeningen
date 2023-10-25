# https://dodona.be/nl/courses/107/series/1295/activities/1432498809

import math

Hitchers = int(input())

Passed = math.floor(Hitchers / 2)
First_Half = []
Second_Half = []

for x in range(Passed):
    Score = float(input())
    First_Half.append(Score)

Nicest = max(First_Half)

while Passed != Hitchers:
    Score = float(input())
    if Score > Nicest:
        Second_Half.append(Score)
    if Second_Half == [] and Passed == Hitchers - 1:
        Second_Half.append(Score)
    Passed += 1

Nicest = Second_Half[0]

print(Nicest)
