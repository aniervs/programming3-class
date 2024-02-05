def part1(data):

        possibles = 0

        for i in range(len(data)):
            colors = {"red": 12, "green": 13, "blue": 14}
            sets = data[i].split(": ")[1]
            groups = map(str.split, sets.replace(";", ",").split(", "))
            f = False
            for key, val in groups:
                if int(key) > colors[val]:
                    f = True

            if not f:
                possibles += i + 1


        return possibles

file_path = "files/task2"
with open(file_path, 'r') as file:
    text = file.read()
arr = text.split('\n')
print(part1(arr))