word = input()
word2 = ""
counter = 0

for x in word:
    if counter % 3 == 0 or counter == 0:
        counter += 1
    else:
        word2 += x
        counter += 1

print(word2)
