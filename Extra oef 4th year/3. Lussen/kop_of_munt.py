# https://dodona.be/nl/courses/107/series/1295/activities/581560564

import random

random.seed(1)

Heads = []
Tails = []

Throws = int(input())

for x in range(1, Throws+1):
    Side = random.randint(0,1)
    if Side == 0:
        Tails.append(Side)
    else:
        Heads.append(Side)

if len(Heads) == len(Tails):
    print("Munt en kop zijn evenveel geworpen")
elif len(Heads) > len(Tails):
    print('Kop is meest geworpen')
else:
    print('Munt is meest geworpen')
