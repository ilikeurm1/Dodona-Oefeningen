import math

# # Constants
# g = 9.81  # m/s^2

# v = float(input("Initial speed of the object (in m/s): "))
# alpha = float(input("Angle the object is thrown at (in degrees): "))

# # Calculations
# rad = math.radians(alpha)   # Convert degrees to radians
# vx  = v * math.cos(rad)     # Horizontal component of velocity
# vy  = v * math.sin(rad)     # Vertical component of velocity

# t_flight = 2 * vy / g           # Time of flight
# max_height = (vy**2) / (2 * g)  # Maximum height
# range = vx * t_flight           # Horizontal range

# print(f"The projectile will fly for around {t_flight:.2f} seconds, reach a maximum height of {max_height:.2f} meters, and land {range:.2f} meters away.")


print(
    "\n\n",
    "Simulation: ", "\n",
    f"g = {(g := float(input('What is g on this planet (in m/s^2) | (enter for 9.81): ') or 9.81))} m/s^2", "\n",
    f"v = {(v := float(input('Initial speed of the object (in m/s): ')))} m/s", "\n",
    f"alpha = {(alpha := float(input('Angle the object is thrown at (in degrees): ')))} degrees ({f"{(rad := math.radians(alpha)):.2f}"} radians)", "\n",
    f"vx = {(vx := v * math.cos(rad)):.2f} m/s", "\n",
    f"vy = {(vy := v * math.sin(rad)):.2f} m/s", "\n",
    f"t_flight = {(t_flight := 2 * vy / g):.2f} s", "\n",
    f"max_height = {(max_height := (vy**2) / (2 * g)):.2f} m", "\n", 
    f"range = {(range := vx * t_flight):.2f} m",
    sep=''
)
