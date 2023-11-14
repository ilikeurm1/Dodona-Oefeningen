Points_x = []
Points_y = []

def Remove_Doubles_from(list):
    for i in list:
        Entries = list.count(i)
        if Entries > 1:
            list.remove(i)
            list.remove(i)
    return list
    
for i in range(3):
    x = int(input())
    y = int(input())
    Points_x.append(x)
    Points_y.append(y)

Points_x = Remove_Doubles_from(Points_x)
Points_y = Remove_Doubles_from(Points_y)

print(Points_x[0])
print(Points_y[0])
