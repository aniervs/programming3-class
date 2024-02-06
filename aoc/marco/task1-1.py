import sys

sum = 0

for line in sys.stdin:
    line = line.strip()
    for x in [10, 1]:
        for i in range(len(line)):
            c = line[i]
            if c.isnumeric():
                sum += x * int(c)
                break
        line = line[::-1]

print(sum)
