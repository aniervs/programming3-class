def calculate_ways_to_win_from_file(file_path):
    """
    Calculate the number of ways to beat the record in each race from the file.
    """
    def ways_to_win(time, distance):
        ways = 0
        for hold_time in range(time):
            travel_time = time - hold_time
            travel_distance = travel_time * hold_time
            if travel_distance > distance:
                ways += 1
        return ways

    with open(file_path, 'r') as file:
        lines = file.readlines()
        times = list(map(int, lines[0].split()[1:]))
        distances = list(map(int, lines[1].split()[1:]))
        races = list(zip(times, distances))

    ways_to_win_each_race = [ways_to_win(time, distance) for time, distance in races]

    product_of_ways = 1
    for ways in ways_to_win_each_race:
        product_of_ways *= ways

    return product_of_ways, ways_to_win_each_race

file_path = 'aoc/mikhail/puzzles_input/puzzle6.txt'

product_of_ways, ways_to_win_each_race = calculate_ways_to_win_from_file(file_path)
product_of_ways, ways_to_win_each_race

print(product_of_ways, ways_to_win_each_race)

