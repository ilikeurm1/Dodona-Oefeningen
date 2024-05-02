word = input()
word2 = ""
counter = 0

for x in word:
    if not counter % 3 == 0 or counter == 0:
        word2 += x
    counter += 1

print(word2)
