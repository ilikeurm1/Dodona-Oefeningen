word = input()

first = word.find('a')
last = word.rfind('a')

word = word[:first+1] + word[first+1:last].replace("a", "A") + word[last:]

print(word)
