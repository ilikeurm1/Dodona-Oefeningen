# https://dodona.be/nl/courses/107/series/1295/activities/685894639

a = int
Sum = 0
while True:
    a = float(input())
    Sum = Sum + a
    if a == 0:
        break

print(f"De totale prijs is € {Sum:.2f}")
