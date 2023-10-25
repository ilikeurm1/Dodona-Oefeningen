Massa = float(input("massa: "))
LengteInCm = int(input("lengte: "))
LengteInM = (LengteInCm / 100)
BMI = round(Massa / (LengteInM * LengteInM), 2)

print("Je hebt een BMI van", BMI)