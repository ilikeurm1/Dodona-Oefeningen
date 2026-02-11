BMI = round(float(input()) / ((float(input()) / 100) ** 2), 2)

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

# h = float(input())
# l = int(input())
# l_cm = l / 100
# BMI = round(h / l_cm ** 2, 2)
