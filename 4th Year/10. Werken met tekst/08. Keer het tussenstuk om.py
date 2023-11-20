word = input()

first = word.find('a')
last = word.rfind('a')


if first == 0 and last == len(word) - 1:
    print(word)
else:
    print(word[:first] + word[last:first -1 :-1] + word[last + 1:])
