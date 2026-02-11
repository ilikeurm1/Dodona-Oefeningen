from math import log2, ceil

mm = float(input("Please input the thickness of the paper (in mm): ")) / 1000
Limit = float(input("Please input the height you want the paper to reach (in m): "))

# While loop solution

folds = 0 # set folds to 0

while mm < Limit:
    folds += 1 # add 1 fold
    mm *= 2 # Dubble thickness
    print(f'na {folds}x vouwen heb je een dikte van {mm} meter')

print(f'De gewenste hoogte is bereikt na {folds}x vouwen')


"""
Logarithm solution

Vars:
h(n) = Limit 
h(0) = mm

Formula:
h(n) = h(0) * 2^n

=> log2(h(n)) = log2(h(0)) + n
=> log2(h(n)) - log2(h(0)) = n


since n has to be an int
as you can only fold paper an int amount of times
ceil(n) gives us the actual minimum amount of folds
to reach 'at least' Limit height

"""

# n = ceil(log2(Limit) - log2(mm)) # Calculate the amount of folds

# print(f'De gewenste hoogte is bereikt na {n}x vouwen (h = {mm * 2**n})')

# code to make the inbetween steps visible

# while True:
#     action = input("Which step do you want to know the height of? (int/q): ")
#     if action.lower() in ("q", "quit", "end", "break"):
#         break
    
#     try:
#         action = int(action)
#     except ValueError:
#         print("Please insert a number or 'q' to quit")
#         continue

#     print(f'After {action}x folds the paper would be {mm * 2**action} meter thicc')
