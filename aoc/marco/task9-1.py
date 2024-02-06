import sys

sum = 0

def diff(a):
    res = []
    for i in range(len(a)-1):
        res.append(a[i + 1] - a[i])
    return res

def next(a):
    if max(a) == 0 and min(a) == 0:
        return 0
    d = diff(a)
    n = next(d)
    return a[-1] + n

for line in sys.stdin:
    a = list(map(int, line.strip().split(" ")))
    sum += next(a)

print(sum)
