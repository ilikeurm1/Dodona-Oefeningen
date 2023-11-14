Black_x = [1,3,5,7]
Black_y = [2,4,6,8]

def IsWhite(x, y):
    if x in Black_x:
        if y in Black_y:
            return True
        return False  
    if x not in Black_x:
        if y in Black_y:
            return False
        return True
    return None

x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())


Color_1 = IsWhite(x1, y1)
Color_2 = IsWhite(x2, y2)

if Color_1 == Color_2:
    print("DEZELFDE KLEUR")
else:
    print("VERSCHILLENDE KLEUR")
