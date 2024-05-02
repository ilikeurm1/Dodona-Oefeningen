f = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711]

l = int(input())

for x in f:
    print(x)
    if x > l:
        break
 
# fibonacchi = [0, 1, 1]

# for i in range(20):
#     x = fibonacchi[-2]
#     y = fibonacchi[-1]
#     fibonacchi.append(x + y)

# n = int(input())

# for x in fibonacchi:
#     print(x)
#     if x > n:
#         break
