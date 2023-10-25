# https://dodona.be/nl/courses/107/series/1244/activities/1954949630

import math

degrees = int(round(float(input()) / 10, 0))

if degrees == 18 or degrees == 0:
    print("18/36")

elif degrees < 10:
    print(f"0{degrees}/{degrees + 18}")

elif degrees < 18 and degrees > 9:
    print(f"{degrees}/{degrees + 18}")

elif degrees > 27:
    print(f"{degrees - 18}/{degrees}")

else:
    print(f"0{degrees - 18}/{degrees}")