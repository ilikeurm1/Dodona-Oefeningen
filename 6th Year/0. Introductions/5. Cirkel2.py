from math import pi, floor
# r = int(input("Radius: "))

# A = pi * r**2
# C = 2 * pi * r

# print(f"A: {floor(A)}")
# print(f"C: {floor(C)}")

print(f"{(r := int(input("Radius: ")))}\n {"\033[F"}", f"Area: {pi * r**2:.3f}\nCircumference: {2 * pi * r:.3f}", sep="")
