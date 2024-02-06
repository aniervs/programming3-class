import math


def part2(data):
    _sum = 0

    for line in data:
        counts = {"red": 0, "green": 0, "blue": 0}
        _, sets = line.split(": ")
        sets = sets.split("; ")
        for _set in sets:
            _set = {k: int(v) for v, k in map(str.split, _set.split(", "))}
            counts = {k: max(v, _set.get(k, 0)) for k, v in counts.items()}
        _sum += math.prod(counts.values())

    return _sum


with open('input2-1.txt', 'r') as file:
    lines = file.readlines()
    print(part2(lines))
