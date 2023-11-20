import math

side1 = int(input())
side2 = int(input())

pow1 = math.pow(side1, 2)
pow2 = math.pow(side2, 2)

print(f"De derde zijde is {math.sqrt(pow1 + pow2):.3f}")
