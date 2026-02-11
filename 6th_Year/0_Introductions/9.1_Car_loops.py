from math import sin, radians, ceil, sqrt

# in this exercise we have the angle and the distance to jump so we calculate the minimum speed

g = 9.81
theta: int = 30

x: int = int(input("Enter the distance to jump (in m): "))

v = sqrt((x * g) / sin(2 * radians(theta))) * 3.6 # min speed in km/h

print(f"De auto moet minimaal {v:.2f} ({ceil(v):.1f}) km/h rijden om de sprong te halen.")
