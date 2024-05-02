Name1: str = input()
Name2: str = input()
Same: str = ''

for letter in Name1:
    if letter in Name2:
        Same += letter

if len(Same) > 0:
    print(Same)
else:
    print('Er zijn geen gemeenschappelijke tekens gevonden')
