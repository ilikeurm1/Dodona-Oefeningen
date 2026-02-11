Speeds = []

for _ in range(4):
    Speeds.append(int(input()))

Speeds.sort()

A = Speeds[0]
B = Speeds[1]
C = Speeds[2]
D = Speeds[3]
final = min([2 * A + B + C + D, A + 3 * B + D])

if final >= 60:
    hour = final // 60
    minutes = final - (hour * 60)
    print(f"De snelste tijd om over te steken is {hour} uur en {minutes} minuten")
else:
    print(f"De snelste tijd om over te steken is {final} minuten")
