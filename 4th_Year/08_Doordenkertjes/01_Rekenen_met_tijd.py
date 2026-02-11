Uur1, Min1 = int(input()), int(input())
Uur2, Min2 = int(input()), int(input())

Tijd_In_Min1 = (Uur1 * 60) + Min1
Tijd_In_Min2 = (Uur2 * 60) + Min2

Difference = Tijd_In_Min2 - Tijd_In_Min1

Uur_Difference = Difference // 60
Min_Difference = Difference % 60
print(f"{Uur_Difference} uur en {Min_Difference} minuten")


# # ---> Imports <---
# import math

# # ---> Variabelen <---
# Uur_In_Minuten = 60

# Uur1 = int(input('Uur getal 1: '))
# Min1 = int(input('Min getal 1: '))

# Uur2 = int(input('Uur getal 2: '))
# Min2 = int(input('Min getal 2: '))

# # ---> Berekeningen <---
# Tijd_In_Min1 = (Uur1 * Uur_In_Minuten) + Min1
# Tijd_In_Min2 = (Uur2 * Uur_In_Minuten) + Min2

# Difference = Tijd_In_Min2 - Tijd_In_Min1

# Uur_Difference = math.floor(Difference / 60)
# Min_Difference = Difference % 60
# print(f"{Uur_Difference} uur en {Min_Difference} minuten")
