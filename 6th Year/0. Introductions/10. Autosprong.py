from math import sin, radians

g = 9.81

v: int      = int(input("Enter the speed of the car (in km/h): ")) / 3.6
theta: int  = int(input("Enter the angle of the slope (in degrees): "))
x: int      = int(input("Enter the distance to jump (in m): "))

delta_x = (v**2 * sin(2 * radians(theta))) / g

margin = delta_x - x

s: str = f"De auto legt {delta_x:.2f} meter af en "

if margin < 0:
    s += f"komt dus {abs(margin):.2f} meter te kort."
elif margin < 5:
    s += "haalt het net."
else:
    s += f"haalt het met {margin:.2f} meter overschot."

print(s)


print(
    f"De auto legt {(
        delta := ((
                (v := int(input('Enter the speed of the car (in km/h): ')) / 3.6) ** 2) 
            * sin(2 * radians(theta := int(input('Enter the angle of the slope (in degrees): ')))) / g)):.2f} meter af en " + (f"komt dus {abs(margin := delta - (x := int(input('Enter the distance to jump (in m): ')))):.2f} meter te kort." if margin < 0 else ("haalt het net." if margin < 5 else f"haalt het met {margin:.2f} meter overschot.")))

