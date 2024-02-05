

def extrapolate_next_value(history):
    # Convert the history string into a list of integers
    history = list(map(int, history.split()))
    sequences = [history]

    # Generate sequences of differences until all values in a sequence are 0
    while sequences[-1].count(sequences[-1][0]) != len(sequences[-1]):
        new_sequence = [sequences[-1][i+1] - sequences[-1][i] for i in range(len(sequences[-1])-1)]
        sequences.append(new_sequence)

    # Backtrack to find the next value in the original sequence
    for i in range(len(sequences)-2, -1, -1):
        sequences[i].append(sequences[i][-1] + sequences[i+1][-1])

    # The next value is the last element of the first (original) sequence
    return sequences[0][-1]

def process_file(filename):
    # Open the file and read the histories
    with open(filename, 'r') as file:
        # Filter out empty lines or lines that do not contain a proper sequence
        histories = [line.strip() for line in file.readlines() if line.strip() and all(c.isdigit() or c.isspace() for c in line)]

    # Find the next value for each history and calculate their sum
    next_values_sum = sum(extrapolate_next_value(history) for history in histories)
    return next_values_sum

filename = '../TextFiles/day9.txt'
total_sum = process_file(filename)
print(total_sum)

