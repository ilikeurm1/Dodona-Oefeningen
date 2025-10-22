# mins = int(eval(input("Minutes: ")))

print(
    "\033[F" + str(mins := int(eval(input(), {"__builtins__": None}))), 
    "minutes is:", 
    f"{mins // (24 * 60) // 365}y:{mins // (24 * 60) % 365}d:{mins // 60 % 24:02}h:{mins % 60:02}m"
)
