l = [x+1 for x in range(int(input()))]
print(*['*' * i for i in l], sep='\n')
print(*['*' * i for i in reversed(l[:-1])], sep='\n')

# x = int(input())

# for i in range(1, x + 1):
#     print(i * '*')
# for i in range(x-1, 0, -1):
#     print(i * '*')
