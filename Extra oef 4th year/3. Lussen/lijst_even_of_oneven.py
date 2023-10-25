# https://dodona.be/nl/courses/107/series/1246/activities/1624746422

Even = []
Uneven = []

amount = int(input())

for i in range(amount):
    x = int(input())
    if x % 2 == 0:
        Even.append(x)
    else:
        Uneven.append(x)

print(Even)
print(Uneven)
