row = []

for _ in range(int(input())):
    row.append(int(input()))

row.reverse()

for x in row:
    y = x - 1
    if y == 0:
        y = len(row) + 1
    if y not in row:
        print(y)
        break

# entries = int(input())

# row = []

# for x in range(entries):
#     x = int(input())
#     row.append(x)

# row.sort(reverse=True)

# for x in row:
#     y = x - 1
#     if y == 0:
#         y = entries + 1
#     if y not in row:
#         print(y)
#         break
