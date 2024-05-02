entries = int(input())

full = []

for x in range(entries + 1):
    full.append(x + 1)

for x in range(entries):
    x = int(input())
    full.remove(x)

print(full[0])


# entries = int(input())

# row = []
# full = []

# for x in range(entries + 1):
#     full.append(x + 1)

# for x in range(entries):
#     x = int(input())
#     row.append(x)

# for x in row:
#     full.remove(x)

# print(full[0])

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
