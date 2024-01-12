word = input()

amounts_of_ps = word.count("p")

if amounts_of_ps == 0:
    print("-2")
elif amounts_of_ps == 1:
    print("-1")
else:
    word = word.replace("p", "x", 1)
    print(word.find("p"))
