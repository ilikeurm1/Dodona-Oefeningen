from math import pi, sqrt
print(f"{round((round((int(input()) ** 2 * pi / 4) / 10 ** 6, 6) / round(sqrt(float(input()) * float(input()) / 3600), 2)) ** -1, 0)} m&m's")

# from math import pi, sqrt
# Dia = int(input('What is the diameter of the MNM: '))
# Human_Length = float(input('How tall is the human: '))
# Human_Thiccness = float(input('How THICC is the human: '))
# r = Dia / 2
# r_squared_in_mm = pow(r, 2)
# MnM_A_inMM = r_squared_in_mm * pi
# MnM_A = round(MnM_A_inMM / 1000000, 6)
# Human_A = round(sqrt((Human_Length * Human_Thiccness) / 3600), 2)
# Amount_MnMs = round(Human_A / MnM_A, 0)
# print(f"{Amount_MnMs} m&m's")
