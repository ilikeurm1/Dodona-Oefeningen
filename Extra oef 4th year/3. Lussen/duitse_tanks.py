# https://dodona.be/nl/courses/107/series/1295/activities/1100982831

Serials = []

while True:
    n = int(input())
    if n > 0:
        Serials.append(n)
    else:
        break

t = (((len(Serials) + 1) * max(Serials)) / len(Serials)) - 1

print(f"Het aantal geproduceerde tanks wordt geschat op {round(t, 0):.0f}.")

