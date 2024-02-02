import sys

sum = 0

for line in sys.stdin:
    game, rounds = line.strip().split(": ")
    id = int(game.split("Game ")[1])
    min_red = 0
    min_blue = 0
    min_green = 0
    for round in rounds.split("; "):
        for cubes in round.split(", "):
            amount, color = cubes.split(" ")
            amount = int(amount)
            if color == "red":
                min_red = max(min_red, amount)
            if color == "green":
                min_green = max(min_green, amount)
            if color == "blue":
                min_blue = max(min_blue, amount)
    sum += min_red * min_green * min_blue

print(sum)
