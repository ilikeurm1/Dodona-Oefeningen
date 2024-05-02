def IsWhite(x: int, y: int) -> str:
    return "W" if (x + y) % 2 == 1 else "B"
        
print("DEZELFDE KLEUR") if IsWhite(int(input()), int(input())) == IsWhite(int(input()), int(input())) else print("VERSCHILLENDE KLEUR")


# def IsWhite(x, y):
#     if (x + y) % 2 == 1:
#         Color = "White"
#     else:
#         Color = "Black"
#     return Color

# x1 = int(input())
# y1 = int(input())

# x2 = int(input())
# y2 = int(input())

# Color_1 = IsWhite(x1, y1)
# Color_2 = IsWhite(x2, y2)

# if Color_1 == Color_2:
#     print("DEZELFDE KLEUR")
# else:
#     print("VERSCHILLENDE KLEUR")
