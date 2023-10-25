import math

x = int(input('lengte 1'))
y = int(input('lengte 2'))
L1 = math.pow(x, 2)
L2 = math.pow(y, 2)
z = (L1+L2)
L3 = math.sqrt(z)

print ("De derde zijde is", round(L3, 2))