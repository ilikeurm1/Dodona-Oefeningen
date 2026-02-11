word = input()

first = word.find("f")
last = word.rfind("f")

print(first) if first == last else print(first, last)
