List_Type = int(input())
My_List = []

if List_Type == 1:
    while True:
        a = input()
        if a != "einde":
            list.append(My_List, a)
        else:
            break
elif List_Type == 2:
    while True:
        a = int(input())
        if a != -1:
            list.append(My_List, a)
        else:
            break

print(sorted(My_List))
