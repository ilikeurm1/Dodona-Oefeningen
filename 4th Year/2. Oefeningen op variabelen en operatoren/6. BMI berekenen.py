Weight = float(input())
Length = int(input())

BMI = Weight / (Length / 100) ** 2

print(f'Je hebt een BMI van {round(BMI, 2)}')
