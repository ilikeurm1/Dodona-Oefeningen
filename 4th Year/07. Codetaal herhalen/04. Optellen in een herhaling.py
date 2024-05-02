amount = int(input()); Numbers = [int(input()) for _ in range(amount)]
print(f"Het gemiddelde van deze {amount} getallen is: {round(sum(Numbers) / len(Numbers), 1)}")

# print(f"Het gemiddelde van deze {(amount := int(input()))} getallen is: {(Numbers := [int(input()) for _ in range(amount)]) and round(sum(Numbers) / len(Numbers), 1)}")

# Numbers: list[int] = []
# amount = int(input())

# for x in range(amount):
#     Number = int(input())
#     Numbers.append(Number)

# Average = sum(Numbers) / amount

# print(f"Het gemiddelde van deze {amount} getallen is: {round(Average, 1)}")
