word = input()

amounts_of_ps = word.count("p")

if amounts_of_ps == 0 or amounts_of_ps == 1:
    print(amounts_of_ps - 2)
else:
    word = word.replace("p", "x", 1)
    print(word.find("p"))
