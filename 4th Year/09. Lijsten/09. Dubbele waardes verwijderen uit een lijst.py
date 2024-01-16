List = [1, 3, 7,  2, 5, 6, 3, 8, 5, 7, 6, 1]
Better_List = []

for i in List:
    if i not in Better_List:
        Better_List.append(i)

print(sorted(Better_List))
