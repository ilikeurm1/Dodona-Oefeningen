g: int = int(input())
m: int = 1
found: bool = False

while 2 ** m <= g and not found:
    r = g / 2 ** m
    if r % 2 == 1:
        print(m)
        print(f'{r:.0f}')
        found = True
    m += 1

print(0, g, sep='\n') if not found else ...
