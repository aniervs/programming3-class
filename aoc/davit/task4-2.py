import re

with open('txt/day4.txt', 'r') as f:
    l = f.read().splitlines()

cd = {}

for ln in l:
    li = int(re.findall(r'\d+', ln)[0])
    cd[li] = 1

for ln in l:
    li = int(re.findall(r'\d+', ln)[0])
    wn = [int(x) for x in ln.split(':')[1].split('|')[0].split(' ') if x]
    mn = [int(x) for x in ln.split(':')[1].split('|')[1].split(' ') if x]

    ms = [x for x in mn if x in wn]    

    for i in range(len(ms)):
        ci = cd.get(li + (i + 1), 0)
        cd[li + (i + 1)] = ci + cd[li]

fs = sum(cd.values())

print(fs)