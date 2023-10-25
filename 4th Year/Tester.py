import random
import math

g = int(input())

while True:
    m = random.randint(0, 50)
    r = random.randint(1, 50)
    if g / r == math.pow(2, m) and r % 2 == 1:
        print(f"""{m}
{r}""")
        break