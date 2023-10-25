Numbers = []
amount = int(input())

for x in range(amount):
    Number = int(input())
    list.append(Numbers, Number)

Average = sum(Numbers) / len(Numbers)

print(f"Het gemiddelde van deze {amount} getallen is: {round(Average, 1)}")