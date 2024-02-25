

def extrapolate_next_value(history):

    history = list(map(int, history.split()))
    sequences = [history]

    while sequences[-1].count(sequences[-1][0]) != len(sequences[-1]):
        new_sequence = [sequences[-1][i+1] - sequences[-1][i] for i in range(len(sequences[-1])-1)]
        sequences.append(new_sequence)

    for i in range(len(sequences)-2, -1, -1):
        sequences[i].append(sequences[i][-1] + sequences[i+1][-1])

    return sequences[0][-1]

def process_file(filename):

    with open(filename, 'r') as file:

        histories = [line.strip() for line in file.readlines() if line.strip() and all(c.isdigit() or c.isspace() for c in line)]

    next_values_sum = sum(extrapolate_next_value(history) for history in histories)
    return next_values_sum

filename = '../TextFiles/day9.txt'
total_sum = process_file(filename)
print(total_sum)

