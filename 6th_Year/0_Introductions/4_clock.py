# mins = int(eval(input("Minutes: ")))

print(
    "\033[F" + str(mins := int(eval(input(), {"__builtins__": None}))),
    "minutes is:",
    f"{mins // (24 * 60 * 365)}y:{mins // (24 * 60) % 365}d:{mins // 60 % 24:02}h:{mins % 60:02}m",
)

print(
    "\033[F" + str(secs := int(eval(input(), {"__builtins__": None}))),
    "seconds is:",
    f"{secs // (24 * 60 * 60 * 365)}y:{secs // (24 * 60 * 60) % 365}d:{secs // (60 * 60) % 24:02}h:{secs // 60 % 60:02}m:{secs % 60}s",
)
