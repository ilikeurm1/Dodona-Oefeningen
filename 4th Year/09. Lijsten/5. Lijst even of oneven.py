Even_List = []
Uneven_List = []

a = int(input())

for x in range(a):
    b = int(input())
    if b % 2 == 0:
        list.append(Even_List, b)
    else:
        list.append(Uneven_List, b)

print(f"""{Even_List}
{Uneven_List}""")