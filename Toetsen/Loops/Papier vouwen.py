from math import log2, ceil

mm, Limit = input().split('/') # get input

mm = float(mm) # convert to correct type
Limit = int(Limit) # convert to correct type

mm /= 1000 # set mm to m


# While loop solution

# folds = 0 # set folds to 0

# while mm < Limit:
#     folds += 1 # add 1 fold
#     mm *= 2 # Dubble thickness
#     print(f'na {folds}x vouwen heb je een dikte van {mm} meter')

# print(f'De gewenste hoogte is bereikt na {folds}x vouwen')


"""
Logarithm solution

Formula:
h(n) = Limit 
h(0) = mm

h(n) = h(0) * 2^n

log2 both sides

=> log2(hn) = log2(h0) + n
=> log2(hn) - log2(h0) = n

"""

n = ceil(log2(Limit) - log2(mm)) # ceil to get the actual int fold amount and not a float

print(f'De gewenste hoogte is bereikt na {n}x vouwen (h = {mm * 2**n})')

# code to make the inbetween steps visible

# while True:
#     action = input("Which step do you want to know the height of? (num/q): ")
#     if action == "q":
#         break
    
#     try:
#         action = int(action)
#     except ValueError:
#         print("Please insert a number or 'q' to quit")
#         continue

#     print(f'na {action}x vouwen heb je een dikte van {mm * 2**action} meter')
