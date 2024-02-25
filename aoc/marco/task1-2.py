import sys

sum = 0
numbers = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

for line in sys.stdin:
    line = line.strip()
    for x in [10, 1]:
        for i in range(len(line)):
            c = line[i]
            if c.isnumeric():
                sum += x * int(c)
                break
            found = False
            for j in range(1,10):
                if line[i:i+len(numbers[j])] == numbers[j]:
                    sum += x * j
                    found = True
                    break
            if found:
                break
        line = line[::-1]
        for i in range(1,10):
            numbers[i] = numbers[i][::-1]

print(sum)
