word = input()

first = word.find('a')
last = word.rfind('a')

print(word[:first] + word[last + 1:])
