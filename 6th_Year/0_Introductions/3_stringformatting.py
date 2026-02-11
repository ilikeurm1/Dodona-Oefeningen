a: str = "abc"
b: str = "def"
max_len = max(len(a), len(b)) + 1

print(f"{a:<{max_len}}|{b:>{max_len}}")
