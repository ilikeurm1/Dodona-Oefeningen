List_Type: int = int(input())
My_List: list[str] = []

if List_Type == 1:
    while True:
        a = input()
        if a != "einde":
            My_List.append(a)
        else:
            break
else:
    while True:
        a = int(input())
        if a != -1:
            list.append(My_List, a)
        else:
            break

print(sorted(My_List))
