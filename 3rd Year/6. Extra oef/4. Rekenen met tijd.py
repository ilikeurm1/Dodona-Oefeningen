from math import floor
u1 = int(input()); m1 = int(input()); u2 = int(input()); m2 = int(input())
print(f"{floor((-u1 * 60 + m1 + u2 * 60 + m2) / 60)} uur en {(-u1 * 60 + m1 + u2 * 60 + m2) % 60} minuten")

# from math import floor
# Uur_In_Minuten = 60
# Uur1 = int(input('Uur getal 1: '))
# Min1 = int(input('Min getal 1: '))
# Uur2 = int(input('Uur getal 2: '))
# Min2 = int(input('Min getal 2: '))
# Tijd_In_Min1 = (Uur1 * Uur_In_Minuten) + Min1
# Tijd_In_Min2 = (Uur2 * Uur_In_Minuten) + Min2
# Difference = Tijd_In_Min2 - Tijd_In_Min1
# Uur_Difference = floor(Difference / 60)
# Min_Difference = Difference % 60
# print(Uur_Difference, 'uur en', Min_Difference, 'minuten')
