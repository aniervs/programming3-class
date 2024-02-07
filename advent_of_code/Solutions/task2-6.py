


# function to calculate the number of ways to beat the record for each race
def calculate_ways_to_win(races):
    ways_to_win = []
    for race in races:
        ways = 0
        for hold_time in range(race["duration"]):  # Try each possible hold time
            speed = hold_time  # Speed increases by 1 mm/ms for each ms held
            travel_time = race["duration"] - hold_time
            distance = speed * travel_time
            if distance > race["record_distance"]:
                ways += 1
        ways_to_win.append(ways)
    return ways_to_win

# function to and extract race details
def parse_races_from_text(text):
    lines = text.strip().split('\n')
    times = list(map(int, lines[0].split()[1:]))
    distances = list(map(int, lines[1].split()[1:]))

    races = []
    for time, distance in zip(times, distances):
        races.append({"duration": time, "record_distance": distance})

    return races

def read_file_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()

file_path = "../TextFiles/day6.txt"

file_content = read_file_content(file_path)

races_from_text = parse_races_from_text(file_content)

# Calculate the number of ways to win
ways_to_win_from_text = calculate_ways_to_win(races_from_text)

# Calculate the product of the number of ways to win for each race
total_ways_to_win_from_text = 1
for ways in ways_to_win_from_text:
    total_ways_to_win_from_text *= ways

print(ways_to_win_from_text, total_ways_to_win_from_text)
