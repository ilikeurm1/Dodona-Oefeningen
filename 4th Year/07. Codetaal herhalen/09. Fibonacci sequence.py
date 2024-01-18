fibonacchi = [0, 1, 1]

for i in range(20):
    x = fibonacchi[-2]
    y = fibonacchi[-1]
    fibonacchi.append(x + y)

n = int(input())

for x in fibonacchi:
    print(x)
    if x > n:
        break
