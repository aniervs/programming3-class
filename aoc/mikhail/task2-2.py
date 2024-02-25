def possible_games(game_data, red_cubes, green_cubes, blue_cubes):
    possible_game_ids = []

    for line in game_data:
        game_id = int(line.split(':')[0].split(' ')[1])

        sets = line.strip().split('; ')

        sets[0] = sets[0].split(': ')[1]

        is_possible = True
        for set in sets:
            counts = {'red': 0, 'green': 0, 'blue': 0}
            cubes = set.split(', ')
            for cube in cubes:
                num, color = cube.split(' ')
                counts[color] += int(num)

            if counts['red'] > red_cubes or counts['green'] > green_cubes or counts['blue'] > blue_cubes:
                is_possible = False
                break

        if is_possible:
            possible_game_ids.append(game_id)

    return sum(possible_game_ids)

file_path = 'aoc/mikhail/puzzles_input/puzzle2.txt'

with open(file_path, 'r') as file:
    game_data = file.readlines()

sum_possible_games = possible_games(game_data, 12, 13, 14)
print(sum_possible_games)
