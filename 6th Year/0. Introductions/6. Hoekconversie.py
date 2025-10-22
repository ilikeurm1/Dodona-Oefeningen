import math

deg = float(input("Angle in degrees: "))
rad = math.radians(deg)
sin = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
back_to_deg = math.degrees(rad)

print(
    f"Angle in degrees: {deg}\n", 
    f"Angle in radians: {rad:.2f}\n",
    f"sin: {sin:.2f}\n",
    f"cos: {cos:.2f}\n",
    f"tan: {tan:.2f}\n",
    f"back to deg: {back_to_deg:.2f}"
)
