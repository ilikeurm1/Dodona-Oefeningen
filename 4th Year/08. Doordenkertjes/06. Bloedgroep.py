Letter1 = str(input('Letter 1: ').upper())
Letter2 = str(input('Letter 2: ').upper())

if Letter1 == 'A' and Letter2 == 'B':
    Result = 'AB'
elif Letter1 == 'B' and Letter2 == 'A':
    Result = 'AB'
elif Letter1 == 'O' and Letter2 != Letter1:
    Result = Letter2
elif Letter2 == 'O' and Letter1 != Letter2:
    Result = Letter1
elif Letter1 == Letter2:
    Result = Letter1

print(f"The combination of the ABO alleles {Letter1} and {Letter2} results in blood type {Result}.")
