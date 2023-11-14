# ---> imports <---

import math

# ---> Variables <---

Country = input('Country: ')
LE = float(input('LE: '))
MYS = float(input('MYS: '))
EYS = float(input('EYS: '))
GNIpc = float(input('GNIpc: '))

# ---> Calculations <---

LEI = (LE - 20) / (82.3 - 20)
MYSI = MYS / 13.2
EYSI = EYS / 20.6
EI = math.sqrt(MYSI * EYSI) / 0.951
II = (math.log(GNIpc) - math.log(100)) / (math.log(107721) - math.log(100))
HDI = math.pow(LEI * EI * II, 1/3)

# ---> Output <---

print(f"The HDI of {Country} is {HDI:.3f}.")
