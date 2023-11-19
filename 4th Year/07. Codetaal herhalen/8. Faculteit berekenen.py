x = int(input())

def faculteit( n ):
    if n <= 1:
        return 1
    return n * faculteit( n-1 )

print(faculteit(x))
