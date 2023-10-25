# https://dodona.be/nl/courses/107/series/1295/activities/683768040

def solve_pythagorean_triplets(n):
    solutions = []
    for a in range(1, n):
        denom = 2 * (n-a)
        num = 2 * a ** 2 + n ** 2 - 2 * n *a
        if denom > 0 and num % denom == 0:
            c = num // denom
            b = n - a - c
            if b > a:
                solutions.append((a, b, c))

    return solutions

Answer_List = solve_pythagorean_triplets(int(input()))

for x in range(1, len(Answer_List) + 1):
    print(Answer_List[x - 1])
