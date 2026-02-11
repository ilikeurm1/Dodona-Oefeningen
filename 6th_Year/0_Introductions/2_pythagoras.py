def pytha(a: float, b: float) -> str:
    return f"A triangle with side {a} and {b} has {(a**2 + b**2) ** .5} as it's hypotenuse."

print(
    pytha(
        float(input("Getal 1: ")), 
        float(input("Getal 2: "))
    )
)
