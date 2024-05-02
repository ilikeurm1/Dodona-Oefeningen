Numbers = []

while 0 not in Numbers:
    Numbers.append(int(input()))

print(Numbers.index(max(Numbers)) + 1)


# Numbers = []
# x = -1

# while x != 0:
#     x = int(input())
#     Numbers.append(x)

# Max = max(Numbers)

# print(Numbers.index(Max) + 1)


# # Non list version

# x, Max, Count = -1, 0, 1
# while x != 0:
#     x = int(input())
#     if x > Max:
#         Max = x
#         Position = Count
#     Count += 1

# print(Position)
