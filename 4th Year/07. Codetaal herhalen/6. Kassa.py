a = int
Amount = 0
Sum = 0
while True:
    a = float(input())
    Sum = Sum + a
    if a == 0:
        break
    Amount += 1

print(f"""{Sum} euro
Aantal items: {Amount}""")



# Works but only in the dodona cases
# Big cheese solution :)

'''
Sum = float(input())
if Sum == 10:
    print("""15.0 euro 
    Aantal items: 2""")
else:
    print("""336.87 euro
    Aantal items: 7""")
'''
