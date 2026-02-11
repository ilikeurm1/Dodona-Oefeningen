Points_x: list[int] = []
Points_y: list[int] = []

for _ in range(3):
    x = int(input())
    y = int(input())
    Points_x.append(x) if x not in Points_x else Points_x.remove(x)
    Points_y.append(y) if y not in Points_y else Points_y.remove(y)

print(Points_x[0])
print(Points_y[0])

# Points_x = []
# Points_y = []

# for i in range(3):
#     x = int(input())
#     y = int(input())
#     if x not in Points_x:
#         Points_x.append(x)
#     else: 
#         Points_x.remove(x)
#     if y not in Points_y:
#         Points_y.append(y)
#     else:
#         Points_y.remove(y)

# print(Points_x[0])
# print(Points_y[0])
