def part2(data):
    _time = int(data[0].split(":")[1].replace(" ", ""))
    _dist = int(data[1].split(":")[1].replace(" ", ""))
    curr = _time ** 2 // 4
    diff = curr - _dist
    steps = diff ** 0.5
    if steps.is_integer():
        steps -= 1
    steps = int(steps)
    if _time % 2:
        while steps ** 2 + steps >= diff:
            steps -= 1
    count = steps * 2 + (2 if _time % 2 else 1)
    return count


with open('input2-1.txt', 'r') as file:
    lines = file.readlines()
    print(part2(lines))
