# ---> Imports <---

import math

# ---> Variables <---

Dia = int(input('What is the diameter of the MNM: '))
Human_Length = float(input('How tall is the human: '))
Human_Thiccness = float(input('How THICC is the human: '))

# ---> Calculations <---

r = Dia / 2
r_squared_in_mm = math.pow(r, 2)
MnM_A_inMM = r_squared_in_mm * math.pi
MnM_A = round(MnM_A_inMM / 1000000, 6)
Human_A = round(math.sqrt((Human_Length * Human_Thiccness)/3600), 2)

Amount_MnMs = round(Human_A / MnM_A, 0)

# ---> Output <---
print(f"{Amount_MnMs} m&m's")
