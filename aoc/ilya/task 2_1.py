def count_possible_sets(data):
    possible_count = 0

    for i, line in enumerate(data, 1):
        color_limits = {"red": 12, "green": 13, "blue": 14}
        sets = line.split(": ")[1]
        groups = map(str.split, sets.replace(";", ",").split(", "))
        is_possible = all(int(key) <= color_limits[val] for key, val in groups)

        if is_possible:
            possible_count += i

    return possible_count

with open('task2.txt', 'r') as file:
    content = file.read()

lines = content.split('\n')
print(count_possible_sets(lines))
