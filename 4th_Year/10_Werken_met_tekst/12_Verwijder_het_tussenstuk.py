word = input()

first, last = word.find('a'), word.rfind('a')

print(word[:first] + word[last + 1:])
