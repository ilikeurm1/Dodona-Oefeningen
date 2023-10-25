# https://dodona.be/nl/courses/107/series/1244/activities/325610135

import math

x1 = float(input())
y1 = float(input())
r1 = float(input())

x2 = float(input())
y2 = float(input())
r2 = float(input())

d = round(math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2)), 6)

if d == 0:
    print("concentrisch")
elif d == round(abs(r1 - r2), 6):
    print("binnen rakend")
elif d == round(r1 + r2, 6):
    print("buiten rakend")
elif d < abs(r1 - r2):
    print("omsluitend")
elif abs(r1 - r2) < d < r1 + r2:
    print("snijdend")
else:
    print("gescheiden")