from math import pi


def cirkel_opp(radius: float) -> float:
    """
    Returns the area of a circle given its radius.
    """

    return pi * radius**2

print(cirkel_opp(5))
