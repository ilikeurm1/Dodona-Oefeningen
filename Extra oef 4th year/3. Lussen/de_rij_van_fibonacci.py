# https://dodona.be/nl/courses/107/series/1295/activities/1996857061

n = int(input())

Fibonacci = [1, 1]

Number_1 = Fibonacci[0]
Number_2 = Fibonacci[1]
Counter = 0

while True:
    Sum = Number_1 + Number_2
    Fibonacci.append(Sum)
    Number_1 = Number_2
    Number_2 = Sum
    Counter += 1
    if Counter == 350:
        break

if n == 1 or n == 2:
    print('1')
else:
    print(Fibonacci[n - 1])
