# https://dodona.be/nl/courses/107/series/1244/activities/1199472779

x = int(input())
y = int(input())

def function2(x, y):
    print(f"{x} x {y} = 10 x ({x - 5} + {y - 5}) + ({10 - x} x {10 - y}) = {x * y}")

def function3(x, y):
    print(f"{x} x {y} = 100 + 10 x ({x - 10} + {y - 10}) + ({x - 10} x {y - 10}) = {x * y}")


if x <= 5 and y <= 5 or x == 10 or y == 10:
    print(f"{x} x {y} = {x * y}")
elif x >= 6 and y >= 6 and x <= 9 and y <= 9:
    function2(x, y)
elif x >= 11 and y >= 11 and x <= 15 and y <= 15:
    function3(x, y)
else:
    function3(x, y)
    