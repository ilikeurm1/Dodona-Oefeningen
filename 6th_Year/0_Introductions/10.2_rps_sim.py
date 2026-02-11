import random

winning_combos: dict[str, str] = {
    "rock": "paper", 
    "paper": "scissors", 
    "scissors": "rock"
}

stats: dict[str, dict[str, int]] = {
    "scores": {
        "c1_w": 0,
        "c2_w": 0,
        "ties": 0
    },
    "winning_hand": {
        "rock": 0,
        "paper": 0,
        "scissors": 0
    },
    "rounds": {
        "rounds_played": 0, 
        "max_rounds": 10000
    },
}

simulate: bool = True

def condition() -> bool:
    if simulate:
        return stats["rounds"]["rounds_played"] < stats["rounds"]["max_rounds"]
    return stats["scores"]["c1_w"] < 3 and stats["scores"]["c2_w"] < 3

while condition():
    c1: str = random.choice(["rock", "paper", "scissors"])
    c2: str = random.choice(["rock", "paper", "scissors"])

    if c1 == c2: stats["scores"]["ties"] += 1 # noqa: E701
    elif c2 != winning_combos[c1]: stats["scores"]["c1_w"] += 1; stats["winning_hand"][c1] += 1  # noqa: E701, E702
    else: stats["scores"]["c2_w"] += 1; stats["winning_hand"][c2] += 1  # noqa: E701, E702
    
    stats["rounds"]["rounds_played"] += 1

print(stats)