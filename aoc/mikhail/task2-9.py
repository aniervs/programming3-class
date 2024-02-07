from itertools import combinations

def extrapolate_next_value(history):
    """
    Extrapolate the next value in the history based on the provided methodology.
    """
    sequences = [history]

    while sequences[-1].count(sequences[-1][0]) != len(sequences[-1]):
        sequences.append([sequences[-1][i+1] - sequences[-1][i] for i in range(len(sequences[-1])-1)])

    for i in range(len(sequences) - 2, -1, -1):
        sequences[i].append(sequences[i][-1] + sequences[i+1][-1])

    return sequences[0][-1]

def sum_extrapolated_values_from_file(file_path):
    """
    Sum the extrapolated next values for each history from the file.
    """
    with open(file_path, 'r') as file:
        histories = file.readlines()

    total_sum = 0
    for history in histories:
        numbers = list(map(int, history.strip().split()))
        next_value = extrapolate_next_value(numbers)
        total_sum += next_value

    return total_sum

file_path = 'aoc/mikhail/puzzles_input/puzzle9.txt'

sum_of_extrapolated_values = sum_extrapolated_values_from_file(file_path)
sum_of_extrapolated_values

print(sum_of_extrapolated_values)