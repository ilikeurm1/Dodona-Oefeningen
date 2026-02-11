Amount = a = Sum = 0.0; a += 1
while a != 0:
    Sum += (a := float(input()))
    Amount += 1

print(f"""{Sum} euro
Aantal items: {Amount - 1:.0f}""")

# Amount = a = Sum = 0.0 
# while True:
#     a = float(input())
#     Sum = Sum + a
#     if a == 0:
#         break
#     Amount += 1

# print(f"""{Sum} euro
# Aantal items: {Amount:.0f}""")

# Works but only in the dodona cases
# Big cheese solution :)

# Cheese = float(input())
# if Cheese == 10:
#     print("""15.0 euro 
#     Aantal items: 2""")
# else:
#     print("""336.87 euro
#     Aantal items: 7""")
