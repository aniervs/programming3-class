def calculate_points(data):
    return sum(int(2 ** (len(set(win.split()) & set(your.split())) - 1)) for win, your in (line.split(":")[1].split("|") for line in data))

with open('task4.txt', 'r') as file:
    lines = file.readlines()
    print(calculate_points(lines))
