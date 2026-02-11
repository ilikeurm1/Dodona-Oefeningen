sentence: str = input()
new: str = ""

for x in sentence:
    if x == "1":
        new += "één"
    else:
        new += x

print(new)
