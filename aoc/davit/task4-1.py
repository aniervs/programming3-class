with open('./txt/day4.txt', 'r') as f:
    l = f.read().splitlines()

#Part 1 
tp = 0
for ln in l:
    wn = [int(x) for x in ln.split(':')[1].split('|')[0].split(' ') if x]
    mn = [int(x) for x in ln.split(':')[1].split('|')[1].split(' ') if x]

    ms = [x for x in mn if x in wn]

    if ms:
        tp += 2 ** (len(ms) - 1)

print(tp)


