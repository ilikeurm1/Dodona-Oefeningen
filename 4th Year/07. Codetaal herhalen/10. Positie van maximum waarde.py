Numbers = []
x = -1

while x != 0:
    x = int(input())
    Numbers.append(x)

Max = max(Numbers)

print(Numbers.index(Max) + 1)
