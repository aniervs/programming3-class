import math


def part1(data):
    _times = [*map(int, data[0].split(":")[1].strip().split())]
    _dists = [*map(int, data[1].split(":")[1].strip().split())]

    counts = []
    for i in range(len(_times)):
        _time = _times[i]
        _dist = _dists[i]
        counts.append(sum((t * (_time - t) > _dist) for t in range(_time)))

    return math.prod(counts)


with open('input2-1.txt', 'r') as file:
    lines = file.readlines()
    print(part1(lines))
