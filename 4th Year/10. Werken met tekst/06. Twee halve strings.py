from math import ceil

word = input()

part1 = word[:ceil(len(word) / 2)]
part2 = word[ceil(len(word) / 2):]

print(part2+part1)
