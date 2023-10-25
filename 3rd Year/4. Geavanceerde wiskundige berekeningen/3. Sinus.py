import math

Hoek = int(input("graden is: "))
Radialen = math.radians(Hoek)
Sinus = math.sin(Radialen)
A = Sinus * (2 * math.pi)

print(round(A, 2))