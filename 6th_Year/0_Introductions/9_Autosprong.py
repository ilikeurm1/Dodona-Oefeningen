from math import sin, radians

g = 9.81

v: float        = float(input("Enter the speed of the car (in km/h): ")) / 3.6
theta: int      = int(input("Enter the angle of the slope (in degrees): "))
x: int          = int(input("Enter the distance to jump (in m): "))

delta_x = (v**2 * sin(2 * radians(theta))) / g

margin = delta_x - x

print(f"De auto legt {delta_x:.2f} meter af en ", end="")

if margin < 0:
    print(f"komt dus {abs(margin):.2f} meter te kort.")
elif margin < 5:
    print("haalt het net.")
else:
    print(f"haalt het met {margin:.2f} meter overschot.")
