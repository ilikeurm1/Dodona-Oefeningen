from math import pow, sqrt, log
print(f"The HDI of {input()} is {pow(((float(input()) - 20) / (82.3 - 20)) * (sqrt((float(input()) / 13.2) * (float(input()) / 20.6)) / 0.951) * (log(float(input())) - log(100)) / (log(107721) - log(100)), 1/3):.3f}.")


# import math

# Country = input('What country: ')
# LE = float(input('What is LE: '))
# MYS = float(input('What is MYS: '))
# EYS = float(input('What is EYS: '))
# GNIpc = float(input('What is GNIpc: '))

# LEI = (LE - 20) / (82.3 - 20)
# MYSI = MYS / 13.2
# EYSI = EYS / 20.6
# EI = (math.sqrt(MYSI * EYSI)) / 0.951
# II = (math.log(GNIpc) - math.log(100)) / (math.log(107721) - math.log(100))

# HDI = math.pow(LEI * EI * II, 1/3) 

# print(f'The HDI of {Country} is {HDI:.3f}.')
