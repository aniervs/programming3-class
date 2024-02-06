def part1(data):
    thresholds = {"red": 12, "green": 13, "blue": 14}
    possibles = 0

    for line in data:
        game_info, sets = line.split(": ")
        groups = map(str.split, sets.replace(";", ",").split(", "))
        if all(int(cube_nums) <= thresholds[cube_color] for cube_nums, cube_color in groups):
            possibles += int(game_info.split(" ")[1])

    return possibles


with open('input2-1.txt', 'r') as file:
    lines = file.readlines()
    print(part1(lines))
