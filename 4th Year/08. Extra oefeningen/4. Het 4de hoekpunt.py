Points_x = []
Points_y = []

for i in range(3):
    x = int(input())
    y = int(input())
    if x not in Points_x:
        Points_x.append(x)
    else: 
        Points_x.remove(x)
    if y not in Points_y:
        Points_y.append(y)
    else:
        Points_y.remove(y)

print(Points_x[0])
print(Points_y[0])
