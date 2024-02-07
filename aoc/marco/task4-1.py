import sys

sum = 0

def read_list(l):
    return [int(x) for x in l.split(" ") if x != ""]

for line in sys.stdin:
    card = line.strip().split(": ")[1]
    winning, yours = list(map(read_list, card.split(" | ")))
    winning = set(winning)
    count = 0
    for x in yours:
        if x in winning:
            count += 1
    if count > 0:
        sum += pow(2, count - 1)

print(sum)
