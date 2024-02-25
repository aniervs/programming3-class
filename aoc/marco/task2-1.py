import sys

sum = 0

for line in sys.stdin:
    game, rounds = line.strip().split(": ")
    id = int(game.split("Game ")[1])
    possible = True
    for round in rounds.split("; "):
        for cubes in round.split(", "):
            amount, color = cubes.split(" ")
            amount = int(amount)
            if color == "red" and amount > 12:
                possible = False
            if color == "green" and amount > 13:
                possible = False
            if color == "blue" and amount > 14:
                possible = False
    if possible:
        sum += id

print(sum)
