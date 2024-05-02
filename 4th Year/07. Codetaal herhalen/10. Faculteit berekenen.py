def fac(x: int) -> int:
     return x * fac(x - 1) if x > 1 else 1

print(fac(int(input())))

# x = int(input())

# def faculteit( n ):
#     if n <= 1:
#         return 1
#     return n * faculteit(n - 1)

# print(faculteit(x))
