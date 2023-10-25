# https://dodona.be/nl/courses/107/series/1244/activities/387716745

V = float(input())
L = float(input())
rho = float(input())
mu = float(input())

Reynolds = (V * L * rho) / mu

if Reynolds < 2000:
    print(f"{Reynolds} (laminaire stroming)")
elif Reynolds >=2000 and Reynolds <= 4000:
    print(f"{Reynolds} (omslagstroming)")
else:
    print(f"{Reynolds} (turbulente stroming)")
