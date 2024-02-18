import sys

sum = 0

def diff(a):
    res = []
    for i in range(len(a)-1):
        res.append(a[i + 1] - a[i])
    return res

def prev(a):
    if max(a) == 0 and min(a) == 0:
        return 0
    d = diff(a)
    n = prev(d)
    return a[0] - n

for line in sys.stdin:
    a = list(map(int, line.strip().split(" ")))
    sum += prev(a)

print(sum)
