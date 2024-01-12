word = input()

first = word.find("f")
last = word.rfind("f")

if first == last:
    print(first)
else:
    print(first, last)
