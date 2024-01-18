number = int(input())

List = []

for i in range(number):
    x = int(input())
    List.append(x)

zeros = List.count(0)

print(zeros)
