import math

word = input()

part1 = word[:math.ceil(len(word) / 2)]
part2 = word[math.ceil(len(word) / 2):]

print(part2+part1)
