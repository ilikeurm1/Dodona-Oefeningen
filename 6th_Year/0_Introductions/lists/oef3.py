# Matthijs Duhoux

pows = [-5, 12, -3, 8, 0, -2, 15]

print("Negative: [", *([n for n in pows if n > 0]), "]")
print("Positive: [", *([n for n in pows if n < 0]), "]")
