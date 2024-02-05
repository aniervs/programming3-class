



# Define the limits for the cubes
cube_limits = {'red': 12, 'green': 13, 'blue': 14}

# Parse the games and check if they are possible within the cube limits
def parse_games(games_str, limits):
    possible_games = []
    for game in games_str.strip().split('\n'):
        game_id, *subsets = game.replace(':', ';').split(';')
        game_id = int(game_id.split(' ')[1])  # Extract the game ID number
        is_possible = True
        for subset in subsets:
            counts = {'red': 0, 'green': 0, 'blue': 0}
            for color_info in subset.split(','):
                number, color = color_info.strip().split(' ')
                color = color.rstrip('s')  # Remove 's' from the end to match keys in limits
                counts[color] += int(number)
                if counts[color] > limits[color]:
                    is_possible = False
                    break
            if not is_possible:
                break
        if is_possible:
            possible_games.append(game_id)
    return possible_games

# Function to read game data from a file and parse it
def read_and_parse_games(file_path, limits):
    with open(file_path, 'r') as file:
        games_str = file.read()
    return parse_games(games_str, limits)

# Assuming 'hey.txt' is saved at a specific location
file_path = '../TextFiles/day2.txt'  # Update this with the actual path to your hey.txt file

# Use the function to read from the file and find possible games
possible_game_ids = read_and_parse_games(file_path, cube_limits)
sum_of_ids = sum(possible_game_ids)

# Print the results
print(f"Sum of IDs of possible games: {sum_of_ids}")
print(f"Possible game IDs: {possible_game_ids}")
