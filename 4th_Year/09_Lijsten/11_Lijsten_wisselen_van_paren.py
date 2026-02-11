List = [9544, 2723, 3562, 9920, 9439, 1526, 5069, 5283, 5748, 9548, 9391, 3481]

def Swap(lst, Swapped_Amount):
    if Swapped_Amount == len(lst) // 2:
        return lst
    lst[Swapped_Amount * 2], lst[Swapped_Amount * 2 + 1] = lst[Swapped_Amount * 2 + 1], lst[Swapped_Amount * 2]
    Swapped_Amount += 1
    return Swap(lst, Swapped_Amount)

Newer_List = Swap(List, 0)

print(Newer_List)


# List = [9544, 2723, 3562, 9920, 9439, 1526, 5069, 5283, 5748, 9548, 9391, 3481]

# def Swap(list, Swapped_Amount):
#     if Swapped_Amount == len(list) // 2:
#         return list
#     First_element = list[Swapped_Amount * 2]
#     Second_element = list[Swapped_Amount * 2 + 1]
#     list[Swapped_Amount * 2] = Second_element
#     list[Swapped_Amount * 2 + 1] = First_element
#     Swapped_Amount += 1
#     return Swap(list, Swapped_Amount)

# Newer_List = Swap(List, 0)

# print(Newer_List)


# # Cheese way
# print("[2723, 9544, 9920, 3562, 1526, 9439, 5283, 5069, 9548, 5748, 3481, 9391]")
