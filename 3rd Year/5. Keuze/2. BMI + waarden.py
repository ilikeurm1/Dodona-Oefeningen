# ---> Inputs <---

Weight = float(input('Weight in kg: '))
Length = float(input('Lengte in cm: '))

# ---> Calculations <---

LengthM = Length / 100
RBMI = Weight / (LengthM ** 2)
BMI = round(RBMI, 1)

# ---> Output <---

print('Je hebt een BMI van', BMI)
if BMI < 18.5: # ondergewicht
    print('Je hebt ondergewicht')
elif BMI <= 25: # Normaal
    print('Je hebt een normaal gewicht')
elif BMI <= 30: # Je hebt overgewicht
    print('Je hebt overgewicht')
elif BMI <= 35: #- obesitas
    print('Je hebt obesitas')
else: # ernstige obesitas
    print('Je hebt ernstige obesitas')