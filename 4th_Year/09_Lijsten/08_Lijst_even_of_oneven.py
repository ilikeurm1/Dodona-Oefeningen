Even_List: list[int] = []
Uneven_List: list[int] = []

for x in range(int(input())):
    b = int(input())
    Even_List.append(b) if b % 2 == 0 else Uneven_List.append(b)

print(f"""{Even_List}
{Uneven_List}""")


# Even_List = []
# Uneven_List = []

# a = int(input())

# for x in range(a):
#     b = int(input())
#     if b % 2 == 0:
#         list.append(Even_List, b)
#     else:
#         list.append(Uneven_List, b)

# print(f"""{Even_List}
# {Uneven_List}""")
