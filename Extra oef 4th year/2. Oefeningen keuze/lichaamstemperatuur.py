# https://dodona.be/nl/courses/107/series/1244/activities/328212300

import math

T = float(input())
e_Benadering = 100 / T
e = math.e

if e_Benadering < e - 0.1:
    print("je hebt koorts")
elif e_Benadering > e + 0.1:
    print("je bent onderkoeld")
else:
    print("je hebt een normale lichaamstemperatuur")
