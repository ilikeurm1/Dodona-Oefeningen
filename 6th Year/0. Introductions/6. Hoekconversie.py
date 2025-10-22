import math

print(
    f"deg = {(deg := float(input('Angle in degrees: ')))}", "\r", 
    "Angle in radians: ", f"{(rad := math.radians(deg)):.2f}", "\n", 
    "sin: ", f"{math.sin(rad):.2f}", "\n", 
    "cos: ", f"{math.cos(rad):.2f}", "\n", 
    "tan: ", f"{math.tan(rad):.2f}", "\n", 
    "back to deg: ", f"{math.degrees(rad):.2f}", 
    sep=''
)
