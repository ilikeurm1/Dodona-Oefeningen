# ---> Imports <---

import math

# ---> Variables <---

Dia_MandM = int(input('What diameter does the M&M have?: '))
Length_Human = float(input('Hoe groot is de persoon (in cm)?: '))
Weight_Human = float(input('Hoe veel weegt de persoon (in kg)?: '))

# ---> Calculations <---

Opp_Human = round(math.sqrt((Length_Human * Weight_Human)/3600), 2)
Opp_MandM = math.pow(Dia_MandM, 2) * math.pi / 4
Opp_MandM_inM = round(Opp_MandM / math.pow(10, 6), 6)

Amount_Of_MandM = round(Opp_Human / Opp_MandM_inM, 0)

# ---> Output <---

print(f"{Amount_Of_MandM} m&m's")