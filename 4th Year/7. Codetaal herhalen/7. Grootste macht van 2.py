import random
import math

g = int(input())

amount = 0
smallest_m = []
smallest_r = []

while True:
    m = random.randint(0, 50)
    r = random.randint(1, 50)
    if g / r == math.pow(2, m) and r % 2 == 1:
        list.append(smallest_m, m)
        list.append(smallest_r, r)
        break

end_m = smallest_m[0]
end_r = smallest_r[0]

print(f"""{end_m}
{end_r}""")
