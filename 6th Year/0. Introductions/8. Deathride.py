from math import sqrt

h = float(input("Height of the drop (in meters): "))
d = float(input("Distance from the target (in meters): "))
m = float(input("Mass of the rider (in kg): "))
g = 9.81  # m/s^2, gravitational acceleration

x = sqrt(h**2 + d**2) # Total distance traveled

v = ((sqrt(2 * g * h)) * 3.6) * .4 # Speed at the bottom of the drop in km/h and some adjustments for friction and air resistance

print(f"The rider travelled {x:.2f} meters and will reach a speed of approximately {v:.2f} km/h.")

# print("\n\n", "Simulation: ", "\n", f"h = {(h := float(input('\nHeight of the drop (in meters): ')))} m", "\n", f"d = {(d := float(input('Distance from the target (in meters): ')))} m", "\n", f"m = {(m := float(input('Mass of the rider (in kg): ')))} kg", "\n", f"g = {(g := float(input('What is the gravitational constant on this planet (in m/s^2) | (enter for 9.81): ') or 9.81))} m/s^2", "\n\n", f"x = {(x := sqrt(h**2 + d**2)):.2f} m", "\n", f"v = {(v := ((sqrt(2 * g * h)) * 3.6) * .4):.2f} km/h", "\n\n", f"The rider travelled {x:.2f} meters and will reach a speed of approximately {v:.2f} km/h.", sep='')
