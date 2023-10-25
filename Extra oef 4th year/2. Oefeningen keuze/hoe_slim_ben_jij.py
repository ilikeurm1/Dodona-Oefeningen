# https://dodona.be/nl/courses/107/series/1244/activities/625610721

x = str(input())
digits = []

amount_of_0 = 0

for i in x:
    digits.append(int(i))

for x in digits:
    if x == 1 or x == 2 or x == 3 or x == 5 or x == 7:
        amount_of_0 += 0
    elif x == 4 or x == 6 or x == 9 or x == 0:
        amount_of_0 += 1
    else:
        amount_of_0 += 2

print(amount_of_0)
