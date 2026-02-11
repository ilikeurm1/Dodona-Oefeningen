word: str = input()

first: int = word.find('a')
last: int = word.rfind('a')

print(word[:first+1] + word[first+1:last].replace("a", "A") + word[last:])
