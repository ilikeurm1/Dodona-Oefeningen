lst: list[str] = []

while 'einde' not in lst:
    lst.append(input())

print(sorted(lst[:-1], reverse=True))

# My_List = []

# while True:
#     a = input()
#     if a != "einde":
#         list.append(My_List, a)
#     else:
#         break

# print(sorted(My_List, reverse=True))
