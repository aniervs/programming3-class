def part2(data):

        possibles = 0

        for line in data:
            colors = {"red": 0, "green": 0, "blue": 0}
            sets = line.split(": ")[1]
            groups = map(str.split, sets.replace(";", ",").split(", "))
            for key, val in groups:
                if int(key) > colors[val]:
                    colors[val] = int(key)

            # print(colors)
            possibles += colors["red"] * colors["green"] * colors["blue"]


        return possibles

file_path = "files/task2"
with open(file_path, 'r') as file:
    text = file.read()
arr = text.split('\n')
print(part2(arr))