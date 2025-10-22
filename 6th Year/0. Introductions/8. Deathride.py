from math import sqrt

h = float(input("Height of the drop (in meters): "))
d = float(input("Distance from the target (in meters): "))
m = float(input("Mass of the rider (in kg): "))
g = 9.81  # m/s^2, gravitational acceleration

x = sqrt(h**2 + d**2) # Total distance traveled

v = ((sqrt(2 * g * h)) * 3.6) * .4 # Speed at the bottom of the drop in km/h and some adjustments for friction and air resistance

print(f"The rider travelled {x:.2f} meters and will reach a speed of approximately {v:.2f} km/h.")
