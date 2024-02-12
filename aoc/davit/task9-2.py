def calculate_and_print_differences(sequence, level=0):
    differences = [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]

    spaces = "  " * level
    formatted_sequence = "  ".join(map(str, sequence))
    formatted_differences = "  ".join(map(str, differences))
    print(f"{spaces}{formatted_sequence}")
    print(f"{spaces}  {formatted_differences}")

    return differences
def calculate_previous_value(sequence, level=0):
    if len(set(sequence)) == 1:
        return sequence[0]

    differences = calculate_and_print_differences(sequence, level)
    return sequence[0] - calculate_previous_value(differences, level + 1)

with open("./txt/day9.txt", "r") as file:
    input_data = [[int(num) for num in line.split()] for line in file.readlines()]

total_sum = sum(calculate_previous_value(row) for row in input_data)
print(f"\nTotal: {total_sum}")
