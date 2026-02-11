import math

# Constants
g = 9.81  # m/s^2

v = float(input("Initial speed of the object (in m/s): "))
alpha = float(input("Angle the object is thrown at (in degrees): "))

# Calculations
rad = math.radians(alpha)   # Convert degrees to radians
vx  = v * math.cos(rad)     # Horizontal component of velocity
vy  = v * math.sin(rad)     # Vertical component of velocity

t_flight = 2 * vy / g           # Time of flight
max_height = (vy**2) / (2 * g)  # Maximum height
range = vx * t_flight           # Horizontal range

print(f"The projectile will fly for around {t_flight:.2f} seconds, reach a maximum height of {max_height:.2f} meters, and land {range:.2f} meters away.")
